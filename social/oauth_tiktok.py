#!/usr/bin/env python3
"""Obtenir le premier jeton de rafraîchissement TikTok, une seule fois.

TikTok ne délivre pas de jeton depuis son tableau de bord : il faut passer par le
flux OAuth. Et il **refuse les URL de redirection en http**, y compris localhost —
d'où le fonctionnement par copier-coller : on renvoie vers une page du site, et tu
recolles ici l'URL de retour, qui contient le code.

    python3 social/oauth_tiktok.py --client-key CLE --client-secret SECRET

L'URL de redirection déclarée dans le portail développeur doit être exactement :
    https://anthropie.org/mots/
"""
from __future__ import annotations

import argparse
import urllib.parse
import webbrowser

import requests

REDIRECT = "https://anthropie.org/mots/"
SCOPES = "video.publish,video.upload"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--client-key", required=True)
    p.add_argument("--client-secret", required=True)
    a = p.parse_args()

    url = ("https://www.tiktok.com/v2/auth/authorize/?" + urllib.parse.urlencode({
        "client_key": a.client_key, "scope": SCOPES, "response_type": "code",
        "redirect_uri": REDIRECT, "state": "lesmots"}))
    print("1. Une page TikTok s'ouvre. Autorise l'accès avec @Anthropie.LesMots.")
    print("2. Tu atterris sur anthropie.org/mots/ — la page n'a pas changé, c'est normal :")
    print("   ce qui compte est dans la barre d'adresse.")
    print("3. Copie l'URL COMPLÈTE de la barre d'adresse et colle-la ci-dessous.\n")
    print(url + "\n")
    try:
        webbrowser.open(url)
    except Exception:
        pass

    retour = input("URL de retour : ").strip()
    q = urllib.parse.parse_qs(urllib.parse.urlparse(retour).query)
    if "code" not in q:
        raise SystemExit(f"aucun paramètre `code` dans cette URL — reçu : {list(q)}")
    code = urllib.parse.unquote(q["code"][0]).split("*")[0] + "*" if q["code"][0].endswith("*") \
        else urllib.parse.unquote(q["code"][0])

    r = requests.post("https://open.tiktokapis.com/v2/oauth/token/",
                      headers={"Content-Type": "application/x-www-form-urlencoded"},
                      data={"client_key": a.client_key, "client_secret": a.client_secret,
                            "code": code, "grant_type": "authorization_code",
                            "redirect_uri": REDIRECT},
                      timeout=60)
    d = r.json()
    if "refresh_token" not in d:
        raise SystemExit(f"échange refusé : {r.status_code} {d}")
    print("\n=== À coller dans les secrets GitHub ===")
    print("TIKTOK_REFRESH_TOKEN =", d["refresh_token"])
    print(f"\n(jeton d'accès valable {d.get('expires_in')} s ; "
          f"le rafraîchissement expire dans {d.get('refresh_expires_in')} s — "
          "ensuite le workflow s'en occupe seul, à condition qu'il tourne au moins "
          "une fois par an)")


if __name__ == "__main__":
    main()
