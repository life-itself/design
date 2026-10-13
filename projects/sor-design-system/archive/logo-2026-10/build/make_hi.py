"""Step 1 of the logo build. #4 mark rebuilt sharp: same bird, same print layout, from the 1254 px original.
Usage: python -I make_hi.py ../parts/source-logo-600.png ../parts/source-logo-1254.png ../parts/bird-cutprint-2400.png <tmp-dir>

#4 was made at 600 px (logo.png). The reference is the same artwork at 1254 px. This script
  1. re-runs #4's print layout at 600 px exactly as make6/make7 did ("pushed a little, then bird in front"),
     recording how far each print moved,
  2. applies those same moves to the prints of the 1254 px reference,
  3. draws the bird from its 2400 px mask (same rough cut-and-printed edge, +30%),
  4. writes prints-hi.npy (the fingerprint layer), hi.json (crop box) and bird.d (the bird traced to a vector path)
     into <tmp-dir>, for make_final.py.
(Tracing the prints as vectors was tried on 2026-10-13 and rejected: the ridges came out blotchy.)
"""
import sys, os, json
import numpy as np, cv2
from PIL import Image
from scipy import ndimage as ndi
import potrace

logo_p, ref_p, bird_p, out = sys.argv[1:5]
os.makedirs(out, exist_ok=True)
RED, INK, WHITE = (229, 32, 28), (27, 25, 22), (255, 255, 255)

# ---------------- 1. #4 layout at 600 px (same maths as make6/make7) ----------------
W, K = 600, 4; WK = W * K
L = np.asarray(Image.open(logo_p).convert("RGB")).astype(float)
a_r = np.clip((L[..., 0] - L[..., 1]) / 197, 0, 1)
a_k = np.clip((255 - L[..., 0] - 26 * a_r) / 255, 0, 1)
k_big = cv2.resize(a_k, (WK, WK), interpolation=cv2.INTER_CUBIC)
lab, n = ndi.label(k_big > 0.5)
main = np.argmax(ndi.sum(k_big > 0.5, lab, range(1, n + 1))) + 1
ys, xs = np.nonzero(lab == main); cy, cx = ys.mean(), xs.mean()
ys0, xs0 = int(ys.min()) - 40, int(xs.min()) - 40
cut = np.asarray(Image.open(bird_p))[..., 3].astype(np.float32) / 255
bird2400 = np.zeros((WK, WK), np.float32); bird2400[ys0:ys0 + cut.shape[0], xs0:xs0 + cut.shape[1]] = cut
s = 1.30
M = np.float32([[s, 0, cx * (1 - s)], [0, s, cy * (1 - s)]])
bird2400 = cv2.warpAffine(bird2400, M, (WK, WK), flags=cv2.INTER_LINEAR)   # the #4 bird, 4x of 600
ba600 = cv2.resize(bird2400, (W, W), interpolation=cv2.INTER_AREA)

prints = a_r > 0.04
plab, pn = ndi.label(ndi.binary_dilation(prints, iterations=1))
objs = ndi.find_objects(plab)
RC = np.array([cx / K, cy / K])

def hits(zone):
    h = np.unique(plab[zone & prints]); return set(h[h > 0].tolist())

def push_moves(ba, margin=1, max_move=24, overlap_ok=0.25):
    zone = ndi.binary_dilation(ba > 0.3, iterations=margin)
    moving = hits(zone)
    occ = (a_r * ~np.isin(plab, list(moving))) > 0.04
    order = sorted(moving, key=lambda i: np.hypot(*(np.array(ndi.center_of_mass(plab == i))[::-1] - RC)))
    moves = {}
    for i in order:
        sl = objs[i - 1]; m = (plab[sl] == i)
        cyx = np.array(ndi.center_of_mass(m)) + [sl[0].start, sl[1].start]
        d = cyx[::-1] - RC; d = d / (np.linalg.norm(d) + 1e-6)
        done = False
        for step in range(2, max_move + 1, 2):
            for jit in (0, 6, -6, 12, -12):
                t = np.deg2rad(jit)
                dd = np.array([d[0] * np.cos(t) - d[1] * np.sin(t), d[0] * np.sin(t) + d[1] * np.cos(t)])
                ox, oy = (dd * step).round().astype(int)
                y0, x0 = sl[0].start + oy, sl[1].start + ox
                y1, x1 = y0 + m.shape[0], x0 + m.shape[1]
                if y0 < 0 or x0 < 0 or y1 > W or x1 > W: continue
                if (zone[y0:y1, x0:x1] & m).any(): continue
                if (occ[y0:y1, x0:x1] & m).sum() > overlap_ok * m.sum(): continue
                occ[y0:y1, x0:x1] |= m; moves[i] = (ox, oy); done = True; break
            if done: break
        if not done:
            moves[i] = (0, 0)      # stays; the white gap cuts it
    return moves

moves600 = push_moves(ba600)

