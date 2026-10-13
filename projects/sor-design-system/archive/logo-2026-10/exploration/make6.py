"""Bigger original swallow, keeping the fingerprints.
Usage: python -I make6.py <logo.png> <outdir>
Methods:
  remove  prints the bird would touch are deleted (previous approach, for comparison)
  push    those prints slide outward along their ray from the centre until clear; none lost
  front   every print kept; the bird sits on top with a thin white gap cut around it
  mix     a short push (prints can only move a little), then the white gap for the rest
"""
import sys, os
import numpy as np, cv2
from PIL import Image
from scipy import ndimage as ndi

logo_p, out = sys.argv[1:3]
os.makedirs(out, exist_ok=True)
RED, INK, CHALK = (229, 32, 28), (27, 25, 22), (255, 255, 255)
W, K = 600, 4
WK = W * K

L = np.asarray(Image.open(logo_p).convert("RGB")).astype(float)
R, G = L[..., 0], L[..., 1]
a_r = np.clip((R - G) / 197, 0, 1)
a_k = np.clip((255 - R - 26 * a_r) / 255, 0, 1)

k_big = cv2.resize(a_k, (WK, WK), interpolation=cv2.INTER_CUBIC)
lab, n = ndi.label(k_big > 0.5)
main = np.argmax(ndi.sum(k_big > 0.5, lab, range(1, n + 1))) + 1
ys, xs = np.nonzero(lab == main)
cy, cx = ys.mean(), xs.mean()
k_big = k_big * (lab == main)

prints = a_r > 0.04
plab, pn = ndi.label(ndi.binary_dilation(prints, iterations=1))
objs = ndi.find_objects(plab)
RC = np.array([cx / K, cy / K])          # push away from the bird's centre

def bird_at(pct):
    s = pct / 100
    M = np.float32([[s, 0, cx * (1 - s)], [0, s, cy * (1 - s)]])
    b = cv2.warpAffine(k_big.astype(np.float32), M, (WK, WK), flags=cv2.INTER_LINEAR)
    return cv2.resize(b, (W, W), interpolation=cv2.INTER_AREA)

def hits(zone):
    h = np.unique(plab[zone & prints]); return set(h[h > 0].tolist())

def push(ba, margin=4, max_move=120, overlap_ok=0.12):
    zone = ndi.binary_dilation(ba > 0.3, iterations=margin)
    moving = hits(zone)
    ra = a_r * ~np.isin(plab, list(moving))
    occ = (ra > 0.04)
    # move the innermost first so outer ones see where they landed
    order = sorted(moving, key=lambda i: np.hypot(*(np.array(ndi.center_of_mass(plab == i))[::-1] - RC)))
    left = []
    for i in order:
        sl = objs[i - 1]
        m = (plab[sl] == i)
        patch = a_r[sl] * m
        cyx = np.array(ndi.center_of_mass(m)) + [sl[0].start, sl[1].start]
        d = cyx[::-1] - RC
        d = d / (np.linalg.norm(d) + 1e-6)
        placed = False
        for step in range(2, max_move + 1, 2):
            for jit in (0, 6, -6, 12, -12):
                t = np.deg2rad(jit)
                dd = np.array([d[0] * np.cos(t) - d[1] * np.sin(t), d[0] * np.sin(t) + d[1] * np.cos(t)])
                ox, oy = (dd * step).round().astype(int)
                y0, x0 = sl[0].start + oy, sl[1].start + ox
                y1, x1 = y0 + m.shape[0], x0 + m.shape[1]
                if y0 < 0 or x0 < 0 or y1 > W or x1 > W:
                    continue
                if (zone[y0:y1, x0:x1] & m).any():
                    continue
                if (occ[y0:y1, x0:x1] & m).sum() > overlap_ok * m.sum():
                    continue
                ra[y0:y1, x0:x1] = np.maximum(ra[y0:y1, x0:x1], patch)
                occ[y0:y1, x0:x1] |= m
                placed = True
                break
            if placed:
                break
        if not placed:
            left.append(i)
    return ra, left

def halo(ra, ba, gap=3):
    cut = ndi.binary_dilation(ba > 0.15, iterations=gap)
    soft = cv2.GaussianBlur(cut.astype(np.float32), (0, 0), 0.7)
    return ra * (1 - soft)

def rgba(color, alpha):
    a = np.zeros((W, W, 4), np.uint8); a[..., :3] = color
    a[..., 3] = np.clip(alpha * 255, 0, 255).astype(np.uint8)
    return Image.fromarray(a, "RGBA")

for pct in (120, 130):
    ba = bird_at(pct)
    zone = ndi.binary_dilation(ba > 0.3, iterations=4)
    res = {
        "remove": a_r * ~np.isin(plab, list(hits(zone))),
        "push": push(ba)[0],
        "front": halo(a_r, ba),
    }
    ra_mix, _ = push(ba, margin=1, max_move=24, overlap_ok=0.25)
    # prints that couldn't move far enough stay where they were, cut by the gap
    res["mix"] = halo(np.maximum(ra_mix, 0), ba)
    for name, ra in res.items():
        for tag, rc, bc in (("", RED, INK), ("-black", INK, INK), ("-white", CHALK, CHALK), ("-dark", RED, CHALK)):
            Image.alpha_composite(rgba(rc, ra), rgba(bc, ba)).save(f"{out}/keep-{name}-{pct}{tag}.png")
print("done")
