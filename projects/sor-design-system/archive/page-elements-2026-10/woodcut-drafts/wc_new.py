"""Draft woodcuts, round 1: a drift of leaves (after plate 9) and a sprout growing out of the soil
(after plate 10). Same technique as wc.py: black fills, white carved cuts via a mask, a rough edge.
Writes SVGs and review.html next to this file."""
import math, pathlib, random

random.seed(7)
R = random.uniform
HERE = pathlib.Path(__file__).parent
EL = {}


def el(name, w, h, fills=(), cuts=(), inks=(), title=''):
    EL[name] = dict(w=w, h=h, fills=list(fills), cuts=list(cuts), inks=list(inks), title=title)


def poly(pts):
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + ' Z'


def circ(cx, cy, r):
    return f'M{cx-r:.1f} {cy:.1f} a{r:.1f} {r:.1f} 0 1 0 {2*r:.1f} 0 a{r:.1f} {r:.1f} 0 1 0 {-2*r:.1f} 0 Z'


def leaf(x, y, ang, L, W, veins=6, stem=0):
    """Plate 9's leaf, at base (x, y) pointing along `ang`. W < L*.3 reads as a leaf turning in the air."""
    a = math.radians(ang); ux, uy = math.cos(a), math.sin(a); px, py = -uy, ux
    P = lambda u, v: (x + ux * u + px * v, y + uy * u + py * v)
    tip = P(L, 0)
    fills, cuts, inks = [], [], []
    for s in (1, -1):
        c1, c2 = P(L * .12, s * W * 1.05), P(L * .72, s * W * .7)
        fills.append(f'M{x:.1f} {y:.1f} C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {tip[0]:.1f} {tip[1]:.1f} L{x:.1f} {y:.1f} Z')
    m0, m1 = P(L * .06, 0), P(L * .92, 0)
    cuts.append((f'M{m0[0]:.1f} {m0[1]:.1f} L{m1[0]:.1f} {m1[1]:.1f}', max(1.0, L / 75)))
    for i in range(veins):
        t = .14 + i * (.7 / veins)
        half = W * (.85 - abs(t - .4) * .9)
        for s in (1, -1):
            b = P(L * (t + (.03 if s < 0 else 0)), 0)
            q = P(L * (t + .05), s * half * .5)
            e = P(L * (t + .14), s * half * .92)
            cuts.append((f'M{b[0]:.1f} {b[1]:.1f} Q{q[0]:.1f} {q[1]:.1f} {e[0]:.1f} {e[1]:.1f}', max(.7, L / 120) * R(.85, 1.2)))
    if stem:
        s0 = P(-stem, R(-2, 2))
        inks.append((f'M{x:.1f} {y:.1f} L{s0[0]:.1f} {s0[1]:.1f}', max(1.2, L / 55)))
    return fills, cuts, inks


def add(acc, part):
    for a, b in zip(acc, part): a += b


# ---------- 9a: three leaves rising, like the swallow flock ----------
acc = ([], [], [])
for (x, y, ang, L, W) in [(40, 168, -62, 96, 30), (160, 92, -40, 66, 13), (246, 46, -18, 46, 11)]:
    add(acc, leaf(x, y, ang, L, W, stem=L * .14))
el('leaves-rising', 300, 180, *acc, title='Woodcut: three leaves rising on the air')

# ---------- 9b: five leaves tumbling down, some turned edge-on ----------
acc = ([], [], [])
for (x, y, ang, L, W) in [(24, 40, -20, 70, 22), (118, 54, 120, 54, 7), (170, 108, 20, 62, 20),
                          (60, 150, -70, 42, 12), (238, 168, 200, 50, 10)]:
    add(acc, leaf(x, y, ang, L, W, veins=5, stem=L * .14))
el('leaves-falling', 300, 210, *acc, title='Woodcut: leaves tumbling on the wind')


# ---------- soil ----------
def soil(x0, x1, top, bottom, n, k=1.3):
    # a soft mound, not a block: the top rises gently, the ends taper into the ground line
    pts = []
    for i in range(n + 1):
        t = i / n; e = min(1, k * math.sin(math.pi * t) ** .6)
        pts.append((x0 + (x1 - x0) * t, bottom - (bottom - top) * e + R(-2, 2)))
    for i in range(n, -1, -1):
        t = i / n
        pts.append((x0 + (x1 - x0) * t, bottom + R(-2.5, 2.5) * math.sin(math.pi * t)))
    cuts = []
    for k in range(int((bottom - top) / 9)):        # strata: short carved dashes, sparser lower down
        y = top + 10 + k * 9
        for _ in range(int((x1 - x0) / 60)):
            sx = R(x0 + 6, x1 - 40)
            cuts.append((f'M{sx:.1f} {y + R(-2, 2):.1f} l{R(10, 30):.1f} {R(-1.5, 1.5):.1f}', R(.8, 1.4)))
    for _ in range(int((x1 - x0) / 25)):            # pebbles
        cuts.append((circ(R(x0 + 8, x1 - 8), R(top + 12, bottom - 6), R(1.5, 3.5)).replace(' Z', ''), 1.1))
    return poly(pts), cuts


