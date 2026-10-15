"""Draft woodcuts, round 2: colour. After the woodcut mood board (moodboard/woodcuts/): flowers,
one flat spot colour or two, a second block printed a little off register, grain in the ink.
Every piece is built from layers; each layer is its own block with its own cuts and its own ink
(currentColor, var(--c2), var(--c3)), so the review page can try colourways without redrawing.
Writes colour-*.svg and colour.html next to this file."""
import math, pathlib, random
from wc_new import leaf, soil, roots, seed_cut, circ, poly

random.seed(11)
R = random.uniform
HERE = pathlib.Path(__file__).parent
EL = {}


def layer(col='currentColor', dx=0, dy=0):
    return dict(col=col, dx=dx, dy=dy, fills=[], cuts=[], inks=[], holes=[])


def add(L, part):
    f, c, i = part
    L['fills'] += f; L['cuts'] += c; L['inks'] += i


def scallop(cx, cy, r0, r1, n, rot=0):
    pts = []
    for k in range(2 * n):
        a = math.radians(rot) + math.pi * k / n
        r = (r1 if k % 2 == 0 else r0) * R(.96, 1.04)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d = f'M{(pts[-1][0] + pts[0][0]) / 2:.1f} {(pts[-1][1] + pts[0][1]) / 2:.1f}'
    for k, p in enumerate(pts):
        q = pts[(k + 1) % len(pts)]
        d += f' Q{p[0]:.1f} {p[1]:.1f} {(p[0] + q[0]) / 2:.1f} {(p[1] + q[1]) / 2:.1f}'
    return d + ' Z'


def blade(x, y, ang, L, W, bend=.25):
    """A long leaf with one white vein, as in the mustard flower (mood board 06)."""
    a = math.radians(ang); ux, uy = math.cos(a), math.sin(a); px, py = -uy, ux
    P = lambda u, v: (x + ux * u + px * v, y + uy * u + py * v)
    tip = P(L, W * bend * 2)
    c1, c2, c3, c4 = P(L * .2, W * 1.1), P(L * .75, W * (1 + bend)), P(L * .7, -W * (.5 - bend)), P(L * .2, -W * .9)
    d = (f'M{x:.1f} {y:.1f} C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {tip[0]:.1f} {tip[1]:.1f} '
         f'C{c3[0]:.1f} {c3[1]:.1f} {c4[0]:.1f} {c4[1]:.1f} {x:.1f} {y:.1f} Z')
    v0, v1, v2 = P(L * .12, W * .1), P(L * .55, W * (.35 + bend)), P(L * .9, W * bend * 1.8)
    return [d], [(f'M{v0[0]:.1f} {v0[1]:.1f} Q{v1[0]:.1f} {v1[1]:.1f} {v2[0]:.1f} {v2[1]:.1f}', max(1.2, W / 9))], []


# ---------- flowers: two blooms on one stem, solid with cut-out petals (mood board 06) ----------
K = layer()
K['fills'].append('M104 296 C106 250 108 200 112 150 L118 150 C116 200 114 250 116 296 Z')        # stem
K['fills'].append('M112 196 C122 170 134 140 148 104 L153 106 C140 142 128 172 117 200 Z')        # branch
K['fills'].append(scallop(84, 120, 40, 48, 14, rot=6))                                          # open bloom
for k in range(14):
    a = math.radians(6 + k * 360 / 14 + 360 / 28)
    K['cuts'].append((f'M{84 + math.cos(a) * 22:.1f} {120 + math.sin(a) * 22:.1f} L{84 + math.cos(a) * 39:.1f} {120 + math.sin(a) * 39:.1f}', 3.8))
for k in range(9):
    a = math.radians(k * 40 + 10)
    K['cuts'].append((circ(84 + math.cos(a) * 13, 120 + math.sin(a) * 13, 2.2).replace(' Z', ''), 2.4))
K['cuts'].append((circ(84, 120, 19).replace(' Z', ''), 1.6))
fan = 'M150 100 C128 92 116 70 120 50 C134 34 168 34 182 50 C186 70 172 92 150 100 Z'               # bloom seen side-on
K['fills'] += [fan, 'M140 98 Q150 116 160 98 Z']
for k in range(9):
    a = math.radians(-160 + k * 17.5)
    K['cuts'].append((f'M{150 + math.cos(a) * 14:.1f} {92 + math.sin(a) * 14:.1f} L{150 + math.cos(a) * 46:.1f} {92 + math.sin(a) * 46:.1f}', 4.6))
