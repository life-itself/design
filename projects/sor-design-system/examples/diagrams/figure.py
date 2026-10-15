"""A new Seeds of Renaissance figure, from scratch: copy this file into your own repo, change
the content in FIGURE, run it. Rules: diagrams.md. More drawings to borrow from (curves and a
shaded gap, layers with brackets, line, bar and dot charts): build.py beside this file.

Text is set as outlines in Apfel Grotezk, so the SVG renders anywhere without the fonts.
draw() lays panels out in a row; for another shape (a cycle, a grid, layers) write your own
draw() with the same helpers. From system/build/outline.py: apfel and apfel_m (Regular and Mittel;
.cap is the cap height as a fraction of the size, .path() measures and outlines text),
signature(theme, url) returns (svg, width) with height DISC, and write_figure() crops the SVG to
the drawing: the margin M on three sides, and the bottom at H - foot.

Run:  python figure.py [out-name]
  -> out-name.svg (tight, transparent: for a paper or a web page; commit this one)
     out-name.share.png, .share@2x.png (the full canvas on white: for sharing alone)
Needs: fonttools, uharfbuzz (python3 -m venv .venv && .venv/bin/pip install fonttools uharfbuzz),
Google Chrome for the PNGs ($CHROME), and the design repo: ~/src/life-itself/design, or set
SOR_SYSTEM to its projects/sor-design-system/system folder."""
import math, os, pathlib, sys

SOR = pathlib.Path(os.environ.get("SOR_SYSTEM", pathlib.Path.home() / "src/life-itself/design/projects/sor-design-system/system"))
sys.path.insert(0, str(SOR / "build"))
from outline import apfel, apfel_m, signature, write_figure, INK, RED, DISC  # noqa: E402

# ── The content: change this ─────────────────────────────────────
FIGURE = dict(
    title="From Crisis to Renaissance",                     # ideally the claim, title case
    subtitle="Three movements, each making the next possible",  # what the figure shows, one line
    signature="seedsofrenaissance.org",                     # or a publication line, or None
    key=2,                                                  # the panel the figure is about (red label), or None
    panels=[  # heading, lines (sentence case)
        ("Sensemaking", ["Seeing the crisis", "beneath the crises"]),
        ("New practices", ["Living the change", "in small groups"]),
        ("Renaissance", ["A culture that", "wants what's good"]),
    ],
)

# ── The house style (diagrams.md): sizes at a 1600 px canvas ─────
M, SIG_FOOT, SIG_GAP = 72, 56, 36   # margin; signature to the bottom edge; drawing to the signature
TINT = "#fbdbdb"                    # the red tint: the logo red at 16% on white. Panels and the key area
PAD, GAP = 40, 110                  # inside a panel, all four sides; between panels (room for an arrow)
LW, LW2, HEAD = 4, 2, 18            # line for what matters, line for scaffolding, arrowhead length (24 on a 4 px line)
TITLE, SUBTITLE, HEADING, LABEL, TAG = 46, 28, 32, 29, 21


def text(s, size, x, y, face=apfel, opacity=1.0, anchor="start", colour=None, track=0.0):
    """Outlined text, baseline at y. Returns (svg, width)."""
    d, w = face.path(s, size, 0, 0, track=track)
    dx = x - {"start": 0, "middle": w / 2, "end": w}[anchor]
    attrs = (f' fill-opacity="{opacity}"' if opacity < 1 else "") + (f' fill="{colour}"' if colour else "")
    return f'<path transform="translate({dx:.1f} {y:.1f})" d="{d}"{attrs}/>', w


def tag(s, x, y, anchor="start", colour=None):  # axis names and one-to-three-word tags: Apfel Mittel, uppercase, tracked
    return text(s.upper(), TAG, x, y, apfel_m, anchor=anchor, colour=colour, track=TAG * 0.1)[0]


def arrow(pts, colour=INK, sw=LW2, L=HEAD):
    """A solid line with a solid arrowhead at the end; the line stops at the head's base."""
    pts = list(pts)
    a = math.atan2(pts[-1][1] - pts[-2][1], pts[-1][0] - pts[-2][0])
    tip = pts[-1]
    pts[-1] = (tip[0] - 0.8 * L * math.cos(a), tip[1] - 0.8 * L * math.sin(a))
    w, bx, by = L * 0.4, tip[0] - L * math.cos(a), tip[1] - L * math.sin(a)
    nx, ny = -math.sin(a) * w, math.cos(a) * w
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    return (f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M{tip[0]:.1f} {tip[1]:.1f} L{bx + nx:.1f} {by + ny:.1f} L{bx - nx:.1f} {by - ny:.1f} Z" fill="{colour}"/>')


def panel(x, y, head, lines, key=False):
    """A panel: no outline, square corners, the red tint, as wide as its longest line plus PAD.
    Returns (svg, width, height). Only the key panel's heading is red."""
    cap = apfel_m.cap * HEADING
    w = max([apfel_m.path(head, HEADING, 0, 0)[1]] + [apfel.path(t, LABEL, 0, 0)[1] for t in lines]) + 2 * PAD
    out, ty = [], y + PAD + cap                     # the heading's capitals sit PAD below the top
    out.append(text(head, HEADING, x + PAD, ty, apfel_m, colour=RED if key else None)[0])
    ty += 8 if lines else 0
    for t in lines:
        ty += 42
        out.append(text(t, LABEL, x + PAD, ty)[0])
    h = ty - y + PAD                                 # last baseline to the bottom edge: PAD again
    return f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h:.1f}" fill="{TINT}"/>' + "".join(out), w, h


def draw(f):
    out, x, top = [], M, M + 170
    boxes = []
    for i, (head, lines) in enumerate(f["panels"]):
        svg, w, h = panel(x, top, head, lines, key=(i == f["key"]))
        out.append(svg); boxes.append((x, w, h)); x += w + GAP
    for (x0, w0, h0), (x1, _, _) in zip(boxes, boxes[1:]):  # arrows between panels, at the headings' height
        y = top + PAD + apfel_m.cap * HEADING / 2
        out.append(arrow([(x0 + w0 + 22, y), (x1 - 22, y)]))
    sig, sw = signature("light", url=f["signature"])
    W = round(max(x - GAP + M, M + sw + M))                # the canvas is as wide as the drawing
    H = round(top + max(h for _, _, h in boxes) + SIG_GAP + 24 + DISC + SIG_FOOT)
    out += [text(f["title"], TITLE, M, M + 42)[0],
            text(f["subtitle"], SUBTITLE, M, M + 84, opacity=0.6)[0],
            f'<g transform="translate({W - M - sw:.1f} {H - SIG_FOOT - DISC})">{sig}</g>']
    return "".join(out), W, H


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "figure"
    body, W, H = draw(FIGURE)
    write_figure(pathlib.Path(name + ".svg"), FIGURE["title"], body, W, H, M, SIG_FOOT)
