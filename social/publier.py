#!/usr/bin/env python3
"""Chaîne complète du mot du jour : résolution → visuels → hébergement → publication.

Usage :
    python3 social/publier.py                     # aujourd'hui, publie partout
    python3 social/publier.py --date 2026-09-01    # une date précise
    python3 social/publier.py --blanc              # rend les fichiers, ne publie rien
    python3 social/publier.py --lot 30             # 30 jours d'avance, sans publier
    python3 social/publier.py --sans-tiktok

Secrets attendus dans l'environnement (voir social/README.md) :
    IG_USER_ID, IG_ACCESS_TOKEN, FB_APP_ID, FB_APP_SECRET
    TIKTOK_CLIENT_KEY, TIKTOK_CLIENT_SECRET, TIKTOK_REFRESH_TOKEN
    GITHUB_REPOSITORY, GITHUB_TOKEN, GH_PAT
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import traceback
from datetime import date, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))

import assets
import instagram
import legende
import render
import tiktok
from motdujour import load_pool, mot_du_jour

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE / "out"
FUSEAU = ZoneInfo("Europe/Zurich")


def env(nom: str, obligatoire: bool = True) -> str:
    v = os.environ.get(nom, "").strip()
    if obligatoire and not v:
        raise SystemExit(f"secret manquant : {nom}")
    return v


def journal(**kv):
    print(json.dumps(kv, ensure_ascii=False), flush=True)


def fabriquer(jour: date, pool=None) -> tuple[dict, dict[str, Path]]:
    mot = mot_du_jour(jour, pool)
    fichiers = render.tout(mot, SORTIE)
    (SORTIE / f"{mot['date']}-{mot['slug']}.txt").write_text(
        "—— INSTAGRAM ——\n" + legende.instagram(mot) + "\n\n—— TIKTOK ——\n" + legende.tiktok(mot),
        encoding="utf-8")
    return mot, fichiers


def publier_jour(jour: date, avec_instagram: bool, avec_tiktok: bool, blanc: bool) -> dict:
    mot, fichiers = fabriquer(jour)
    journal(etape="visuels", mot=mot["mot"], lexique=mot["lexique"],
            **{k: str(v) for k, v in fichiers.items()})
    resultat = {"date": mot["date"], "mot": mot["mot"], "slug": mot["slug"]}
    if blanc:
        journal(etape="blanc", message="aucune publication (--blanc)")
        return resultat

    depot = env("GITHUB_REPOSITORY")
    urls = assets.pousser([fichiers["video"], fichiers["couverture"], fichiers["carte"]],
                          mot["date"], depot, env("GITHUB_TOKEN"))
    for nom, url in urls.items():
        if not assets.attendre_disponible(url):
            urls[nom] = assets.url_secours(url, depot)
            journal(etape="hébergement", repli=urls[nom])
    journal(etape="hébergement", **urls)

    if avec_instagram:
        try:
            media = instagram.publier_reel(
                env("IG_USER_ID"), env("IG_ACCESS_TOKEN"),
                video_url=urls[fichiers["video"].name],
                cover_url=urls[fichiers["couverture"].name],
                legende=legende.instagram(mot))
            resultat["instagram"] = media
            journal(etape="instagram", statut="publié", media_id=media)
        except Exception as e:
            resultat["instagram_erreur"] = str(e)
            journal(etape="instagram", statut="échec", erreur=str(e))
            traceback.print_exc()

    if avec_tiktok:
        try:
            jetons = tiktok.rafraichir_token(env("TIKTOK_CLIENT_KEY"), env("TIKTOK_CLIENT_SECRET"),
                                             env("TIKTOK_REFRESH_TOKEN"))
            _memoriser_refresh(jetons.get("refresh_token"))
            r = tiktok.publier(jetons["access_token"], fichiers["video"], legende.tiktok(mot),
                               mode=os.environ.get("TIKTOK_MODE", "direct"),
                               visibilite=os.environ.get("TIKTOK_VISIBILITE", "PUBLIC_TO_EVERYONE"))
            resultat["tiktok"] = r
            journal(etape="tiktok", statut="publié", **{k: str(v) for k, v in r.items()})
        except Exception as e:
            resultat["tiktok_erreur"] = str(e)
            journal(etape="tiktok", statut="échec", erreur=str(e))
            traceback.print_exc()

    return resultat


def _memoriser_refresh(nouveau: str | None):
    """TikTok fait tourner le refresh_token : on le réécrit dans les secrets du dépôt."""
    pat = os.environ.get("GH_PAT", "").strip()
    if not nouveau or not pat:
        if nouveau and not pat:
            journal(etape="coffre", statut="ignoré",
                    message="GH_PAT absent : le nouveau refresh_token TikTok n'est pas conservé")
        return
    import coffre
    coffre.ecrire_secret(env("GITHUB_REPOSITORY"), "TIKTOK_REFRESH_TOKEN", nouveau, pat)
    journal(etape="coffre", statut="TIKTOK_REFRESH_TOKEN mis à jour")


def rafraichir_instagram():
    """Prolonge le jeton Instagram longue durée et le réécrit dans les secrets."""
    import coffre
    nouveau, duree = instagram.rafraichir_token(
        env("IG_ACCESS_TOKEN"),
        env("FB_APP_ID", obligatoire=False),
        env("FB_APP_SECRET", obligatoire=False))
    coffre.ecrire_secret(env("GITHUB_REPOSITORY"), "IG_ACCESS_TOKEN", nouveau, env("GH_PAT"))
    journal(etape="coffre", statut="IG_ACCESS_TOKEN prolongé", expire_dans_jours=round(duree / 86400, 1))


def main():
    p = argparse.ArgumentParser(description="Publie le mot du jour sur Instagram et TikTok.")
    p.add_argument("--date", help="AAAA-MM-JJ (défaut : aujourd'hui à Zurich)")
    p.add_argument("--blanc", action="store_true", help="fabrique les fichiers sans rien publier")
    p.add_argument("--lot", type=int, metavar="N", help="fabrique N jours d'avance, sans publier")
    p.add_argument("--sans-instagram", action="store_true")
    p.add_argument("--sans-tiktok", action="store_true")
    p.add_argument("--rafraichir-instagram", action="store_true",
                   help="prolonge le jeton Instagram (à lancer une fois par mois)")
    a = p.parse_args()

    if a.rafraichir_instagram:
        rafraichir_instagram()
        return

    jour = date.fromisoformat(a.date) if a.date else datetime.now(FUSEAU).date()

    if a.lot:
        pool = load_pool()
        for i in range(a.lot):
            mot, fichiers = fabriquer(jour + timedelta(days=i), pool)
            journal(etape="lot", jour=mot["date"], mot=mot["mot"])
        return

    r = publier_jour(jour, not a.sans_instagram, not a.sans_tiktok, a.blanc)
    print(json.dumps(r, ensure_ascii=False, indent=2))
    if r.get("instagram_erreur") or r.get("tiktok_erreur"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