K['cuts'].append(('M142 101 Q150 106 158 101', 1.6))
add(K, blade(110, 286, -118, 150, 30, .2))
add(K, blade(114, 284, -64, 156, 30, -.2))
add(K, blade(116, 230, -30, 60, 12, .1))
EL['colour-flower'] = dict(w=230, h=300, layers=[K], title='Woodcut: two flowers on one stem, solid with cut-out petals')

# ---------- tulips: two blocks, flowers in one colour, leaves and frame in another (mood board 07) ----------
G, Rd = layer('var(--c3)'), layer('var(--c2)')
G['fills'] += [poly([(4, 4), (196, 4), (196, 11), (4, 11)]), poly([(4, 309), (196, 309), (196, 316), (4, 316)]),   # hand-cut frame
               poly([(4, 4), (11, 4), (11, 316), (4, 316)]), poly([(189, 4), (196, 4), (196, 316), (189, 316)])]
for _ in range(14):
    x, y = R(6, 194), R(6, 314)
    G['cuts'].append((f'M{x:.1f} {y:.1f} l{R(-2, 2):.1f} {R(-2, 2):.1f}', R(1, 2)))
for (x0, y0, x1, y1) in [(86, 300, 74, 110), (108, 300, 132, 130), (98, 300, 96, 200)]:
    G['inks'].append((f'M{x0} {y0} Q{(x0 + x1) / 2 + 4} {(y0 + y1) / 2} {x1} {y1}', 5))
add(G, blade(92, 302, -112, 150, 26, .15))
add(G, blade(102, 302, -70, 140, 22, -.15))


def tulip(L, x, y, s, lean=0):
    P = lambda u, v: (x + (u + lean * (v - 0) * -.0) * s, y + v * s)
    pts = dict(b=P(0, 0), l=P(-24, -34), lt=P(-18, -66), m=P(0, -58), mt=P(2, -74), r=P(24, -36), rt=P(18, -66))
    f = lambda k: f'{pts[k][0]:.1f} {pts[k][1]:.1f}'
    L['fills'].append(f'M{f("b")} C{P(-22, -2)[0]:.1f} {P(-22, -2)[1]:.1f} {f("l")} {f("lt")} '
                      f'Q{P(-8, -56)[0]:.1f} {P(-8, -56)[1]:.1f} {f("mt")} Q{P(8, -56)[0]:.1f} {P(8, -56)[1]:.1f} {f("rt")} '
                      f'C{f("r")} {P(22, -2)[0]:.1f} {P(22, -2)[1]:.1f} {f("b")} Z')
    for k in range(9):                                                   # petal folds, carved
        u = -16 + k * 4
        top = P(u * .9, -60 + abs(u) * .2)
        bot = P(u * .35, -10 - abs(u) * .4)
        mid = P(u * .9 + (2 if u > 0 else -2), -34)
        L['cuts'].append((f'M{bot[0]:.1f} {bot[1]:.1f} Q{mid[0]:.1f} {mid[1]:.1f} {top[0]:.1f} {top[1]:.1f}', R(.9, 1.5) * s))
    a, b = P(-2, -2), P(-6, -48)
    L['cuts'].append((f'M{a[0]:.1f} {a[1]:.1f} Q{P(-12, -24)[0]:.1f} {P(-12, -24)[1]:.1f} {b[0]:.1f} {b[1]:.1f}', 2 * s))


tulip(Rd, 74, 112, 1.05); tulip(Rd, 132, 134, 1.0); tulip(Rd, 96, 206, 1.1)
EL['colour-tulips'] = dict(w=200, h=320, layers=[G, Rd], title='Woodcut: three tulips in a hand-cut frame, two colours')

# ---------- pomegranate: a black key over a flat colour, off register (mood board 01) ----------
U, K, K2 = layer('var(--c2)', 5, 4), layer(), layer()
body = scallop(110, 120, 78, 80, 18)
crown = 'M92 52 L88 30 L100 42 L110 24 L120 42 L132 30 L128 52 Z'
U['fills'] += [body, crown]
K['fills'].append(circ(110, 120, 80)); K['holes'].append(circ(110, 120, 72))      # the key's outline ring
K2['fills'].append(crown)
for k in range(3):
    K2['cuts'].append((f'M{100 + k * 10} 50 L{98 + k * 12} 38', 1.4))
for _ in range(110):                                                     # seed cells, black on the colour
    a, r = R(0, 2 * math.pi), 62 * math.sqrt(R(0, 1))
    K2['fills'].append(scallop(110 + r * math.cos(a), 122 + r * math.sin(a), 2.6, 4.2, 3, R(0, 90)))
