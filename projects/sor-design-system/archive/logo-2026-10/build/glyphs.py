"""Polyamine words as SVG path data, per glyph, with the font's kerning (via HarfBuzz).
Outlines only: the font file itself is never published.
Used by logo-set.html (the lockup workbench).
Usage: python -I glyphs.py <Polyamine.ttf> ../parts/wordmark-glyphs.json
"""
import sys, json
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ttf, out = sys.argv[1:3]
font = TTFont(ttf)
gs = font.getGlyphSet()
upem = font["head"].unitsPerEm
blob = hb.Blob.from_file_path(ttf)
hbfont = hb.Font(hb.Face(blob))

def word(text):
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(hbfont, buf, {"kern": True, "liga": True})
    order = font.getGlyphOrder()
    glyphs, x = [], 0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        name = order[info.codepoint]
        pen = SVGPathPen(gs)
        # flip y so the baseline is y=0 and caps go up to -capHeight
        gs[name].draw(TransformPen(pen, (1, 0, 0, -1, x + pos.x_offset, -pos.y_offset)))
        glyphs.append({"d": pen.getCommands(), "x": x, "adv": pos.x_advance})
        x += pos.x_advance
    return {"glyphs": glyphs, "width": x}

data = {"upem": upem, "cap": font["OS/2"].sCapHeight, "space": gs["space"].width,
        "SEEDS": word("SEEDS"), "RENAISSANCE": word("RENAISSANCE"), "O": word("O"), "F": word("F"), "S": word("S"), "R": word("R")}
json.dump(data, open(out, "w"))
print(data["cap"], data["SEEDS"]["width"], data["RENAISSANCE"]["width"], data["space"])
