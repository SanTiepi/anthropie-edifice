"""Publication sur une Page Facebook (Graph API).

Canal d'archive plus que de portée : la Page reçoit la carte du jour et sa
légende, avec le lien vers le mot. Un jeton de Page dérivé d'un jeton
utilisateur longue durée n'expire pas, donc rien à renouveler ici.
"""
from __future__ import annotations

import requests

BASE = "https://graph.facebook.com"
TIMEOUT = 90


class ErreurFacebook(RuntimeError):
    pass


def _verifier(r: requests.Response, quoi: str) -> dict:
    try:
        d = r.json()
    except Exception:
        raise ErreurFacebook(f"{quoi} → {r.status_code} {r.text[:300]}")
    if r.status_code >= 400 or "error" in d:
        raise ErreurFacebook(f"{quoi} → {r.status_code} {d}")
    return d


def publier_photo(page_id: str, jeton: str, image_url: str, legende: str,
                  version: str = "v25.0") -> str:
    d = _verifier(requests.post(f"{BASE}/{version}/{page_id}/photos",
                                data={"url": image_url, "caption": legende,
                                      "access_token": jeton}, timeout=TIMEOUT), "photo")
    return d.get("post_id") or d["id"]


def jeton_de_page(page_id: str, jeton_utilisateur: str, version: str = "v25.0") -> str:
    """Récupère le jeton de la Page à partir d'un jeton utilisateur longue durée."""
    d = _verifier(requests.get(f"{BASE}/{version}/{page_id}",
                               params={"fields": "access_token",
                                       "access_token": jeton_utilisateur},
                               timeout=TIMEOUT), "jeton de page")
    return d["access_token"]