for (x, y, ang) in [(176, 70, -40), (40, 176, 150), (190, 168, 30)]:
    add(K2, leaf(x, y, ang, 46, 15, veins=4, stem=6))
for k in range(14):                                                      # stray gouge marks round the edge
    a = R(0, 2 * math.pi); r = R(86, 96)
    K2['inks'].append((f'M{110 + r * math.cos(a):.1f} {120 + r * math.sin(a):.1f} l{math.cos(a + 1.6) * R(4, 9):.1f} {math.sin(a + 1.6) * R(4, 9):.1f}', 1.4))
EL['colour-pomegranate'] = dict(w=224, h=224, layers=[U, K, K2], title='Woodcut: a pomegranate, black key over a flat colour')

# ---------- sprout: soil in one colour, the sprout in another ----------
S, P2 = layer(), layer('var(--c2)')
d, c = soil(6, 214, 178, 262, 12); S['fills'].append(d); S['cuts'] += c
S['cuts'].append(seed_cut(112, 204, 9)); S['cuts'] += roots(112, 212, 44, 26, 2.2)
S['cuts'].append(('M112 196 Q110 188 111 178', 2.6))
P2['inks'].append(('M111 182 C108 150 104 126 112 96', 5))
add(P2, leaf(112, 98, -158, 62, 19, veins=5))
add(P2, leaf(112, 98, -24, 66, 20, veins=5))
add(P2, leaf(112, 96, -92, 26, 8, veins=2))
EL['colour-sprout'] = dict(w=220, h=264, layers=[S, P2], title='Woodcut: a sprout out of the soil, two colours')

# ---------- leaves rising, each in its own colour ----------
ls = [layer('var(--c2)'), layer('var(--c3)'), layer()]
for L, (x, y, ang, Ln, W) in zip(ls, [(40, 168, -62, 96, 30), (160, 92, -40, 66, 13), (246, 46, -18, 46, 11)]):
    add(L, leaf(x, y, ang, Ln, W, stem=Ln * .14))
EL['colour-leaves'] = dict(w=300, h=180, layers=ls, title='Woodcut: three leaves rising, three colours')


def svg(name, e, cls=None, style=''):
    w, h = e['w'], e['h']
    defs = (f'<filter id="r-{name}" x="-5%" y="-5%" width="110%" height="110%">'
            f'<feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="1" seed="5" result="n"/>'
            f'<feDisplacementMap in="SourceGraphic" in2="n" scale="2" result="d"/>'
            f'<feTurbulence type="fractalNoise" baseFrequency="1.3" numOctaves="2" seed="9" result="g"/>'
            f'<feColorMatrix in="g" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  9 0 0 0 -6.9" result="dots"/>'
            f'<feComposite in="d" in2="dots" operator="out"/></filter>')
    body = ''
    for i, L in enumerate(e['layers']):
        m = (''.join(f'<path d="{d}" fill="#fff"/>' for d in L['fills'])
             + ''.join(f'<path d="{d}" fill="#000"/>' for d in L['holes'])
             + ''.join(f'<path d="{d}" stroke="#000" stroke-width="{wd:.2f}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>' for d, wd in L['cuts']))
        defs += f'<mask id="m-{name}-{i}" maskUnits="userSpaceOnUse" x="-10" y="-10" width="{w + 20}" height="{h + 20}">{m}</mask>'
        inks = ''.join(f'<path d="{d}" stroke="{L["col"]}" stroke-width="{wd:.2f}" stroke-linecap="round" fill="none"/>' for d, wd in L['inks'])
        fills = ''.join(f'<path d="{d}"/>' for d in L['fills'])
        mv = f' transform="translate({L["dx"]} {L["dy"]})"' if L['dx'] or L['dy'] else ''
        body += f'<g{mv}>{inks}<g fill="{L["col"]}" mask="url(#m-{name}-{i})">{fills}</g></g>'
    head = f'class="{cls}"' if cls else f'width="{w * 3}" height="{h * 3}"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" {head} style="color:#1b1916;--c2:#e5201c;--c3:#6d8b68;{style}">'
            f'<title>{e["title"]}</title><defs>{defs}</defs><g filter="url(#r-{name})">{body}</g></svg>')


for n, e in EL.items():
    (HERE / f'{n}.svg').write_text(svg(n, e))

# ---------- review page ----------
INK = dict(ink='#1b1916', red='#e5201c', brick='#c4432f', oxblood='#7b2129', mustard='#d9831f',
           ochre='#e3ad2b', blue='#25395e', cornflower='#4a6fa5', sage='#6d8b68', chalk='#ece7dc')
