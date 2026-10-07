"""Build the diagram examples (design-34t.20, .25):

  index.html  the signature (decided 2026-10-07: mark + name and URL in Apfel) on three
              real figures from 2rbook, light and dark, at a 1600px export and at 400px
  fonts.html  type for diagrams: Apfel only, no bold; two figures redrawn
  style.html  drawing style: fine, panel and hand, and the figures in a paper page and a web article

Signature text is outlined (system/outline.py). Figures in figures/ are copied from 2rbook,
flattened onto white with the gamma chunk dropped so they render true black.

Run:  python build.py                 -> index.html, fonts.html (link ../../system/fonts.css)
      python build.py --bundle DIR    -> DIR/index.html, DIR/fonts.html, self-contained, for publishing
Needs: fonttools, uharfbuzz."""
import base64, math, pathlib, sys
here = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent.parent / "system"))
from outline import SYSTEM, DISC, THEMES, RED, signature, b64, apfel, apfel_m
apfel_cap = apfel.cap

URL = "seeds-domain.tbd/wisdom"  # a paper's page; placeholder until the domain is decided
W, M = 1600, 72                  # export width, margin
SIG_GAP, SIG_FOOT = 36, 56       # figure to signature, signature to bottom edge
SIG = {th: signature(th, URL, mark_ref="mark") for th in THEMES}

def sig_at(H, theme, width=W):
    svg, w = SIG[theme]
    return f'<g class="sig" transform="translate({width - M - w:.1f} {H - SIG_FOOT - DISC})">{svg}</g>'

# ── Real figures ─────────────────────────────────────────────────
FIGS = [
    dict(id="gap", file="wisdom-gap-figure.png", w=624, h=387, src="2rbook/wisdom/assets",
         title="The wisdom gap", note="Wisdom paper. The source is 624px wide, so it blurs at 1600: re-export at 3x.",
         mask=[(0, 0, 110, 40)]),  # Life Itself badge, top left
    dict(id="val", file="introduction-valueception-diagram.png", w=624, h=323, src="2rbook/wisdom/assets",
         title="Wisdom as a practical capacity", note="Wisdom paper. Also 624px. Red line work beside the red of the mark.",
         mask=[]),
    dict(id="poly", file="from-polycrisis-to-metacrisis-diagram.png", w=1741, h=1330, src="2rbook/framework/assets",
         title="From polycrisis to metacrisis", note="Framework. A tall, dense figure at full resolution.",
         mask=[(1410, 10, 331, 150)]),  # Life Itself Sensemaking Studio badge, top right
]

def figure_svg(f, theme):
    fw = W - 2 * M
    fh = round(fw * f["h"] / f["w"])
    H = M + fh + SIG_GAP + DISC + SIG_FOOT
    filt = ' filter="url(#to-night)"' if theme == "dark" else ""
    return (f'<svg class="fig" viewBox="0 0 {W} {H}" role="img" aria-label="{f["title"]}, {theme}">'
            f'<rect width="{W}" height="{H}" fill="{THEMES[theme]["ground"]}"/>'
            f'<g{filt}><use href="#fig-{f["id"]}" x="{M}" y="{M}" width="{fw}" height="{fh}"/></g>{sig_at(H, theme)}</svg>')

def fig_symbol(f):
    masks = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#ffffff"/>' for x, y, w, h in f["mask"])
    return (f'<symbol id="fig-{f["id"]}" viewBox="0 0 {f["w"]} {f["h"]}">'
            f'<image width="{f["w"]}" height="{f["h"]}" href="{b64(here / "figures" / f["file"])}"/>{masks}</symbol>')

# ── Redrawn figures ──────────────────────────────────────────────
# Drawing styles (design-34t.26), widths at 1600px. Chosen 2026-10-08: panel.
#   fine   Tufte: thin lines, hairline scaffolding, no boxes (layers sit on rules)
#   panel  FT/Economist: no outlines; layers and the accent area in the red tint; bolder lines
# All arrowheads are solid. Lines are solid: no dashes.
STYLES = {
    "fine":  dict(lw=3, lw2=1.5, head=16, box="rule", gap="arrow"),
    "panel": dict(lw=4, lw2=2, head=18, box="panel", gap="shade"),
}
# The red tint: the logo red at 16% on white, 22% on night. Panels and accent areas, never text.
# (Tried warm grey panels with red only for the accent: too faint at 400px and on a web page.)
TINT = {"light": "#fbdbdb", "dark": "#441815"}
PANEL = TINT
PAD = 40  # inside a panel: the same on all four sides (cap height at the top, baseline at the bottom)

