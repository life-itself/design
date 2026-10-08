"""Build the diagram examples: examples/diagrams/index.html, the gallery to point people at,
and img/*.png, the samples the guide (diagrams.md) shows inline. Rules live in diagrams.md;
earlier tryouts and comparisons are in archive/diagrams-*-2026-10.html.

Figures here: the wisdom gap and polycrisis (redrawn in the house style) and three charts
(illustrative data), each in light and dark, at 400px and in black and white, and in use on a
page of a paper and in a web article. The Wisdom paper's real figures are built in 2rbook
(wisdom/assets/build-*.py) and copied into img/ when that repo sits beside this one.

These helpers are also the starting point for a new figure: copy a function, change the content.

Run:  python build.py                 -> index.html, img/*.png (PNGs need Google Chrome)
      python build.py --bundle DIR    -> DIR/index.html, self-contained, for a Claude artifact
Needs: fonttools, uharfbuzz."""
import base64, math, pathlib, re, shutil, subprocess, sys, tempfile
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

# ── Redrawn figures ──────────────────────────────────────────────
# The drawing style ("panel", diagrams.md#drawing-style), widths at 1600px: no outlines; groups
# and the key area in the red tint; solid lines and solid arrowheads, no dashes.
STYLES = {"panel": dict(lw=4, lw2=2, head=18, box="panel", gap="shade")}
# The red tint: the logo red at 16% on white, 40% on night (22% vanished on dark). Panels and accent areas, never text.
TINT = {"light": "#fbdbdb", "dark": "#6b1a17"}
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
    x0, axis = 120, 900
    x1 = W - M - 90  # the axis (x1 + 90) ends at the right margin, aligned with the signature
    tech = lambda t: 830 - 660 * (math.exp(4.2 * t) - 1) / (math.exp(4.2) - 1)
    wis = lambda t: 872 - 250 * (math.exp(1.6 * t) - 1) / (math.exp(1.6) - 1)
    tp = [(x0 + (x1 - x0) * i / 60, tech(i / 60)) for i in range(61)]
    wp = [(x0 + (x1 - x0) * i / 60, wis(i / 60)) for i in range(61)]
    out = [f'<rect width="{W}" height="{H}" fill="{THEMES[theme]["ground"]}"/>']
    if S["gap"] == "shade":  # the accent as an area: the space between the curves, in the red tint
        area = tp[30:] + wp[30:][::-1]
        out.append(f'<path d="M{" L".join(f"{x:.1f} {y:.1f}" for x, y in area)} Z" fill="{TINT[theme]}"/>')
        # label midway between the curves, and centred between the upper curve and the shading's edge
        gt = 0.895; mid = (tech(gt) + wis(gt)) / 2
        lo, hi = 0.0, 1.0
        for _ in range(50):
            t = (lo + hi) / 2; lo, hi = (t, hi) if tech(t) > mid else (lo, t)
        gx = (x0 + (x1 - x0) * t + x1) / 2 + 14  # plus an optical nudge right: exact centre reads as too far left
        out.append(f'<text x="{gx:.1f}" y="{mid + 7:.1f}" text-anchor="middle" class="d-tag" fill="{RED}">Wisdom gap</text>')
    out += [f'<text x="{M}" y="{M + 42}" class="d-title" fill="{ink}">The Wisdom Gap</text>',
            f'<text x="{M}" y="{M + 84}" class="d-subtitle" fill="{ink}">Our power grows faster than our capacity to use it well</text>',
            arrow([(x0 - 40, axis), (x1 + 90, axis)], ink, S["lw2"], S["head"] - 4),
            f'<text x="{x1 + 90}" y="{axis + 44}" text-anchor="end" class="d-tag" fill="{ink}">Time</text>',
            arrow(tp, ink, S["lw"], S["head"] + 4), arrow(wp, ink, S["lw"], S["head"] + 4)]
    if S["gap"] == "arrow":
        gx = x1 - 150; t = (gx - x0) / (x1 - x0); ty, wy = tech(t) + 14, wis(t) - 14
        out += [arrow([(gx, ty), (gx, wy)], RED, S["lw"], S["head"], both=True),
                f'<text x="{gx + 26}" y="{(ty + wy) / 2 + 7}" class="d-tag" fill="{RED}">Wisdom gap</text>']
    out += [f'<text class="d-label" fill="{ink}" text-anchor="end" x="{x1 - 110}" y="258">Technological power</text>',
            f'<text class="d-label" fill="{ink}" text-anchor="end" x="{x1}" y="780">“Wisdom”: our capacity to use it well</text>']
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
    title=(400, 46, ""),                       # title case, ideally the figure's claim; size, not weight, sets it apart
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

