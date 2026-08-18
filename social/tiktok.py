"""Publication TikTok via la Content Posting API v2.

Deux modes, selon l'état d'audit de l'application développeur :
  * "direct" — publication réelle. Exige le scope video.publish ET une application
    auditée par TikTok. Tant que l'app n'est pas auditée, seuls les comptes listés
    comme testeurs peuvent poster, en visibilité privée.
  * "inbox"  — dépôt du fichier dans la boîte de réception TikTok du compte
    (scope video.upload). Fonctionne sans audit ; une notification arrive dans
    l'app, la publication se fait en deux tapes. C'est le mode de repli.
"""
from __future__ import annotations

import os
import time
from pathlib import Path

import requests

BASE = "https://open.tiktokapis.com/v2"
TIMEOUT = 120
TAILLE_MORCEAU = 10_000_000  # 10 Mo : au-dessus de la taille minimale, un seul morceau suffit


class ErreurTikTok(RuntimeError):
    pass


def _verifier(r: requests.Response, quoi: str) -> dict:
    try:
        d = r.json()
    except Exception:
        raise ErreurTikTok(f"{quoi} → {r.status_code} {r.text[:400]}")
    err = (d.get("error") or {}).get("code", "ok")
    if r.status_code >= 400 or err not in ("ok", "", None):
        raise ErreurTikTok(f"{quoi} → {r.status_code} {d}")
    return d


def rafraichir_token(client_key: str, client_secret: str, refresh_token: str) -> dict:
    """Le jeton d'accès vit 24 h ; le jeton de rafraîchissement tourne à chaque appel.

    Le nouveau refresh_token DOIT être réécrit dans le coffre, sinon la chaîne casse.
    """
    r = requests.post(
        f"{BASE}/oauth/token/",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"client_key": client_key, "client_secret": client_secret,
              "grant_type": "refresh_token", "refresh_token": refresh_token},
        timeout=TIMEOUT,
    )
    d = r.json()
    if "access_token" not in d:
        raise ErreurTikTok(f"rafraîchissement refusé → {r.status_code} {d}")
    return d


def info_createur(access_token: str) -> dict:
    r = requests.post(f"{BASE}/post/publish/creator_info/query/",
                      headers={"Authorization": f"Bearer {access_token}",
                               "Content-Type": "application/json; charset=UTF-8"},
                      timeout=TIMEOUT)
    return _verifier(r, "creator_info")["data"]


def _televerser(upload_url: str, chemin: Path):
    donnees = chemin.read_bytes()
    taille = len(donnees)
    r = requests.put(upload_url, data=donnees, timeout=TIMEOUT * 3, headers={
        "Content-Type": "video/mp4",
        "Content-Length": str(taille),
        "Content-Range": f"bytes 0-{taille - 1}/{taille}",
    })
    if r.status_code not in (200, 201, 206):
        raise ErreurTikTok(f"téléversement → {r.status_code} {r.text[:300]}")


def publier(access_token: str, video: Path, titre: str, mode: str = "direct",
            visibilite: str | None = None, attente_max: int = 900) -> dict:
    taille = video.stat().st_size
    entetes = {"Authorization": f"Bearer {access_token}",
               "Content-Type": "application/json; charset=UTF-8"}
    source = {"source": "FILE_UPLOAD", "video_size": taille,
              "chunk_size": taille, "total_chunk_count": 1}

    if mode == "direct":
        info = info_createur(access_token)
        autorisees = info.get("privacy_level_options") or ["SELF_ONLY"]
        niveau = visibilite if visibilite in autorisees else autorisees[0]
        charge = {
            "post_info": {
                "title": titre,
                "privacy_level": niveau,
                "disable_duet": False,
                "disable_comment": False,
                "disable_stitch": False,
                "video_cover_timestamp_ms": 6000,
            },
            "source_info": source,
        }
        url = f"{BASE}/post/publish/video/init/"
    else:
        charge = {"source_info": source}
        url = f"{BASE}/post/publish/inbox/video/init/"

    d = _verifier(requests.post(url, headers=entetes, json=charge, timeout=TIMEOUT), "init")["data"]
    _televerser(d["upload_url"], video)
    etat = _attendre(access_token, d["publish_id"], attente_max)
    return {"publish_id": d["publish_id"], "mode": mode, "etat": etat}


def _attendre(access_token: str, publish_id: str, attente_max: int) -> dict:
    debut = time.time()
    dernier: dict = {}
    while time.time() - debut < attente_max:
        r = requests.post(f"{BASE}/post/publish/status/fetch/",
                          headers={"Authorization": f"Bearer {access_token}",
                                   "Content-Type": "application/json; charset=UTF-8"},
                          json={"publish_id": publish_id}, timeout=TIMEOUT)
        dernier = _verifier(r, "status")["data"]
        statut = dernier.get("status")
        if statut in ("PUBLISH_COMPLETE", "SEND_TO_USER_INBOX"):
            return dernier
        if statut == "FAILED":
            raise ErreurTikTok(f"publication échouée : {dernier}")
        time.sleep(8)
    return dernier
