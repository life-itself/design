"""Current swallow, made less smooth, and bigger in the ring.
Usage: python -I make3.py <logo.png> <outdir>
Treatments (all keep the current silhouette and orientation):
  cut     knife-cut: contour simplified to straight facets, like a blade on lino
  bleed   ink-bleed: edge pushed in and out by fine noise, like a block print
  cutprint  knife-cut facets + slight bleed + uneven ink inside (white specks)
  gouge   cutprint + a few carved white strokes on the wings
"""
import sys, os
import numpy as np, cv2
from PIL import Image
from scipy import ndimage as ndi

logo_p, out = sys.argv[1:3]
os.makedirs(out, exist_ok=True)
rng = np.random.default_rng(7)
RED, INK, CHALK = (229, 32, 28), (27, 25, 22), (255, 255, 255)
W, K = 600, 4                    # logo size, working supersample
WK = W * K

L = np.asarray(Image.open(logo_p).convert("RGB")).astype(float)
R, G = L[..., 0], L[..., 1]
a_r = np.clip((R - G) / 197, 0, 1)
a_k = np.clip((255 - R - 26 * a_r) / 255, 0, 1)

# ---- swallow mask, supersampled ----
k_big = cv2.resize(a_k, (WK, WK), interpolation=cv2.INTER_CUBIC)
bird = k_big > 0.5
lab, n = ndi.label(bird)
bird = lab == (np.argmax(ndi.sum(bird, lab, range(1, n + 1))) + 1)
ys, xs = np.nonzero(bird)
cy, cx = ys.mean(), xs.mean()     # centre of mass: scale about this

def noise(scale_px, amp):
    f = rng.standard_normal((WK, WK)).astype(np.float32)
    f = cv2.GaussianBlur(f, (0, 0), scale_px)
    return f / (f.std() + 1e-6) * amp