def _head(q, a, color, L):
    w = L * 0.4
    bx, by = q[0] - L * math.cos(a), q[1] - L * math.sin(a)
    nx, ny = -math.sin(a) * w, math.cos(a) * w
    return f'<path d="M{q[0]:.1f} {q[1]:.1f} L{bx + nx:.1f} {by + ny:.1f} L{bx - nx:.1f} {by - ny:.1f} Z" fill="{color}"/>'

def line(pts, color, sw):
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'

def arrow(pts, color, sw, L, both=False):
    """A line with a solid arrowhead at the end (and the start, if both). The line stops at the head's base."""
    pts = list(pts)
    def angle(p, q): return math.atan2(q[1] - p[1], q[0] - p[0])
    a1 = angle(pts[-2], pts[-1]); tip1 = pts[-1]
    pts[-1] = (tip1[0] - 0.8 * L * math.cos(a1), tip1[1] - 0.8 * L * math.sin(a1))
    heads = _head(tip1, a1, color, L)
    if both:
        a0 = angle(pts[1], pts[0]); tip0 = pts[0]
        pts[0] = (tip0[0] - 0.8 * L * math.cos(a0), tip0[1] - 0.8 * L * math.sin(a0))
        heads += _head(tip0, a0, color, L)
    return line(pts, color, sw) + heads

def gap_svg(theme="light", style="panel"):
    S = STYLES[style]
    ink, H = THEMES[theme]["ink"], 1080
    x0, x1, axis = 120, 1330, 900
    tech = lambda t: 830 - 660 * (math.exp(4.2 * t) - 1) / (math.exp(4.2) - 1)
    wis = lambda t: 872 - 250 * (math.exp(1.6 * t) - 1) / (math.exp(1.6) - 1)
    tp = [(x0 + (x1 - x0) * i / 60, tech(i / 60)) for i in range(61)]
    wp = [(x0 + (x1 - x0) * i / 60, wis(i / 60)) for i in range(61)]
    out = [f'<rect width="{W}" height="{H}" fill="{THEMES[theme]["ground"]}"/>']
    if S["gap"] == "shade":  # the accent as an area: the space between the curves, in the red tint
        area = tp[30:] + wp[30:][::-1]
        out.append(f'<path d="M{" L".join(f"{x:.1f} {y:.1f}" for x, y in area)} Z" fill="{TINT[theme]}"/>')
        out.append(f'<text x="1150" y="575" class="d-tag" fill="{RED}">Wisdom gap</text>')
    out += [f'<text x="{M}" y="{M + 42}" class="d-title" fill="{ink}">The wisdom gap</text>',
            f'<text x="{M}" y="{M + 84}" class="d-subtitle" fill="{ink}">Our power grows faster than our capacity to use it well</text>',
            arrow([(x0 - 40, axis), (x1 + 90, axis)], ink, S["lw2"], S["head"] - 4),
            f'<text x="{x1 + 90}" y="{axis + 44}" text-anchor="end" class="d-tag" fill="{ink}">Time</text>',
            arrow(tp, ink, S["lw"], S["head"] + 4), arrow(wp, ink, S["lw"], S["head"] + 4)]
    if S["gap"] == "arrow":
        gx = 1180; t = (gx - x0) / (x1 - x0); ty, wy = tech(t) + 14, wis(t) - 14
        out += [arrow([(gx, ty), (gx, wy)], RED, S["lw"], S["head"], both=True),
                f'<text x="{gx + 26}" y="{(ty + wy) / 2 + 7}" class="d-tag" fill="{RED}">Wisdom gap</text>']
    out += [f'<text class="d-label" fill="{ink}" text-anchor="end"><tspan x="1220" y="240">Technological capability</tspan><tspan x="1220" dy="1.3em">and/or social complexity</tspan></text>',
            f'<text class="d-label" fill="{ink}" text-anchor="end"><tspan x="1330" y="770">“Wisdom”: our capacity</tspan><tspan x="1330" dy="1.3em">to manage that complexity</tspan></text>']
    return f'<svg class="fig" viewBox="0 0 {W} {H}" role="img" aria-label="The wisdom gap, redrawn">{"".join(out)}{sig_at(H, theme)}</svg>'

