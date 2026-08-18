"""Résolution du « mot du jour » — réplique exacte du sélecteur client de anthropie.org/mots/.

Le site tire le mot côté navigateur avec un hash FNV-1a 32 bits de la clé de date
`YYYY-M-D` (mois et jour NON zéro-padés, mois 1-12), modulo la taille du pool
dédoublonné par slug, dans l'ordre du fichier `site/src/data/mots.json`.
Toute divergence ici ferait poster un autre mot que celui affiché sur le site.
"""
from __future__ import annotations

import json
import re
import unicodedata
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOTS_JSON = ROOT / "site" / "src" / "data" / "mots.json"

LEX_COLOR = {
    "generaux": "#b07d10",
    "anthropie": "#6a4c93",
    "lutte": "#9b2226",
    "agent": "#2f4b7c",
    "numerique": "#1f7a73",
    "humaine": "#b0491f",
    "vivant": "#517f33",
}
LEX_LABEL = {
    "humaine": "La condition humaine",
    "numerique": "La condition numérique",
    "agent": "La condition d'un agent",
    "vivant": "Le lien au vivant",
    "anthropie": "L'Anthropie",
    "lutte": "La lutte",
    "generaux": "Mots nécessaires",
}

MOIS_FR = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
           "août", "septembre", "octobre", "novembre", "décembre"]


def _to_int32(n: int) -> int:
    """ToInt32 de JS : l'opérateur ^= repasse en entier signé 32 bits."""
    n &= 0xFFFFFFFF
    return n - 0x100000000 if n >= 0x80000000 else n


def _fnv1a(key: str) -> int:
    """« FNV-1a » tel que le site l'exécute — imprécisions du moteur JS comprises.

    Deux pièges, tous deux nécessaires pour tomber sur le même mot que le site :
    1. `h * 16777619` dépasse 2^53 → le moteur arrondit en double avant le `>>> 0`.
       Ce n'est donc pas un FNV-1a entier exact.
    2. `h ^= c` applique ToInt32 : h redevient un entier SIGNÉ à chaque tour, et le
       produit suivant peut être négatif.
    """
    h = 2166136261
    for ch in key:
        h = _to_int32(h) ^ ord(ch)
        h = int(float(h) * 16777619.0) % 4294967296  # ToUint32 (>>> 0)
    return h


def de_mark(s: str) -> str:
    return re.sub(r"[`*_]", "", s)


def teaser(s: str, n: int = 150) -> str:
    """Réplique de teaser() dans index.astro (coupe sur espace, ellipse)."""
    s = de_mark(s).strip()
    if len(s) <= n:
        return s
    cut = s[:n]
    sp = cut.rfind(" ")
    return (cut[:sp] if sp > n * 0.6 else cut).strip() + "…"


def resume(s: str, n: int = 330) -> str:
    """Extrait borné à `n` caractères, coupé sur une fin de phrase quand c'est possible.

    Le site tronque à 150 caractères pour sa vignette ; une carte 1080×1350 tient
    davantage. On évite la coupe en plein milieu d'une proposition : on cherche la
    dernière ponctuation forte, à défaut le dernier espace.
    """
    s = de_mark(s).strip()
    if len(s) <= n:
        return s
    fen = s[:n]
    coupe = max(fen.rfind(". "), fen.rfind(" ; "), fen.rfind(" ! "), fen.rfind(" ? "))
    if coupe > n * 0.45:
        return fen[:coupe + 1].strip()
    sp = fen.rfind(" ")
    return (fen[:sp] if sp > n * 0.6 else fen).strip() + "…"


def load_pool(path: Path | None = None) -> list[dict]:
    """Pool du mot du jour : dédoublonné par slug, ordre du fichier préservé."""
    words = json.loads((path or MOTS_JSON).read_text(encoding="utf-8"))
    seen: set[str] = set()
    pool: list[dict] = []
    for w in words:
        if w["slug"] in seen:
            continue
        seen.add(w["slug"])
        pool.append(w)
    return pool


def date_key(d: date) -> str:
    return f"{d.year}-{d.month}-{d.day}"


def mot_du_jour(d: date, pool: list[dict] | None = None) -> dict:
    pool = pool or load_pool()
    w = dict(pool[_fnv1a(date_key(d)) % len(pool)])
    w["etym_clean"] = de_mark(w["etym"])
    w["corps_clean"] = de_mark(w["corps"]).strip()
    w["corps_teaser"] = teaser(w["corps"])
    w["corps_court"] = resume(w["corps"])
    w["couleur"] = LEX_COLOR.get(w["lexique"], "#a9842b")
    w["lex_label"] = LEX_LABEL.get(w["lexique"], w.get("lexique_label", w["lexique"]))
    w["url"] = f"https://anthropie.org/mots/m/{w['slug']}/"
    w["date"] = d.isoformat()
    w["date_fr"] = f"{d.day} {MOIS_FR[d.month - 1]} {d.year}"
    return w


if __name__ == "__main__":
    import sys
    d = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today()
    m = mot_du_jour(d)
    print(json.dumps(m, ensure_ascii=False, indent=2))