def knife(mask, eps):
    cs, _ = cv2.findContours(mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    m = np.zeros(mask.shape, np.uint8)
    for c in cs:
        cv2.fillPoly(m, [cv2.approxPolyDP(c, eps, True)], 1)
    return m.astype(bool)

def bleed(mask, amp=1.0):
    # signed distance to the edge, nudged by two scales of noise, re-thresholded
    d = ndi.distance_transform_edt(mask) - ndi.distance_transform_edt(~mask)
    d = d + noise(2.5 * K / 4, 1.6 * amp * K / 4) + noise(9 * K / 4, 2.2 * amp * K / 4)
    return d > 0

def specks(mask, density=0.0016, rmin=1, rmax=4):
    # uneven ink: small white flecks inside, none near the edge
    inner = ndi.distance_transform_edt(mask) > 6 * K / 4
    m = mask.copy().astype(np.uint8)
    yy, xx = np.nonzero(inner)
    idx = rng.choice(len(yy), int(len(yy) * density / 8), replace=False)
    for i in idx:
        cv2.ellipse(m, (int(xx[i]), int(yy[i])),
                    (int(rng.integers(rmin, rmax + 1) * K / 2), int(rng.integers(1, 3) * K / 2)),
                    float(rng.uniform(0, 180)), 0, 360, 0, -1)
    return m.astype(bool)

def gouges(mask):
    # carved strokes along the wings: short tapered white lines following each wing's direction.
    m = mask.copy().astype(np.uint8)
    inner = ndi.distance_transform_edt(mask) > 7 * K / 4
    # wing directions in the current mark (pixels in 600px space): (start, end) of each stroke
    strokes = [
        # upper (far) wing: from the body toward the tip at upper left
        ((298, 262), (232, 252)), ((300, 272), (226, 264)), ((304, 281), (246, 278)),
        # near wing: from the shoulder toward the lower left
        ((318, 292), (258, 322)), ((322, 304), (262, 340)), ((326, 316), (280, 352)),
        # tail streamers
        ((300, 318), (236, 323)),
    ]
    for (x0, y0), (x1, y1) in strokes:
        steps = 40
        for t in np.linspace(0, 1, steps):
            x = (x0 + (x1 - x0) * t) * K; y = (y0 + (y1 - y0) * t) * K
            r = max(1, int((1.6 - 1.2 * t) * K / 2))   # taper
            cv2.circle(m, (int(x), int(y)), r, 0, -1)
    return np.where(inner | ~mask, m.astype(bool), mask)  # keep the outline edge intact

def to_alpha(mask):
    a = cv2.GaussianBlur(mask.astype(np.float32), (0, 0), K * 0.45)
    return cv2.resize(a, (W, W), interpolation=cv2.INTER_AREA)

def scale_mask(mask, s):
    M = np.float32([[s, 0, cx * (1 - s)], [0, s, cy * (1 - s)]])
    return cv2.warpAffine(mask.astype(np.uint8), M, (WK, WK), flags=cv2.INTER_NEAREST).astype(bool)

def grain(mask, angle=-18, every=7, dash=0.55):
    # sparse wood-grain: short thin white dashes at one angle, only in thick parts
    h, w = mask.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    t = np.deg2rad(angle)
    u = xx * np.cos(t) + yy * np.sin(t); v = -xx * np.sin(t) + yy * np.cos(t)
    line = np.abs(((v / K) % every) - every / 2) < 0.32
    breaks = noise(14 * K / 4, 1.0) > dash
    inner = ndi.distance_transform_edt(mask) > 5 * K
    return mask & ~(line & breaks & inner)

def keyline(mask, at=4.2, width=0.55):
    # carved white line running inside the edge, broken in places
    d = ndi.distance_transform_edt(mask) / K
    band = np.abs(d - at) < width
    room = ndi.maximum_filter(d, size=int(10 * K)) > at * 2.2   # only where the shape is thick
    keep = noise(10 * K / 4, 1.0) > -0.2
    return mask & ~(band & room & keep)

cut = knife(bird, 1.1 * K)
base = {
    "smooth": bird,
    "cut": cut,
    "bleed": bleed(bird, 0.55),
}
base["cutprint"] = bleed(cut, 0.4)
base["carved"] = keyline(base["cutprint"])
base["grain"] = grain(base["cutprint"])

# ---- prints: drop whole fingerprints that would touch the bigger bird ----
prints_mask = a_r > 0.04
plab, pn = ndi.label(ndi.binary_dilation(prints_mask, iterations=1))

def ring_for(bird_mask_600, clear=6):
    zone = ndi.binary_dilation(bird_mask_600, iterations=clear)
    hit = np.unique(plab[zone & prints_mask]); hit = hit[hit > 0]
    keep = ~np.isin(plab, hit)
    return a_r * keep

def rgba(color, alpha):
    a = np.zeros((W, W, 4), np.uint8); a[..., :3] = color
    a[..., 3] = np.clip(alpha * 255, 0, 255).astype(np.uint8)
    return Image.fromarray(a, "RGBA")

def save(name, ring_a, bird_a, ring_col, bird_col):
    im = Image.alpha_composite(rgba(ring_col, ring_a), rgba(bird_col, bird_a))
    im.save(f"{out}/{name}.png")

for scale in (1.0, 1.2, 1.35):
    for t, m in base.items():
        sm = scale_mask(m, scale) if scale != 1.0 else m
        ba = to_alpha(sm)
        ra = ring_for(ba > 0.3) if scale != 1.0 else a_r
        tag = f"{t}-{int(scale * 100)}"
        save(f"m-{tag}", ra, ba, RED, INK)
        save(f"m-{tag}-black", np.maximum(ra, 0), ba, INK, INK)
        save(f"m-{tag}-white", ra, ba, CHALK, CHALK)
        save(f"m-{tag}-dark", ra, ba, RED, CHALK)
        if scale == 1.0:
            # close-up of the bird alone, cropped
            big = (cv2.GaussianBlur(m.astype(np.float32), (0, 0), K * 0.45) * 255).astype(np.uint8)
            y0, y1 = int(ys.min()) - 40, int(ys.max()) + 40
            x0, x1 = int(xs.min()) - 40, int(xs.max()) + 40
            crop = big[y0:y1, x0:x1]
            a = np.zeros(crop.shape + (4,), np.uint8); a[..., :3] = INK; a[..., 3] = crop
            Image.fromarray(a, "RGBA").save(f"{out}/bird-{t}.png")
print("done")
