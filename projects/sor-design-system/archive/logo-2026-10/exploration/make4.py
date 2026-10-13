"""Swallow C: lower bird of the pencil sketch, filled solid, in the fingerprint ring.
Usage: python -I make4.py <sketch.png> <logo.png> <outdir>
"""
import sys, os
import numpy as np, cv2
from PIL import Image
from scipy import ndimage as ndi

src, logo_p, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
RED, INK, CHALK = (229, 32, 28), (27, 25, 22), (255, 255, 255)
W = 600

g = np.asarray(Image.open(src).convert("L")).astype(np.float32)[690:1330, 425:1055]
dark = g < 175
# seal the sketchy outline: close small gaps, fill everything enclosed
def disk(r):
    y, x = np.ogrid[-r:r + 1, -r:r + 1]; return x * x + y * y <= r * r
pad = 40
dark = np.pad(dark, pad)
# fine pass keeps thin streamers; coarse pass seals the gappy body outline
fine = ndi.binary_fill_holes(ndi.binary_closing(dark, disk(3)))
coarse = ndi.binary_fill_holes(ndi.binary_closing(dark, disk(16)))
coarse = ndi.binary_opening(coarse, disk(14))     # keep only the thick parts it added (body, head)
filled = fine | coarse
filled = ndi.binary_fill_holes(ndi.binary_closing(filled, disk(4)))
lab, n = ndi.label(filled)
sizes = ndi.sum(filled, lab, range(1, n + 1))
keep = [i + 1 for i, s in enumerate(sizes) if s > 0.02 * sizes.max()]  # bird + any detached streamer bits
bird = np.isin(lab, keep)
# light opening only where it's thick, so the thin streamers survive
bird = ndi.binary_fill_holes(bird)
ys, xs = np.nonzero(bird)
bird = bird[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
np.save(f"{out}/mask.npy", bird)

def alpha_img(mask, size=None):
    a = cv2.GaussianBlur(mask.astype(np.float32), (0, 0), 0.8)
    if size: a = cv2.resize(a, size, interpolation=cv2.INTER_AREA)
    return a

def rgba(color, a):
    arr = np.zeros(a.shape + (4,), np.uint8); arr[..., :3] = color
    arr[..., 3] = np.clip(a * 255, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, "RGBA")

rgba(INK, alpha_img(bird)).save(f"{out}/swallow-c.png")
rgba(CHALK, alpha_img(bird)).save(f"{out}/swallow-c-white.png")

# ---- ring ----
L = np.asarray(Image.open(logo_p).convert("RGB")).astype(float)
a_r = np.clip((L[..., 0] - L[..., 1]) / 197, 0, 1)
prints = a_r > 0.04
plab, _ = ndi.label(ndi.binary_dilation(prints, iterations=1))

for size in (230, 270):
    h, w = bird.shape
    s = size / max(h, w)
    bw, bh = round(w * s), round(h * s)
    a = alpha_img(bird, (bw, bh))
    canvas = np.zeros((W, W), np.float32)
    cx, cy = 300, 300
    x0, y0 = cx - bw // 2, cy - bh // 2
    canvas[y0:y0 + bh, x0:x0 + bw] = a
    zone = ndi.binary_dilation(canvas > 0.3, iterations=3)
    hit = np.unique(plab[zone & prints]); hit = hit[hit > 0]
    ra = a_r * ~np.isin(plab, hit)
    for tag, rc, bc in (("", RED, INK), ("-black", INK, INK), ("-white", CHALK, CHALK), ("-dark", RED, CHALK)):
        Image.alpha_composite(rgba(rc, ra), rgba(bc, canvas)).save(f"{out}/ring-c-{size}{tag}.png")
print(bird.shape)
