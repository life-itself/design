"""Build the diagram examples (design-34t.20, .25):

  index.html  the signature (decided 2026-10-07: mark + name and URL in Apfel) on three
              real figures from 2rbook, light and dark, at a 1600px export and at 400px
  fonts.html  type for diagrams: Apfel only, no bold; two figures redrawn

Signature text is outlined (system/outline.py). Figures in figures/ are copied from 2rbook,
flattened onto white with the gamma chunk dropped so they render true black.

Run:  python build.py                 -> index.html, fonts.html (link ../../system/fonts.css)
      python build.py --bundle DIR    -> DIR/index.html, DIR/fonts.html, self-contained, for publishing
Needs: fonttools, uharfbuzz."""
import base64, math, pathlib, sys
here = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent.parent / "system"))
from outline import SYSTEM, DISC, THEMES, RED, signature, b64

URL = "seeds-domain.tbd/wisdom"  # a paper's page; placeholder until the domain is decided
W, M = 1600, 72                  # export width, margin
SIG_GAP, SIG_FOOT = 36, 56       # figure to signature, signature to bottom edge
SIG = {th: signature(th, URL, mark_ref="mark") for th in THEMES}

def sig_at(H, theme):
    svg, w = SIG[theme]
    return f'<g class="sig" transform="translate({W - M - w:.1f} {H - SIG_FOOT - DISC})">{svg}</g>'

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

# ── Redrawn figures, for the type tryout ─────────────────────────
# Line work is deliberately plain and the same in every option: only the type changes.
LW, LW2, HEAD = 3.5, 2.5, 18  # main and scaffolding strokes, arrowhead length, at 1600

def arrowhead(p, q, color, sw=LW, L=HEAD):
    a = math.atan2(q[1] - p[1], q[0] - p[0])
    pts = [(q[0] - L * math.cos(a + s * 0.45), q[1] - L * math.sin(a + s * 0.45)) for s in (1, -1)]
    return (f'<path d="M{pts[0][0]:.1f} {pts[0][1]:.1f} L{q[0]:.1f} {q[1]:.1f} L{pts[1][0]:.1f} {pts[1][1]:.1f}" '
            f'fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')

def line(d, color, sw=LW, extra=""):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{extra}/>'

def gap_svg(theme="light"):
    ink, H = THEMES[theme]["ink"], 1080
    x0, x1, axis = 120, 1330, 900
    tech = lambda t: 830 - 660 * (math.exp(4.2 * t) - 1) / (math.exp(4.2) - 1)
    wis = lambda t: 872 - 250 * (math.exp(1.6 * t) - 1) / (math.exp(1.6) - 1)
    def curve(fn):
        pts = [(x0 + (x1 - x0) * i / 60, fn(i / 60)) for i in range(61)]
        return pts, "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    tp, td = curve(tech); wp, wd = curve(wis)
    gx = 1180; t = (gx - x0) / (x1 - x0); ty, wy = tech(t) + 20, wis(t) - 20
    body = (f'<rect width="{W}" height="{H}" fill="{THEMES[theme]["ground"]}"/>'
            f'<text x="{M}" y="{M + 42}" class="d-title" fill="{ink}">The wisdom gap</text>'
            f'<text x="{M}" y="{M + 84}" class="d-subtitle" fill="{ink}">Our power grows faster than our capacity to use it well</text>'
            + line(f"M{x0 - 40} {axis} L{x1 + 90} {axis}", ink, LW2) + arrowhead((x0, axis), (x1 + 90, axis), ink, LW2)
            + f'<text x="{x1 + 90}" y="{axis + 44}" text-anchor="end" class="d-tag" fill="{ink}">Time</text>'
            + line(td, ink) + arrowhead(tp[-3], tp[-1], ink) + line(wd, ink) + arrowhead(wp[-3], wp[-1], ink)
            + line(f"M{gx} {ty} L{gx} {wy}", RED, LW, ' stroke-dasharray="14 12"')
            + arrowhead((gx, wy), (gx, ty), RED) + arrowhead((gx, ty), (gx, wy), RED)
            + f'<text x="{gx + 26}" y="{(ty + wy) / 2 + 7}" class="d-tag" fill="{RED}">Wisdom gap</text>'
            f'<text class="d-label" fill="{ink}" text-anchor="end"><tspan x="1220" y="240">Technological capability</tspan><tspan x="1220" dy="1.3em">and/or social complexity</tspan></text>'
            f'<text class="d-label" fill="{ink}" text-anchor="end"><tspan x="1330" y="770">“Wisdom”: our capacity</tspan><tspan x="1330" dy="1.3em">to manage that complexity</tspan></text>')
    return f'<svg class="fig" viewBox="0 0 {W} {H}" role="img" aria-label="The wisdom gap, redrawn">{body}{sig_at(H, theme)}</svg>'

