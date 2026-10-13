"""Bird B: top-left swallow from the three-swallows image, as a solid silhouette in the ring.
Usage: python -I make2.py <swallows.png> <ring-dir (v3/img)> <outdir>
"""
import sys, os
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi

src, ringdir, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
INK, CHALK = (27, 25, 22), (255, 255, 255)

im = Image.open(src).convert("L").crop((110, 145, 290, 360))   # top-left bird + margin
S = 8                                                           # small source: work big
big = im.resize((im.width * S, im.height * S), Image.LANCZOS).filter(ImageFilter.GaussianBlur(S * 0.35))
g = np.asarray(big).astype(float)
dark = g < 200
dark = ndi.binary_closing(dark, structure=np.ones((3, 3)), iterations=S)
dark = ndi.binary_fill_holes(dark)
lab, n = ndi.label(dark)
bird = lab == (np.argmax(ndi.sum(dark, lab, range(1, n + 1))) + 1)
bird = ndi.binary_opening(bird, structure=np.ones((3, 3)), iterations=S // 2)
mask = Image.fromarray((bird * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(S * 0.4))
# re-threshold the blurred mask: smooth edges without a soft halo, then a light AA
m = np.asarray(mask).astype(float)
m = np.clip((m - 110) / 40, 0, 1)
mask = Image.fromarray((m * 255).astype(np.uint8)).resize((im.width * 4, im.height * 4), Image.LANCZOS)

def rgba(color, alpha_img):
    a = np.asarray(alpha_img)
    arr = np.zeros(a.shape + (4,), np.uint8); arr[..., :3] = color; arr[..., 3] = a
    return Image.fromarray(arr, "RGBA")

def orient(img, angle):
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img = img.rotate(angle, resample=Image.BICUBIC, expand=True)
    return img.crop(img.getbbox())

def in_ring(ring, b, size=175, cx=290, cy=296):
    s = size / max(b.size)
    b = b.resize((round(b.width * s), round(b.height * s)), Image.LANCZOS)
    base = ring.copy(); base.alpha_composite(b, (cx - b.width // 2, cy - b.height // 2))
    return base

rings = {k: Image.open(f"{ringdir}/ring-{k}.png").convert("RGBA") for k in ("red", "black", "white")}
for ang in (0, 15, 30):
    blk, wht = orient(rgba(INK, mask), ang), orient(rgba(CHALK, mask), ang)
    blk.save(f"{out}/swallow-b-{ang}.png"); wht.save(f"{out}/swallow-b-{ang}-white.png")
    in_ring(rings["red"], blk).save(f"{out}/ring-b-{ang}.png")
    in_ring(rings["black"], blk).save(f"{out}/ring-b-{ang}-black.png")
    in_ring(rings["white"], wht).save(f"{out}/ring-b-{ang}-white.png")
    in_ring(rings["red"], wht).save(f"{out}/ring-b-{ang}-dark.png")
print("done")