# ---------------- 2. same moves on the 1254 px reference ----------------
R_ = np.asarray(Image.open(ref_p).convert("RGB")).astype(float)
H = R_.shape[0]; f = H / W
ar_hi = np.clip((R_[..., 0] - R_[..., 1]) / (245 - 46), 0, 1)
pm_hi = ar_hi > 0.04
hlab, hn = ndi.label(ndi.binary_dilation(pm_hi, iterations=2))
hobjs = ndi.find_objects(hlab)
coms = ndi.center_of_mass(pm_hi, hlab, range(1, hn + 1))
ra_hi = ar_hi.copy()
moved = np.zeros_like(ar_hi)
for j, (yy, xx) in enumerate(coms, start=1):
    lo = plab[min(W - 1, int(round(yy / f))), min(W - 1, int(round(xx / f)))]
    if lo == 0:  # centroid fell in a gap: take the 600-px label most of this component lands on
        sl = hobjs[j - 1]; m = hlab[sl] == j
        ys_, xs_ = np.nonzero(m)
        labs = plab[np.clip(((ys_ + sl[0].start) / f).astype(int), 0, W - 1), np.clip(((xs_ + sl[1].start) / f).astype(int), 0, W - 1)]
        labs = labs[labs > 0]
        lo = np.bincount(labs).argmax() if len(labs) else 0
    if lo in moves600:
        ox, oy = moves600[lo]
        sl = hobjs[j - 1]; m = hlab[sl] == j
        patch = ar_hi[sl] * m
        ra_hi[sl][m] = 0
        if (ox, oy) == (0, 0):
            moved[sl] = np.maximum(moved[sl], patch); continue
        dy, dx = int(round(oy * f)), int(round(ox * f))
        y0, x0 = sl[0].start + dy, sl[1].start + dx
        y1, x1 = y0 + m.shape[0], x0 + m.shape[1]
        cy0, cx0 = max(0, -y0), max(0, -x0)
        y0c, x0c, y1c, x1c = max(0, y0), max(0, x0), min(H, y1), min(H, x1)
        moved[y0c:y1c, x0c:x1c] = np.maximum(moved[y0c:y1c, x0c:x1c], patch[cy0:cy0 + y1c - y0c, cx0:cx0 + x1c - x0c])
ra_hi = np.maximum(ra_hi, moved)

# bird at 1254 frame from the 2400 mask
ba_hi = cv2.resize(bird2400, (H, H), interpolation=cv2.INTER_AREA)
# white gap (3 px at 600 -> ~6 px here)
cutz = ndi.binary_dilation(ba_hi > 0.15, iterations=int(round(3 * f)))
ra_hi = ra_hi * (1 - cv2.GaussianBlur(cutz.astype(np.float32), (0, 0), 0.7 * f))

# crop: same box as marks.py, scaled
tot = 1 - (1 - ra_hi) * (1 - ba_hi)
yy_, xx_ = np.nonzero(tot > 0.03)
ccx, ccy = (xx_.min() + xx_.max()) / 2, (yy_.min() + yy_.max()) / 2
half = int(max(xx_.max() - xx_.min(), yy_.max() - yy_.min()) / 2) + int(6 * f)
box = (int(ccx - half), int(ccy - half), int(ccx + half), int(ccy + half))

def rgba(c, a):
    arr = np.zeros(a.shape + (4,), np.uint8); arr[..., :3] = c; arr[..., 3] = np.clip(a * 255, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, "RGBA")

np.save(f"{out}/prints-hi.npy", ra_hi); np.save(f"{out}/bird-hi.npy", ba_hi)

# ---------------- 3. the bird as a vector ----------------
side = box[2] - box[0]
def trace(mask, scale, turd=2, alpha=1.0, opt=0.2):
    bm = potrace.Bitmap(~mask)   # potracer traces False pixels as ink
    path = bm.trace(turdsize=turd, alphamax=alpha, opticurve=True, opttolerance=opt)
    parts = []
    for curve in path:
        sp = curve.start_point
        d = [f"M{sp.x / scale:.2f},{sp.y / scale:.2f}"]
        for seg in curve.segments:
            if seg.is_corner:
                d.append(f"L{seg.c.x / scale:.2f},{seg.c.y / scale:.2f}L{seg.end_point.x / scale:.2f},{seg.end_point.y / scale:.2f}")
            else:
                d.append(f"C{seg.c1.x / scale:.2f},{seg.c1.y / scale:.2f} {seg.c2.x / scale:.2f},{seg.c2.y / scale:.2f} {seg.end_point.x / scale:.2f},{seg.end_point.y / scale:.2f}")
        d.append("Z"); parts.append("".join(d))
    return "".join(parts)

# bird: trace the 2400 mask, cropped to the same box (in 2400 space)
fb = WK / H
bx = [int(v * fb) for v in box]
bmask = bird2400[bx[1]:bx[3], bx[0]:bx[2]] > 0.5
bird_d = trace(bmask, scale=bmask.shape[0] / side, turd=4, alpha=1.0, opt=0.2)

open(f"{out}/bird.d", "w").write(bird_d)
json.dump({"side": side, "box": box, "moved": len([m for m in moves600.values() if m != (0, 0)]), "kept": len(moves600)}, open(f"{out}/hi.json", "w"))
print("side", side, "prints moved", sum(1 for m in moves600.values() if m != (0, 0)))
