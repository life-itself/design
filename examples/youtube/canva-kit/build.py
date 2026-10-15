#!/usr/bin/env python3
"""Build the Canva kit for the podcast thumbnail: swallows and fingerprints from the bottom left.

Writes one HTML page per layer into src/, then export.sh screenshots each one into png/.
Every layer is a full 1280 × 720 canvas, so in Canva each PNG is dropped in and stretched
to fill the page, and everything lands in the right place.

The ground itself (white, swallows, fingerprints, logo) comes from system/build/swallows.py,
shared with the Instagram templates. The earlier top-left layout is archived in
archive/podcast-thumbnails-2026-10/.
"""
import sys as _sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_sys.path.insert(0, str(HERE.parents[2] / "system" / "build"))
import swallows as sw  # noqa: E402

SRC = HERE / "src"
SYS = "../../../../system"          # from src/ to system/
FACE = f"{SYS}/img/otm-guest-placeholder-cut.png"
INK = "#1b1916"
W, H = 1280, 720

# Layout, on the 1280 × 720 artboard
Q = dict(x=80, size=112, base1=185, base2=297)           # quote: two lines of Polyamine; left margin matches the head's crop on the right
NAME = dict(x=80, size=48, base=375)                      # guest name: Apfel Grotezk Mittel
LOGO = dict(x=80, y=405, w=330)                           # the lockup with "PODCAST" after the name, under the guest's name
SW = dict(x=-150, y=520, w=500, rot=-6)                   # the swallow flock, tucked into the bottom-left corner
RINGS = [(120, 700, 700, 15), (0, 720, 480, 40)]         # fingerprint rings: around the flock, and filling the corner
CLEAR = (10, 40, 710, 480)                                # the prints fade out of this area, behind the words


def background(wash=False):
    return sw.white(W, H, wash) + sw.prints(SYS, RINGS) + sw.swallows(SYS, **SW)


def logo():
    """The horizontal lockup, then PODCAST on the same line in Polyamine, like the name, at the same cap height."""
    w, lh = LOGO["w"], LOGO["w"] * sw.LOCKUP_ASPECT
    cap = lh * 0.237                                    # cap height of the name inside the lockup
    base = LOGO["y"] + lh * 0.63                        # baseline of the name inside the lockup
    size = round(cap / 0.72, 1)
    return (sw.lockup(SYS, **LOGO) +
            f'<text x="{LOGO["x"] + w + size * 0.45:.1f}" y="{base:.1f}" font-family="Polyamine" '
            f'font-size="{size}" letter-spacing="{size * 0.02:.1f}" fill="{INK}">PODCAST</text>')


def face_one():
    return f'<image href="{FACE}" x="560" y="10" width="800" height="800"/>'


def face_two():
    back = (f'<image href="{FACE}" x="520" y="70" width="640" height="640" mask="url(#mFace)" '
            f'transform="translate({2 * 520 + 640} 0) scale(-1 1)"/>')
    front = f'<image href="{FACE}" x="800" y="40" width="700" height="700" mask="url(#mFace)"/>'
    return back + front


def words(name="Guest Name", name_size=48):
    return (f'<text x="{Q["x"]}" y="{Q["base1"]}" font-family="Polyamine" font-size="{Q["size"]}" fill="{INK}">Hope isn\'t</text>'
            f'<text x="{Q["x"]}" y="{Q["base2"]}" font-family="Polyamine" font-size="{Q["size"]}" fill="{INK}">optimism</text>'
            f'<text x="{NAME["x"]}" y="{NAME["base"]}" font-family="Apfel Grotezk" font-weight="500" font-size="{name_size}" fill="{INK}">{name}</text>')


def guides():
    m = "#e0007a"
    lab = f'font-family="Apfel Grotezk, Arial, sans-serif" font-size="17" fill="{m}" stroke="#fff" stroke-width="5" paint-order="stroke"'
    box = f'fill="{m}" fill-opacity=".06" stroke="{m}" stroke-width="2" stroke-dasharray="8 6"'
    qtop = Q["base1"] - 89
    lh = round(LOGO["w"] * sw.LOCKUP_ASPECT)
    lw = round(LOGO["w"] * 1.37)                            # the lockup plus PODCAST
    return (
        f'<rect x="{Q["x"]}" y="{qtop}" width="530" height="215" {box}/>'
        f'<text x="{Q["x"] + 8}" y="{qtop - 8}" {lab}>QUOTE · Polyamine 112 px · 2 lines, 3–5 words · max width 530</text>'
        f'<rect x="{Q["x"]}" y="{NAME["base"] - 44}" width="530" height="58" {box}/>'
        f'<text x="{Q["x"] + 300}" y="{NAME["base"] - 8}" {lab}>NAME · Apfel Grotezk Mittel 48</text>'
        f'<rect x="{LOGO["x"]}" y="{LOGO["y"] - 6}" width="{lw}" height="{lh + 12}" {box}/>'
        f'<text x="{LOGO["x"] + 8}" y="{LOGO["y"] + lh + 30}" {lab}>LOGO · lockup + PODCAST in Polyamine · always here</text>'
        f'<rect x="650" y="20" width="610" height="700" {box}/>'
        f'<text x="662" y="44" {lab}>FACE · cut out, greyscale · head 70–80% of the height</text>'
        f'<rect x="1090" y="640" width="190" height="80" fill="{m}" fill-opacity=".22"/>'
        f'<text x="1270" y="632" text-anchor="end" {lab}>KEEP CLEAR · YouTube time</text>'
        f'<text x="300" y="640" {lab}>SWALLOWS + FINGERPRINTS · background</text>'
    )


PAGES = {
    "01-background": background(),
    "01-background-wash": background(wash=True),
    "02-background-with-logo": background() + logo(),
    "02-background-with-logo-wash": background(wash=True) + logo(),
    "03-swallows": sw.swallows(SYS, **SW),
    "04-fingerprints": sw.prints(SYS, RINGS),
    "05-logo": logo(),
    "06-guest-example": face_one(),
    "07-two-guests-example": face_two(),
    "08-guides": guides(),
    "example-one-guest": background() + face_one() + words() + logo(),
    "example-two-guests": background() + face_two() + words("Name One &amp; Name Two", 42) + logo(),
    "example-with-guides": background() + face_one() + words() + logo() + guides(),
}

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{name}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600&display=swap">
<link rel="stylesheet" href="{sys}/fonts.css">
<style>
@font-face{{font-family:"Polyamine";src:url({sys}/fonts/Polyamine-Regular.woff2) format("woff2")}}
html,body{{margin:0;background:transparent}} svg{{display:block}}
</style></head><body>
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">{defs}{body}</svg>
</body></html>
"""

if __name__ == "__main__":
    SRC.mkdir(exist_ok=True)
    for old in SRC.glob("*.html"):
        old.unlink()
    for name, body in PAGES.items():
        (SRC / f"{name}.html").write_text(PAGE.format(name=name, sys=SYS, W=W, H=H, defs=sw.defs(W, H, CLEAR), body=body))
        print(name)
