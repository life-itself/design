#!/usr/bin/env python3
"""Build the podcast's square artwork: the show art (one image for the whole podcast).

Pure sunlight, the swallows and fingerprints from the bottom left (system/swallows.py, as on the
episode cover), the mark, SEEDS of RENAISSANCE big, PODCAST small: in a podcast app everyone
already knows it's a podcast, so the name leads.

Drawn on a 1000 × 1000 artboard; export.sh renders it at 3× (3000 × 3000), the size Apple and
Spotify ask for. Square episode art is the Instagram 1:1 podcast template, exported at 3000 too.
"""
import sys as _sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_sys.path.insert(0, str(HERE.parents[1] / "system"))
import swallows as sw  # noqa: E402

SRC = HERE / "src"
SYS = "../../../system"            # from src/ to system/
INK = "#1b1916"
W = H = 1000

MARK = dict(cx=500, y=120, s=330)                         # the mark, centred
NAME = dict(w=860, y=495)                                 # the wordmark, nearly the full width
POD = dict(size=46, y=650)                                # PODCAST, small
SW = dict(x=-140, y=660, w=480, rot=-6)
RINGS = [(150, 960, 860, 15), (0, 1000, 560, 40)]
CLEAR = (60, 60, 880, 640)


def show_art(wash=False):
    nh = round(NAME["w"] * 291 / 2400)
    return (sw.white(W, H, wash) + sw.prints(SYS, RINGS) + sw.swallows(SYS, **SW)
            + f'<image href="{SYS}/logo/mark/seeds-mark-colour.png" x="{MARK["cx"] - MARK["s"] / 2}" y="{MARK["y"]}" width="{MARK["s"]}" height="{MARK["s"]}"/>'
            + f'<image href="{SYS}/logo/lockups/seeds-logo-wordmark-colour-2400.png" x="{(W - NAME["w"]) / 2}" y="{NAME["y"]}" width="{NAME["w"]}" height="{nh}"/>'
            + f'<text x="{W / 2}" y="{POD["y"]}" text-anchor="middle" font-family="Polyamine" font-size="{POD["size"]}" '
              f'letter-spacing="{POD["size"] * 0.3:.0f}" fill="{INK}">PODCAST</text>')


PAGES = {"show-art": show_art(), "show-art-wash": show_art(wash=True)}

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{name}</title>
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
