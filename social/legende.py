"""Légendes des publications — voix du site, aucune concession au registre social."""
from __future__ import annotations

BASE_TAGS = ["lesmots", "motdujour", "néologisme", "étymologie", "languefrançaise",
             "vocabulaire", "motrare", "grecancien", "latin"]

TAGS_LEXIQUE = {
    "humaine": ["conditionhumaine", "philosophie", "psychologie"],
    "numerique": ["numérique", "écrans", "intelligenceartificielle"],
    "agent": ["intelligenceartificielle", "philosophiedelesprit", "IA"],
    "vivant": ["vivant", "écologie", "nature"],
    "anthropie": ["anthropie", "éducation", "apprentissage"],
    "lutte": ["politique", "émancipation", "histoire"],
    "generaux": ["quotidien", "travail", "introspection"],
}

SIGNATURE = "anthropie.org/mots"


def _hashtags(mot: dict, n: int = 12) -> str:
    tags = BASE_TAGS + TAGS_LEXIQUE.get(mot["lexique"], [])
    vus, sortie = set(), []
    for t in tags:
        if t.lower() not in vus:
            vus.add(t.lower())
            sortie.append("#" + t)
    return " ".join(sortie[:n])


def instagram(mot: dict) -> str:
    return "\n".join([
        f"{mot['mot']}",
        "",
        mot.get("etym_court") or mot["etym_clean"],
        "",
        mot["corps_clean"],
        "",
        f"Un mot forgé parmi 478, pour nommer ce que la langue avait laissé muet.",
        f"Le dictionnaire entier : {SIGNATURE} — lien en bio.",
        "Sans auteur, CC0 : à prendre, à traduire, à reforger.",
        "",
        _hashtags(mot),
    ])


def tiktok(mot: dict) -> str:
    """Le titre TikTok est court : le mot, sa définition ramassée, la source."""
    corps = mot["corps_court"] if len(mot["corps_clean"]) > 200 else mot["corps_clean"]
    txt = f"{mot['mot']} — {corps}\n{(mot.get('etym_court') or mot['etym_clean'])}\n{SIGNATURE} · CC0\n{_hashtags(mot, 8)}"
    return txt[:2150]


def alt_text(mot: dict) -> str:
    return (f"Carte typographique sur fond parchemin. Le mot « {mot['mot']} », son étymologie "
            f"({(mot.get('etym_court') or mot['etym_clean'])}) et sa définition : {mot['corps_court']}")


if __name__ == "__main__":
    import sys
    from datetime import date
    from motdujour import mot_du_jour
    m = mot_du_jour(date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today())
    print("—— INSTAGRAM ——\n" + instagram(m))
    print("\n—— TIKTOK ——\n" + tiktok(m))
