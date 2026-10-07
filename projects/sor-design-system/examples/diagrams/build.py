"""Build the diagram examples (design-34t.20, .25):

  index.html  the signature (decided 2026-10-07: mark + name and URL in Apfel) on three
              real figures from 2rbook, light and dark, at a 1600px export and at 400px
  fonts.html  diagram typography tryout: two figures redrawn, set in six candidate faces

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
            f'<text x="{M}" y="{M + 50}" class="d-title" fill="{ink}">The wisdom gap</text>'
            + line(f"M{x0 - 40} {axis} L{x1 + 90} {axis}", ink, LW2) + arrowhead((x0, axis), (x1 + 90, axis), ink, LW2)
            + f'<text x="{x1 + 90}" y="{axis + 44}" text-anchor="end" class="d-tag" fill="{ink}">Time</text>'
            + line(td, ink) + arrowhead(tp[-3], tp[-1], ink) + line(wd, ink) + arrowhead(wp[-3], wp[-1], ink)
            + line(f"M{gx} {ty} L{gx} {wy}", RED, LW, ' stroke-dasharray="14 12"')
            + arrowhead((gx, wy), (gx, ty), RED) + arrowhead((gx, ty), (gx, wy), RED)
            + f'<text x="{gx + 26}" y="{(ty + wy) / 2 + 7}" class="d-tag" fill="{RED}">Wisdom gap</text>'
            f'<text class="d-label" fill="{ink}" text-anchor="end"><tspan x="1220" y="200">Technological capability</tspan><tspan x="1220" dy="1.3em">and/or social complexity</tspan></text>'
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
    out, y, placed = [], 190, []
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
           f'<text x="{M}" y="{M + 50}" class="d-title" fill="{ink}">From polycrisis to metacrisis</text>']
    ry, rh = placed[-1]
    poly_svg.crop = (bx - 12, ry - 12, bw + 24, rh + 24)
    return f'<svg class="fig" viewBox="0 0 {W} {H}" role="img" aria-label="From polycrisis to metacrisis, redrawn">{"".join(pre + out)}{sig_at(H, theme)}</svg>'

# Candidate type for diagrams. Roles: title, head (box heading), big (bracket labels),
# label (annotations, bullets), sub (secondary, 60% ink), tag (axis names, one-to-three-word tags).
APFEL, BRIC = '"Apfel Grotezk", "Hanken Grotesk", sans-serif', '"Bricolage Grotesque", sans-serif'
OPTS = [
    dict(id="apfel", name="Apfel Grotezk only", system=True,
         why="The system's label face, used for every role. Three weights (Regular, Mittel, Fett).",
         f=dict(title=(APFEL, 700), head=(APFEL, 700), big=(APFEL, 500), label=(APFEL, 400), sub=(APFEL, 400), tag=(APFEL, 500))),
    dict(id="apfel-bric", name="Apfel titles, Bricolage labels", system=True,
         why="Apfel for the title, headings and tags; Bricolage, the reading face, for everything read as text.",
         f=dict(title=(APFEL, 700), head=(APFEL, 700), big=(APFEL, 500), label=(BRIC, 400), sub=(BRIC, 400), tag=(APFEL, 500))),
    dict(id="bric", name="Bricolage only", system=True,
         why="The reading face for every role, at small optical sizes, weights from the variable font.",
         f=dict(title=(BRIC, 650), head=(BRIC, 600), big=(BRIC, 600), label=(BRIC, 400), sub=(BRIC, 400), tag=(BRIC, 600))),
    dict(id="hanken", name="Hanken Grotesk", system=False,
         why="A plain modern grotesk, already the fallback for Apfel in the tokens. Would be a fifth face.",
         f={r: ('"Hanken Grotesk", sans-serif', w) for r, w in dict(title=700, head=700, big=600, label=400, sub=400, tag=600).items()}),
    dict(id="plex", name="IBM Plex Sans", system=False,
         why="Engineered for interfaces and technical drawing; very even, clear at small sizes. Would be a fifth face.",
         f={r: ('"IBM Plex Sans", sans-serif', w) for r, w in dict(title=600, head=600, big=500, label=400, sub=400, tag=500).items()}),
    dict(id="atkinson", name="Atkinson Hyperlegible Next", system=False,
         why="Designed for legibility at low vision: distinct letter shapes, big x-height. Would be a fifth face.",
         f={r: ('"Atkinson Hyperlegible Next", sans-serif', w) for r, w in dict(title=700, head=700, big=600, label=400, sub=400, tag=600).items()}),
]
SIZES = dict(title=60, head=40, big=44, label=32, sub=27, tag=24)  # at 1600: smallest ~27px, about 7px at 400

def opt_css():
    css = []
    for o in OPTS:
        for role, (fam, wt) in o["f"].items():
            extra = ""
            if role == "tag": extra = "text-transform:uppercase;letter-spacing:.1em;"
            if role == "sub": extra = "fill-opacity:.62;"
            if fam == BRIC: extra += "font-variation-settings:'opsz' 14;" if role in ("label", "sub") else "font-variation-settings:'opsz' 36;"
            css.append(f'.o-{o["id"]} .d-{role}{{font-family:{fam};font-weight:{wt};font-size:{SIZES[role]}px;{extra}}}')
    return "\n".join(css)

# ── Page shell ───────────────────────────────────────────────────
GOOGLE = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700"
          "&family=Hanken+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700"
          "&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700&display=swap")

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
    strips = "".join(
        f'<div class="strip" style="background:{THEMES[th]["ground"]}"><svg width="{w + 64:.0f}" height="{DISC + 64}" viewBox="-32 -32 {w + 64:.0f} {DISC + 64}">{svg}</svg></div>'
        for th, (svg, w) in SIG.items())
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
      <li>Light grounds: the mark on its white disc. Dark grounds: the inverted mark, no disc (provisional until the inverted mark is designed).</li>
      <li>The URL is a placeholder (<code>{URL}</code>) until the domain is decided.</li>
    </ul>
  </div>
  <section id="actual" style="margin-top:0">
    <h2>At actual size</h2>
    <p class="fnote">As it sits in a 1600px export.</p>
    <div class="strips">{strips}</div>
  </section>
  {"".join(secs)}'''
    return shell("Diagram signature", body, bundle)

# ── fonts.html: typography tryout ────────────────────────────────
def crop(svg):
    x, y, w, h = poly_svg.crop
    return f'<svg width="{w}" height="{h}" viewBox="{x} {y} {w} {h}">{svg[svg.index(">") + 1:-6]}</svg>'

def fonts_page(bundle):
    buttons = "".join(f'<button data-o="{o["id"]}" aria-pressed="{str(i == 0).lower()}">{o["name"]}</button>' for i, o in enumerate(OPTS))
    big = "".join(f'''
<div class="opt o-{o["id"]}" data-o="{o["id"]}"{"" if i == 0 else " hidden"}>
  <h2>{o["name"]}{"<span class=tag-sys>in the system</span>" if o["system"] else "<span class=tag-sys>fifth face</span>"}</h2>
  <p class="why">{o["why"]}</p>
  <div class="pair">{zoomable(poly_svg(), "Text-heavy: title, box headings, secondary lines, bullets, bracket labels.")}{zoomable(gap_svg(), "Sparse: title, two annotations, two tags.")}</div>
  <h3 class="label">The smallest text at 1:1 (1600px export)</h3>
  <div class="crop">{crop(poly_svg())}</div>
</div>''' for i, o in enumerate(OPTS))
    thumbs = "".join(f'<figure class="thumb o-{o["id"]}"><div class="thumb-box">{poly_svg()}</div><figcaption><b>{o["name"]}</b></figcaption></figure>' for o in OPTS)
    body = f'''
  <p class="label">Seeds of Renaissance design system · Diagrams · Tryout</p>
  <h1>Type for diagrams</h1>
  <div class="intro">
    <p>Diagrams are working type, not billboard: they should read at 400px in a feed and printed small on a page. Two figures redrawn and set six ways. The line work is plain and identical in all six; the drawing style comes after the type is picked.</p>
  </div>
  <section class="prose" style="margin-top:0">
    <h2>What diagram typography usually does</h2>
    <ul>
      <li><b>One family</b>, with hierarchy from size and weight, not from mixing faces. The Economist, the FT and Datawrapper all chart in a single sans.</li>
      <li><b>A sturdy sans</b> with a large x-height and open shapes, so labels hold up when the image is shrunk, and figures that line up.</li>
      <li><b>Three sizes at most</b>: title, label, note.</li>
      <li><b>Sentence case</b> for labels, set on the thing they name. Capitals only for short tags such as axis names.</li>
      <li><b>No display or handwriting faces.</b> The title is the same family in bold, top left. Our World in Data, with its serif titles, is the exception.</li>
    </ul>
    <p>That points to the label face, not Polyamine. The question is whether Apfel can carry the reading-sized labels too, or needs Bricolage or a plainer face beside it.</p>
  </section>
  <section>
    <div class="bar" role="group" aria-label="Typeface option">{buttons}</div>
    {big}
  </section>
  <section>
    <h2>All six at 400px</h2>
    <p class="fnote">The same figure as it appears in a feed. Which one can you still read?</p>
    <div class="thumbs">{thumbs}</div>
  </section>'''
    js = """
const opts = document.querySelectorAll('.opt'), btns = document.querySelectorAll('.bar button');
btns.forEach(b => b.addEventListener('click', () => {
  opts.forEach(o => o.hidden = o.dataset.o !== b.dataset.o);
  btns.forEach(x => x.setAttribute('aria-pressed', x === b));
  try { localStorage.setItem('diagram-font', b.dataset.o) } catch (e) {}
}));
try { const s = localStorage.getItem('diagram-font'); if (s) document.querySelector(`.bar button[data-o="${s}"]`)?.click() } catch (e) {}
"""
    return shell("Type for diagrams", body, bundle, extra_css=opt_css(), js=js, figs=False)

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
