"""Cut the Leap assets from the AI-retouched sources in build/src/.
plate-ai.png  -> assets/plate.jpg   (road + clouds, no people, no tear)
field-ai.png  -> assets/field.jpg   (yellow field + blue sky, shown through the tear)
lineup-*.png  -> assets/walker-N.webp (3 panels: body | left leg | right leg) + walkers.json
"""
import json, os, cv2, numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', 'assets')
Image.open(f'{HERE}/plate-ai.png').convert('L').resize((1200, 1200), Image.LANCZOS).save(f'{OUT}/plate.jpg', quality=84)
Image.open(f'{HERE}/field-ai.png').convert('RGB').resize((1200, 1200), Image.LANCZOS).save(f'{OUT}/field.jpg', quality=84)

H_OUT = 720
meta = []; debug = []
LEG_TOP = {5: 482}  # hand fixes where the legs touch above the knee
for sheet in ['lineup-a.png', 'lineup-b.png']:
    im = cv2.imread(f'{HERE}/{sheet}').astype(np.float32)
    b, g, r = im[..., 0], im[..., 1], im[..., 2]
    spill = g - np.maximum(r, b)
    alpha = np.clip(1 - (spill - 25) / 70, 0, 1)
    grey = np.clip((r + b) / 2, 0, 255)
    m = (alpha > .5).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    big = sorted([i for i in range(1, n) if st[i, cv2.CC_STAT_AREA] > 20000], key=lambda i: st[i, 0])
    for i in big:
        x, y, w, h = st[i, :4]
        keep = cv2.dilate((lab == i).astype(np.uint8), np.ones((5, 5), np.uint8))
        a = alpha * keep
        x0, y0, x1, y1 = max(x - 6, 0), max(y - 6, 0), min(x + w + 6, im.shape[1]), min(y + h + 6, im.shape[0])
        A = a[y0:y1, x0:x1]; G = grey[y0:y1, x0:x1]
        s = H_OUT / A.shape[0]
        A = cv2.resize(A, None, fx=s, fy=s, interpolation=cv2.INTER_AREA); G = cv2.resize(G, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
        hh, ww = A.shape
        solid = A > .5
        # leg region: rows (from the bottom up) where the silhouette has a clear gap between two legs
        gaps = []
        for yy in range(hh):
            xs = np.where(solid[yy])[0]
            if len(xs) < 2: gaps.append(None); continue
            d = np.diff(xs); k = np.argmax(d)
            gaps.append((xs[k] + xs[k + 1]) / 2 if d[k] > 4 and xs[0] < xs[k] and xs[-1] > xs[k + 1] else None)
        # legs start at the top of the longest run of rows (lower half) with a gap between two legs
        has = [g is not None for g in gaps]; runs = []; start = None
        for yy in range(int(hh * .45), hh):
            if has[yy] and start is None: start = yy
            if (not has[yy] or yy == hh - 1) and start is not None:
                runs.append((yy - start, start)); start = None
        legTop = LEG_TOP.get(len(meta), max(runs)[1])
        split = np.zeros(hh)
        last = ww / 2
        for yy in range(hh - 1, -1, -1):
            if gaps[yy] is not None and yy >= legTop: last = gaps[yy]
            split[yy] = last
        body = A.copy(); body[legTop + 14:] = 0   # body overlaps the leg tops so no seam shows
        legs = A.copy(); legs[:legTop - 6] = 0
        X = np.arange(ww)[None, :]
        L = legs * (X < split[:, None]); R = legs * (X >= split[:, None])
        panels = []
        for M in (body, L, R):
            panels.append(np.dstack([G, G, G, M * 255]))
        atlas = np.hstack(panels).clip(0, 255).astype(np.uint8)
        idx = len(meta)
        Image.fromarray(atlas).save(f'{OUT}/walker-{idx}.webp', quality=82, method=6)
        ys, xs = np.where(solid[-40:]); footX = float(xs.mean()) if len(xs) else ww / 2
        meta.append(dict(w=ww, h=hh, legTop=int(legTop), footX=round(footX, 1)))
        dbg = np.dstack([G, G, G]).astype(np.uint8); dbg[legTop, :] = (0, 0, 255)
        for yy in range(legTop, hh): dbg[yy, int(split[yy])] = (0, 255, 0)
        dbg[A < .5] = (255, 255, 255)
        debug.append(cv2.resize(dbg, (int(ww * 360 / hh), 360)))
json.dump(meta, open(f'{OUT}/walkers.json', 'w'))
print(json.dumps(meta))
cv2.imwrite(f'{HERE}/debug-walkers.png', np.hstack(debug))
