"""Final lockups (mark + wordmark) in every colourway, as SVG and PNG.
Layout matches the page's lockup bench exactly, using the saved "Final version" settings.
Step 4 of the logo build.
Usage: python -I lockups.py <Polyamine.ttf> <Fraunces-Italic[var].ttf> ../parts ../lockups
The "of" is Fraunces italic frozen at the chosen axes; both faces become outlines, no font files ship.
"""
import sys, os, base64, io, json
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from PIL import Image
import resvg_py

poly_p, fr_p, markdir, out = sys.argv[1:5]
os.makedirs(out, exist_ok=True)

FINAL = {"lineGap": 1.4, "markGap": 0.35, "markH": 2.7, "markH2": 1.1, "markS": 0.4,
         "ofGap": 0.8, "ofGapR": 0.8, "ofOpsz": 101, "ofShift": 0.17, "ofSize": 1.15, "ofSoft": 39,
         "ofWeight": 350, "ofWonk": 0, "track": 20}
F = FINAL

def shaper(path, ttfont=None):
    font = ttfont or TTFont(path)
    data = io.BytesIO(); font.save(data)
    face = hb.Face(hb.Blob(data.getvalue()))
    return font, hb.Font(face)

poly, poly_hb = shaper(poly_p)
C = poly["OS/2"].sCapHeight
SPACE = poly.getGlyphSet()["space"].width

fr_var = TTFont(fr_p)
fr = instancer.instantiateVariableFont(fr_var, {"opsz": F["ofOpsz"], "wght": F["ofWeight"], "SOFT": F["ofSoft"], "WONK": F["ofWonk"]})
fr, fr_hb = shaper(None, fr)
fr.save(os.path.join(out, "_fraunces-of-instance.ttf.tmp"))  # local only, deleted below

def run(font, hbfont, text, x, y, scale=1.0, track=0.0):
    """Shape text; return (svg path data list, advance) in Polyamine units."""
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(hbfont, buf, {"kern": True})
    gs, order = font.getGlyphSet(), font.getGlyphOrder()
    paths, cx = [], 0.0
    for i, (info, pos) in enumerate(zip(buf.glyph_infos, buf.glyph_positions)):
        pen = SVGPathPen(gs)
        gs[order[info.codepoint]].draw(TransformPen(pen, (scale, 0, 0, -scale, x + cx + i * track, y)))
        paths.append(pen.getCommands())
        cx += pos.x_advance * scale
    n = len(buf.glyph_infos)
    return paths, cx + track * (n - 1)

FR_SCALE = F["ofSize"] * C / fr["head"].unitsPerEm

def line(words, x, y):
    paths, cx = [], x
    for i, w in enumerate(words):
        if i:
            cx += SPACE * F["ofGap"] if w == "of" else SPACE * F["ofGapR"] if words[i - 1] == "of" else SPACE
        if w == "of":
            p, adv = run(fr, fr_hb, "of", cx, y - F["ofShift"] * C, FR_SCALE)
        else:
            p, adv = run(poly, poly_hb, w, cx, y, 1.0, F["track"])
        paths += p; cx += adv
    return paths, cx - x

WAYS = {  # prints ink, bird colour, text colour
    "colour": ("red", "#1b1916", "#1b1916"), "colour-dark": ("red", "#ffffff", "#ffffff"),
    "black": ("ink", "#1b1916", "#1b1916"), "white": ("white", "#ffffff", "#ffffff"), "red": ("red", "#e5201c", "#e5201c"),
}
# the mark is two parts: the fingerprint image (1130 px) and the bird as a vector path
SIDE = json.load(open(f"{markdir}/mark-parts.json"))["side"]
BIRD = open(f"{markdir}/mark-bird.d").read()
prints_b64 = {k: base64.b64encode(open(f"{markdir}/mark-prints-{k}.png", "rb").read()).decode() for k in ("red", "ink", "white")}

def svg(paths, marks, vb, ink, way):
    x0, y0, w, h = vb
    pk, bird_fill, _ = WAYS[way]
    imgs = "".join(f'<image x="{x:.1f}" y="{y:.1f}" width="{s:.1f}" height="{s:.1f}" href="data:image/png;base64,{prints_b64[pk]}"/>'
                   f'<path transform="translate({x:.2f} {y:.2f}) scale({s / SIDE:.6f})" fill="{bird_fill}" fill-rule="evenodd" d="{BIRD}"/>' for x, y, s in marks)
    body = "".join(f'<path d="{d}"/>' for d in paths if d)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.1f} {y0:.1f} {w:.1f} {h:.1f}" width="{w / 10:.0f}" height="{h / 10:.0f}">'
            f'<title>Seeds of Renaissance</title>{imgs}<g fill="{ink}">{body}</g></svg>')

pad = C * 0.25
L, LW = line(["SEEDS", "of", "RENAISSANCE"], 0, 0)
layouts = {}
# horizontal
M, gap = F["markH"] * C, F["markGap"] * C
p, _ = line(["SEEDS", "of", "RENAISSANCE"], M + gap, 0)
layouts["horizontal"] = (p, [(0, -C / 2 - M / 2, M)], (-pad, -C / 2 - M / 2 - pad, M + gap + LW + 2 * pad, M + 2 * pad))
# stacked
S, sg = F["markS"] * LW, C * 0.9
layouts["stacked"] = (L, [(LW / 2 - S / 2, -C - sg - S, S)], (-pad, -C - sg - S - pad, LW + 2 * pad, S + sg + C + C * 0.35 + 2 * pad))
# two lines beside the mark
lg = F["lineGap"] * C; blockH = C + lg; M3 = F["markH2"] * blockH; g3 = F["markGap"] * C
p1, a1 = line(["SEEDS", "of"], 0, 0); p2, a2 = line(["RENAISSANCE"], 0, 0); W3 = max(a1, a2)
midY = (-C + lg) / 2; top3 = min(-C, midY - M3 / 2); h3 = max(blockH + C * 0.3, M3)
pl = line(["SEEDS", "of"], M3 + g3, 0)[0] + line(["RENAISSANCE"], M3 + g3, lg)[0]
layouts["two-lines-left"] = (pl, [(0, midY - M3 / 2, M3)], (-pad, top3 - pad, M3 + g3 + W3 + 2 * pad, h3 + 2 * pad))
pr = line(["SEEDS", "of"], W3 - a1, 0)[0] + line(["RENAISSANCE"], W3 - a2, lg)[0]
layouts["two-lines-right"] = (pr, [(W3 + g3, midY - M3 / 2, M3)], (-pad, top3 - pad, W3 + g3 + M3 + 2 * pad, h3 + 2 * pad))
# wordmark alone
layouts["wordmark"] = (L, [], (-pad, -C - pad, LW + 2 * pad, C * 1.35 + 2 * pad))

index = {}
for name, (paths, marks, vb) in layouts.items():
    for way, (_, _, ink) in WAYS.items():
        doc = svg(paths, marks, vb, ink, way)
        base = f"seeds-logo-{name}-{way}"
        open(f"{out}/{base}.svg", "w").write(doc)
        for wpx in (2400, 1200):
            png = resvg_py.svg_to_bytes(svg_string=doc, width=wpx)
            open(f"{out}/{base}-{wpx}.png", "wb").write(bytes(png))
    index[name] = {"aspect": vb[2] / vb[3]}
os.remove(os.path.join(out, "_fraunces-of-instance.ttf.tmp"))
print({k: round(v["aspect"], 2) for k, v in index.items()})
