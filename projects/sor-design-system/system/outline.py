"""Text to SVG outlines, and the diagram signature, for the build scripts.

Outlining (fontTools + HarfBuzz, with kerning) makes signature text render the same
everywhere, without the fonts installed. Used by build-signature.py and
examples/diagrams/build.py. Needs: fonttools, uharfbuzz.

The signature (decided 2026-10-07, diagrams.md): mark, then the name and an optional
second part (the URL, or a publication line such as "Wisdom · White paper No. 6") set in
Apfel Grotezk at 60% ink, one line. url=None gives the name alone. Light: the mark on its white disc. Dark: the
inverted mark (provisional, design-34t.24), no disc. Sizes are for a 1600px export."""
import base64, math, pathlib
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

SYSTEM = pathlib.Path(__file__).resolve().parent
URL = "seeds-domain.tbd"  # placeholder until the domain is decided (brand.md Open)
NAME = "Seeds of Renaissance"
INK, CHALK, WHITE, NIGHT, RED = "#1b1916", "#ece7dc", "#ffffff", "#171613", "#e5201c"
THEMES = {"light": dict(ground=WHITE, ink=INK), "dark": dict(ground=NIGHT, ink=CHALK)}


class Face:
    def __init__(self, path):
        self.tt = TTFont(path)
        self.glyphs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()
        self.upem = self.tt["head"].unitsPerEm
        self.cap = self.tt["OS/2"].sCapHeight / self.upem
        self.hb = hb.Font(hb.Face(hb.Blob.from_file_path(str(path))))

    def path(self, text, size, x, y, track=0.0, skew=0.0):
        """SVG path d for text with its baseline at (x, y). Returns (d, width)."""
        buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
        hb.shape(self.hb, buf, {"kern": True, "liga": True})
        sc, cx = size / self.upem, 0.0
        pen = SVGPathPen(self.glyphs, ntos=lambda v: f"{v:.1f}")
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            t = (sc, 0, sc * math.tan(math.radians(skew)), -sc, x + cx + pos.x_offset * sc, y - pos.y_offset * sc)
            self.glyphs[self.order[info.codepoint]].draw(TransformPen(pen, t))
            cx += pos.x_advance * sc + track
        return pen.getCommands(), cx - track


apfel = Face(SYSTEM / "fonts/ApfelGrotezk-Regular.otf")
apfel_m = Face(SYSTEM / "fonts/ApfelGrotezk-Mittel.otf")


def b64(p, mime="image/png"):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()


DISC, TXT = 64, 20  # at a 1600px export: mark 64px (diagrams.md minimum), text 20px


def _baseline(face, size):
    return DISC / 2 + face.cap * size / 2


def signature(theme, url=URL, mark_ref=None):
    """The signature as an SVG fragment, origin top-left, height DISC. Returns (svg, width).
    mark_ref: id of a <symbol> holding the mark (pages that share one copy); otherwise
    the mark is embedded."""
    ink = THEMES[theme]["ink"]
    r, m = DISC / 2, DISC * (0.85 if theme == "light" else 1)
    img = "img/logo-256.png" if theme == "light" else "img/logo-inverted-256.png"
    if mark_ref:
        mark = f'<use href="#{mark_ref}-{theme}" x="{r - m / 2:.1f}" y="{r - m / 2:.1f}" width="{m:.1f}" height="{m:.1f}"/>'
    else:
        mark = f'<image x="{r - m / 2:.1f}" y="{r - m / 2:.1f}" width="{m:.1f}" height="{m:.1f}" href="{b64(SYSTEM / img)}"/>'
    if theme == "light":  # the mark is a square image on white: clip it to its disc
        disc = (f'<clipPath id="sor-disc"><circle cx="{r}" cy="{r}" r="{r}"/></clipPath>'
                f'<circle cx="{r}" cy="{r}" r="{r}" fill="{WHITE}"/>')
        mark = f'<g clip-path="url(#sor-disc)">{mark}</g>'
    else:
        disc = ""
    x, y = DISC + 18, _baseline(apfel_m, TXT)
    d1, w1 = apfel_m.path(NAME.upper(), TXT, x, y, track=TXT * 0.1)
    dot = x + w1 + 14
    if not url:
        return disc + mark + f'<path d="{d1}" fill="{ink}" fill-opacity=".6"/>', x + w1
    d2, w2 = apfel.path(url, TXT, dot + 18, y, track=TXT * 0.02)
    text = (f'<g fill="{ink}" fill-opacity=".6"><path d="{d1}"/>'
            f'<circle cx="{dot + 2:.1f}" cy="{r:.1f}" r="2.2"/><path d="{d2}"/></g>')
    return disc + mark + text, dot + 18 + w2
