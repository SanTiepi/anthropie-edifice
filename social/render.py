"""Rendu des visuels quotidiens : carte 4:5 (Instagram) + vidéo 9:16 (TikTok / Reels).

Charte reprise telle quelle de site/src/pages/mots/og/[slug].png.ts :
parchemin #f4ead4, encre #2b2118, or #a9842b, une couleur par lexique, Cardo.
"""
from __future__ import annotations

import math
import os
import shutil
import subprocess
import tempfile
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "site" / "src" / "og-fonts"
CARDO_B = str(FONT_DIR / "Cardo-Bold.ttf")
CARDO_R = str(FONT_DIR / "Cardo-Regular.ttf")

PARCHEMIN = (244, 234, 212)
ENCRE = (43, 33, 24)
SEPIA = (111, 96, 72)
OR = (169, 132, 43)

FPS = 30
DUREE = 9.0  # secondes


# ---------------------------------------------------------------- utilitaires

def hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def font(bold: bool, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(CARDO_B if bold else CARDO_R, size)


def largeur(d: ImageDraw.ImageDraw, txt: str, f: ImageFont.FreeTypeFont, tracking: float = 0.0) -> float:
    if not tracking:
        return d.textlength(txt, font=f)
    return d.textlength(txt, font=f) + tracking * max(len(txt) - 1, 0)


def texte(d: ImageDraw.ImageDraw, xy, txt: str, f, fill, tracking: float = 0.0, alpha: float = 1.0):
    """Dessine du texte, avec interlettrage optionnel et opacité simulée sur parchemin."""
    if alpha <= 0.003:
        return
    if alpha < 1.0:
        fill = tuple(round(PARCHEMIN[i] + (fill[i] - PARCHEMIN[i]) * alpha) for i in range(3))
    x, y = xy
    if not tracking:
        d.text((x, y), txt, font=f, fill=fill)
        return
    for ch in txt:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + tracking


def decouper(d: ImageDraw.ImageDraw, txt: str, f, maxw: float) -> list[str]:
    lignes, courante = [], ""
    for mot in txt.split():
        essai = f"{courante} {mot}".strip()
        if d.textlength(essai, font=f) <= maxw or not courante:
            courante = essai
        else:
            lignes.append(courante)
            courante = mot
    if courante:
        lignes.append(courante)
    return lignes


def ajuster(d: ImageDraw.ImageDraw, txt: str, maxw: float, taille_max: int, lignes_max: int,
            bold=False, taille_min: int = 20) -> tuple[ImageFont.FreeTypeFont, list[str]]:
    """Plus grande taille de police qui tient le texte en `lignes_max` lignes."""
    for taille in range(taille_max, taille_min - 1, -2):
        f = font(bold, taille)
        lignes = decouper(d, txt, f, maxw)
        if len(lignes) <= lignes_max:
            return f, lignes
    f = font(bold, taille_min)
    return f, decouper(d, txt, f, maxw)


def taille_lemme(mot: str, base: int) -> int:
    n = len(mot)
    ratio = 1.0 if n <= 9 else 0.82 if n <= 13 else 0.66 if n <= 17 else 0.54
    return int(base * ratio)


def fond(w: int, h: int, couleur: tuple[int, int, int], derive: float = 0.0) -> Image.Image:
    """Parchemin + halo radial de la couleur du lexique + grain fin."""
    img = Image.new("RGB", (w, h), PARCHEMIN)
    halo = Image.new("L", (w // 4, h // 4), 0)
    hd = ImageDraw.Draw(halo)
    cx, cy = int(w * 0.86) // 4, int(h * (-0.02 + derive)) // 4
    r = int(max(w, h) * 0.62) // 4
    for i in range(28, 0, -1):
        rr = r * i / 28
        hd.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=int(46 * (1 - i / 28) ** 1.6))
    halo = halo.resize((w, h), Image.LANCZOS).filter(ImageFilter.GaussianBlur(12))
    img = Image.composite(Image.new("RGB", (w, h), couleur), img, halo)
    grain = Image.effect_noise((w, h), 7).filter(ImageFilter.GaussianBlur(0.4)).point(lambda v: 128 + (v - 128) * 0.10)
    return Image.blend(img, Image.merge("RGB", (grain, grain, grain)), 0.055)


def ease(t: float) -> float:
    """Sortie douce (cubic out), bornée."""
    t = min(max(t, 0.0), 1.0)
    return 1 - (1 - t) ** 3


def fenetre(t: float, debut: float, duree: float) -> float:
    return ease((t - debut) / duree) if duree > 0 else (1.0 if t >= debut else 0.0)


# ---------------------------------------------------------------- composition

def _bloc(d, mot, maxw, tailles, dispo: float):
    """Compose le bloc central et le contraint à tenir dans `dispo` pixels.

    On dégrade dans cet ordre : taille du corps, puis longueur de l'extrait.
    Rien ne doit jamais chevaucher la règle du pied — d'où la boucle d'ajustement
    plutôt qu'une mise en page à hauteurs fixes.
    """
    from motdujour import resume

    f_m = font(True, taille_lemme(mot["mot"], tailles["lemme"]))
    f_e, l_e = ajuster(d, mot.get("etym_court") or mot["etym_clean"], maxw, tailles["etym"], 3)
    h_lemme = f_m.size * 1.16
    h_etym = len(l_e) * f_e.size * 1.42
    ecart1, ecart2 = tailles["ecart_etym"], tailles["ecart_corps"]
    dispo_corps = dispo - (h_lemme + ecart1 + h_etym + ecart2)

    plein = mot["corps_clean"]
    variantes = [plein] + [resume(plein, n) for n in (300, 250, 200, 160, 130) if n < len(plein)]
    choix = None
    for corps in variantes:
        court = len(corps)
        taille_max = tailles["corps"] if court > 230 else int(tailles["corps"] * 1.16) if court > 130 else int(tailles["corps"] * 1.34)
        for taille in range(taille_max, tailles["corps_min"] - 1, -2):
            f_c = font(False, taille)
            l_c = decouper(d, corps, f_c, maxw)
            if len(l_c) * taille * 1.46 <= dispo_corps and len(l_c) <= tailles["lignes"]:
                choix = (f_c, l_c)
                break
        if choix:
            break
    if not choix:
        f_c = font(False, tailles["corps_min"])
        l_c = decouper(d, variantes[-1], f_c, maxw)[: tailles["lignes"]]
        choix = (f_c, l_c)
    f_c, l_c = choix

    total = h_lemme + ecart1 + h_etym + ecart2 + len(l_c) * f_c.size * 1.46
    return dict(f_m=f_m, f_e=f_e, l_e=l_e, f_c=f_c, l_c=l_c,
                h=total, ecart1=ecart1, ecart2=ecart2, h_lemme=h_lemme, h_etym=h_etym)


def _dessiner_bloc(d, b, mot, M, y, t, t_mot, t_etym, t_def, a_mot):
    texte(d, (M, y - int(28 * (1 - a_mot))), mot["mot"], b["f_m"], ENCRE, alpha=a_mot)
    y += b["h_lemme"] + b["ecart1"]
    for i, ligne in enumerate(b["l_e"]):
        a = fenetre(t, t_etym + i * 0.12, 0.70)
        texte(d, (M + 2, y - int(14 * (1 - a))), ligne, b["f_e"], SEPIA, alpha=a)
        y += b["f_e"].size * 1.42
    y += b["ecart2"]
    for i, ligne in enumerate(b["l_c"]):
        a = fenetre(t, t_def + i * 0.16, 0.75)
        texte(d, (M, y - int(16 * (1 - a))), ligne, b["f_c"], ENCRE, alpha=a)
        y += b["f_c"].size * 1.46
    return y


def carte(mot: dict, w: int = 1080, h: int = 1350, t: float | None = None) -> Image.Image:
    """Carte 4:5 pour le feed Instagram. Si `t` est donné, rendu animé à l'instant t."""
    anime = t is not None
    t = 1e9 if t is None else t
    coul = hex_rgb(mot["couleur"])
    img = fond(w, h, coul, derive=0.012 * math.sin(t * 0.5) if anime else 0.0)
    d = ImageDraw.Draw(img)
    M = 96
    maxw = w - 2 * M
    T_MOT, T_ETYM, T_DEF = 0.95, 1.95, 2.75

    a_bar = fenetre(t, 0.00, 0.70)
    a_kick = fenetre(t, 0.35, 0.60)
    a_mot = fenetre(t, T_MOT, 0.80)

    d.rectangle([0, 0, 15, int(h * a_bar)], fill=coul)

    y_regle_haut = 170
    f_k = font(True, 30)
    texte(d, (M, 118 - int(14 * (1 - a_kick))), mot["lex_label"].upper(), f_k, coul, tracking=4.2, alpha=a_kick)
    d.rectangle([M, y_regle_haut, w - M, y_regle_haut + 1],
                fill=tuple(round(PARCHEMIN[i] + (OR[i] - PARCHEMIN[i]) * 0.45 * a_kick) for i in range(3)))

    y_regle_bas = h - 156
    b = _bloc(d, mot, maxw, dict(
        lemme=150, etym=38, corps=54, corps_min=34, lignes=9,
        ecart_etym=26, ecart_corps=58), dispo=y_regle_bas - y_regle_haut - 90)
    # bloc centré optiquement entre les deux règles (léger décalage vers le haut)
    y = y_regle_haut + (y_regle_bas - y_regle_haut - b["h"]) * 0.46
    _dessiner_bloc(d, b, mot, M, y, t, T_MOT, T_ETYM, T_DEF, a_mot)

    a_pied = fenetre(t, T_DEF + 0.16 * len(b["l_c"]) + 0.5, 0.80)
    d.rectangle([M, y_regle_bas, w - M, y_regle_bas + 1],
                fill=tuple(round(PARCHEMIN[i] + (OR[i] - PARCHEMIN[i]) * 0.4 * a_pied) for i in range(3)))
    texte(d, (M, y_regle_bas + 30), "Les mots", font(True, 36), ENCRE, alpha=a_pied)
    f_s = font(False, 27)
    texte(d, (M, y_regle_bas + 82), "anthropie.org/mots · mot forgé · racines grecques et latines · CC0",
          f_s, SEPIA, alpha=a_pied)
    texte(d, (w - M - largeur(d, mot["date_fr"], f_s), y_regle_bas + 30), mot["date_fr"], f_s, SEPIA, alpha=a_pied)
    return img


def story(mot: dict, t: float, w: int = 1080, h: int = 1920,
          reperes: tuple[float, float, float] | None = None) -> Image.Image:
    """Image 9:16 animée à l'instant t (TikTok, Reels, Stories).

    `reperes` cale l'apparition du lemme, de l'étymologie et de la définition
    sur la voix off : l'image suit ce qui est dit au lieu de le devancer.
    """
    coul = hex_rgb(mot["couleur"])
    img = fond(w, h, coul, derive=0.010 * math.sin(t * 0.45))
    d = ImageDraw.Draw(img)
    M = 104
    maxw = w - 2 * M
    T_MOT, T_ETYM, T_DEF = reperes or (1.05, 2.15, 3.05)

    a_bar = fenetre(t, 0.00, 0.80)
    a_kick = fenetre(t, 0.40, 0.60)
    a_mot = fenetre(t, T_MOT, 0.85)

    d.rectangle([0, 0, 17, int(h * a_bar)], fill=coul)

    # zones sûres TikTok / Reels : ~250 px en haut, ~470 px en bas, ~140 px à droite
    texte(d, (M, 262), "LE MOT DU JOUR", font(True, 30), coul, tracking=6.0, alpha=a_kick)
    texte(d, (M, 314), mot["lex_label"], font(False, 32), SEPIA, alpha=a_kick)
    y_regle_haut = 392
    d.rectangle([M, y_regle_haut, w - M, y_regle_haut + 1],
                fill=tuple(round(PARCHEMIN[i] + (OR[i] - PARCHEMIN[i]) * 0.45 * a_kick) for i in range(3)))

    y_regle_bas = h - 470
    b = _bloc(d, mot, maxw, dict(
        lemme=162, etym=40, corps=58, corps_min=36, lignes=11,
        ecart_etym=30, ecart_corps=66), dispo=y_regle_bas - y_regle_haut - 110)
    y = y_regle_haut + (y_regle_bas - y_regle_haut - b["h"]) * 0.44
    _dessiner_bloc(d, b, mot, M, y, t, T_MOT, T_ETYM, T_DEF, a_mot)

    a_pied = fenetre(t, T_DEF + 0.16 * len(b["l_c"]) + 0.6, 0.90)
    d.rectangle([M, y_regle_bas, w - M, y_regle_bas + 1],
                fill=tuple(round(PARCHEMIN[i] + (OR[i] - PARCHEMIN[i]) * 0.4 * a_pied) for i in range(3)))
    texte(d, (M, y_regle_bas + 36), "Les mots", font(True, 40), ENCRE, alpha=a_pied)
    texte(d, (M, y_regle_bas + 96), "478 mots pour ce que la langue laissait muet", font(False, 30), SEPIA, alpha=a_pied)
    texte(d, (M, y_regle_bas + 146), "anthropie.org/mots", font(True, 32), coul, tracking=1.5, alpha=a_pied)
    return img


# ---------------------------------------------------------------- sorties

def ecrire_carte(mot: dict, dest: Path) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    carte(mot).save(dest, "JPEG", quality=94, subsampling=0)
    return dest


def ecrire_couverture(mot: dict, dest: Path) -> Path:
    """Vignette 9:16 figée (image de couverture du Reel / du post TikTok)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    story(mot, 1e9).save(dest, "JPEG", quality=94, subsampling=0)
    return dest


def ecrire_video(mot: dict, dest: Path, duree: float = DUREE, fps: int = FPS,
                 audio: Path | None = None,
                 reperes: tuple[float, float, float] | None = None) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    n = int(duree * fps)
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(n):
            story(mot, i / fps, reperes=reperes).save(Path(tmp) / f"f{i:04d}.png", "PNG")
        piste = (["-i", str(audio)] if audio and Path(audio).exists()
                 else ["-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100"])
        cmd = [
            "ffmpeg", "-y", "-loglevel", "error",
            "-framerate", str(fps), "-i", str(Path(tmp) / "f%04d.png"),
            *piste,
            "-shortest",
            "-c:v", "libx264", "-preset", "slow", "-crf", "19",
            "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0",
            "-r", str(fps), "-c:a", "aac", "-b:a", "128k",
            "-movflags", "+faststart", str(dest),
        ]
        subprocess.run(cmd, check=True)
    return dest


def tout(mot: dict, dossier: Path) -> dict[str, Path]:
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg introuvable — requis pour la vidéo 9:16")
    base = f"{mot['date']}-{mot['slug']}"
    audio, duree, reperes = None, DUREE, None
    if os.environ.get("SANS_SON", "").strip() not in ("1", "true", "oui"):
        try:
            import son
            audio, duree, reperes = son.piste(mot, dossier / f"{base}.wav")
        except Exception as e:  # noqa: BLE001 — une vidéo muette vaut mieux que rien
            print(f"[render] piste audio indisponible ({e}) — vidéo muette", flush=True)
    return {
        "carte": ecrire_carte(mot, dossier / f"{base}.jpg"),
        "couverture": ecrire_couverture(mot, dossier / f"{base}-cover.jpg"),
        "video": ecrire_video(mot, dossier / f"{base}.mp4", duree=duree,
                              audio=audio, reperes=reperes),
    }


if __name__ == "__main__":
    import sys
    from motdujour import mot_du_jour
    d = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today()
    m = mot_du_jour(d)
    for k, v in tout(m, ROOT / "social" / "out").items():
        print(f"{k:12} {v}  ({v.stat().st_size // 1024} Ko)")
