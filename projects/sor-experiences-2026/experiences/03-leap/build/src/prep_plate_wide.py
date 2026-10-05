"""Wide plate: AI outpaint (plate-wide-ai.png) of the square clean plate, with the original
square pasted back in the centre (feathered) so the scene geometry stays exact.
Square was placed at 70% height in a 16:9 canvas: x0=965,y0=268,S=1254 of 3184x1791.
Writes assets/plate-wide.jpg (unit square = 1000px) and prints its scene extent."""
import os, cv2, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', 'assets')
W, H, X0, Y0, S = 3184, 1791, 965, 268, 1254
wide = cv2.resize(cv2.imread(f'{HERE}/plate-wide-ai.png', 0), (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32)
sq = cv2.imread(f'{HERE}/plate-ai.png', 0).astype(np.float32)
# register: tiny shift between the model's redraw and the original
a = wide[Y0:Y0+S, X0:X0+S]; (dx, dy), _ = cv2.phaseCorrelate(sq, a); print('shift', round(dx, 1), round(dy, 1))
M = np.float32([[1, 0, -dx], [0, 1, -dy]]); wide = cv2.warpAffine(wide, M, (W, H), borderMode=cv2.BORDER_REFLECT)
# match tone of the outpaint to the original around the seam
ring = np.zeros((H, W), np.uint8); cv2.rectangle(ring, (X0, Y0), (X0+S, Y0+S), 1, 80)
inner = ring[Y0:Y0+S, X0:X0+S] > 0
mw, sw = wide[Y0:Y0+S, X0:X0+S][inner].mean(), wide[Y0:Y0+S, X0:X0+S][inner].std()
ms, ss = sq[inner].mean(), sq[inner].std()
wide = (wide - mw) * (ss / sw) + ms
# feathered paste
m = np.zeros((S, S), np.float32); F = 70
m[F:-F, F:-F] = 1; m = cv2.GaussianBlur(m, (0, 0), F / 2.5)
roi = wide[Y0:Y0+S, X0:X0+S]; wide[Y0:Y0+S, X0:X0+S] = roi * (1 - m) + sq * m
k = 1000 / S
out = cv2.resize(np.clip(wide, 0, 255).astype(np.uint8), (round(W * k), round(H * k)), interpolation=cv2.INTER_AREA)
cv2.imwrite(f'{OUT}/plate-wide.jpg', out, [cv2.IMWRITE_JPEG_QUALITY, 82])
print('size', out.shape[1], out.shape[0], 'scene x', round(-X0 / S, 4), 'y', round(-Y0 / S, 4), 'w', round(W / S, 4), 'h', round(H / S, 4))
