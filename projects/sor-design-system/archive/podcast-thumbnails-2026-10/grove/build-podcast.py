"""Podcast episode thumbnails on sunlight: speaker, seed spiral, logo, podcast name,
one-line tagline and a one-to-two-line episode title. Six versions from structured
(masculine) to poetic (feminine). Writes podcast.html.
"""
import base64, math, pathlib, random

HERE = pathlib.Path(__file__).parent
SYS = HERE.parents[2] / "system"


def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()


def font(family, path, weight=400, style="normal", fmt="truetype"):
    mime = "otf" if fmt == "opentype" else "ttf"
    return (f'@font-face{{font-family:"{family}";font-weight:{weight};font-style:{style};'
            f'src:url(data:font/{mime};base64,{b64(path)}) format("{fmt}")}}')


FONTS = "\n".join([
    font("Polyamine", "/Users/shiwei/Library/Fonts/Polyamine.ttf"),
    font("Restora", "/Users/shiwei/Library/Fonts/FontsFree-Net-RestoraExtraLight.ttf", 200),
    font("Restora", "/Users/shiwei/Library/Fonts/nasir-udin-restorathinitalic.otf", 200, "italic", "opentype"),
    (SYS / "fonts.css").read_text().splitlines()[2],  # Apfel Grotezk 500
])

sheet = (SYS / "graphics/woodcuts/elements/seeds.svg").read_text()
DEFS = (sheet[sheet.index("<defs>") + 6:sheet.rindex("</defs>")]
        + f'<image id="spk" href="data:image/jpeg;base64,{b64(SYS / "img/otm-guest-placeholder.jpg")}" width="800" height="800"/>'
        + f'<image id="logo" href="data:image/png;base64,{b64(SYS / "img/logo.png")}" width="600" height="600"/>')

SUN, INK, MUTED, RED, NIGHT, CHALK = "#fbefc4", "#1b1916", "#5d584f", "#e5201c", "#171613", "#ece7dc"
PODCAST = "Seeds of Renaissance"
TAG = "Vision and movement for civilisational renewal"
T1, T2 = "What grows", "after the end"   # placeholder episode title


def spiral(cx, cy, size, colour, rot=0):
    return (f'<use href="#c-spiral" x="{cx - size / 2}" y="{cy - size / 2}" width="{size}" height="{size}" '
            f'color="{colour}" transform="rotate({rot} {cx} {cy})"/>')


def photo(clip_id, shape, x, y, size):
    """The speaker, cropped by `shape` (an SVG element string); photo drawn at size × size from (x, y)."""
    k = size / 800
    return (f'<clipPath id="{clip_id}">{shape}</clipPath>'
            f'<g clip-path="url(#{clip_id})"><use href="#spk" transform="translate({x} {y}) scale({k})"/></g>')


def logo_disc(cx, cy, r, clip_id):
    k = (r * 1.76) / 600
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff"/>'
            f'<clipPath id="{clip_id}"><circle cx="{cx}" cy="{cy}" r="{r * .86}"/></clipPath>'
            f'<g clip-path="url(#{clip_id})"><use href="#logo" transform="translate({cx - r * .88} {cy - r * .88}) scale({k})"/></g>')


def arch(x0, x1, top, bottom):
    w = (x1 - x0) / 2
    return f'<path d="M{x0} {bottom}V{top + w}A{w} {w} 0 0 1 {x1} {top + w}V{bottom}Z"/>'


def torn(y, amp=12, seed=3, x0=-10, x1=1290):
    rnd = random.Random(seed)
    pts, x = [], x0
    while x < x1:
        pts.append(f"{x:.0f} {y + rnd.uniform(-amp, amp) * (0.4 if rnd.random() < .6 else 1):.1f}")
        x += rnd.uniform(5, 14)
    return "M" + " L".join(pts) + f" L{x1} 730 L{x0} 730Z"


def svg(body):
    return (f'<svg class="thumb" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="1280" height="720" fill="{SUN}"/>{body}</svg>')


def poly(x, y, size, text, fill=INK, anchor="start"):
    return f'<text x="{x}" y="{y}" font-family="Polyamine" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{text}</text>'


def restora(x, y, size, text, fill=INK, italic=False, anchor="start"):
    st = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" font-family="Restora" font-weight="200"{st} font-size="{size}" fill="{fill}" text-anchor="{anchor}">{text}</text>'


