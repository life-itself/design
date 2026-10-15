"""Build the Grove thumbnail page and the tree PNG sources.

Reads the tree and fingerprint seeds from the Grove channel page
(SoR brand repo, mockups/youtube-grove/index.html), the logo and woodcut
mountains from the design system, and writes:

  thumbnail.html          the artifact page (three grounds, feed sizes)
  png/*.html              one page per PNG, screenshotted by export.sh
"""
import base64, re, pathlib

HERE = pathlib.Path(__file__).parent
SYS = HERE.parents[2] / "system"
GROVE = pathlib.Path("/Users/shiwei/src/SoR brand/mockups/youtube-grove/index.html")

src = GROVE.read_text()
defs = re.search(r"<defs>.*?</defs>", src, re.S).group(0)
trees = re.findall(r'<svg class="tree" viewBox="([^"]*)">(.*?)</svg>', src, re.S)
upright = next(t for vb, t in trees if vb == "0 0 1280 720")
banner = next(t for vb, t in trees if vb == "0 0 2048 1152")
# seeds that fell below the trunk (hidden off-canvas in the original card)
upright = re.sub(r'<use href="#fp\d+" transform="translate\([\d.]+ (6[6-9]\d|[7-9]\d\d)\)[^>]*/>', "", upright)
# the seed that sat at the end of "Renaissance" on the banner
banner = re.sub(r'<use href="#fp\d+" transform="translate\(900 576\)[^>]*/>', "", banner)


def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()


def font(family, path, weight=400, fmt="truetype"):
    mime = "otf" if fmt == "opentype" else "ttf"
    return (f'@font-face{{font-family:"{family}";font-weight:{weight};'
            f'src:url(data:font/{mime};base64,{b64(path)}) format("{fmt}")}}')


apfel = (SYS / "fonts.css").read_text().splitlines()[2]  # Apfel Grotezk 500
fonts = "\n".join([
    font("Polyamine", "/Users/shiwei/Library/Fonts/Polyamine.ttf"),
    font("Restora", "/Users/shiwei/Library/Fonts/FontsFree-Net-RestoraExtraLight.ttf", 200),
    apfel,
])
logo = b64(SYS / "img/logo.png")


def mountain(name, colour):
    svg = (SYS / f"graphics/woodcuts/elements/{name}.svg").read_text().replace("color:#1b1916", f"color:{colour}")
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


def bbox(tree):
    pts = [(float(x), float(y)) for x, y in re.findall(r"[MQ ](\d+(?:\.\d+)?) (\d+(?:\.\d+)?)", tree)]
    pts += [(float(x), float(y)) for x, y in re.findall(r"translate\(([\d.]+) ([\d.]+)\)", tree)]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    pad = 30
    return min(xs) - pad, min(ys) - pad, max(xs) - min(xs) + 2 * pad, max(ys) - min(ys) + 2 * pad


def recolour(tree, stroke):
    return tree.replace('stroke="#C9C3AE"', f'stroke="{stroke}"').replace('opacity=".85"', 'opacity="1"')


GROUNDS = {
    "paper": dict(bg="#fbfaf6", ink="#1b1916", muted="#5d584f", wood="#1b1916", disc="#ffffff", ring="#e0dacf"),
    "sunlight": dict(bg="#fbefc4", ink="#1b1916", muted="#5d584f", wood="#1b1916", disc="#ffffff", ring="#e6d9a8"),
    "night": dict(bg="#171613", ink="#ece7dc", muted="#a49e93", wood="#ece7dc", disc="#ffffff", ring="#38342e"),
}


def thumbnail(g):
    c = GROUNDS[g]
    seeds_filter = ' filter="url(#deepen)"' if g == "sunlight" else ""
    # tree raised so the canopy clears the peaks; mountains drawn over the trunk base
    return f'''<svg class="thumb" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
<rect width="1280" height="720" fill="{c['bg']}"/>
<g transform="translate(30 -150) scale(1.0)"{seeds_filter}>{recolour(upright, c['wood'])}</g>
<use href="#mt-{'chalk' if g=='night' else 'ink'}"/>
<g transform="translate(96 92)">
  <circle cx="62" cy="62" r="62" fill="{c['disc']}" stroke="{c['ring']}" stroke-width="2"/>
  <clipPath id="disc-{g}"><circle cx="62" cy="62" r="54"/></clipPath>
  <use href="#logo-img" clip-path="url(#disc-{g})"/>
</g>
<text x="96" y="318" fill="{c['muted']}" font-family="Apfel Grotezk" font-weight="500" font-size="26" letter-spacing="4">OVER THE MOUNTAINS</text>
<text fill="{c['ink']}" font-family="Polyamine" font-size="96"><tspan x="92" y="420">Seeds of</tspan><tspan x="92" y="514">Renaissance</tspan></text>
<text fill="{c['ink']}" font-family="Restora" font-weight="200" font-size="38"><tspan x="96" y="590">Vision and movement</tspan><tspan x="96" y="636">for civilisational renewal</tspan></text>
</svg>'''