GROUND = dict(white='#ffffff', paper='#fbfaf6', sun='#fbefc4', night='#171613')
# (piece, [(label, key, c2, c3, ground)])
WAYS = [
    ('colour-flower', 'Two flowers, one colour', 'Solid shapes with the petals and seeds cut out, like the mustard flower (06). No black at all.',
     [('Mustard on white', 'mustard', 0, 0, 'white'), ('Mustard on paper', 'mustard', 0, 0, 'paper'), ('Deep blue on sunlight', 'blue', 0, 0, 'sun'),
      ('Red on paper', 'red', 0, 0, 'paper'), ('Ochre yellow on night', 'ochre', 0, 0, 'night'), ('Brick on sunlight', 'brick', 0, 0, 'sun')]),
    ('colour-tulips', 'Tulips, two blocks', 'Flowers in one colour with carved folds; leaves, stems and a hand-cut frame in a second (07).',
     [('Brick and sage', 0, 'brick', 'sage', 'paper'), ('Red and deep blue', 0, 'red', 'blue', 'white'), ('Mustard and deep blue', 0, 'mustard', 'blue', 'paper'),
      ('Red and sage on sunlight', 0, 'red', 'sage', 'sun'), ('Ochre and cornflower on night', 0, 'ochre', 'cornflower', 'night'), ('Oxblood and mustard', 0, 'oxblood', 'mustard', 'white')]),
    ('colour-pomegranate', 'Pomegranate, key and colour', 'A black key printed over a flat colour that sits a little off register and peeks out (01). The seeds are the round cells.',
     [('Ink over red', 'ink', 'red', 0, 'paper'), ('Ink over mustard', 'ink', 'mustard', 0, 'paper'), ('Ink over ochre', 'ink', 'ochre', 0, 'white'),
      ('Deep blue over red', 'blue', 'red', 0, 'paper'), ('Ink over brick on sunlight', 'ink', 'brick', 0, 'sun'), ('Chalk over red on night', 'chalk', 'red', 0, 'night')]),
    ('colour-sprout', 'Sprout, two colours', 'Round 1’s sprout, with the soil in one ink and the living part in another.',
     [('Ink soil, sage sprout', 'ink', 'sage', 0, 'paper'), ('Ink soil, mustard sprout', 'ink', 'mustard', 0, 'white'), ('Ink soil, red sprout', 'ink', 'red', 0, 'paper'),
      ('Deep blue soil, ochre sprout', 'blue', 'ochre', 0, 'paper'), ('Ink soil, sage sprout on sunlight', 'ink', 'sage', 0, 'sun'), ('Chalk soil, ochre sprout on night', 'chalk', 'ochre', 0, 'night')]),
    ('colour-leaves', 'Leaves rising, mixed colours', 'Round 1’s rising leaves, each leaf in its own ink.',
     [('Mustard, red, ink', 'ink', 'mustard', 'red', 'paper'), ('Mustard, sage, deep blue', 'blue', 'mustard', 'sage', 'white'), ('Red, mustard, ink on sunlight', 'ink', 'red', 'mustard', 'sun'),
      ('Ochre, red, chalk on night', 'chalk', 'ochre', 'red', 'night'), ('All mustard', 'mustard', 'mustard', 'mustard', 'paper'), ('All deep blue', 'blue', 'blue', 'blue', 'sun')]),
]
secs = ''
for name, title, note, ways in WAYS:
    tiles = ''
    for j, (label, k, c2, c3, g) in enumerate(ways):
        st = f'color:{INK[k or "ink"]};--c2:{INK[c2] if c2 else INK[k or "ink"]};--c3:{INK[c3] if c3 else INK[k or "ink"]}'
        art = svg(f'{name}-{j}', EL[name], cls='wc', style=st)
        dark = ' dark' if g == 'night' else ''
        tiles += f'<figure class="t{dark}" style="background:{GROUND[g]}">{art}<figcaption>{label}</figcaption></figure>'
    secs += f'<section><h2>{title}</h2><p>{note}</p><div class="grid">{tiles}</div></section>'