def poly_svg(theme="light"):
    ink = THEMES[theme]["ink"]
    bx, bw, pad = M, 830, 40
    boxes = [  # heading, secondary lines, body lines, bullets?
        ("Surface layer", ["Manifest crises"],
         ["Escalating, interacting global crises", "such as the climate crisis and tech x-risk"], False),
        ("Intermediate layer", ["Meta-systemic dysfunctions"],
         ["Collective action problems", "Exponential tech and the wisdom gap", "Degradation of sense-making systems"], True),
        ("Root layer", ["Foundational ideologies (cultural paradigms)", "and deep human tendencies"],
         ["Deep ideological features", "Core aspects of humanity"], True),
    ]
    out, y, placed = [], 210, []
    for i, (head, sub, lines, bullets) in enumerate(boxes):
        h = 66 + 36 * len(sub) + 22 + 44 * len(lines) + 12
        out.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="{h}" rx="18" fill="none" stroke="{ink}" stroke-width="{LW}"/>')
        out.append(f'<text x="{bx + pad}" y="{y + 62}" class="d-head" fill="{ink}">{head}</text>')
        ty = y + 62 + 38
        for t in sub:
            out.append(f'<text x="{bx + pad}" y="{ty}" class="d-sub" fill="{ink}">{t}</text>'); ty += 36
        ty += 22
        for ln in lines:
            if bullets:
                out.append(f'<circle cx="{bx + pad + 6}" cy="{ty - 10}" r="5" fill="{ink}"/>')
                out.append(f'<text x="{bx + pad + 28}" y="{ty}" class="d-label" fill="{ink}">{ln}</text>')
            else:
                out.append(f'<text x="{bx + pad}" y="{ty}" class="d-label" fill="{ink}">{ln}</text>')
            ty += 44
        if placed:  # arrow up into the box above
            top = placed[-1][0] + placed[-1][1]
            out.append(line(f"M{bx + bw / 2} {y} L{bx + bw / 2} {top + 4}", ink, LW2) + arrowhead((bx + bw / 2, y), (bx + bw / 2, top + 4), ink, LW2))
        placed.append((y, h)); y += h + 80
    bottom = y - 80
    def bracket(x, y0, y1, label):
        mid = (y0 + y1) / 2
        return (line(f"M{x - 24} {y0} L{x} {y0} L{x} {y1} L{x - 24} {y1} M{x} {mid} L{x + 36} {mid}", ink, LW2)
                + f'<text x="{x + 54}" y="{mid + 13}" class="d-big" fill="{ink}">{label}</text>')
    out.append(bracket(960, placed[0][0], placed[0][0] + placed[0][1], "Polycrisis"))
    out.append(bracket(1240, placed[0][0], bottom, "Metacrisis"))
    H = bottom + SIG_GAP + DISC + SIG_FOOT
    pre = [f'<rect width="{W}" height="{H}" fill="{THEMES[theme]["ground"]}"/>',
           f'<text x="{M}" y="{M + 42}" class="d-title" fill="{ink}">From polycrisis to metacrisis</text>',
           f'<text x="{M}" y="{M + 84}" class="d-subtitle" fill="{ink}">Three layers of crisis, from what we see to its roots</text>']
    ry, rh = placed[-1]
    poly_svg.crop = (bx - 12, ry - 12, bw + 24, rh + 24)
    return f'<svg class="fig" viewBox="0 0 {W} {H}" role="img" aria-label="From polycrisis to metacrisis, redrawn">{"".join(pre + out)}{sig_at(H, theme)}</svg>'

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
          "&family=Hanken+Grotesk:wght@400;500&display=swap")

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
dialog .inner { width: 1600px; margin: 0 auto; padding: 48px 0 }
dialog .fig { width: 1600px }
dialog .close { position: fixed; top: 12px; right: 16px; font: 500 14px var(--font-body); background: #ffffff; color: #1b1916; border: 0; border-radius: 999px; padding: 8px 14px; cursor: pointer }
"""

ZOOM_JS = """
const dlg = document.getElementById('zoom'), inner = dlg.querySelector('.inner');
document.querySelectorAll('.zoom').forEach(z => z.addEventListener('click', () => {
  const box = document.createElement('div'); box.className = z.closest('[class*="o-"]')?.className.match(/o-[\\w-]+/)?.[0] || '';
  box.append(z.querySelector('svg').cloneNode(true)); inner.replaceChildren(box); dlg.showModal();
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
    <p>Apfel Grotezk only, and no bold. Elegance from restraint, as in FT and Economist charts: the title only a little larger than the labels, a grey subtitle doing the explaining, hierarchy from size and 60% ink rather than weight. Line work is still plain; the drawing style comes next.</p>
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

def for_artifact(html):
    """The publisher adds the document skeleton: keep the head's contents and the body's."""
    head = html[html.index("<title>"):html.index("</head>")]
    return head + html[html.index("<body>") + 6:html.index("</body>")]

if __name__ == "__main__":
    pages = {"index.html": index_page, "fonts.html": fonts_page}
    if len(sys.argv) == 3 and sys.argv[1] == "--bundle":
        out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
        for name, fn in pages.items():
            (out / name).write_text(for_artifact(fn(bundle=True)))
    else:
        for name, fn in pages.items():
            (here / name).write_text(fn(bundle=False))
