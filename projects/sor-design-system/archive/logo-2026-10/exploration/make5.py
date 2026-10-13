"""Original swallow, unchanged, at a range of sizes in the fingerprint ring.
Usage: python -I make5.py <logo.png> <outdir>
Prints that would touch the bigger bird are removed whole (never clipped).
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
k_big = k_big * (lab == main)          # soft edge of the bird only

prints = a_r > 0.04
plab, _ = ndi.label(ndi.binary_dilation(prints, iterations=1))

def rgba(color, alpha):
    a = np.zeros((W, W, 4), np.uint8); a[..., :3] = color
    a[..., 3] = np.clip(alpha * 255, 0, 255).astype(np.uint8)
    return Image.fromarray(a, "RGBA")

for pct in (100, 110, 120, 130, 140, 150, 165):
    s = pct / 100
    M = np.float32([[s, 0, cx * (1 - s)], [0, s, cy * (1 - s)]])
    b = cv2.warpAffine(k_big.astype(np.float32), M, (WK, WK), flags=cv2.INTER_LINEAR)
    ba = cv2.resize(b, (W, W), interpolation=cv2.INTER_AREA)
    if pct == 100:
        ra = a_r
    else:
        zone = ndi.binary_dilation(ba > 0.3, iterations=4)
        hit = np.unique(plab[zone & prints]); hit = hit[hit > 0]
        ra = a_r * ~np.isin(plab, hit)
    for tag, rc, bc in (("", RED, INK), ("-black", INK, INK), ("-white", CHALK, CHALK), ("-dark", RED, CHALK)):
        Image.alpha_composite(rgba(rc, ra), rgba(bc, ba)).save(f"{out}/size-{pct}{tag}.png")
print("done")