def seed_cut(x, y, r=7):
    return (f'M{x - r:.1f} {y:.1f} Q{x:.1f} {y - r * 1.2:.1f} {x + r:.1f} {y:.1f} Q{x:.1f} {y + r * 1.2:.1f} {x - r:.1f} {y:.1f} Z', 1.6)


def roots(x, y, depth, spread, w=2.0):
    out = [(f'M{x:.1f} {y:.1f} Q{x + R(-6, 6):.1f} {y + depth * .5:.1f} {x + R(-4, 4):.1f} {y + depth:.1f}', w)]
    for k in range(int(depth / 12)):
        t = (k + 1) / (depth / 12 + 1); yy = y + depth * t; s = 1 if k % 2 else -1
        out.append((f'M{x:.1f} {yy:.1f} q{s * spread * .5:.1f} {R(2, 6):.1f} {s * spread * (1 - t * .5):.1f} {R(6, 14):.1f}', w * .6))
    return out


# ---------- 10a: one sprout breaking out of the soil ----------
fills, cuts, inks = [], [], []
d, c = soil(6, 214, 178, 262, 12); fills.append(d); cuts += c
cuts.append(seed_cut(112, 204, 9))
cuts += roots(112, 212, 44, 26, 2.2)
cuts.append(('M112 196 Q110 188 111 178', 2.6))                # the shoot, carved where it is still underground
cuts += [('M100 179 l-8 -1', 1.4), ('M124 179 l9 -2', 1.4)]       # the soil cracking open
inks.append(('M111 180 C108 150 104 126 112 96', 5))
add((fills, cuts, inks), leaf(112, 98, -158, 62, 19, veins=5))
add((fills, cuts, inks), leaf(112, 98, -24, 66, 20, veins=5))
add((fills, cuts, inks), leaf(112, 96, -92, 26, 8, veins=2))
el('sprout-from-soil', 220, 264, fills, cuts, inks, title='Woodcut: a sprout breaking out of the soil')

# ---------- 10b: the same sprout growing, in five stages ----------
fills, cuts, inks = [], [], []
d, c = soil(4, 476, 150, 214, 30, k=1.8); fills.append(d); cuts += c
xs = [72, 156, 240, 324, 408]
for i, x in enumerate(xs):
    cuts.append(seed_cut(x, 170, 7))
    if i >= 1: cuts += roots(x, 176, 12 + i * 7, 8 + i * 4, 1.6)
if True:   # 2: a hooked shoot just through the surface
    x = xs[1]; cuts.append((f'M{x} 164 L{x} 151', 2.2))
    inks.append((f'M{x} 152 Q{x - 1} 140 {x + 3} 134 Q{x + 9} 128 {x + 8} 140', 3.4))
    cuts += [(f'M{x - 10} 151 l-6 -1', 1.2), (f'M{x + 10} 151 l6 -1', 1.2)]
x = xs[2]; cuts.append((f'M{x} 164 L{x} 151', 2.4))            # 3: straight, leaves still closed
inks.append((f'M{x} 152 C{x - 2} 134 {x - 1} 118 {x + 1} 106', 3.8))
add((fills, cuts, inks), leaf(x + 1, 108, -101, 22, 6, veins=2))
add((fills, cuts, inks), leaf(x + 1, 108, -79, 22, 6, veins=2))
x = xs[3]; cuts.append((f'M{x} 164 L{x} 151', 2.6))            # 4: leaves open
inks.append((f'M{x} 152 C{x - 3} 128 {x - 4} 104 {x} 86', 4.4))
add((fills, cuts, inks), leaf(x, 88, -160, 36, 12, veins=3))
add((fills, cuts, inks), leaf(x, 88, -22, 38, 12, veins=3))
x = xs[4]; cuts.append((f'M{x} 164 L{x} 151', 2.8))            # 5: first true leaves
inks.append((f'M{x} 152 C{x - 4} 120 {x - 6} 80 {x + 1} 40', 5))
add((fills, cuts, inks), leaf(x - 3, 112, -165, 34, 11, veins=3))
add((fills, cuts, inks), leaf(x - 3, 112, -18, 36, 11, veins=3))
add((fills, cuts, inks), leaf(x - 1, 62, -140, 46, 15, veins=4))
add((fills, cuts, inks), leaf(x, 52, -40, 50, 16, veins=4))
add((fills, cuts, inks), leaf(x + 1, 42, -88, 16, 5, veins=1))
el('sprout-growing', 480, 216, fills, cuts, inks, title='Woodcut: a sprout growing out of the soil, in five stages')


