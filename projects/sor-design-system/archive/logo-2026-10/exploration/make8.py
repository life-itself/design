"""Small-size ladder from #4 (rough cut-and-printed bird, +30%, prints pushed a little then bird in front).
Usage: python -I make8.py <layers-dir from make7> <outdir>
Steps:
  base  #4 as it is
  A     pale prints removed (only the strong reds stay)
  B     A, outer rings only (inner crowd around the bird removed)
  C     about 40 bold prints, real print texture, two rings
  D     about 20 bold prints, bigger, two rings; smooth bird with thicker tail
  E     12 bold dots, one ring; bird bigger
  F     solid red ring; bird bigger
"""
import sys, os
import numpy as np, cv2
from PIL import Image
from scipy import ndimage as ndi

src, out = sys.argv[1:3]
os.makedirs(out, exist_ok=True)
RED, INK, CHALK = (229, 32, 28), (27, 25, 22), (255, 255, 255)
W = 600
C0 = np.array([300.0, 300.0])
rng = np.random.default_rng(3)

ra4 = np.load(f"{src}/layers-cutprint-mix-prints.npy")
ba_rough = np.load(f"{src}/layers-cutprint-bird.npy")
ba_smooth = np.load(f"{src}/layers-smooth-bird.npy")

# ---- analyse the real prints ----
pm = ra4 > 0.04
lab, n = ndi.label(ndi.binary_dilation(pm, iterations=1))
idx = range(1, n + 1)
area = ndi.sum(pm, lab, idx)
mean_a = ndi.mean(ra4, lab, idx)
com = np.array(ndi.center_of_mass(pm, lab, idx))           # (y, x)
rad = np.hypot(com[:, 1] - C0[0], com[:, 0] - C0[1])
ok = area > 60
strength = mean_a

# ---- bird helpers ----
def bird_scale(ba, s):
    ys, xs = np.nonzero(ba > 0.5); cy, cx = ys.mean(), xs.mean()
    M = np.float32([[s, 0, 300 - s * cx], [0, s, 300 - s * cy]])   # also re-centre
    return cv2.warpAffine(ba.astype(np.float32), M, (W, W), flags=cv2.INTER_LINEAR)

def thicken(ba, px):
    m = (ba > 0.5).astype(np.uint8)
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * px + 1, 2 * px + 1))
    m = cv2.dilate(m, k)
    return cv2.GaussianBlur(m.astype(np.float32), (0, 0), 0.8)

