"""Piste sonore des vidéos : une voix qui lit le mot, sur une nappe discrète.

La voix est synthétisée hors ligne par Piper (modèle fr_FR-siwis-medium, MIT).
La nappe est générée ici même — aucune musique tierce, donc aucune question de
droits sur des plateformes qui scannent l'audio.

Tout est facultatif : si Piper manque ou échoue, on retombe sur la nappe seule ;
si numpy manque, la vidéo reste muette comme avant. Une chaîne quotidienne ne
doit jamais casser pour un problème de son.
"""
from __future__ import annotations

import os
import re
import subprocess
import wave
from pathlib import Path

SR = 44100
VOIX_DEFAUT = "fr_FR-siwis-medium"
SILENCE_AVANT = 0.75
PAUSE_MOT = 0.55
PAUSE_DEF = 0.70
QUEUE = 1.50


class SansSon(RuntimeError):
    pass


# ----------------------------------------------------------------- voix

def _modele() -> Path:
    """Télécharge le modèle Piper au premier appel, le garde en cache."""
    nom = os.environ.get("VOIX_PIPER", VOIX_DEFAUT)
    cache = Path(os.environ.get("VOIX_CACHE", Path.home() / ".cache" / "piper"))
    cache.mkdir(parents=True, exist_ok=True)
    onnx = cache / f"{nom}.onnx"
    if not onnx.exists():
        subprocess.run(["python3", "-m", "piper.download_voices", nom],
                       cwd=cache, check=True, timeout=600)
    if not onnx.exists():
        raise SansSon(f"modèle Piper absent : {onnx}")
    return onnx


def _dire(voix, texte: str, dest: Path) -> float:
    with wave.open(str(dest), "wb") as w:
        voix.synthesize_wav(texte, w)
    with wave.open(str(dest), "rb") as w:
        return w.getnframes() / w.getframerate()


def _lisible(txt: str) -> str:
    """Ce qui se lit à voix haute : pas de parenthèses techniques, pas de guillemets."""
    txt = re.sub(r"\([^)]*\)", "", txt)
    txt = txt.replace("«", "").replace("»", "").replace("—", ",")
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt


# ----------------------------------------------------------------- nappe

def _nappe(np, duree: float, graine: int):
    """Nappe originale : bourdon grave + quelques notes espacées, réverbérées."""
    t = np.linspace(0, duree, int(SR * duree), endpoint=False)

    def note(f, debut, longueur, amp, decay):
        s = np.zeros_like(t)
        m = (t >= debut) & (t < debut + longueur)
        lt = t[m] - debut
        env = np.exp(-lt * decay) * (1 - np.exp(-lt * 80))
        w = (np.sin(2 * np.pi * f * lt)
             + 0.45 * np.sin(2 * np.pi * 2 * f * lt) * np.exp(-lt * 4)
             + 0.22 * np.sin(2 * np.pi * 3 * f * lt) * np.exp(-lt * 6)
             + 0.10 * np.sin(2 * np.pi * 4.02 * f * lt) * np.exp(-lt * 8))
        s[m] = amp * env * w
        return s

    def bourdon(f, amp):
        env = np.clip(np.minimum(t / 3.0, (duree - t) / 3.5), 0, 1)
        return amp * env * (np.sin(2 * np.pi * f * t)
                            + 0.5 * np.sin(2 * np.pi * f * 2 * t + 0.4)
                            + 0.25 * np.sin(2 * np.pi * f * 3 * t + 1.1))

    # le lexique du mot décale la fondamentale : chaque famille a sa teinte
    fond = [130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00][graine % 7]
    degres = [1.0, 1.1892, 1.3348, 1.4983, 1.7818]
    x = bourdon(fond / 2, 0.055) + bourdon(fond * 1.4983 / 2, 0.030)
    pas = max(2.0, duree / 6.0)
    for i in range(int(duree / pas) + 1):
        d = degres[(graine + i * 3) % len(degres)]
        x += note(fond * d * 2, 0.4 + i * pas, pas * 1.1, 0.10, 1.6)
        x += note(fond * d, 0.42 + i * pas, pas * 1.1, 0.05, 1.4)

    rev = np.zeros_like(x)
    for d, g in [(0.055, 0.30), (0.11, 0.20), (0.19, 0.13), (0.31, 0.08), (0.47, 0.05)]:
        k = int(d * SR)
        rev[k:] += g * x[:-k]
    x = x + 0.55 * rev
    x /= (np.max(np.abs(x)) + 1e-9)
    f = int(SR * 1.2)
    x[:f] *= np.linspace(0, 1, f)
    x[-f:] *= np.linspace(1, 0, f)
    return x


