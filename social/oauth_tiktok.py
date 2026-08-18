#!/usr/bin/env python3
"""Obtenir le premier jeton de rafraîchissement TikTok, en local, une seule fois.

TikTok ne délivre pas de jeton depuis son tableau de bord : il faut passer par le
flux OAuth. Ce script ouvre le navigateur, récupère le code sur un petit serveur
local, l'échange, et affiche le refresh_token à coller dans les secrets GitHub.

    python3 social/oauth_tiktok.py --client-key CLE --client-secret SECRET

L'URL de redirection doit être déclarée à l'identique dans le portail développeur,
onglet « URL properties » :  http://localhost:8723/callback
"""
from __future__ import annotations

import argparse
import http.server
import threading
import urllib.parse
import webbrowser

import requests

PORT = 8723
REDIRECT = f"http://localhost:{PORT}/callback"
SCOPES = "video.publish,video.upload"
recu: dict = {}


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        recu.update({k: v[0] for k, v in q.items()})
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        ok = "code" in recu
        self.wfile.write(
            f"<h2>{'Autorisation reçue.' if ok else 'Autorisation refusée.'}</h2>"
            "<p>Tu peux fermer cet onglet et revenir au terminal.</p>".encode())

    def log_message(self, *a):
        pass


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--client-key", required=True)
    p.add_argument("--client-secret", required=True)
    a = p.parse_args()

    serveur = http.server.HTTPServer(("localhost", PORT), Handler)
    threading.Thread(target=serveur.handle_request, daemon=True).start()

    url = ("https://www.tiktok.com/v2/auth/authorize/?" + urllib.parse.urlencode({
        "client_key": a.client_key, "scope": SCOPES, "response_type": "code",
        "redirect_uri": REDIRECT, "state": "lesmots"}))
    print("Ouverture du navigateur. Autorise le compte @Anthropie.LesMots.\n" + url)
    webbrowser.open(url)

    while "code" not in recu and "error" not in recu:
        pass
    if "code" not in recu:
        raise SystemExit(f"refusé : {recu}")

    r = requests.post("https://open.tiktokapis.com/v2/oauth/token/",
                      headers={"Content-Type": "application/x-www-form-urlencoded"},
                      data={"client_key": a.client_key, "client_secret": a.client_secret,
                            "code": urllib.parse.unquote(recu["code"]),
                            "grant_type": "authorization_code", "redirect_uri": REDIRECT},
                      timeout=60)
    d = r.json()
    if "refresh_token" not in d:
        raise SystemExit(f"échange refusé : {r.status_code} {d}")
    print("\n=== À coller dans les secrets GitHub ===")
    print("TIKTOK_REFRESH_TOKEN =", d["refresh_token"])
    print(f"\n(jeton d'accès valable {d.get('expires_in')} s, "
          f"rafraîchissement valable {d.get('refresh_expires_in')} s — "
          "le workflow s'en occupe ensuite tout seul)")


if __name__ == "__main__":
    main()