def poly_svg(theme="light", style="panel"):
    S = STYLES[style]
    ink = THEMES[theme]["ink"]
    framed = S["box"] != "rule"
    pad = PAD if framed else 0
    cap = apfel_cap * TYPE["head"][1]
    boxes = [  # heading, secondary lines, body lines, bullets?
        ("Surface layer", ["Manifest crises"],
         ["Escalating, interacting global crises", "such as the climate crisis and tech x-risk"], False),
        ("Intermediate layer", ["Meta-systemic dysfunctions"],
         ["Collective action problems", "Exponential tech and the wisdom gap", "Degradation of sense-making systems"], True),
        ("Root layer", ["Foundational ideologies (cultural paradigms)", "and deep human tendencies"],
         ["Deep ideological features", "Core aspects of humanity"], True),
    ]
    # boxes as wide as their longest line plus padding, not wider (measured with the font itself)
    widest = max([apfel_m.path(b[0], TYPE["head"][1], 0, 0)[1] for b in boxes]
                 + [apfel.path(t, TYPE["sub"][1], 0, 0)[1] for b in boxes for t in b[1]]
                 + [apfel.path(t, TYPE["label"][1], 0, 0)[1] + (28 if b[3] else 0) for b in boxes for t in b[2]])
    bx, bw = M, round(widest + 2 * pad + 8)
    out, y, placed, GAP = [], 210, [], 84
    for i, (head, sub, lines, bullets) in enumerate(boxes):
        top_pad = pad if framed else 34
        text, ty = [], y + top_pad + cap  # heading baseline: its cap height sits pad below the top
        text.append(f'<text x="{bx + pad}" y="{ty:.1f}" class="d-head" fill="{ink}">{head}</text>')
        for t in sub:
            ty += 36; text.append(f'<text x="{bx + pad}" y="{ty:.1f}" class="d-sub" fill="{ink}">{t}</text>')
        ty += 20
        for ln in lines:
            ty += 44  # label baselines; the first sits a clear step below the secondary lines
            if bullets:
                text.append(f'<circle cx="{bx + pad + 6}" cy="{ty - 10:.1f}" r="5" fill="{ink}"/>')
                text.append(f'<text x="{bx + pad + 28}" y="{ty:.1f}" class="d-label" fill="{ink}">{ln}</text>')
            else:
                text.append(f'<text x="{bx + pad}" y="{ty:.1f}" class="d-label" fill="{ink}">{ln}</text>')
        h = ty - y + (pad if framed else 10)  # last baseline to the bottom edge: the same as the top
        if S["box"] == "panel":
            out.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="{h:.1f}" fill="{PANEL[theme]}"/>')
        else:  # rule: a hairline above each layer, nothing else
            out.append(line([(bx, y), (bx + bw, y)], ink, S["lw2"]))
        out += text
        if placed:  # arrow up into the layer above, stopping short of both edges
            top = placed[-1][0] + placed[-1][1]
            ax = bx + bw / 2
            out.append(arrow([(ax, y - 10), (ax, top + 10)], ink, S["lw2"], S["head"]))
        placed.append((y, h)); y += h + GAP
    bottom = y - GAP
    def bracket(x, y0, y1, label):
        mid = (y0 + y1) / 2
        return (line([(x - 24, y0), (x, y0), (x, y1), (x - 24, y1)], ink, S["lw2"]) + line([(x, mid), (x + 36, mid)], ink, S["lw2"])
                + f'<text x="{x + 54}" y="{mid + 13}" class="d-big" fill="{ink}">{label}</text>')
    b1, b2 = bx + bw + 80, bx + bw + 400  # brackets follow the boxes
    out.append(bracket(b1, placed[0][0], placed[0][0] + placed[0][1], "Polycrisis"))
    out.append(bracket(b2, placed[0][0], bottom, "Metacrisis"))
    # the export is as wide as the figure, so the signature sits under it, not out in empty space
    right = b2 + 54 + apfel_m.path("Metacrisis", TYPE["big"][1], 0, 0)[1]
    Wf = round(max(right + M, M + SIG["light"][1] + M))
    H = bottom + SIG_GAP + DISC + SIG_FOOT
    pre = [f'<rect width="{Wf}" height="{H}" fill="{THEMES[theme]["ground"]}"/>',
           f'<text x="{M}" y="{M + 42}" class="d-title" fill="{ink}">From polycrisis to metacrisis</text>',
           f'<text x="{M}" y="{M + 84}" class="d-subtitle" fill="{ink}">Three layers of crisis, from what we see to its roots</text>']
    ry, rh = placed[-1]
    poly_svg.crop = (bx - 12, ry - 12, bw + 24, rh + 24)
    return f'<svg class="fig" viewBox="0 0 {Wf} {H}" role="img" aria-label="From polycrisis to metacrisis, redrawn">{"".join(pre + out)}{sig_at(H, theme, Wf)}</svg>'