USE = f"""<section><h2>In use: faint behind text, or as punctuation</h2><p>The same woodcuts on a page. Left: very pale, large and cropped, as a quiet background behind plain text. Right: small and in full colour, one per section.</p>
<div class="use">
<div class="mock" style="background:#fff"><div class="bg" style="right:-60px;top:-30px;width:300px">{svg('bg-1', EL['colour-flower'], cls='wc', style='color:#dde5ef')}</div>
<div class="txt"><div class="eb">Pale blue on white</div><h3>Seeds of a second renaissance</h3><p>We gather people who want to live, think and build differently, and help them grow the practices, places and stories for what comes next.</p><a>Read the manifesto</a></div></div>
<div class="mock" style="background:#fbfaf6"><div class="txt c"><span class="punct">{svg('pu-1', EL['colour-sprout'], cls='wc', style='color:#1b1916;--c2:#6d8b68')}</span><div class="eb">Punctuation</div><h3>Courses</h3><p>Six-week courses in the practices of renewal, taught in small groups.</p><a>See the courses</a></div></div>
<div class="mock" style="background:#fbefc4"><div class="bg" style="left:-50px;bottom:-60px;width:260px;transform:rotate(-8deg)">{svg('bg-2', EL['colour-tulips'], cls='wc', style='color:#f3dd96;--c2:#f3dd96;--c3:#f3dd96')}</div><div class="bg" style="right:-30px;top:-40px;width:220px">{svg('bg-3', EL['colour-flower'], cls='wc', style='color:#f3dd96')}</div>
<div class="txt"><div class="eb">Pale mustard on sunlight</div><h3>Gatherings</h3><p>Weekends in the hills to slow down, meet others and work on what matters.</p><a>Find a gathering</a></div></div>
<div class="mock" style="background:#fff"><div class="txt"><div class="eb">Punctuation, in a row</div><h3>White papers</h3><p>Long-form thinking on wisdom, culture and the institutions we need.</p><div class="row">{svg('pu-2', EL['colour-leaves'], cls='wc', style='color:#1b1916;--c2:#d9831f;--c3:#e5201c')}</div><a>Read the papers</a></div></div>
</div></section>"""
sw = ''.join(f'<span class="sw"><i style="background:{v}"></i>{k}<br><code>{v}</code></span>' for k, v in INK.items() if k != 'chalk')
(HERE / 'colour.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Woodcuts in Colour</title><style>
body{{margin:0;background:#fbfaf6;color:#1b1916;font:16px/1.5 Georgia,serif;padding:32px 16px 64px}}
main{{max-width:1100px;margin:0 auto}} h1{{font-weight:400;font-size:34px;margin:0 0 4px}} .lede{{color:#5d584f;margin:0 0 20px;max-width:70ch}}
.inks{{display:flex;flex-wrap:wrap;gap:14px;margin:0 0 24px;font:12px/1.3 system-ui;color:#5d584f}} .sw i{{display:block;width:44px;height:44px;border-radius:50%;margin-bottom:4px}}
section{{border-top:1px solid #e0dacf;padding:26px 0}} h2{{font-weight:400;font-size:22px;margin:0 0 4px}} section>p{{margin:0 0 16px;color:#5d584f;max-width:65ch}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}} .t{{margin:0;padding:18px 18px 10px;border:1px solid #ebe6db;display:grid;gap:8px}}
.t .wc{{width:100%;height:260px}} figcaption{{font:12px system-ui;color:#5d584f}} .dark figcaption{{color:#a49e93}}
.use{{display:grid;grid-template-columns:1fr 1fr;gap:12px}} .mock{{position:relative;overflow:hidden;min-height:300px;border:1px solid #ebe6db;display:flex;align-items:center}}
.mock .bg{{position:absolute;pointer-events:none}} .mock .bg .wc{{width:100%;height:auto}} .txt{{position:relative;padding:32px;max-width:340px}} .txt.c{{text-align:center;margin:0 auto}}
.eb{{font:600 11px system-ui;letter-spacing:.12em;text-transform:uppercase;color:#5d584f}} h3{{font:400 28px/1.15 Georgia,serif;margin:8px 0 10px}} .txt p{{margin:0 0 14px}} .txt a{{font:600 14px system-ui;border-bottom:1.5px solid}}
.punct .wc{{width:84px;height:100px}} .row .wc{{width:180px;height:100px;margin:-6px 0 6px}}
@media (max-width:760px){{.use{{grid-template-columns:1fr}} .grid{{grid-template-columns:1fr 1fr}} .t .wc{{height:200px}}}}
</style></head><body><main><h1>Woodcuts in colour, round 2</h1>
<p class="lede">Drafts after the woodcut mood board: flowers, flat spot colour, a second block a little off register, and grain in the ink. The inks being tried:</p>
<div class="inks">{sw}</div>{USE}{secs}</main></body></html>''')
print('ok', list(EL))
