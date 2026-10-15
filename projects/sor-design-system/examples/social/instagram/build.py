#!/usr/bin/env python3
"""Build the Instagram post templates (swallows and fingerprints from the bottom left).

The same background as the podcast thumbnail's bottom-left layout (examples/youtube/canva-kit, the
shared recipe in system/build/swallows.py): white, the black swallow engraving rising from the bottom-left
corner, the logo's fingerprints faded around it. Words sit above the birds; the lockup is top right
for now (provisional).

Writes one HTML page per PNG into src/; export.sh screenshots them into png/.
Every PNG is the full post size, so in Canva each one is dropped in and stretched to fill the page.
"""
import sys as _sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_sys.path.insert(0, str(HERE.parents[2] / "system" / "build"))
import swallows as sw  # noqa: E402

SRC = HERE / "src"
SYS = "../../../../system"           # from src/ to system/
FACE = f"{SYS}/img/otm-guest-placeholder-cut.png"
INK, MUTED = "#1b1916", "#5d584f"

# Two formats. All positions in px on the artboard.
# The logo (horizontal lockup) sits under the words in each template, as on the podcast cover.
# RINGS: fingerprint rings (cx, cy, size, rotation): one around the flock, one filling the corner.
# CLEAR: the prints fade out of this area, behind the words.
FORMATS = {
    "4x5": dict(W=1080, H=1350,
                SW=dict(x=-190, y=850, w=660, rot=-6),
                RINGS=[(130, 1240, 940, 15), (10, 1350, 600, 40)],
                CLEAR=(-200, -200, 1480, 1000)),
    "1x1": dict(W=1080, H=1080,
                SW=dict(x=-170, y=680, w=540, rot=-6),
                RINGS=[(120, 1000, 800, 15), (10, 1080, 520, 40)],
                CLEAR=(-200, -200, 1480, 780)),
}


def defs(F):
    return sw.defs(F["W"], F["H"], F.get("CLEAR"))


def prints(F, opacity=sw.PRINTS_OPACITY):
    return sw.prints(SYS, F["RINGS"], opacity)


def swallows(F):
    return sw.swallows(SYS, **F["SW"])


def logo(y, w=340, podcast=False, x=90):
    """The horizontal lockup at (x, y); with PODCAST after the name, in Polyamine, for podcast posts."""
    out = sw.lockup(SYS, x, y, w)
    if podcast:
        lh = w * sw.LOCKUP_ASPECT
        size = round(lh * 0.237 / 0.72, 1)
        out += (f'<text x="{x + w + size * 0.45:.1f}" y="{y + lh * 0.63:.1f}" font-family="Polyamine" '
                f'font-size="{size}" letter-spacing="{size * 0.02:.1f}" fill="{INK}">PODCAST</text>')
    return out


def apfel(x, y, size, text, fill=INK, weight=500):
    return f'<text x="{x}" y="{y}" font-family="Apfel Grotezk" font-weight="{weight}" font-size="{size}" fill="{fill}">{text}</text>'


def bg(F, quiet=False):
    """The background. quiet: fingerprints only, for carousel inner slides."""
    return sw.white(F["W"], F["H"]) + prints(F) + ("" if quiet else swallows(F))