# Diagram type (2026-10-08): Apfel Grotezk only, no Fett. Restraint as in FT and Economist
# charts: the title only a little larger than the labels, a grey subtitle, hierarchy from
# size and 60% ink rather than weight. Sizes at a 1600px export.
APFEL = '"Apfel Grotezk", "Hanken Grotesk", sans-serif'
TYPE = dict(  # role: (weight, size, extra)
    title=(400, 46, ""),                       # sentence case, ideally the figure's claim; size, not weight, sets it apart
    subtitle=(400, 28, "fill-opacity:.6;"),    # what the figure shows, one line
    head=(500, 32, ""),                        # box headings
    big=(500, 34, ""),                         # bracket and group labels
    label=(400, 29, ""),                       # annotations, bullets
    sub=(400, 26, "fill-opacity:.6;"),         # secondary lines in boxes
    tag=(500, 21, "text-transform:uppercase;letter-spacing:.1em;"),  # axis names, one to three words
)

def type_css():
    return "\n".join(f".d-{r}{{font-family:{APFEL};font-weight:{w};font-size:{z}px;{x}}}" for r, (w, z, x) in TYPE.items())

# ── Page shell ───────────────────────────────────────────────────
GOOGLE = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700"
          "&family=Hanken+Grotesk:wght@400;500&family=Fraunces:opsz,wght@9..144,400&display=swap")

def defs(figs=True):
    marks = "".join(f'<symbol id="mark-{th}" viewBox="0 0 256 256"><image width="256" height="256" href="{b64(SYSTEM / img)}"/></symbol>'
                    for th, img in (("light", "img/logo-256.png"), ("dark", "img/logo-inverted-256.png")))
    return ('<svg class="defs" aria-hidden="true"><defs>' + marks + ("".join(fig_symbol(f) for f in FIGS) if figs else "") +
            # dark mockups of light figures: invert, turn hues back, map black to night and white to chalk
            '<filter id="to-night" color-interpolation-filters="sRGB">'
            '<feColorMatrix type="matrix" values="-1 0 0 0 1  0 -1 0 0 1  0 0 -1 0 1  0 0 0 1 0"/>'
            '<feColorMatrix type="hueRotate" values="180"/>'
            '<feComponentTransfer><feFuncR type="linear" slope="0.836" intercept="0.090"/>'
            '<feFuncG type="linear" slope="0.820" intercept="0.086"/><feFuncB type="linear" slope="0.788" intercept="0.075"/></feComponentTransfer>'
            '</filter></defs></svg>')

CSS = """
/* Layout: one reading column for text, figures in a two-up grid that stacks on phones. */
:root { --ink:#1b1916; --muted:#5d584f; --rule:#e0dacf; --paper:#fbfaf6; --on-ink:#ffffff; --scrim:rgb(23 22 19 / .92);
  --font-body:"Bricolage Grotesque",system-ui,sans-serif; --font-label:"Apfel Grotezk","Hanken Grotesk",system-ui,sans-serif }
/* page chrome only: the figures set their own grounds */
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --ink:#ece7dc; --muted:#a49e93; --rule:#38342e; --paper:#171613; --on-ink:#171613; color-scheme: dark } }
:root[data-theme="dark"] { --ink:#ece7dc; --muted:#a49e93; --rule:#38342e; --paper:#171613; --on-ink:#171613; color-scheme: dark }
* { box-sizing: border-box }
html, body { margin: 0; background: var(--paper); color: var(--ink); font-family: var(--font-body); font-size: 16px; line-height: 1.5 }
a { color: inherit }
.defs { position: absolute; width: 0; height: 0; overflow: hidden }
main { max-width: 1400px; margin-inline: auto; padding: 32px 16px 96px }
h1 { font-weight: 600; font-size: clamp(28px, 4vw, 44px); line-height: 1.05; margin: 0 0 12px; letter-spacing: -.01em; text-wrap: balance }
h2 { font-weight: 600; font-size: 26px; margin: 0 0 6px; text-wrap: balance }
.label { font-family: var(--font-label); text-transform: uppercase; letter-spacing: .08em; font-size: 12px; color: var(--muted); margin: 0 }
.intro { max-width: 70ch; display: grid; gap: 10px; margin-bottom: 24px }
.intro p { margin: 0 }
.intro ul, .prose ul { margin: 0; padding-left: 1.2em }
.prose { max-width: 72ch }
.prose li { margin-bottom: 6px }
section { margin-top: 56px }
.fnote { margin: 0 0 16px; color: var(--muted); max-width: 80ch }
.src { display: block; font-size: 13px }
.pair { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 520px), 1fr)); gap: 20px }
figure { margin: 0; min-width: 0 }
figcaption { font-size: 13px; color: var(--muted); margin-top: 6px }
figcaption b { color: var(--ink); font-weight: 600 }
.zoom { all: unset; display: block; cursor: zoom-in; width: 100% }
.zoom:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px }
.fig { display: block; width: 100%; height: auto; border: 1px solid var(--rule) }
.slot { margin-top: 14px; display: grid; gap: 8px }
.strips { display: flex; flex-wrap: wrap; gap: 12px }
.strip { border: 1px solid var(--rule); max-width: 100%; overflow-x: auto }
.strip svg { display: block }
.thumbs { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 400px), 400px)); gap: 18px 16px; margin-top: 10px }
.thumb-box { width: 400px; max-width: 100% }
h3.label { margin-top: 28px }
.crop { overflow-x: auto; border: 1px solid var(--rule); max-width: 100% }
.crop svg { display: block }
.bar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--paper); border-bottom: 1px solid var(--rule); padding: 10px 0; margin-bottom: 24px; display: flex; gap: 8px; align-items: center; flex-wrap: wrap }
.bar button { font: 500 14px var(--font-body); border: 1px solid var(--ink); background: transparent; color: var(--ink); padding: 6px 13px; border-radius: 999px; cursor: pointer }
.bar button[aria-pressed="true"] { background: var(--ink); color: var(--on-ink) }
.bar button:focus-visible { outline: 2px solid var(--ink); outline-offset: 2px }
.why { margin: 0 0 14px; color: var(--muted) }
.tag-sys { font-family: var(--font-label); font-size: 11px; letter-spacing: .08em; text-transform: uppercase; border: 1px solid var(--rule); border-radius: 999px; padding: 1px 8px; margin-left: 6px; color: var(--muted); white-space: nowrap }
.spec { border-collapse: collapse; font-size: 15px }
.spec th { text-align: left; vertical-align: top; font-family: var(--font-label); font-weight: 500; text-transform: uppercase; letter-spacing: .08em; font-size: 12px; color: var(--muted); padding: 10px 20px 10px 0; white-space: nowrap }
.spec td { padding: 8px 20px 8px 0; border-top: 1px solid var(--rule); vertical-align: top }
.spec tr:first-child td { border-top: 0 }
dialog { padding: 0; border: 0; max-width: 100vw; max-height: 100vh; width: 100vw; height: 100vh; background: var(--scrim); overflow: auto }
dialog .inner { width: fit-content; margin: 0 auto; padding: 48px 0 }
dialog .fig { width: auto }
dialog .close { position: fixed; top: 12px; right: 16px; font: 500 14px var(--font-body); background: #ffffff; color: #1b1916; border: 0; border-radius: 999px; padding: 8px 14px; cursor: pointer }
"""