def thumbnail_speaker():
    """Paper, speaker version: the tree recedes to the top left (no logo, no label),
    and the speaker's portrait rises over the peaks where the tree was."""
    c = GROUNDS["paper"]
    # extend the trunk to the bottom edge, then scale the tree so its canopy fills the top left
    tree = (f'<path d="M1000 940Q1012 850 1000 760" fill="none" stroke="{c["wood"]}" stroke-width="5.6" stroke-linecap="round"/>'
            + recolour(upright, c["wood"]))
    return f'''<svg class="thumb" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
<rect width="1280" height="720" fill="{c['bg']}"/>
<g opacity=".42" transform="translate(-1000 -380) scale(1.3)">{tree}</g>
<clipPath id="speaker"><circle cx="985" cy="292" r="168"/></clipPath>
<circle cx="985" cy="292" r="178" fill="none" stroke="{c['ink']}" stroke-width="2.5"/>
<use href="#speaker-img" clip-path="url(#speaker)"/>
<use href="#mt-ink"/>
<text fill="{c['ink']}" font-family="Polyamine" font-size="96"><tspan x="92" y="436">Seeds of</tspan><tspan x="92" y="530">Renaissance</tspan></text>
<text fill="{c['ink']}" font-family="Restora" font-weight="200" font-size="38"><tspan x="96" y="606">Vision and movement</tspan><tspan x="96" y="652">for civilisational renewal</tspan></text>
</svg>'''


LONG = ["s-sunflower", "s-samara", "s-wheat", "s-pumpkin"]
SEEDS = ["s-sunflower", "s-bean", "s-samara", "s-acorn", "s-pumpkin", "s-stone", "s-wheat", "s-dandelion"]


def thumbnail_burst():
    """Paper, seed burst: woodcut seeds explode outward from the speaker's portrait."""
    import math, random
    c = GROUNDS["paper"]
    rnd = random.Random(7)
    cx, cy, r = 930, 330, 150
    text_box = (60, 370, 680, 690)  # keep the title clear
    placed, out = [], []
    for ring, (rad, n, size) in enumerate([(200, 20, 28), (248, 24, 34), (305, 28, 40), (372, 30, 48), (450, 34, 56), (540, 38, 64), (645, 42, 72)]):
        for i in range(n):
            a = 2 * math.pi * (i + rnd.uniform(-.35, .35) + ring * .37) / n
            d = rad + rnd.uniform(-22, 22)
            x, y = cx + d * math.cos(a), cy + d * math.sin(a)
            s = size * rnd.uniform(.8, 1.15)
            if not (-s < x < 1280 + s * .3 and -s < y < 720 + s * .3):
                continue
            if text_box[0] - s < x < text_box[2] and text_box[1] - s < y < text_box[3]:
                continue
            if (x - cx) ** 2 + (y - cy) ** 2 < (r + 95 + s / 2) ** 2:
                continue
            if any((x - px) ** 2 + (y - py) ** 2 < ((s + ps) * .52) ** 2 for px, py, ps in placed):
                continue
            placed.append((x, y, s))
            red = rnd.random() < .16
            rot = math.degrees(a) + 90 + rnd.uniform(-14, 14)
            out.append(f'<use href="#{rnd.choice(LONG if rnd.random() < .7 else SEEDS)}" x="{-s/2:.1f}" y="{-s/2:.1f}" width="{s:.1f}" height="{s:.1f}" '
                       f'transform="translate({x:.1f} {y:.1f}) rotate({rot:.0f})" color="{"#e5201c" if red else c["ink"]}"/>')
    rays = []
    for i in range(64):
        a = 2 * math.pi * (i + rnd.uniform(-.3, .3)) / 64
        r0, r1 = r + 22 + rnd.uniform(0, 8), r + 30 + rnd.uniform(18, 62)
        rays.append(f'<line x1="{cx + r0 * math.cos(a):.1f}" y1="{cy + r0 * math.sin(a):.1f}" x2="{cx + r1 * math.cos(a):.1f}" y2="{cy + r1 * math.sin(a):.1f}" stroke-width="{rnd.uniform(1.6, 3.6):.1f}"/>')
    return f'''<svg class="thumb" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
<rect width="1280" height="720" fill="{c['bg']}"/>
<g stroke="{c['ink']}" stroke-linecap="round">{"".join(rays)}</g>
{"".join(out)}
<circle cx="{cx}" cy="{cy}" r="{r + 12}" fill="{c['bg']}" stroke="{c['ink']}" stroke-width="2.5"/>
<clipPath id="burst-speaker"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>
<image href="#" data-ref="speaker" x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" clip-path="url(#burst-speaker)"/>
<text fill="{c['ink']}" font-family="Polyamine" font-size="96"><tspan x="80" y="470">Seeds of</tspan><tspan x="80" y="564">Renaissance</tspan></text>
<text fill="{c['ink']}" font-family="Restora" font-weight="200" font-size="38"><tspan x="84" y="624">Vision and movement</tspan><tspan x="84" y="668">for civilisational renewal</tspan></text>
</svg>'''.replace('<image href="#" data-ref="speaker"', f'<image href="data:image/jpeg;base64,{SPEAKER}"')