def apfel(x, y, size, text, fill=INK, track=.12, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="Apfel Grotezk" font-weight="500" font-size="{size}" fill="{fill}" '
            f'letter-spacing="{size * track:.1f}" text-anchor="{anchor}">{text.upper()}</text>')


# ---- the six versions -----------------------------------------------------

def v_halo():
    cx, cy = 985, 360
    return svg(
        spiral(cx, cy, 640, RED)
        + f'<circle cx="{cx}" cy="{cy}" r="196" fill="{SUN}"/>'
        + photo("halo", f'<circle cx="{cx}" cy="{cy}" r="178"/>', cx - 190, cy - 190, 380)
        + f'<circle cx="{cx}" cy="{cy}" r="186" fill="none" stroke="{INK}" stroke-width="3"/>'
        + logo_disc(110, 110, 46, "halo-l") + poly(176, 124, 38, PODCAST)
        + poly(64, 350, 84, T1) + poly(64, 444, 84, T2)
        + restora(66, 642, 30, TAG))


def v_grid():
    x0, y0, s = 760, 96, 420
    return svg(
        spiral(x0 + s / 2, y0 + s / 2, 600, INK, 8)
        + photo("grid", f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}"/>', x0, y0, s)
        + f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="none" stroke="{INK}" stroke-width="8"/>'
        + f'<rect x="64" y="86" width="560" height="8" fill="{INK}"/>'
        + logo_disc(100, 160, 36, "grid-l") + apfel(150, 172, 30, PODCAST)
        + poly(64, 360, 84, T1) + poly(64, 456, 84, T2)
        + f'<rect x="0" y="626" width="1280" height="94" fill="{INK}"/>'
        + apfel(64, 684, 24, TAG, SUN, .1))


def v_torn():
    cx, cy = 330, 300
    return svg(
        spiral(cx, cy, 600, RED, -6)
        + f'<path d="{torn(560, 10, 5)}" fill="{NIGHT}"/>'
        + f'<circle cx="{cx}" cy="{cy}" r="180" fill="{SUN}"/>'
        + photo("torn", f'<circle cx="{cx}" cy="{cy}" r="164"/>', cx - 176, cy - 176, 352)
        + f'<circle cx="{cx}" cy="{cy}" r="172" fill="none" stroke="{INK}" stroke-width="3"/>'
        + poly(640, 240, 88, T1) + poly(640, 338, 88, T2)
        + logo_disc(110, 640, 40, "torn-l") + poly(166, 653, 36, PODCAST, CHALK)
        + restora(640, 652, 28, TAG, CHALK))


def v_bloom():
    x0, x1, top = 800, 1150, 120
    cx = (x0 + x1) / 2
    return svg(
        spiral(cx, top + 175, 700, RED, 14)
        + f'<path d="M{x0 - 16} 720V{top + 159}A{(x1 - x0) / 2 + 16} {(x1 - x0) / 2 + 16} 0 0 1 {x1 + 16} {top + 159}V720Z" fill="{SUN}"/>'
        + photo("bloom", arch(x0, x1, top, 720), x0 - 90, top - 10, 530)
        + f'<path d="M{x0 - 8} 720V{top + 167}A{(x1 - x0) / 2 + 8} {(x1 - x0) / 2 + 8} 0 0 1 {x1 + 8} {top + 167}V720" fill="none" stroke="{INK}" stroke-width="2"/>'
        + logo_disc(104, 104, 40, "bloom-l") + poly(160, 117, 34, PODCAST)
        + restora(60, 350, 86, T1, italic=True) + restora(60, 446, 86, T2, italic=True)
        + restora(64, 640, 30, TAG))


def v_two_voices():
    cx, cy = 1040, 300
    return svg(
        spiral(cx, cy, 740, INK, -10)
        + spiral(120, 690, 220, RED, 30)
        + f'<circle cx="{cx}" cy="{cy}" r="170" fill="{SUN}"/>'
        + photo("two", f'<circle cx="{cx}" cy="{cy}" r="156"/>', cx - 168, cy - 168, 336)
        + logo_disc(104, 100, 38, "two-l") + apfel(156, 112, 28, PODCAST)
        + poly(64, 330, 88, T1) + restora(66, 426, 80, T2, italic=True)
        + apfel(66, 520, 20, TAG, MUTED, .1))