def svg(name, e, scale=3, cls=None):
    w, h = e['w'], e['h']
    m = (''.join(f'<path d="{d}" fill="#fff"/>' for d in e['fills'])
         + ''.join(f'<path d="{d}" stroke="#000" stroke-width="{wd:.2f}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>' for d, wd in e['cuts']))
    inks = ''.join(f'<path d="{d}" stroke="currentColor" stroke-width="{wd:.2f}" stroke-linecap="round" fill="none"/>' for d, wd in e['inks'])
    fills = ''.join(f'<path d="{d}"/>' for d in e['fills'])
    head = f'class="{cls}"' if cls else f'width="{w * scale}" height="{h * scale}" style="color:#1b1916"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" {head}>'
            f'<title>{e["title"]}</title><defs><filter id="r-{name}" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="1" seed="5" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="2"/></filter>'
            f'<mask id="m-{name}" maskUnits="userSpaceOnUse" x="-10" y="-10" width="{w + 20}" height="{h + 20}">{m}</mask></defs>'
            f'<g filter="url(#r-{name})">{inks}<g fill="currentColor" mask="url(#m-{name})">{fills}</g></g></svg>')


for n, e in EL.items():
    (HERE / f'{n}.svg').write_text(svg(n, e))

# review page: each draft on paper, sunlight and night, next to the plate it answers
ref = HERE.parent
def old(name):
    s = (ref / f'{name}.svg').read_text()
    return s.replace(f'r-{name}', f'o-{name}').replace(f'm-{name}', f'om-{name}').replace('style="color:#1b1916"', '', 1).replace(' width=', ' data-w=', 1).replace(' height=', ' data-h=', 1).replace('<svg ', '<svg class="wc" ', 1)

PLATES = [
    ('9a', 'leaves-rising', 'Three leaves rising on the air, built like the swallow flock: big, then smaller as they rise away.', 'leaf-single'),
    ('9b', 'leaves-falling', 'Leaves tumbling down. The narrow ones are turned edge-on, so they read as moving.', 'leaf-single'),
    ('10a', 'sprout-from-soil', 'One sprout breaking out of dark soil: the seed husk, roots and buried shoot are carved into the ground.', 'leaf-sprig'),
    ('10b', 'sprout-growing', 'The same sprout growing, left to right: seed, the hooked shoot breaking through, closed leaves, open leaves, first true leaves.', 'leaf-sprig'),
]
cards = ''
for no, name, note, was in PLATES:
    art = svg(name, EL[name], cls='wc')
    cards += f'''<section class="plate"><div class="head"><span class="no">Plate {no}</span><h2>{EL[name]["title"].replace("Woodcut: ", "").capitalize()}</h2><p>{note}</p></div>
<div class="grounds"><div class="g paper">{art}</div><div class="g sun">{art.replace(f'r-{name}', f's-{name}').replace(f'm-{name}', f'sm-{name}')}</div><div class="g night">{art.replace(f'r-{name}', f'n-{name}').replace(f'm-{name}', f'nm-{name}')}</div></div>
<div class="was"><span>Replaces</span>{old(was)}<code>{was}</code></div></section>'''

(HERE / 'review.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>New Woodcuts</title><style>
:root{{--paper:#fbfaf6;--ink:#1b1916;--muted:#5d584f;--sun:#fbefc4;--night:#171613;--chalk:#ece7dc}}
body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.5 Georgia,serif;padding:32px 16px 64px}}
main{{max-width:1100px;margin:0 auto}} h1{{font-weight:400;font-size:34px;margin:0 0 4px}} .lede{{color:var(--muted);margin:0 0 32px}}
.plate{{border-top:1px solid #d9d4c8;padding:28px 0}} .no{{font:600 12px/1 system-ui;letter-spacing:.12em;text-transform:uppercase;color:#e5201c}}
h2{{font-weight:400;font-size:22px;margin:6px 0 4px}} .head p{{margin:0 0 16px;color:var(--muted);max-width:60ch}}
.grounds{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}} .g{{padding:22px;display:grid;place-items:center;min-height:200px}}
.g .wc{{width:100%;max-height:300px}} .paper{{background:#fff;border:1px solid #e6e1d6;color:var(--ink)}} .sun{{background:var(--sun);color:var(--ink)}} .night{{background:var(--night);color:var(--chalk)}}
.was{{display:flex;align-items:center;gap:12px;margin-top:12px;color:var(--muted);font:13px system-ui}} .was .wc{{width:56px;height:56px}}
@media (max-width:700px){{.grounds{{grid-template-columns:1fr}}}}
</style></head><body><main><h1>New woodcuts, round 1</h1>
<p class="lede">Drafts only, not in the library yet. Each one on paper, sunlight and night.</p>{cards}</main></body></html>''')
print('ok', list(EL))
