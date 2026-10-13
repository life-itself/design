"""Logo variants + new swallow silhouette.
Usage: python -I make.py <logo.png> <bird.jpg> <outdir>
"""
import sys, os
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi

logo_p, bird_p, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)

RED = (229, 32, 28)
INK = (27, 25, 22)      # --ink
CHALK = (255, 255, 255)

def rgba(color, alpha):
    h, w = alpha.shape
    a = np.zeros((h, w, 4), np.uint8)
    a[..., :3] = color
    a[..., 3] = np.clip(alpha * 255, 0, 255).astype(np.uint8)
    return Image.fromarray(a, "RGBA")

# ---- 1. Unmix the current logo into a red layer and a black layer ----
L = np.asarray(Image.open(logo_p).convert("RGB")).astype(float)
R, G = L[..., 0], L[..., 1]
a_r = np.clip((R - G) / (223 - 26), 0, 1)                  # red ink coverage
a_k = np.clip((255 - R - (255 - RED[0]) * a_r) / 255, 0, 1)  # black ink coverage
a_all = 1 - (1 - a_r) * (1 - a_k)

prints = rgba(RED, a_r)
def comp(*layers):
    base = Image.new("RGBA", layers[0].size, (0, 0, 0, 0))
    for l in layers:
        base = Image.alpha_composite(base, l)
    return base

comp(prints, rgba(INK, a_k)).save(f"{out}/logo-colour.png")
comp(prints, rgba(CHALK, a_k)).save(f"{out}/logo-colour-dark.png")
rgba(INK, a_all).save(f"{out}/logo-black.png")
rgba(CHALK, a_all).save(f"{out}/logo-white.png")
prints.save(f"{out}/ring-red.png")
rgba(INK, a_r).save(f"{out}/ring-black.png")
rgba(CHALK, a_r).save(f"{out}/ring-white.png")

# ---- 2. New swallow: cut out, fill solid, mirror, rotate ----
B = np.asarray(Image.open(bird_p).convert("L")).astype(float)
S = 3  # work at 3x for smooth edges
big = np.asarray(Image.fromarray(B.astype(np.uint8)).resize(
    (B.shape[1] * S, B.shape[0] * S), Image.LANCZOS)).astype(float)
dark = big < 150
# seal hairline gaps in the engraving, then fill every enclosed white area
closed = ndi.binary_closing(dark, structure=np.ones((3, 3)), iterations=6)
filled = ndi.binary_fill_holes(closed)
# keep the biggest piece (the bird), drop specks
lab, n = ndi.label(filled)
sizes = ndi.sum(filled, lab, range(1, n + 1))
bird = lab == (np.argmax(sizes) + 1)
# undo the closing's swelling a little so the outline stays crisp
bird = ndi.binary_opening(bird, structure=np.ones((3, 3)), iterations=2)
bird = ndi.binary_fill_holes(bird)
mask = Image.fromarray((bird * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
mask = mask.resize((B.shape[1], B.shape[0]), Image.LANCZOS)

# engraved (keeps line texture, transparent) for comparison
eng = np.clip((235 - B) / 200, 0, 1)

def orient(img, angle):
    img = img.transpose(Image.FLIP_LEFT_RIGHT)          # face right
    img = img.rotate(angle, resample=Image.BICUBIC, expand=True)  # CCW = nose up
    return img.crop(img.getbbox())

m = np.asarray(mask).astype(float) / 255
sil = rgba(INK, m)
engr = rgba(INK, eng)
sil.save(f"{out}/swallow-solid-original.png")
for ang in (25, 35, 45):
    o = orient(sil, ang); o.save(f"{out}/swallow-solid-{ang}.png")
    orient(engr, ang).save(f"{out}/swallow-engraved-{ang}.png")
    orient(rgba(CHALK, m), ang).save(f"{out}/swallow-solid-{ang}-white.png")

# ---- 3. Try the new bird in the ring ----
W = 600
def in_ring(ring, bird_img, width=205, cx=295, cy=300):
    b = bird_img.copy()
    h = int(b.height * width / b.width)
    b = b.resize((width, h), Image.LANCZOS)
    base = ring.copy()
    # clear the centre so prints don't touch the bird
    base.alpha_composite(b, (cx - width // 2, cy - h // 2))
    return base

for ang in (25, 35, 45):
    in_ring(prints, Image.open(f"{out}/swallow-solid-{ang}.png")).save(f"{out}/ring-new-{ang}.png")
    in_ring(prints, Image.open(f"{out}/swallow-solid-{ang}-white.png")).save(f"{out}/ring-new-{ang}-dark.png")
    in_ring(rgba(INK, a_r), Image.open(f"{out}/swallow-solid-{ang}.png")).save(f"{out}/ring-new-{ang}-black.png")
    in_ring(rgba(CHALK, a_r), Image.open(f"{out}/swallow-solid-{ang}-white.png")).save(f"{out}/ring-new-{ang}-white.png")
print("done")
