"""Publication Threads (API officielle Meta, graph.threads.net).

Threads est le canal le mieux ajusté au projet : c'est un fil de texte, et un
mot avec sa définition y tient sans mise en scène. On publie l'image de la
carte avec la légende ; le texte seul reste possible si l'image manque.

Jeton : longue durée (60 jours), prolongé par /refresh_access_token. Comme pour
TikTok, le jeton renouvelé doit être réécrit dans le coffre.
"""
from __future__ import annotations

import time

import requests

BASE = "https://graph.threads.net/v1.0"
TIMEOUT = 60
LIMITE_TEXTE = 500


class ErreurThreads(RuntimeError):
    pass


def _verifier(r: requests.Response, quoi: str) -> dict:
    try:
        d = r.json()
    except Exception:
        raise ErreurThreads(f"{quoi} → {r.status_code} {r.text[:300]}")
    if r.status_code >= 400 or "error" in d:
        raise ErreurThreads(f"{quoi} → {r.status_code} {d}")
    return d


def identifiant(jeton: str) -> str:
    d = _verifier(requests.get(f"{BASE}/me", params={"fields": "id,username",
                                                    "access_token": jeton}, timeout=TIMEOUT), "me")
    return d["id"]


def publier(jeton: str, texte: str, image_url: str | None = None,
            user_id: str | None = None, attente: int = 30) -> str:
    uid = user_id or identifiant(jeton)
    texte = texte[:LIMITE_TEXTE]
    charge = {"access_token": jeton, "text": texte,
              "media_type": "IMAGE" if image_url else "TEXT"}
    if image_url:
        charge["image_url"] = image_url
    d = _verifier(requests.post(f"{BASE}/{uid}/threads", data=charge, timeout=TIMEOUT), "conteneur")
    creation = d["id"]
    # Meta traite le média après la création du conteneur : on lui laisse le temps
    time.sleep(attente if image_url else 3)
    d = _verifier(requests.post(f"{BASE}/{uid}/threads_publish",
                                data={"access_token": jeton, "creation_id": creation},
                                timeout=TIMEOUT), "publication")
    return d["id"]


def rafraichir_token(jeton: str) -> tuple[str, int]:
    """Prolonge un jeton longue durée. À lancer une fois par mois."""
    d = _verifier(requests.get(f"{BASE}/refresh_access_token",
                               params={"grant_type": "th_refresh_token", "access_token": jeton},
                               timeout=TIMEOUT), "refresh")
    return d["access_token"], int(d.get("expires_in", 0))


def echanger_code(code: str, client_id: str, client_secret: str, redirect_uri: str) -> dict:
    """Code OAuth → jeton court → jeton longue durée (60 jours)."""
    court = _verifier(requests.post("https://graph.threads.net/oauth/access_token",
                                    data={"client_id": client_id, "client_secret": client_secret,
                                          "grant_type": "authorization_code",
                                          "redirect_uri": redirect_uri, "code": code},
                                    timeout=TIMEOUT), "code→jeton")
    longue = _verifier(requests.get(f"{BASE}/access_token",
                                    params={"grant_type": "th_exchange_token",
                                            "client_secret": client_secret,
                                            "access_token": court["access_token"]},
                                    timeout=TIMEOUT), "jeton long")
    return {"access_token": longue["access_token"],
            "expires_in": longue.get("expires_in"),
            "user_id": court.get("user_id")}
