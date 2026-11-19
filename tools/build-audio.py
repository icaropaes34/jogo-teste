#!/usr/bin/env python3
"""Builds audio/*.mp3 for Patrol from CC0 source packs (see README, "Sons e música").

Usage: python3 tools/build-audio.py <source-dir>
<source-dir> holds the original files, flat, with the names used below
(Kenney packs as shipped, Digital Audio prefixed dig_, Interface Sounds prefixed ui_,
Beatscribe fanfares as <system>_ogg_<name>.ogg, music as music_<name>.ogg).
Needs ffmpeg (with libmp3lame) and numpy.
"""
import os, subprocess, sys
import numpy as np

SR = 44100
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = sys.argv[1] if len(sys.argv) > 1 else 'src'
OUT = os.path.join(ROOT, 'audio')
os.makedirs(OUT, exist_ok=True)

def load(name, ch=1):
    p = os.path.join(SRC, name)
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', str(ch), '-ar', str(SR), '-'], check=True, capture_output=True).stdout
    a = np.frombuffer(raw, np.float32).copy()
    return a.reshape(-1, ch) if ch > 1 else a

def seg(a, t0, t1=None):
    return a[int(t0 * SR): None if t1 is None else int(t1 * SR)]

def fade(a, fin=0.005, fout=0.02):
    a = a.copy(); n = len(a)
    i = min(n, int(fin * SR)); o = min(n, int(fout * SR))
    if i: a[:i] *= np.linspace(0, 1, i)
    if o: a[n - o:] *= np.linspace(1, 0, o) ** 2
    return a

def mix(*parts):
    """parts: (signal, gain, offset seconds)"""
    n = max(int(off * SR) + len(s) for s, g, off in parts)
    out = np.zeros(n, np.float32)
    for s, g, off in parts:
        k = int(off * SR); out[k:k + len(s)] += s * g
    return out

def loop(a, xf=0.4):
    """seamless loop: the tail is crossfaded into the head"""
    k = int(xf * SR); body = a[k:].copy()
    w = np.linspace(0, 1, k)
    body[-k:] = body[-k:] * np.sqrt(1 - w) + a[:k] * np.sqrt(w)
    return body

def norm(a, peak=0.89):
    m = np.max(np.abs(a)) or 1
    return a * (peak / m)

def save(name, a, kbps=96, ch=1):
    p = os.path.join(OUT, name + '.mp3')
    data = np.clip(a, -1, 1).astype(np.float32).tobytes()
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ac', str(ch), '-ar', str(SR), '-i', '-', '-c:a', 'libmp3lame', '-b:a', f'{kbps}k', '-ac', str(ch), p], input=data, check=True)
    print(f'{name:12s} {len(a) / SR:6.2f}s {os.path.getsize(p) / 1024:7.1f} KB')

def copy_music(name, src, kbps=96):
    p = os.path.join(OUT, name + '.mp3')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(SRC, src), '-c:a', 'libmp3lame', '-b:a', f'{kbps}k', '-ar', str(SR), '-ac', '2', p], check=True)
    print(f'{name:12s} {os.path.getsize(p) / 1024:7.1f} KB')

# ---- loops (engine, afterburner, wind) ----
save('eng_low', norm(loop(load('space_engine_low_000.ogg'), 0.5)), 80)
save('eng_roar', norm(loop(load('space_engine_large_000.ogg'), 0.5)), 96)
save('burner', norm(loop(load('thruster_fire_003.ogg'), 0.5)), 96)
save('wind', norm(loop(load('wind-strong.mp3'), 1.0)), 64)
save('prop', norm(loop(load('engine_circular_001.ogg'), 0.5)), 96)

# ---- weapons ----
crunch = load('explosion_crunch_000.ogg'); clank = load('impact_metal_heavy_002.ogg')
save('gun', norm(fade(mix((fade(seg(crunch, 0, 0.11), 0.002, 0.06), 1, 0), (fade(seg(clank, 0, 0.08), 0.001, 0.05), 0.45, 0)), 0.001, 0.03)))
thr = load('thruster_fire_001.ogg'); thump = load('impact_punch_heavy_002.ogg')
save('missile', norm(mix((fade(seg(thr, 0.3, 2.0), 0.03, 1.2), 1, 0.02), (fade(thump, 0.001, 0.2), 0.8, 0))))
hiss = load('thruster_fire_000.ogg'); pop = load('impact_punch_heavy_003.ogg')
save('flare', norm(mix((fade(seg(hiss, 0.5, 1.2), 0.01, 0.5), 0.7, 0.03), (fade(pop, 0.001, 0.15), 1, 0))))

# ---- explosions and hits ----
save('boom_s', norm(mix((load('explosion_crunch_002.ogg'), 1, 0), (load('low_frequency_explosion_001.ogg'), 0.9, 0))))
save('boom_l', norm(mix((load('explosion_crunch_004.ogg'), 1, 0), (load('low_frequency_explosion_000.ogg'), 1, 0), (load('explosion_crunch_001.ogg'), 0.5, 0.18))))
save('hit', norm(mix((load('impact_metal_003.ogg'), 1, 0), (load('impact_plate_heavy_000.ogg'), 0.7, 0))))
save('tink', norm(fade(load('impact_metal_heavy_000.ogg'), 0.001, 0.05), 0.7))

# ---- warnings and interface ----
save('lock', norm(load('dig_two_tone_1.ogg'), 0.6))
save('mslwarn', norm(fade(seg(load('dig_tone_1.ogg'), 0, 0.12), 0.002, 0.03), 0.6))
save('alert', norm(load('dig_low_three_tone.ogg'), 0.7))
save('click', norm(load('ui_toggle_001.wav'), 0.7))
save('confirm', norm(load('ui_confirmation_001.wav'), 0.7))

# ---- fanfares ----
for n, s in [('jg_boss', 'NES_ogg_boss_appears.ogg'), ('jg_clear', 'NES_ogg_victory.ogg'), ('jg_win', 'SNES_ogg_victory.ogg'), ('jg_over', 'NES_ogg_game_over.ogg')]:
    save(n, norm(fade(load(s), 0.002, 0.3), 0.8), 96)

# ---- music (seamless loops by the composer) ----
for n, s in [('mus_title', 'music_title.ogg'), ('mus_fly', 'music_level-1.ogg'), ('mus_combat1', 'music_level-2.ogg'), ('mus_combat2', 'music_level-3.ogg'), ('mus_boss', 'music_boss.ogg'), ('mus_over', 'music_ending.ogg')]:
    copy_music(n, s, 96)
