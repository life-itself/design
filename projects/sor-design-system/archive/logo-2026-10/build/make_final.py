"""Step 2 of the logo build. The final #4 mark: vector bird + high-resolution fingerprint image.
Usage: python -I make_final.py <tmp-dir from make_hi.py> <system/logo>
Writes, per colourway, into mark/:
  seeds-mark-<way>.svg   self-contained (prints embedded as PNG, bird as a vector path)
  seeds-mark-<way>.png   1130 px master (the prints' native resolution)
and into parts/ the pieces the other steps use: mark-prints-<ink>.png, mark-bird.d, mark-parts.json
"""
import sys, os, base64, json
import numpy as np
from PIL import Image
import resvg_py

hi, logo = sys.argv[1:3]
out = f"{logo}/parts"
ra = np.load(f"{hi}/prints-hi.npy")
box = json.load(open(f"{hi}/hi.json"))["box"]
bird_d = open(f"{hi}/bird.d").read()
crop = ra[box[1]:box[3], box[0]:box[2]]
side = crop.shape[0]

INKS = {"red": (229, 32, 28), "ink": (27, 25, 22), "white": (255, 255, 255)}
for k, c in INKS.items():
    arr = np.zeros(crop.shape + (4,), np.uint8); arr[..., :3] = c
    arr[..., 3] = np.clip(crop * 255, 0, 255).astype(np.uint8)
    Image.fromarray(arr, "RGBA").save(f"{out}/mark-prints-{k}.png", optimize=True)
open(f"{out}/mark-bird.d", "w").write(bird_d)
json.dump({"side": side}, open(f"{out}/mark-parts.json", "w"))

WAYS = {"colour": ("red", "#1b1916"), "colour-dark": ("red", "#ffffff"), "black": ("ink", "#1b1916"),
        "white": ("white", "#ffffff"), "red": ("red", "#e5201c")}
for way, (pk, bird_fill) in WAYS.items():
    b64 = base64.b64encode(open(f"{out}/mark-prints-{pk}.png", "rb").read()).decode()
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {side} {side}" width="{side}" height="{side}">'
           f'<title>Seeds of Renaissance</title>'
           f'<image x="0" y="0" width="{side}" height="{side}" href="data:image/png;base64,{b64}"/>'
           f'<path fill="{bird_fill}" fill-rule="evenodd" d="{bird_d}"/></svg>')
    open(f"{logo}/mark/seeds-mark-{way}.svg", "w").write(svg)
    open(f"{logo}/mark/seeds-mark-{way}.png", "wb").write(bytes(resvg_py.svg_to_bytes(svg_string=svg, width=side)))
print("side", side)
