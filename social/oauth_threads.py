#!/usr/bin/env python3
"""Échange un code OAuth Threads contre un jeton longue durée, et le range au coffre.

Usage :
    python3 social/oauth_threads.py --code <CODE>            # demande le secret en masqué
    python3 social/oauth_threads.py --url "<URL de retour>"  # colle l'URL complète

Le secret de l'application n'est jamais passé en argument : il est saisi à
l'invite, sans écho, et n'apparaît ni dans l'historique ni dans les journaux.
"""
from __future__ import annotations

import argparse
import getpass
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import threads  # noqa: E402

REDIRECTION = "https://anthropie.org/mots/"


def autoriser_url(client_id: str) -> str:
    return ("https://threads.net/oauth/authorize"
            f"?client_id={client_id}"
            f"&redirect_uri={REDIRECTION}"
            "&scope=threads_basic,threads_content_publish"
            "&response_type=code")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--code")
    p.add_argument("--url", help="URL de retour complète, avec ?code=…")
    p.add_argument("--client-id", required=True)
    p.add_argument("--depot", default="SanTiepi/anthropie-edifice")
    a = p.parse_args()

    code = a.code
    if not code and a.url:
        code = parse_qs(urlparse(a.url).query).get("code", [""])[0]
        code = code.split("#")[0]
    if not code:
        print("Ouvre cette adresse, autorise, puis relance avec --url :")
        print(" ", autoriser_url(a.client_id))
        return

    secret = getpass.getpass("Secret de l'application Meta (saisie masquée) : ").strip()
    d = threads.echanger_code(code, a.client_id, secret, REDIRECTION)

    for nom, valeur in (("THREADS_TOKEN", d["access_token"]),
                        ("THREADS_USER_ID", str(d.get("user_id") or ""))):
        if not valeur:
            continue
        subprocess.run(["gh", "secret", "set", nom, "--repo", a.depot, "--body", valeur], check=True)
        print(f"{nom} → coffre")
    print("jeton valable ~", round(int(d.get("expires_in") or 0) / 86400), "jours")


if __name__ == "__main__":
    main()