# ---- stamp library: the strongest, cleanest real prints ----
sp = cv2.morphologyEx((ra4 > 0.25).astype(np.uint8), cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
slab, sn = ndi.label(sp)
stamps = []
for i, sl in enumerate(ndi.find_objects(slab)):
    m = slab[sl] == i + 1
    a = m.sum()
    if not (350 < a < 1100):
        continue
    ys, xs = np.nonzero(m)
    cov = np.cov(np.vstack([xs, ys])); ev, evec = np.linalg.eigh(cov)
    ax_b, ax_a = 2 * np.sqrt(ev)                      # semi-axes
    fill = a / (np.pi * ax_a * ax_b)
    if fill < 0.8 or ax_a / ax_b < 1.25 or ax_a / ax_b > 2.2:
        continue
    p = ra4[sl] * m
    if p.mean() < 0.45:
        continue
    p = p / max(p.max(), 1e-6)
    ang = np.degrees(np.arctan2(evec[1, 1], evec[0, 1]))
    h, w = p.shape
    S = int(np.hypot(h, w)) + 4
    canvas = np.zeros((S, S), np.float32)
    canvas[(S - h) // 2:(S - h) // 2 + h, (S - w) // 2:(S - w) // 2 + w] = p
    R = cv2.getRotationMatrix2D((S / 2, S / 2), ang - 90, 1.0)
    canvas = cv2.warpAffine(canvas, R, (S, S))
    yy_, xx_ = np.nonzero(canvas > 0.05)
    c = canvas[yy_.min():yy_.max() + 1, xx_.min():xx_.max() + 1]
    if c.shape[0] < c.shape[1]:
        c = c.T
    stamps.append((p.mean(), c))
stamps = [c for _, c in sorted(stamps, key=lambda t: -t[0])][:16]
print("stamps:", len(stamps))

def stamp_ring(layer, n, r, length, solid=0.0, phase=0.0, jitter=0.0):
    """n prints on a circle of radius r, long axis pointing along the ray, `length` px long."""
    for k in range(n):
        t = 2 * np.pi * (k / n) + phase + rng.uniform(-jitter, jitter)
        st = stamps[k % len(stamps)]
        s = length / st.shape[0]
        st = cv2.resize(st, (max(2, int(st.shape[1] * s)), max(2, int(st.shape[0] * s))), interpolation=cv2.INTER_AREA)
        # ink: real texture, pushed towards solid as `solid` -> 1
        st = np.clip(st * (1 + 2.5 * solid) - 0.15 * solid, 0, 1)
        h, w = st.shape
        S = int(np.hypot(h, w)) + 4
        c = np.zeros((S, S), np.float32)
        c[(S - h) // 2:(S - h) // 2 + h, (S - w) // 2:(S - w) // 2 + w] = st
        M = cv2.getRotationMatrix2D((S / 2, S / 2), -np.degrees(t) + 90, 1.0)
        c = cv2.warpAffine(c, M, (S, S))
        x = int(C0[0] + r * np.cos(t) - S / 2); y = int(C0[1] + r * np.sin(t) - S / 2)
        x0, y0 = max(x, 0), max(y, 0); x1, y1 = min(x + S, W), min(y + S, W)
        layer[y0:y1, x0:x1] = np.maximum(layer[y0:y1, x0:x1], c[y0 - y:y1 - y, x0 - x:x1 - x])
    return layer

def ellipse_ring(layer, n, r, a, b, phase=0.0):
    m = np.zeros((W * 4, W * 4), np.uint8)
    for k in range(n):
        t = 2 * np.pi * k / n + phase
        cx, cy = C0[0] + r * np.cos(t), C0[1] + r * np.sin(t)
        cv2.ellipse(m, (int(cx * 4), int(cy * 4)), (int(b * 4), int(a * 4)), np.degrees(t) + 90, 0, 360, 1, -1)
    e = cv2.resize(m.astype(np.float32), (W, W), interpolation=cv2.INTER_AREA)
    return np.maximum(layer, e)

def clear(ra, ba, gap):
    cut = ndi.binary_dilation(ba > 0.15, iterations=gap)
    return ra * (1 - cv2.GaussianBlur(cut.astype(np.float32), (0, 0), 0.7))

steps = {}
steps["base"] = (ra4, ba_rough)

A = np.clip((ra4 - 0.33) * 2.6, 0, 1)                  # pale prints fade out, strong ones go solid
A = A * cv2.GaussianBlur((A > 0.05).astype(np.float32), (0, 0), 0.6)
steps["A"] = (A, ba_rough)
yy0, xx0 = np.mgrid[0:W, 0:W]
outer_px = np.clip((np.hypot(xx0 - 300, yy0 - 300) - 170) / 12, 0, 1)
steps["B"] = (A * outer_px, ba_rough)

Cb = bird_scale(ba_rough, 1.05)
Cl = np.zeros((W, W), np.float32)
Cl = stamp_ring(Cl, 24, 252, 46, solid=0.25, jitter=0.03)
Cl = stamp_ring(Cl, 16, 196, 40, solid=0.25, phase=np.pi / 16, jitter=0.03)
steps["C"] = (clear(Cl, Cb, 8), Cb)

Db = thicken(bird_scale(ba_smooth, 1.12), 2)
Dl = np.zeros((W, W), np.float32)
Dl = stamp_ring(Dl, 12, 248, 66, solid=0.6)
Dl = stamp_ring(Dl, 8, 182, 54, solid=0.6, phase=np.pi / 8)
steps["D"] = (clear(Dl, Db, 10), Db)

Eb = thicken(bird_scale(ba_smooth, 1.22), 3)
El = ellipse_ring(np.zeros((W, W), np.float32), 12, 238, 40, 24)
steps["E"] = (clear(El, Eb, 10), Eb)

Fb = thicken(bird_scale(ba_smooth, 1.22), 3)
yy, xx = np.mgrid[0:W, 0:W]
rr = np.hypot(xx - 300, yy - 300)
Fl = np.clip(1 - np.abs(rr - 246) / 34, 0, 1)
Fl = np.clip((Fl - 0.02) * 40, 0, 1)
steps["F"] = (Fl.astype(np.float32), Fb)

def rgba(color, alpha):
    a = np.zeros((W, W, 4), np.uint8); a[..., :3] = color
    a[..., 3] = np.clip(alpha * 255, 0, 255).astype(np.uint8)
    return Image.fromarray(a, "RGBA")

for k, (ra, ba) in steps.items():
    for tag, rc, bc in (("", RED, INK), ("-dark", RED, CHALK), ("-black", INK, INK), ("-white", CHALK, CHALK)):
        Image.alpha_composite(rgba(rc, ra), rgba(bc, ba)).save(f"{out}/ladder-{k}{tag}.png")
print("done")
