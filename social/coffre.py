"""Réécriture des secrets GitHub Actions depuis le workflow lui-même.

Nécessaire parce que TikTok fait tourner son refresh_token à chaque rafraîchissement :
sans réécriture, la chaîne casse au deuxième jour. Requiert un jeton personnel
(secret GH_PAT) avec la permission « Secrets: read and write » sur le dépôt.
"""
from __future__ import annotations

import base64

import requests
from nacl import encoding, public

API = "https://api.github.com"


def _entetes(pat: str) -> dict:
    return {"Authorization": f"Bearer {pat}", "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"}


def ecrire_secret(depot: str, nom: str, valeur: str, pat: str) -> None:
    r = requests.get(f"{API}/repos/{depot}/actions/secrets/public-key", headers=_entetes(pat), timeout=30)
    r.raise_for_status()
    cle = r.json()
    scelle = public.SealedBox(public.PublicKey(cle["key"].encode(), encoding.Base64Encoder()))
    chiffre = base64.b64encode(scelle.encrypt(valeur.encode())).decode()
    r = requests.put(f"{API}/repos/{depot}/actions/secrets/{nom}", headers=_entetes(pat),
                     json={"encrypted_value": chiffre, "key_id": cle["key_id"]}, timeout=30)
    if r.status_code not in (201, 204):
        raise RuntimeError(f"écriture du secret {nom} → {r.status_code} {r.text[:300]}")
