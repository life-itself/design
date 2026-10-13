"""Export the full mark (#4, every fingerprint) at standard sizes, in every colourway.
Step 3 of the logo build.
Usage: python -I sizes.py ../parts ../mark/sizes   (also writes ../favicon.ico)
No simplified drawings: the same full mark at every size (decided 2026-10-13).
Each size is drawn for its size: the bird is rendered from its vector path at exactly that size,
the fingerprints are reduced from the 1130 px image and lightly sharpened.
"""
import sys, json
from PIL import Image, ImageFilter
import resvg_py

src, out = sys.argv[1:3]
SIZES = (1024, 512, 256, 180, 128, 96, 64, 48, 32, 24, 16)
side = json.load(open(f"{src}/mark-parts.json"))["side"]
bird_d = open(f"{src}/mark-bird.d").read()
WAYS = {"colour": ("red", "#1b1916"), "colour-dark": ("red", "#ffffff"), "black": ("ink", "#1b1916"),
        "white": ("white", "#ffffff"), "red": ("red", "#e5201c")}
prints = {k: Image.open(f"{src}/mark-prints-{k}.png").convert("RGBA") for k in ("red", "ink", "white")}

def bird(px, fill):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {side} {side}" width="{px}" height="{px}">'
           f'<path fill="{fill}" fill-rule="evenodd" d="{bird_d}"/></svg>')
    import io
    return Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=svg, width=px)))).convert("RGBA")

def draw(way, px):
    pk, fill = WAYS[way]
    p = prints[pk].resize((px, px), Image.LANCZOS)
    if px <= 512:   # small reductions lose snap: a light unsharp mask on the prints' alpha
        r, g, b, a = p.split()
        a = a.filter(ImageFilter.UnsharpMask(radius=0.8, percent=70, threshold=0))
        p = Image.merge("RGBA", (r, g, b, a))
    return Image.alpha_composite(p, bird(px, fill))

for way in WAYS:
    for px in SIZES:
        draw(way, px).save(f"{out}/seeds-mark-{way}-{px}.png", optimize=True)
        if px <= 128:
            draw(way, px * 2).save(f"{out}/seeds-mark-{way}-{px}@2x.png", optimize=True)
fav = [draw("colour", s) for s in (16, 32, 48)]
fav[2].save(f"{out}/../favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)], append_images=fav[:2])
print("ok")