def defs():
    marks = "".join(f'<symbol id="mark-{th}" viewBox="0 0 256 256"><image width="256" height="256" href="{b64(SYSTEM / img)}"/></symbol>'
                    for th, img in (("light", "img/logo-256.png"), ("dark", "img/logo-inverted-256.png")))
    return f'<svg class="defs" aria-hidden="true"><defs>{marks}</defs></svg>'

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

def shell(title, body, bundle, extra_css="", js=""):
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
{defs()}
<main>{body}</main>
<dialog id="zoom"><button class="close">Close</button><div class="inner"></div></dialog>
<script>{ZOOM_JS}{js}</script>
</body>
</html>'''

def zoomable(svg, caption):
    return f'<figure><button class="zoom" aria-label="Open at 1600px">{svg}</button><figcaption>{caption}</figcaption></figure>'

# ── Figures in use: a page of the paper and a web article ───────
PAPER_P = [
    "Amid the decline of modern industrialised society, we are obliged to trace the shape of wisdom in negative space. Manifold crises, the threat of systemic collapse, and a general inability to change direction suggest a profound lack of collective capacity to choose action for the greater good. At the same time, with societal complexity escalating faster than our capacity to manage it, our technologically enabled power to inflict catastrophic harm upon ourselves, each other and our world likewise continues to grow: a disconnect known as ‘the wisdom gap.’",
    "It’s uncontroversial to associate wisdom with rational understanding: with the capacity to grasp what’s going on in a given context, and apply knowledge and analysis to interpret events and guide action. The complexity of our times plainly overwhelms understanding, and it’s tempting to suggest that this shortfall alone explains our ‘wisdom gap’. Still, most would intuitively agree that there’s more to wisdom than analytical skill.",
]
CAPTION = "A rapidly growing gap between society’s technological and social complexity and our “wisdom”, our capacity to manage that complexity well. The curves show a direction, not measured trajectories."

CONTEXT_CSS = """
.sv svg.fig { border: 0 }
.sv svg.fig > rect:first-child { fill: transparent }  /* in a page the figure takes the page's ground */
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

# ── Charts with data (2026-10-08) ────────────────────────────────
# Static figures for papers and posts, not dashboards: emphasis after the FT and the Economist.
# Red for the series the chart is about; a warm grey for the rest (validated: >= 3:1 on the
# ground, CVD dE 10.8 against the red); ink when two things are compared. Data is illustrative.
CH = {"light": dict(grey="#8a847a", rule="#e0dacf"), "dark": dict(grey="#8f897f", rule="#38342e")}
# ticks: Apfel Regular 24px at 60% ink; values at bar ends and dots 26px in ink (see charts_page CSS)

def chart_frame(theme, title, subtitle, body, H, source="Source: illustrative data, for the design system"):
    ink = THEMES[theme]["ink"]
    return (f'<svg class="fig" viewBox="0 0 {W} {H}" role="img" aria-label="{title}">'
            f'<rect width="{W}" height="{H}" fill="{THEMES[theme]["ground"]}"/>'
            f'<text x="{M}" y="{M + 42}" class="d-title" fill="{ink}">{title}</text>'
            f'<text x="{M}" y="{M + 84}" class="d-subtitle" fill="{ink}">{subtitle}</text>'
            f'{body}<text x="{M}" y="{H - SIG_FOOT - DISC / 2 + 8}" class="d-source" fill="{ink}">{source}</text>'
            f'{sig_at(H, theme)}</svg>')

def chart_line(theme="light"):
    ink, c = THEMES[theme]["ink"], CH[theme]
    years = list(range(2015, 2026))
    series = [  # name, values, emphasised?
        ("Gatherings", [100, 106, 113, 121, 128, 74, 92, 131, 152, 171, 189], True),
        ("Talks", [100, 103, 108, 112, 116, 58, 84, 110, 118, 124, 128], False),
        ("Courses", [100, 99, 103, 104, 106, 88, 97, 101, 103, 102, 104], False),
        ("Retreats", [100, 98, 96, 95, 93, 40, 58, 70, 74, 77, 79], False),
    ]
    x0, x1, y0, y1, H = M + 70, 1330, 900, 220, 1080
    X = lambda i: x0 + (x1 - x0) * i / (len(years) - 1)
    Y = lambda v: y0 - (y0 - y1) * v / 200
    # an event as a pale band behind the data, labelled at its top (not a note among the lines)
    out = [f'<rect x="{X(4.5):.1f}" y="{Y(200):.1f}" width="{X(5.5) - X(4.5):.1f}" height="{Y(0) - Y(200):.1f}" fill="{c["rule"]}" fill-opacity=".55"/>',
           f'<text x="{X(5):.1f}" y="{Y(200) - 14:.1f}" text-anchor="middle" class="d-tick" fill="{ink}">Pandemic</text>']
    for v in (0, 50, 100, 150, 200):
        out.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="{ink if v == 0 else c["rule"]}" stroke-width="{2 if v == 0 else 1.5}"/>')
        out.append(f'<text x="{x0 - 16}" y="{Y(v) + 8:.1f}" text-anchor="end" class="d-tick" fill="{ink}">{v}</text>')
    for i, yv in enumerate(years):
        if yv % 2 == 1 or yv == 2025:
            out.append(f'<text x="{X(i):.1f}" y="{y0 + 40}" text-anchor="middle" class="d-tick" fill="{ink}">{yv}</text>')
    for name, vals, em in sorted(series, key=lambda s: s[2]):  # the emphasised line drawn last, on top
        col, sw = (RED, 4) if em else (c["grey"], 3)
        out.append(line([(X(i), Y(v)) for i, v in enumerate(vals)], col, sw))
        out.append(f'<circle cx="{X(len(vals) - 1):.1f}" cy="{Y(vals[-1]):.1f}" r="7" fill="{col}" stroke="{THEMES[theme]["ground"]}" stroke-width="3"/>')
        out.append(f'<text x="{x1 + 22}" y="{Y(vals[-1]) + 9:.1f}" class="{"d-label-em" if em else "d-label"}" fill="{ink}">{name} <tspan fill-opacity=".6">{vals[-1]}</tspan></text>')
    return chart_frame(theme, "Gatherings have grown fastest since the pandemic",
                       "Attendance by kind of event, indexed (2015 = 100) · illustrative data", "".join(out), H)

def chart_bars(theme="light"):
    ink, c = THEMES[theme]["ink"], CH[theme]
    rows = [("Time with the people I love", 64), ("Time in nature", 52), ("Meaningful work", 47),
            ("Quiet and reflection", 39), ("Learning", 33), ("Community", 28), ("Money", 21)]
    lx, x0, x1, top, band, bar = M, 560, 1380, 210, 82, 44
    X = lambda v: x0 + (x1 - x0) * v / 70
    H = top + band * len(rows) + 60 + SIG_GAP + DISC + SIG_FOOT
    out = []
    for v in (0, 10, 20, 30, 40, 50, 60, 70):
        out.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{top - 6}" y2="{top + band * len(rows)}" stroke="{ink if v == 0 else c["rule"]}" stroke-width="{2 if v == 0 else 1.5}"/>')
        out.append(f'<text x="{X(v):.1f}" y="{top + band * len(rows) + 40}" text-anchor="middle" class="d-tick" fill="{ink}">{v}</text>')
    for i, (name, v) in enumerate(rows):
        em = name == "Money"
        yc = top + band * i + band / 2
        out.append(f'<text x="{lx}" y="{yc + 10:.1f}" class="{"d-label-em" if em else "d-label"}" fill="{ink}">{name}</text>')
        out.append(f'<rect x="{X(0) + 1}" y="{yc - bar / 2:.1f}" width="{X(v) - X(0) - 1:.1f}" height="{bar}" fill="{RED if em else TINT[theme]}"/>')  # the tint for the rest, as in panels
        out.append(f'<text x="{X(v) + 14:.1f}" y="{yc + 9:.1f}" class="d-tick-strong" fill="{ink}">{v}</text>')
    return chart_frame(theme, "People want more time, not more money",
                       "What people would most like more of, % choosing each · illustrative data", "".join(out), H)

def chart_dumbbell(theme="light"):
    ink, c = THEMES[theme]["ink"], CH[theme]
    rows = [("Science", 70, 62), ("Local community", 61, 58), ("Big tech", 48, 27),
            ("Courts", 52, 41), ("News media", 38, 24), ("Government", 36, 22)]
    rows.sort(key=lambda r: r[2] - r[1])  # biggest fall first
    lx, x0, x1, top, band = M, 500, 1380, 260, 92
    X = lambda v: x0 + (x1 - x0) * v / 80
    H = top + band * len(rows) + 60 + SIG_GAP + DISC + SIG_FOOT
    out = [f'<circle cx="{M + 10}" cy="{top - 62}" r="10" fill="{c["grey"]}"/><text x="{M + 30}" y="{top - 54}" class="d-label" fill="{ink}">2015</text>',
           f'<circle cx="{M + 140}" cy="{top - 62}" r="10" fill="{RED}"/><text x="{M + 160}" y="{top - 54}" class="d-label" fill="{ink}">2025</text>']
    for v in (0, 20, 40, 60, 80):
        out.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{top - 10}" y2="{top + band * len(rows)}" stroke="{c["rule"]}" stroke-width="1.5"/>')
        out.append(f'<text x="{X(v):.1f}" y="{top + band * len(rows) + 40}" text-anchor="middle" class="d-tick" fill="{ink}">{v}</text>')
    for i, (name, a, b) in enumerate(rows):
        yc = top + band * i + band / 2
        out.append(f'<text x="{lx}" y="{yc + 10:.1f}" class="d-label" fill="{ink}">{name}</text>')
        out.append(f'<line x1="{X(b):.1f}" x2="{X(a):.1f}" y1="{yc}" y2="{yc}" stroke="{TINT[theme]}" stroke-width="12" stroke-linecap="round"/>')
        out.append(f'<circle cx="{X(a):.1f}" cy="{yc}" r="10" fill="{c["grey"]}" stroke="{THEMES[theme]["ground"]}" stroke-width="3"/>')
        out.append(f'<circle cx="{X(b):.1f}" cy="{yc}" r="10" fill="{RED}" stroke="{THEMES[theme]["ground"]}" stroke-width="3"/>')
        out.append(f'<text x="{X(b) - 22:.1f}" y="{yc + 8:.1f}" text-anchor="end" class="d-tick-strong" fill="{ink}">{b}</text>')
    return chart_frame(theme, "Trust fell in every institution",
                       "Share who trust each a great deal or quite a lot, %, 2015 and 2025 · illustrative data", "".join(out), H)

CHART_CSS = """
.d-tick { font-family: "Apfel Grotezk", "Hanken Grotesk", sans-serif; font-size: 24px; fill-opacity: .6; font-variant-numeric: tabular-nums }
.d-tick-strong { font-family: "Apfel Grotezk", "Hanken Grotesk", sans-serif; font-size: 26px; font-variant-numeric: tabular-nums }
.d-label-em { font-family: "Apfel Grotezk", "Hanken Grotesk", sans-serif; font-weight: 500; font-size: 29px }
.d-source { font-family: "Apfel Grotezk", "Hanken Grotesk", sans-serif; font-size: 20px; fill-opacity: .6 }
"""

# ── The gallery ──────────────────────────────────────────────────
GUIDE = "../../diagrams.md"
EXAMPLES = [  # id, title, what it shows, the rules it illustrates (guide anchors), maker
    ("wisdom-gap", "The wisdom gap", "A conceptual curve. The key area in the red tint, labelled in red; two weights of line; solid arrowheads.",
     [("Drawing style", "drawing-style"), ("Type", "type")], gap_svg),
    ("polycrisis", "From polycrisis to metacrisis", "A framework. Layers as panels in the red tint, sized to their text, with even padding; brackets for groups.",
     [("Drawing style", "drawing-style")], poly_svg),
    ("chart-line", "Lines: one series in red", "Change over time. The series the title is about in red, the rest grey, names at the line ends, an event as a pale band.",
     [("Charts with data", "charts-with-data")], chart_line),
    ("chart-bars", "Ranked bars: one bar in red", "Comparison. Bars in the tint, the one that matters in red, values at the tips.",
     [("Charts with data", "charts-with-data")], chart_bars),
    ("chart-dots", "Before and after: two dots per row", "Change between two dates. Older in grey, newer in red, joined by the tint; a small key.",
     [("Charts with data", "charts-with-data")], chart_dumbbell),
]
PAPER = here.parents[4] / "2rbook" / "wisdom" / "assets"  # the real paper figures, if that repo is beside this one
REAL = [("wisdom-gap-figure", "The Wisdom Gap", "Fig. 1"), ("dimensions-of-wisdom", "Three Dimensions of Wisdom", "")]

def gallery_page(bundle):
    def img(name, alt):
        src = b64(here / "img" / f"{name}.png") if bundle else f"img/{name}.png"
        return f'<img class="fig" src="{src}" alt="{alt}" loading="lazy">'
    toc = " · ".join(f'<a href="#{k}">{t}</a>' for k, t, *_ in EXAMPLES) + ' · <a href="#in-use">In a page</a> · <a href="#paper">The Wisdom paper</a>'
    secs = "".join(f'''
  <section id="{k}">
    <h2>{t}</h2>
    <p class="fnote">{what} Rules: {", ".join(f'<a href="{GUIDE}#{a}">{n}</a>' for n, a in rules)}.</p>
    <div class="pair">{zoomable(fn("light"), "Light. Click for full size.")}{zoomable(fn("dark"), "Dark.")}</div>
    <div class="thumbs">
      <figure class="thumb"><div class="thumb-box">{fn("light")}</div><figcaption>At 400px, as in a feed</figcaption></figure>
      <figure class="thumb"><div class="thumb-box">{fn("dark")}</div><figcaption>At 400px, dark</figcaption></figure>
      <figure class="thumb"><div class="thumb-box bw">{fn("light")}</div><figcaption>Printed in black and white</figcaption></figure>
    </div>
  </section>''' for k, t, what, rules, fn in EXAMPLES)
    real = "".join(f'<figure>{img(n, t)}<figcaption>{f"<b>{fig}</b> · " if fig else ""}{t}</figcaption></figure>' for n, t, fig in REAL if (here / "img" / f"{n}.png").exists())
    body = f'''
  <p class="label">Seeds of Renaissance design system · Diagrams</p>
  <h1>Diagram examples</h1>
  <div class="intro">
    <p>Finished figures in the house style, to copy. Each is shown in light and dark, at 400px as in a feed, and printed in black and white; then in use, on a page of a paper and in a web article. How to make one, and the rules: <a href="{GUIDE}">the diagrams guide</a>.</p>
    <p class="fnote">Chart data is illustrative, made up for the style. Do not quote it.</p>
    <p class="fnote">{toc}</p>
  </div>
  {secs}
  <section id="in-use">
    <h2>In a page</h2>
    <p class="fnote">Beside running text: Bricolage for the text, Apfel in the figure. In a page the figure has no white box; it takes the page's ground. The caption gives the number and a sentence, not the title again.</p>
    <h3 class="label">A page of the paper (A4, figure as a plate)</h3>
    <div class="sheet-wrap"><div class="sheet">
      <div class="rh"><span>4</span><span>Wisdom and Wanting What’s Good</span></div>
      <h4 class="ph2">Addressing the wisdom gap</h4>
      <p class="pp">{PAPER_P[0]}<sup>7</sup></p>
      <figure class="plate"><div class="art sv">{gap_svg("light")}</div>
        <figcaption><span class="flbl">Fig. 1</span><span>{CAPTION}<sup>8</sup></span></figcaption></figure>
      <p class="pp">{PAPER_P[1]}</p>
    </div></div>
    <h3 class="label">A web article</h3>
    <div class="web-wrap"><article class="web">
      <p class="wlabel">White paper No. 6 · Wisdom and Wanting What’s Good</p>
      <h4 class="wh2">Addressing the wisdom gap</h4>
      <p>{PAPER_P[0]}</p>
      <figure class="wfig sv">{poly_svg("light")}<figcaption><span class="flbl">Fig. 2</span> The crises we see sit on deeper dysfunctions, which sit on ideas and tendencies we rarely examine. Working on the surface alone does not reach the root.</figcaption></figure>
      <p>{PAPER_P[1]}</p>
    </article></div>
  </section>
  {f'''<section id="paper">
    <h2>The Wisdom paper</h2>
    <p class="fnote">The figures as published in <i>Wisdom and Wanting What’s Good</i> (white paper No. 6), signed with the paper's line in the slot. Built in 2rbook (<code>wisdom/assets/build-*.py</code>).</p>
    <div class="pair">{real}</div>
  </section>''' if real else ""}'''
    return shell("Diagram examples", body, bundle, extra_css=type_css() + CHART_CSS + CONTEXT_CSS + ".bw svg { filter: grayscale(1) }\n.sv { display: block }")

def export_pngs():
    """img/*.png: each example at full size on its ground, for the guide to show inline; plus the
    paper's real figures, copied from 2rbook if it is there."""
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    (here / "img").mkdir(exist_ok=True)
    for name, *_ in REAL:
        if (PAPER / f"{name}.share.png").exists():
            shutil.copy2(PAPER / f"{name}.share.png", here / "img" / f"{name}.png")
    if not pathlib.Path(chrome).exists():
        print("no Chrome: skipped the example PNGs"); return
    css = type_css() + CHART_CSS
    for k, _, _, _, fn in EXAMPLES:
        if k == "wisdom-gap":
            continue  # the paper's own figure (wisdom-gap-figure.png) stands for it
        svg = fn("light")
        w, h = (float(v) for v in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).groups())
        with tempfile.TemporaryDirectory() as tmp:
            page = pathlib.Path(tmp) / "f.html"
            page.write_text(f'<html><head><link rel="stylesheet" href="{(SYSTEM / "fonts.css").as_uri()}"><style>{css} body{{margin:0}} .defs{{position:absolute;width:0;height:0}} svg.fig{{display:block;width:{w}px;height:{h}px}}</style></head><body>{defs()}{svg}</body></html>')
            subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={int(w)},{int(h)}",
                            "--virtual-time-budget=3000", f"--screenshot={here / 'img' / (k + '.png')}", page.as_uri()], check=True, capture_output=True)
        print("img/" + k + ".png")

def for_artifact(html):
    """The publisher adds the document skeleton: keep the head's contents and the body's."""
    head = html[html.index("<title>"):html.index("</head>")]
    body = html[html.index("<body>") + 6:html.index("</body>")]
    return head + body.replace(f'href="{GUIDE}', 'href="https://sor-design-system-rufuspollock.flowershow.me/diagrams')

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--bundle":
        out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(for_artifact(gallery_page(bundle=True)))
    else:
        export_pngs()
        (here / "index.html").write_text(gallery_page(bundle=False))