ZOOM_JS = """
const dlg = document.getElementById('zoom'), inner = dlg.querySelector('.inner');
document.querySelectorAll('.zoom').forEach(z => z.addEventListener('click', () => {
  const box = document.createElement('div'); box.className = z.closest('[class*="o-"]')?.className.match(/o-[\\w-]+/)?.[0] || '';
  const svg = z.querySelector('svg').cloneNode(true); svg.style.width = svg.viewBox.baseVal.width + 'px';  /* 1:1 */
  box.append(svg); inner.replaceChildren(box); dlg.showModal();
}));
dlg.querySelector('.close').addEventListener('click', () => dlg.close());
dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close() });
"""

def shell(title, body, bundle, extra_css="", js="", figs=True):
    fonts = (f"<style>{(SYSTEM / 'fonts.css').read_text()}</style>" if bundle
             else '<link rel="stylesheet" href="../../system/fonts.css">')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{GOOGLE}">
{fonts}
<style>{CSS}{extra_css}</style>
</head>
<body>
{defs(figs)}
<main>{body}</main>
<dialog id="zoom"><button class="close">Close</button><div class="inner"></div></dialog>
<script>{ZOOM_JS}{js}</script>
</body>
</html>'''

def zoomable(svg, caption):
    return f'<figure><button class="zoom" aria-label="Open at 1600px">{svg}</button><figcaption>{caption}</figcaption></figure>'

# ── index.html: the signature ────────────────────────────────────
def index_page(bundle):
    def strip(svg, w, th):
        return (f'<div class="strip" style="background:{THEMES[th]["ground"]}"><svg width="{w + 64:.0f}" height="{DISC + 64}" '
                f'viewBox="-32 -32 {w + 64:.0f} {DISC + 64}">{svg}</svg></div>')
    slots = [("The URL", URL), ("A publication line", "Wisdom · White paper No. 6"), ("Name only", None)]
    strips = "".join(
        f'<div class="slot"><p class="label">{label}</p><div class="strips">'
        + "".join(strip(*signature(th, url, mark_ref="mark"), th) for th in THEMES) + '</div></div>'
        for label, url in slots)
    secs = []
    for f in FIGS:
        thumbs = "".join(f'<figure class="thumb"><div class="thumb-box">{figure_svg(f, th)}</div><figcaption>{th.title()}</figcaption></figure>' for th in THEMES)
        secs.append(f'''
