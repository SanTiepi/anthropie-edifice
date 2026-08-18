"""Mise en ligne des visuels du jour sur une branche orpheline, pour l'API Instagram.

Instagram ne prend pas d'envoi de fichier : il faut lui donner une URL publique.
On pousse donc les fichiers du jour sur la branche `social-assets` du dépôt — ce qui
fait aussi office d'archive publique — et on sert les URLs via jsDelivr, qui renvoie
les bons types MIME (raw.githubusercontent renvoie de l'octet-stream).
"""
from __future__ import annotations

import subprocess
import tempfile
import time
from pathlib import Path

import requests

BRANCHE = "social-assets"


def _git(*args, cwd=None):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True)


def pousser(fichiers: list[Path], sous_dossier: str, depot: str, token: str,
            branche: str = BRANCHE) -> dict[str, str]:
    """Pousse les fichiers et renvoie {nom_de_fichier: url_publique}."""
    remote = f"https://x-access-token:{token}@github.com/{depot}.git"
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        _git("init", "-q", str(tmp))
        _git("remote", "add", "origin", remote, cwd=tmp)
        _git("config", "user.name", "mot-du-jour", cwd=tmp)
        _git("config", "user.email", "bot@anthropie.org", cwd=tmp)
        existe = subprocess.run(["git", "fetch", "--depth", "1", "origin", branche],
                                cwd=tmp, capture_output=True, text=True).returncode == 0
        if existe:
            _git("checkout", "-q", "-b", branche, "FETCH_HEAD", cwd=tmp)
        else:
            _git("checkout", "-q", "--orphan", branche, cwd=tmp)
            (tmp / "README.md").write_text(
                "# social-assets\n\nVisuels quotidiens de « Les mots » (anthropie.org/mots).\n"
                "Branche technique : elle sert d'hébergement public pour les APIs Instagram\n"
                "et d'archive des cartes publiées. CC0, comme l'édifice.\n", encoding="utf-8")
        dest = tmp / sous_dossier
        dest.mkdir(parents=True, exist_ok=True)
        for f in fichiers:
            (dest / f.name).write_bytes(f.read_bytes())
        _git("add", "-A", cwd=tmp)
        etat = subprocess.run(["git", "status", "--porcelain"], cwd=tmp, capture_output=True, text=True)
        if etat.stdout.strip():
            _git("commit", "-q", "-m", f"mot du jour · {sous_dossier}", cwd=tmp)
            _git("push", "-q", "origin", branche, cwd=tmp)
    return {f.name: f"https://cdn.jsdelivr.net/gh/{depot}@{branche}/{sous_dossier}/{f.name}"
            for f in fichiers}


def url_secours(url_jsdelivr: str, depot: str, branche: str = BRANCHE) -> str:
    chemin = url_jsdelivr.split(f"@{branche}/", 1)[1]
    return f"https://raw.githubusercontent.com/{depot}/{branche}/{chemin}"


def attendre_disponible(url: str, essais: int = 20, pause: float = 6.0) -> bool:
    """jsDelivr met parfois une minute à voir un fichier neuf."""
    for _ in range(essais):
        try:
            r = requests.get(url, headers={"Range": "bytes=0-63"}, timeout=30)
            if r.status_code in (200, 206):
                return True
        except requests.RequestException:
            pass
        time.sleep(pause)
    return False