SPEAKER = b64(SYS / "img/otm-guest-placeholder.jpg")
GRAPHICS = (SYS / "graphics.svg").read_text()

MDEFS = f'<image id="speaker-img" href="data:image/jpeg;base64,{b64(SYS / "img/otm-guest-placeholder.jpg")}" x="817" y="124" width="336" height="336"/>' + ''.join(f'<image id="mt-{n}" href="{mountain("mountain-range", col)}" x="560" y="372" width="780" height="487.5"/>' for n, col in [("ink", "#1b1916"), ("chalk", "#ece7dc")])
DEEPEN = '<svg width="0" height="0" style="position:absolute"><filter id="deepen"><feColorMatrix type="saturate" values="1.25"/></filter></svg>'

# ---- artifact page -------------------------------------------------------
cards = []
for g, label, note in [
    ("burst", "Paper · seed burst", "A separate direction: the design system’s woodcut seeds explode out of the speaker’s portrait, a few in the logo red. No tree, no mountains. Portrait is a placeholder."),
    ("speaker", "Paper · speaker", "The tree steps back into the top left, behind the type, in place of the logo. The speaker’s portrait rises over the peaks where the tree stood. Portrait is a placeholder."),
    ("paper", "Paper", "The default ground. Logo on its white disc, woodcut mountains in ink, the Grove tree rising behind them."),
    ("sunlight", "Sunlight", "Pale yellow for joy. Same ink woodcut; the disc gets a warm hairline so it doesn’t float."),
    ("night", "Night", "The system’s one dark ground. Mountains and branches turn chalk, as woodcuts do on night."),
]:
    t = {"speaker": thumbnail_speaker, "burst": thumbnail_burst}.get(g, lambda: thumbnail(g))()
    feed = "".join(
        f'<figure class="feed" style="width:{w}px"><div class="fr">{t}<span class="dur">1:12:40</span></div>'
        f'<figcaption>{w}px · {cap}</figcaption></figure>'
        for w, cap in [(360, "desktop home"), (168, "up next")])
    cards.append(f'''<section class="g">
<div class="eb">{label} · {GROUNDS.get(g, GROUNDS['paper'])['bg']}</div><h2>{label}</h2><p class="note">{note}</p>
<div class="full">{t}</div>
<div class="feeds">{feed}</div>
</section>''')