def v_seal():
    cx, cy = 640, 268
    return svg(
        spiral(cx, cy, 470, RED)
        + f'<circle cx="{cx}" cy="{cy}" r="138" fill="{SUN}"/>'
        + photo("seal", f'<circle cx="{cx}" cy="{cy}" r="126"/>', cx - 136, cy - 136, 272)
        + f'<circle cx="{cx}" cy="{cy}" r="132" fill="none" stroke="{INK}" stroke-width="2.5"/>'
        + logo_disc(96, 92, 34, "seal-l") + poly(144, 104, 32, PODCAST)
        + poly(640, 598, 76, f"{T1} {T2}", anchor="middle")
        + restora(640, 656, 28, TAG, anchor="middle"))


VERSIONS = [
    ("halo", "Halo", "Balanced", v_halo,
     "The red spiral as a halo around the speaker. Polyamine title, Restora tagline, logo and name small at the top. The even mix: hard type, soft ring."),
    ("grid", "Grid", "More masculine", v_grid,
     "A square portrait in a heavy ink frame, the spiral in ink behind it, a rule at the top and an ink band carrying the tagline in caps. Straight edges, few curves."),
    ("torn", "Torn ground", "Masculine leaning", v_torn,
     "Mirrored: the speaker left, the title right. A night band tears in along the bottom (the system’s dark ground and torn edge) to carry the logo and tagline."),
    ("bloom", "Bloom", "More feminine, poetic", v_bloom,
     "The speaker in an arch, the red spiral opening around it like a flower. Title in Restora italic for a softer, poetic voice. Lots of air."),
    ("two", "Two voices", "Combined", v_two_voices,
     "The title itself joins both: Polyamine for the first line, Restora italic for the second. A large ink spiral radiates from the speaker; a small red spiral is sown in the corner."),
    ("seal", "Seal", "Balanced, formal", v_seal,
     "Centred and symmetrical, like a seal: the speaker in a small red spiral, the title on one line beneath. Calm and formal; the title must stay short."),
]

cards = []
for vid, name, lean, fn, note in VERSIONS:
    t = fn()
    feeds = "".join(
        f'<figure class="feed" style="width:{w}px"><div class="fr">{t}<span class="dur">1:12:40</span></div>'
        f'<figcaption>{w}px · {cap}</figcaption></figure>' for w, cap in [(360, "desktop home"), (168, "up next")])
    cards.append(f'<section class="v" id="{vid}"><div class="eb">{lean}</div><h2>{name}</h2><p class="note">{note}</p>'
                 f'<div class="full">{t}</div><div class="feeds">{feeds}</div></section>')

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Podcast Thumbnails</title>
<style>
{FONTS}
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
.toc{{display:flex;flex-wrap:wrap;gap:8px 18px;margin:8px 0 0;padding:0;list-style:none;font-size:14px}}
.toc a{{color:var(--ink)}}
.v{{border-top:1px solid var(--ru);padding:36px 0 8px}}
.full svg,.fr svg{{display:block;width:100%;height:auto;border-radius:10px}}
.full{{box-shadow:0 0 0 1px var(--ru);border-radius:10px}}
.feeds{{display:flex;flex-wrap:wrap;gap:24px;align-items:flex-start;margin-top:18px}}
.feed{{margin:0}}.fr{{position:relative}}.fr svg{{border-radius:8px}}
.dur{{position:absolute;right:4px;bottom:4px;background:rgba(0,0,0,.8);color:#fff;font:600 11px system-ui;padding:1px 4px;border-radius:4px}}
figcaption{{margin-top:6px;font-size:11px}}
</style></head><body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>{DEFS}</defs></svg>
<div class="wrap">
<header><div class="eb">Seeds of Renaissance · YouTube · podcast episode thumbnails</div>
<h1>Speaker in the seed spiral</h1>
<p>Six podcast covers on sunlight (#fbefc4): the speaker, the woodcut sunflower spiral, the logo on its white disc, the podcast name kept small, the tagline on one line and room for a one-to-two-line episode title. They run from structured to poetic. Episode title and portrait are placeholders.</p>
<ul class="toc">{"".join(f'<li><a href="#{v[0]}">{v[1]}</a> · {v[2].lower()}</li>' for v in VERSIONS)}</ul></header>
{"".join(cards)}
</div></body></html>'''
(HERE / "podcast.html").write_text(page)
print(len(page))