# ----------------------------------------------------------------- montage

def piste(mot: dict, dest: Path) -> tuple[Path, float, tuple[float, float, float]]:
    """Écrit la piste audio et rend (fichier, durée, repères d'animation).

    Les repères disent au rendu quand faire apparaître le lemme, l'étymologie
    et la définition : l'image suit la voix au lieu de la précéder.
    """
    import numpy as np

    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.parent / "_voix"
    tmp.mkdir(exist_ok=True)

    segments: list[tuple[float, "np.ndarray"]] = []
    t_mot = SILENCE_AVANT
    t_etym = t_mot + 0.9
    t_def = t_etym + 0.6
    duree_voix = 0.0

    try:
        from piper import PiperVoice
        voix = PiperVoice.load(str(_modele()))
        d_mot = _dire(voix, _lisible(mot["mot"]) + ".", tmp / "a.wav")
        d_def = _dire(voix, _lisible(mot["corps_court"] or mot["corps_clean"]), tmp / "b.wav")
        d_sig = _dire(voix, "Les mots. anthropie point org.", tmp / "c.wav")

        def lire(p):
            with wave.open(str(p), "rb") as w:
                a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
                if w.getnchannels() == 2:
                    a = a.reshape(-1, 2).mean(axis=1)
                sr = w.getframerate()
            if sr != SR:
                a = np.interp(np.arange(0, len(a) / sr, 1 / SR), np.arange(len(a)) / sr, a)
            return a

        t_mot = SILENCE_AVANT
        t_etym = t_mot + d_mot + 0.30
        t_def = t_mot + d_mot + PAUSE_MOT
        t_sig = t_def + d_def + PAUSE_DEF
        duree_voix = t_sig + d_sig
        segments = [(t_mot, lire(tmp / "a.wav")),
                    (t_def, lire(tmp / "b.wav")),
                    (t_sig, lire(tmp / "c.wav"))]
    except Exception as e:  # noqa: BLE001 — le son ne doit jamais bloquer la publication
        print(f"[son] voix indisponible ({e}) — nappe seule", flush=True)

    duree = max(9.0, (duree_voix + QUEUE) if duree_voix else 11.0)
    n = int(duree * SR)
    voix_mix = np.zeros(n)
    for debut, a in segments:
        i = int(debut * SR)
        a = a[:max(0, n - i)]
        voix_mix[i:i + len(a)] += a

    graine = sum(ord(c) for c in mot["slug"])
    bed = _nappe(np, duree, graine)

    if segments:
        env = np.abs(voix_mix)
        k = int(0.12 * SR)
        env = np.convolve(env, np.ones(k) / k, mode="same")
        env = env / (env.max() + 1e-9)
        duck = 1.0 - 0.62 * np.clip(env * 4, 0, 1)
        mix = 0.28 * bed * duck + 0.95 * voix_mix
    else:
        mix = 0.55 * bed

    mix /= (np.max(np.abs(mix)) + 1e-9)
    mix *= 0.86
    f = int(SR * 0.9)
    mix[:f] *= np.linspace(0, 1, f)
    mix[-f:] *= np.linspace(1, 0, f)

    st = np.stack([mix, mix], axis=1)
    with wave.open(str(dest), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())

    for p in tmp.glob("*.wav"):
        p.unlink(missing_ok=True)
    tmp.rmdir()
    return dest, duree, (t_mot, t_etym, t_def)


if __name__ == "__main__":
    import sys
    from datetime import date
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from motdujour import mot_du_jour
    m = mot_du_jour(date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today())
    p, d, c = piste(m, Path("out") / f"{m['slug']}.wav")
    print(p, round(d, 2), [round(x, 2) for x in c])