pngs = "".join(
    f'<figure class="el {cls}"><img src="png/{name}.png" alt="{alt}"><figcaption><b>{name}.png</b> · {alt}</figcaption></figure>'
    for name, cls, alt in [
        ("grove-tree-ink", "lt", "upright tree, ink branches, for paper and sunlight"),
        ("grove-tree-chalk", "dk", "upright tree, chalk branches, for night"),
        ("grove-branch-ink", "lt", "the banner’s sideways tree, ink branches"),
        ("grove-branch-chalk", "dk", "the banner’s sideways tree, chalk branches"),
        ("seeds-spiral-ink", "lt", "the sunflower spiral woodcut, ink (SVG alongside)"),
        ("seeds-spiral-red", "lt", "the sunflower spiral woodcut, logo red (SVG alongside)"),
        ("seeds-spiral-chalk", "dk", "the sunflower spiral woodcut, chalk for night (SVG alongside)"),
    ])

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Grove Thumbnail</title>
<style>
{fonts}
:root{{--bg:#f3f2ee;--sf:#fff;--ink:#1b1916;--mu:#5d584f;--ru:#e0dacf}}
@media(prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#121110;--sf:#1c1b19;--ink:#ece7dc;--mu:#a49e93;--ru:#38342e}}}}
:root[data-theme="dark"]{{--bg:#121110;--sf:#1c1b19;--ink:#ece7dc;--mu:#a49e93;--ru:#38342e}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 system-ui,-apple-system,sans-serif;padding:0 16px 64px}}
.wrap{{max-width:1100px;margin:auto}}
header{{padding:44px 0 12px}}
h1{{font:400 clamp(30px,5vw,52px)/1.05 Polyamine,Georgia,serif;margin:8px 0 12px}}
h2{{font:400 32px/1.1 Polyamine,Georgia,serif;margin:4px 0 6px}}
.eb,figcaption{{font:500 12px "Apfel Grotezk",ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--mu)}}
header p,.note{{color:var(--mu);max-width:68ch;margin:0 0 16px}}
.g{{border-top:1px solid var(--ru);padding:36px 0 8px}}
.full svg,.fr svg{{display:block;width:100%;height:auto;border-radius:10px}}
.full{{box-shadow:0 0 0 1px var(--ru);border-radius:10px}}
.feeds{{display:flex;flex-wrap:wrap;gap:24px;align-items:flex-start;margin-top:18px}}
.feed{{margin:0}}.fr{{position:relative}}.fr svg{{border-radius:8px;box-shadow:0 0 0 1px var(--ru)}}
.feed[style*="168"] .fr svg{{border-radius:5px}}
.dur{{position:absolute;right:4px;bottom:4px;background:rgba(0,0,0,.8);color:#fff;font:600 11px system-ui;padding:1px 4px;border-radius:4px}}
figcaption{{margin-top:6px;font-size:11px}}
.els{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;margin-top:16px}}
.el{{margin:0;border:1px solid var(--ru);border-radius:10px;padding:16px;background:var(--sf)}}
.el img{{display:block;width:100%;height:220px;object-fit:contain;border-radius:6px;
  background:repeating-conic-gradient(#0000 0 25%,#0000000d 0 50%) 0 0/16px 16px}}
.el.lt img{{background-color:#fbfaf6}}.el.dk img{{background-color:#171613}}
.el b{{color:var(--ink)}}
</style></head><body>{DEEPEN}<svg width="0" height="0" style="position:absolute" aria-hidden="true">{defs}<defs><image id="logo-img" href="data:image/png;base64,{logo}" x="8" y="8" width="108" height="108"/>{MDEFS}</defs></svg>
{GRAPHICS}<div class="wrap">
<header><div class="eb">Seeds of Renaissance · YouTube · Grove thumbnail</div>
<h1>Grove thumbnail, with logo and mountains</h1>
<p>A 1280 × 720 thumbnail: the logo on its white disc, the name in Polyamine, the tagline in Restora, and the woodcut mountain range with the Grove tree rising behind it. Each ground is shown full size and at the two feed sizes, with the duration badge in place.</p></header>
{"".join(cards)}
<section class="g"><div class="eb">Elements</div><h2>Elements as PNG</h2>
<p class="note">Transparent PNGs at 4×: the Grove tree and the sunflower spiral seeds. Each spiral also comes as an SVG. The checkerboard shows the transparency.</p>
<div class="els">{pngs}</div></section>
</div></body></html>'''
(HERE / "thumbnail.html").write_text(page)

# ---- PNG sources ---------------------------------------------------------
(HERE / "png").mkdir(exist_ok=True)
for name, tree, stroke in [
    ("grove-tree-ink", upright, "#1b1916"),
    ("grove-tree-chalk", upright, "#ece7dc"),
    ("grove-branch-ink", banner, "#1b1916"),
    ("grove-branch-chalk", banner, "#ece7dc"),
]:
    x, y, w, h = bbox(tree)
    (HERE / "png" / f"{name}.html").write_text(
        f'<!doctype html><html><head><style>html,body{{margin:0;background:transparent}}svg{{display:block}}</style></head><body>'
        f'<svg width="0" height="0" style="position:absolute">{defs}</svg>'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" width="{w:.0f}" height="{h:.0f}">'
        f'{recolour(tree, stroke)}</svg></body></html>')
    print(name, round(w), round(h))

# ---- the sunflower spiral (c-spiral from system/graphics/woodcuts/elements/seeds.svg) -------
sheet = (SYS / "graphics/woodcuts/elements/seeds.svg").read_text()
spiral_defs = sheet[sheet.index("<defs>"):sheet.rindex("</defs>") + len("</defs>")]
for name, colour in [("seeds-spiral-ink", "#1b1916"), ("seeds-spiral-red", "#e5201c"), ("seeds-spiral-chalk", "#ece7dc")]:
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="600" height="600" style="color:{colour}">'
           f'{spiral_defs}<use href="#c-spiral" x="0" y="0" width="200" height="200"/></svg>')
    (HERE / "png" / f"{name}.svg").write_text(svg)
    (HERE / "png" / f"{name}.html").write_text(
        '<!doctype html><html><head><style>html,body{margin:0;background:transparent}svg{display:block}</style></head>'
        f'<body>{svg}</body></html><!-- export size: width="600" height="600" -->')
    print(name, 600, 600)
