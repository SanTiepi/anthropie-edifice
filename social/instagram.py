"""Publication Instagram — deux chemins d'authentification possibles.

* mode « instagram » (défaut) : Instagram API **with Instagram Login**.
  Hôte graph.instagram.com, jeton utilisateur Instagram, permissions
  instagram_business_basic + instagram_business_content_publish.
  **Aucune Page Facebook n'est requise.** C'est le chemin le plus court.
* mode « facebook » : Instagram API with Facebook Login. Hôte graph.facebook.com,
  jeton de Page, et compte Instagram obligatoirement relié à une Page Facebook.

Dans les deux cas la Graph API ne prend pas d'envoi de fichier : elle va chercher
le média à une URL publique (voir assets.py).
"""
from __future__ import annotations

import os
import time

import requests

TIMEOUT = 60


def _mode() -> str:
    return os.environ.get("IG_LOGIN_MODE", "instagram").strip().lower()


def _hote() -> str:
    return "https://graph.instagram.com" if _mode() == "instagram" else "https://graph.facebook.com"


def _version() -> str:
    return os.environ.get("IG_API_VERSION", "v25.0")


class ErreurInstagram(RuntimeError):
    pass


def _url(chemin: str) -> str:
    return f"{_hote()}/{_version()}/{chemin}"


def _post(chemin: str, **params):
    r = requests.post(_url(chemin), data=params, timeout=TIMEOUT)
    try:
        corps = r.json()
    except ValueError:
        corps = {"texte": r.text[:400]}
    if r.status_code >= 400 or "error" in corps:
        raise ErreurInstagram(f"POST {chemin} → {r.status_code} {corps}")
    return corps


def _get(chemin: str, **params):
    r = requests.get(_url(chemin), params=params, timeout=TIMEOUT)
    corps = r.json()
    if r.status_code >= 400 or "error" in corps:
        raise ErreurInstagram(f"GET {chemin} → {r.status_code} {corps}")
    return corps


def publier_reel(ig_user_id: str, token: str, video_url: str, cover_url: str | None, legende: str,
                 partager_au_feed: bool = True, attente_max: int = 600) -> str:
    """Publie un Reel. `cover_url` est abandonnée si l'API la refuse (elle n'est pas
    documentée pour tous les chemins d'authentification) — mieux vaut un Reel avec la
    vignette automatique qu'aucun Reel."""
    base = dict(media_type="REELS", video_url=video_url, caption=legende,
                share_to_feed="true" if partager_au_feed else "false", access_token=token)
    try:
        conteneur = _post(f"{ig_user_id}/media", **base, **({"cover_url": cover_url} if cover_url else {}))["id"]
    except ErreurInstagram as e:
        if not cover_url or "cover_url" not in str(e):
            raise
        conteneur = _post(f"{ig_user_id}/media", **base)["id"]
    _attendre(conteneur, token, attente_max)
    return _post(f"{ig_user_id}/media_publish", creation_id=conteneur, access_token=token)["id"]


def publier_image(ig_user_id: str, token: str, image_url: str, legende: str, alt: str | None = None,
                  attente_max: int = 300) -> str:
    params = dict(image_url=image_url, caption=legende, access_token=token)
    if alt:
        params["alt_text"] = alt
    conteneur = _post(f"{ig_user_id}/media", **params)["id"]
    _attendre(conteneur, token, attente_max)
    return _post(f"{ig_user_id}/media_publish", creation_id=conteneur, access_token=token)["id"]


def _attendre(conteneur: str, token: str, attente_max: int):
    """Le conteneur doit passer à FINISHED : l'encodage vidéo prend souvent 1 à 3 minutes.
    Meta recommande d'interroger une fois par minute — on reste large mais peu bavard."""
    debut = time.time()
    while time.time() - debut < attente_max:
        etat = _get(conteneur, fields="status_code,status", access_token=token)
        code = etat.get("status_code")
        if code in ("FINISHED", "PUBLISHED"):
            return
        if code in ("ERROR", "EXPIRED"):
            raise ErreurInstagram(f"conteneur {conteneur} en {code} : {etat}")
        time.sleep(20)
    raise ErreurInstagram(f"conteneur {conteneur} toujours pas prêt après {attente_max}s")


def rafraichir_token(token_actuel: str, app_id: str = "", app_secret: str = "") -> tuple[str, int]:
    """Prolonge le jeton longue durée de 60 jours.

    Instagram Login : /refresh_access_token, sans secret, mais le jeton doit avoir plus
    de 24 h et moins de 60 jours — passé ce délai il est mort et il faut refaire l'OAuth.
    Facebook Login : échange fb_exchange_token, avec l'app id et le secret.
    """
    if _mode() == "instagram":
        d = _get("refresh_access_token", grant_type="ig_refresh_token", access_token=token_actuel)
    else:
        d = _get("oauth/access_token", grant_type="fb_exchange_token", client_id=app_id,
                 client_secret=app_secret, fb_exchange_token=token_actuel)
    return d["access_token"], int(d.get("expires_in", 0))


def echanger_longue_duree(token_court: str, app_secret: str) -> tuple[str, int]:
    """Instagram Login : jeton court (1 h) → jeton longue durée (60 jours)."""
    d = _get("access_token", grant_type="ig_exchange_token", client_secret=app_secret,
             access_token=token_court)
    return d["access_token"], int(d.get("expires_in", 0))


def diagnostic(ig_user_id: str, token: str) -> dict:
    """À lancer une fois au montage : vérifie que le jeton voit bien le compte."""
    champs = "id,username,name,media_count" if _mode() == "instagram" else \
             "id,username,name,followers_count,media_count"
    return _get(ig_user_id, fields=champs, access_token=token)