<section id="{f["id"]}">
  <h2>{f["title"]}</h2>
  <p class="fnote">{f["note"]} <span class="src">From <code>{f["src"]}/{f["file"]}</code>; Life Itself badge masked where present.</span></p>
  <div class="pair">{zoomable(figure_svg(f, "light"), "Light · 1600px export, scaled to fit. Click for 1:1.")}{zoomable(figure_svg(f, "dark"), "Dark · figure colour-inverted for the mockup; real dark figures are drawn in chalk.")}</div>
  <h3 class="label">At 400px, as in a feed</h3>
  <div class="thumbs">{thumbs}</div>
</section>''')
    body = f'''
  <p class="label">Seeds of Renaissance design system · Diagrams</p>
  <h1>The diagram signature</h1>
  <div class="intro">
    <p>Every published figure carries this signature, bottom right inside its margin, so it stays attributed when it is cropped and reshared. Rules: <code>diagrams.md</code>. Files: <code>system/img/signature.svg</code> and <code>signature-dark.svg</code>, with PNGs and an Excalidraw scene.</p>
    <ul>
      <li>Sized for a <b>1600px-wide export</b>: mark 64px, text 20px, 72px margin.</li>
      <li>Light grounds: the mark on its white disc. Dark grounds: a placeholder mark until the system settles the mark on dark.</li>
      <li>After the name, one optional slot: the URL, a publication line, or nothing. The URL is a placeholder (<code>{URL}</code>) until the domain is decided.</li>
    </ul>
  </div>
  <section id="actual" style="margin-top:0">
    <h2>At actual size</h2>
    <p class="fnote">As it sits in a 1600px export, with the three uses of the slot after the name.</p>
    {strips}
  </section>
  {"".join(secs)}'''
    return shell("Diagram signature", body, bundle)

# ── fonts.html: typography tryout ────────────────────────────────
def crop(svg):
    x, y, w, h = poly_svg.crop
    return f'<svg width="{w}" height="{h}" viewBox="{x} {y} {w} {h}">{svg[svg.index(">") + 1:-6]}</svg>'

def fonts_page(bundle):
    thumbs = "".join(f'<figure class="thumb"><div class="thumb-box">{fn(th)}</div><figcaption>{name} · {th}</figcaption></figure>'
                     for name, fn in (("Polycrisis", poly_svg), ("Wisdom gap", gap_svg)) for th in THEMES)
    rows = "".join(f"<tr><th>{r}</th><td>Apfel {'Mittel' if w == 500 else 'Regular'} {z}px{', 60% ink' if 'opacity' in x else ''}{', uppercase, tracked' if 'upper' in x else ''}</td><td>{d}</td></tr>"
                   for (r, (w, z, x)), d in zip(TYPE.items(), [
                       "Sentence case. Ideally the claim, not the topic.", "What the figure shows, one line.",
                       "Box and panel headings.", "Bracket and group labels.", "Annotations and bullets.",
                       "Secondary lines inside boxes.", "Axis names and one-to-three-word tags only."]))
    body = f'''
  <p class="label">Seeds of Renaissance design system · Diagrams</p>
  <h1>Type for diagrams</h1>
  <div class="intro">
    <p>Apfel Grotezk only, and no bold. Elegance from restraint, as in FT and Economist charts: the title only a little larger than the labels, a grey subtitle doing the explaining, hierarchy from size and 60% ink rather than weight. Drawn in the chosen style, panels (<a href="style.html">drawing style</a>).</p>
    <p class="fnote">Subtitles are draft copy.</p>
  </div>
  <section style="margin-top:0">
    <div class="pair">{zoomable(poly_svg(), "Text-heavy. Click for 1:1.")}{zoomable(gap_svg(), "Sparse. Click for 1:1.")}</div>
    <h3 class="label">The smallest text at 1:1 (1600px export)</h3>
    <div class="crop">{crop(poly_svg())}</div>
  </section>
  <section>
    <h2>The scale</h2>
    <div class="crop" style="border:0"><table class="spec">{rows}</table></div>
  </section>
  <section>
    <h2>At 400px, as in a feed</h2>
    <div class="thumbs">{thumbs}</div>
  </section>'''
    return shell("Type for diagrams", body, bundle, extra_css=type_css(), figs=False)

# ── style.html: drawing style, and figures in context ───────────
SNAMES = {"fine": ("Fine", "After Tufte. Thin lines, hairlines for scaffolding, no boxes: layers sit on a rule. The accent as a red arrow."),
          "panel": ("Panels", "After the FT and the Economist. No outlines: layers are panels in the red tint, the same as the wisdom gap, as wide as their text, with equal padding."),
}
PAPER_P = [
    "Amid the decline of modern industrialised society, we are obliged to trace the shape of wisdom in negative space. Manifold crises, the threat of systemic collapse, and a general inability to change direction suggest a profound lack of collective capacity to choose action for the greater good. At the same time, with societal complexity escalating faster than our capacity to manage it, our technologically enabled power to inflict catastrophic harm upon ourselves, each other and our world likewise continues to grow: a disconnect known as ‘the wisdom gap.’",
    "It’s uncontroversial to associate wisdom with rational understanding: with the capacity to grasp what’s going on in a given context, and apply knowledge and analysis to interpret events and guide action. The complexity of our times plainly overwhelms understanding, and it’s tempting to suggest that this shortfall alone explains our ‘wisdom gap’. Still, most would intuitively agree that there’s more to wisdom than analytical skill.",
]
CAPTION = "A rapidly growing gap between society’s technological and social complexity and our “wisdom”, our capacity to manage that complexity well. The curves show a direction, not measured trajectories."

def variants(fn):
    return "".join(f'<div class="sv" data-s="{k}">{fn("light", k)}</div>' for k in SNAMES)

def style_page(bundle):
    secs = "".join(f'''
  <section id="{k}">
    <h2>{name}</h2>
    <p class="fnote">{why}</p>
    <div class="pair">{zoomable(poly_svg("light", k), "Click for 1:1.")}{zoomable(gap_svg("light", k), "Click for 1:1.")}</div>
  </section>''' for k, (name, why) in SNAMES.items())
    bw = "".join(f'<figure class="thumb"><div class="thumb-box bw">{gap_svg("light", k)}</div><figcaption><b>{SNAMES[k][0]}</b></figcaption></figure>' for k in SNAMES)
    small = "".join(f'<figure class="thumb"><div class="thumb-box">{poly_svg("light", k)}</div><figcaption><b>{SNAMES[k][0]}</b></figcaption></figure>' for k in SNAMES)
    buttons = "".join(f'<button data-s="{k}" aria-pressed="{str(k == "panel").lower()}">{n}</button>' for k, (n, _) in SNAMES.items())
    body = f'''
  <p class="label">Seeds of Renaissance design system · Diagrams</p>
  <h1>Drawing style for diagrams</h1>
  <div class="intro">
    <p>Two ways to draw the same two figures, with the type fixed (Apfel only, no bold) and one red accent. References: Tufte, the FT, the Economist. Then the figures in context: on a page of the paper and in a web article.</p>
  </div>
  {secs}
  <section>
    <h2>Printed in black and white</h2>
    <p class="fnote">The red has to survive a black-and-white printer: as a grey area or panel, or as an arrow with its label.</p>
    <div class="thumbs">{bw}</div>
  </section>
  <section>
    <h2>At 400px, as in a feed</h2>
    <div class="thumbs">{small}</div>
  </section>
  <section id="context">
    <h2>In context</h2>
    <p class="fnote">The figure beside running text: Bricolage for the text, Apfel in the figure. Switch the style to see each one on the page.</p>
    <div class="bar" role="group" aria-label="Drawing style in context">{buttons}</div>
    <div class="ctx" data-style="panel">
      <h3 class="label">A page of the paper (A4, figure as a plate)</h3>
      <div class="sheet-wrap"><div class="sheet">
        <div class="rh"><span>4</span><span>Wisdom and Wanting What’s Good</span></div>
        <h4 class="ph2">Addressing the wisdom gap</h4>
        <p class="pp">{PAPER_P[0]}<sup>7</sup></p>
        <figure class="plate"><div class="art">{variants(gap_svg)}</div>
          <figcaption><span class="flbl">Fig. 1</span><span>{CAPTION}<sup>8</sup></span></figcaption></figure>
        <p class="pp">{PAPER_P[1]}</p>
      </div></div>
      <h3 class="label">A web article</h3>
      <div class="web-wrap"><article class="web">
        <p class="wlabel">White paper No. 6 · Wisdom and Wanting What’s Good</p>
        <h4 class="wh2">Addressing the wisdom gap</h4>
        <p>{PAPER_P[0]}</p>
        <figure class="wfig">{variants(poly_svg)}<figcaption><span class="flbl">Fig. 2</span> The crises we see sit on deeper dysfunctions, which sit on ideas and tendencies we rarely examine. Working on the surface alone does not reach the root.</figcaption></figure>
        <p>{PAPER_P[1]}</p>
      </article></div>
    </div>
  </section>'''
    css = """
.bw svg { filter: grayscale(1) }
.ctx[data-style="fine"] .sv:not([data-s="fine"]), .ctx[data-style="panel"] .sv:not([data-s="panel"]) { display: none }
.sv svg.fig { border: 0 }
.sv svg.fig > rect:first-child { fill: transparent }  /* in context the figure sits on the page, not on a white box */
/* the paper page and the web article are depictions of light, printed or on-brand pages: fixed colours */
.sheet-wrap, .web-wrap { overflow-x: auto; max-width: 100%; margin-top: 10px }
.sheet-wrap { background: #e4dfd5; padding: 24px }
.sheet { width: 210mm; min-height: 297mm; box-sizing: border-box; padding: 22mm 20mm 26mm 24mm; background: #fbfaf6; color: #1b1916; box-shadow: 0 1px 3px rgb(0 0 0 / .18); font-family: "Bricolage Grotesque", sans-serif }
.rh { display: flex; gap: 6mm; font: 500 7pt "Apfel Grotezk", sans-serif; letter-spacing: .16em; text-transform: uppercase; color: #5d584f; margin-top: -10mm; margin-bottom: 10mm }
.ph2 { font: 400 19pt/1.15 "Restora", "Fraunces", Georgia, serif; margin: 0 0 14.5pt; width: 118mm }
.pp { font-size: 10.5pt; line-height: 14.5pt; width: 118mm; margin: 0; text-indent: 0 }
.pp + .pp { text-indent: 1.4em }
.pp sup, .plate sup { color: #e5201c; font-size: .7em }
.plate { margin: 14.5pt 0; break-inside: avoid }
.plate .art { border-top: .5pt solid #e0dacf; border-bottom: .5pt solid #e0dacf; padding: 2mm 0 }
.plate .art svg { display: block; width: 100%; height: auto }
.plate figcaption { display: grid; grid-template-columns: 14mm 118mm; margin-top: 3mm; font-size: 8.5pt; line-height: 11.5pt; color: #5d584f; font-style: italic }
.flbl { font: 500 7pt "Apfel Grotezk", sans-serif; letter-spacing: .16em; text-transform: uppercase; color: #1b1916; font-style: normal; padding-top: 1.5pt }
.web { background: #fbfaf6; color: #1b1916; padding: 48px clamp(16px, 5vw, 64px); min-width: 0 }
.web > p, .web > h4, .web > .wlabel { max-width: 680px; margin-inline: auto }
.web p { font-size: 18px; line-height: 1.6; margin-block: 0 1em }
.wlabel { font: 500 12px "Apfel Grotezk", sans-serif !important; letter-spacing: .1em; text-transform: uppercase; color: #5d584f }
.wh2 { font: 400 32px/1.15 "Restora", "Fraunces", Georgia, serif; margin-block: 0 16px }
.wfig { max-width: 960px; margin: 32px auto }
.wfig svg { display: block; width: 100%; height: auto }
.wfig figcaption { max-width: 680px; margin: 10px auto 0; font-size: 14px; color: #5d584f; line-height: 1.5 }
.wfig .flbl { font-size: 11px; margin-right: 8px }
"""
    js = """
const ctx = document.querySelector('.ctx'), sb = document.querySelectorAll('#context .bar button');
sb.forEach(b => b.addEventListener('click', () => {
  ctx.dataset.style = b.dataset.s; sb.forEach(x => x.setAttribute('aria-pressed', x === b));
}));
"""
    return shell("Diagram drawing style", body, bundle, extra_css=type_css() + css, js=js, figs=False)

ARTIFACTS = {"index.html": "https://claude.ai/artifact/TYhQ6hnqSPp7dUUuF5Se2f",
             "fonts.html": "https://claude.ai/artifact/JQs6MvaQM2a9rvWm1c3p61",
             "style.html": "https://claude.ai/artifact/H4unZtofiTcy894NucUS59"}

def for_artifact(html):
    """The publisher adds the document skeleton: keep the head's contents and the body's."""
    head = html[html.index("<title>"):html.index("</head>")]
    body = html[html.index("<body>") + 6:html.index("</body>")]
    for page, url in ARTIFACTS.items():  # sibling pages are separate artifacts once published
        body = body.replace(f'href="{page}"', f'href="{url}"')
    return head + body

if __name__ == "__main__":
    pages = {"index.html": index_page, "fonts.html": fonts_page, "style.html": style_page}
    if len(sys.argv) == 3 and sys.argv[1] == "--bundle":
        out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
        for name, fn in pages.items():
            (out / name).write_text(for_artifact(fn(bundle=True)))
    else:
        for name, fn in pages.items():
            (here / name).write_text(fn(bundle=False))