# Type helpers. size in px; lines are baselines.
def poly(x, y, size, text, fill=INK, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text x="{x}" y="{y}" font-family="Polyamine" font-size="{size}" fill="{fill}"{a}>{text}</text>'


def resto(x, y, size, text, fill=INK):
    return f'<text x="{x}" y="{y}" font-family="Restora" font-weight="200" font-size="{size}" fill="{fill}">{text}</text>'


def brico(x, y, size, text, fill=INK, weight=600):
    return f'<text x="{x}" y="{y}" font-family="Bricolage Grotesque" font-weight="{weight}" font-size="{size}" fill="{fill}">{text}</text>'


def label(x, y, text, fill=MUTED, size=30):
    return (f'<text x="{x}" y="{y}" font-family="Apfel Grotezk" font-weight="500" font-size="{size}" letter-spacing="{size * 0.12:.1f}" '
            f'fill="{fill}">{text.upper()}</text>')


def lines(fn, x, y0, size, lh, texts, **kw):
    return "".join(fn(x, round(y0 + i * size * lh), size, t, **kw) for i, t in enumerate(texts))


def face(F, x, y, s, fade=False, flip=False):
    t = f' transform="translate({2 * x + s} 0) scale(-1 1)"' if flip else ""
    m = ' mask="url(#mFace)"' if fade else ""
    return f'<image href="{FACE}" x="{x}" y="{y}" width="{s}" height="{s}"{m}{t}/>'


# Guides: pink boxes for where things go. (x, y, w, h, label)
def guides(F, boxes):
    m = "#e0007a"
    lab = f'font-family="Apfel Grotezk, Arial, sans-serif" font-size="22" fill="{m}"'
    box = f'fill="{m}" fill-opacity=".06" stroke="{m}" stroke-width="2" stroke-dasharray="10 7"'
    out = ""
    for x, y, w, h, t in boxes:
        out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {box}/><text x="{x + 10}" y="{y - 10}" {lab} stroke="#fff" stroke-width="5" paint-order="stroke">{t}</text>'
    return out


# ---- The templates. Each: (format, quiet background?, content, guide boxes) ----
F4, F1 = FORMATS["4x5"], FORMATS["1x1"]

LG = lambda y, w=340, extra="": (90, y - 6, round(w * (1.37 if extra else 1)), round(w * 211 / 1200) + 12, "LOGO · lockup" + extra)

T = {
    "podcast-4x5": (F4, False,
        lines(poly, 90, 300, 124, 1.0, ["Hope isn't", "optimism"]) + apfel(90, 530, 54, "Guest Name")
        + logo(572, 360, podcast=True) + face(F4, 420, 660, 800),
        [(90, 200, 900, 230, "QUOTE · Polyamine 124 px · 2–3 lines, 3–6 words"),
         (90, 478, 600, 70, "NAME · Apfel Grotezk Mittel 54"),
         LG(572, 360, " + PODCAST in Polyamine"),
         (520, 690, 560, 660, "FACE · cut out, greyscale")]),
    "podcast-1x1": (F1, False,
        lines(poly, 90, 270, 108, 1.0, ["Hope isn't", "optimism"]) + apfel(90, 470, 48, "Guest Name")
        + logo(505, 300, podcast=True) + face(F1, 470, 340, 720),
        [(90, 182, 900, 205, "QUOTE · Polyamine 108 px · 2 lines"),
         (90, 424, 420, 62, "NAME · Apfel Grotezk Mittel 48"),
         LG(505, 300, " + PODCAST"),
         (560, 390, 520, 690, "FACE · cut out, greyscale")]),
    "quote-4x5": (F4, False,
        lines(resto, 90, 280, 84, 1.12, ["We are the bridge", "between the dying", "past and the", "future unborn."])
        + label(90, 650, "From the manifesto") + logo(700),
        [(90, 200, 900, 400, "QUOTE · Restora 84 px · up to ~20 words · Polyamine if 10 or fewer"),
         (90, 615, 600, 50, "SOURCE · Apfel 30, capitals"), LG(700)]),
    "quote-1x1": (F1, False,
        lines(resto, 90, 230, 72, 1.12, ["We are the bridge", "between the dying", "past and the", "future unborn."])
        + label(90, 545, "From the manifesto") + logo(585, 300),
        [(90, 160, 900, 330, "QUOTE · Restora 72 px · up to ~15 words"),
         (90, 510, 600, 50, "SOURCE · Apfel 30, capitals"), LG(585, 300)]),
    "announcement-4x5": (F4, False,
        label(90, 220, "Global Connection Call") + lines(poly, 90, 370, 140, 1.0, ["Find the", "others"])
        + brico(90, 600, 52, "Thursday 6 November · 18:00 UK") + brico(90, 670, 40, "An hour, online. Everyone welcome.", fill=MUTED, weight=400)
        + logo(725),
        [(90, 182, 600, 50, "SERIES · Apfel 30, capitals"),
         (90, 255, 900, 270, "TITLE · Polyamine 140 px · 2–4 words"),
         (90, 550, 900, 140, "WHEN · Bricolage SemiBold 52 · DETAIL · Bricolage 40"), LG(725)]),
    "statement-4x5": (F4, False,
        lines(poly, 90, 310, 116, 1.0, ["Vision and", "movement for", "civilisational", "rebirth"]) + logo(710),
        [(90, 222, 900, 440, "STATEMENT · Polyamine 116 px · 5–10 words"), LG(710)]),
    "statement-1x1": (F1, False,
        lines(poly, 90, 230, 100, 1.0, ["Vision and", "movement for", "civilisational", "rebirth"]) + logo(570, 300),
        [(90, 150, 900, 400, "STATEMENT · Polyamine 100 px · 5–10 words"), LG(570, 300)]),
    "carousel-1-cover-4x5": (F4, False,
        label(90, 220, "Seeds of Renaissance · 1/5") + lines(poly, 90, 350, 132, 1.0, ["What comes", "after", "modernity?"])
        + brico(90, 690, 40, "Swipe →", fill=MUTED, weight=500) + logo(735),
        [(90, 182, 600, 50, "SERIES AND COUNT · Apfel 30"),
         (90, 245, 900, 400, "TITLE · Polyamine 132 px · a question works well"),
         (90, 657, 300, 48, "PROMPT · Bricolage 40"), LG(735)]),
    "carousel-2-inner-4x5": (F4, True,
        resto(84, 360, 240, "1") + lines(brico, 90, 500, 56, 1.3,
            ["Modernity gave us", "abundance, and lost", "the thread of meaning."], weight=500)
        + label(90, 1170, "2/5") + logo(1205, 300),
        [(90, 195, 300, 190, "NUMBER · Restora 240 px"),
         (90, 445, 900, 230, "TEXT · Bricolage Medium 56 px · 10–20 words"),
         (90, 1135, 200, 50, "COUNT · Apfel 30"), LG(1205, 300)]),
    "carousel-5-close-4x5": (F4, False,
        lines(poly, 90, 320, 136, 1.0, ["Come to", "a call"])
        + lines(brico, 90, 560, 48, 1.3, ["An hour, online, once a month.", "Link in bio."], weight=500) + logo(690),
        [(90, 210, 900, 270, "CALL TO ACTION · Polyamine 136 px"),
         (90, 515, 900, 130, "DETAIL · Bricolage Medium 48"), LG(690)]),
}

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{name}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..600&display=swap">
<link rel="stylesheet" href="{sys}/fonts.css">
<style>
@font-face{{font-family:"Polyamine";src:url({sys}/fonts/Polyamine-Regular.woff2) format("woff2")}}
@font-face{{font-family:"Restora";font-weight:200;src:url({sys}/fonts/Restora-ExtraLight.woff2) format("woff2")}}
html,body{{margin:0;background:transparent}} svg{{display:block}}
</style></head><body>
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">{defs}{body}</svg>
</body></html>
"""


def pages():
    out = {}
    # Free-standing elements. (The lockup and the full-strength prints are copied as files by export.sh.)
    E = dict(W=1000, H=1000, RINGS=[(500, 500, 1000, 0)])
    out["element-fingerprint-ring-faded"] = (E, prints(E))
    for key, F in FORMATS.items():
        out[f"bg-{key}"] = (F, bg(F))
        out[f"bg-{key}-quiet"] = (F, bg(F, quiet=True))
        out[f"layer-{key}-swallows"] = (F, swallows(F))
        out[f"layer-{key}-fingerprints"] = (F, prints(F))
    for name, (F, quiet, content, boxes) in T.items():
        base = bg(F, quiet)
        out[f"example-{name}"] = (F, base + content)
        out[f"guides-{name}"] = (F, guides(F, boxes))
        out[f"example-{name}-with-guides"] = (F, base + content + guides(F, boxes))
    return out


if __name__ == "__main__":
    SRC.mkdir(exist_ok=True)
    for old in SRC.glob("*.html"):
        old.unlink()
    for name, (F, body) in pages().items():
        (SRC / f"{name}.html").write_text(PAGE.format(name=name, sys=SYS, W=F["W"], H=F["H"], defs=defs(F), body=body))
        print(name)
