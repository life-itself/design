import random,math,os,sys,json
random.seed(31)
R=random.uniform
OUT=sys.argv[1]
EL={}
def el(name,w,h,fills=(),cuts=(),inks=(),title='',refills=()):
    EL[name]=dict(w=w,h=h,fills=list(fills),cuts=list(cuts),inks=list(inks),title=title,refills=list(refills))
def poly(pts): return 'M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)+' Z'
def circ(cx,cy,r): return f'M{cx-r:.1f} {cy:.1f} a{r:.1f} {r:.1f} 0 1 0 {2*r:.1f} 0 a{r:.1f} {r:.1f} 0 1 0 {-2*r:.1f} 0 Z'
def jag(x0,y0,x1,y1,n,amp):
    return [(x0+(x1-x0)*i/n+R(-1,1), y0+(y1-y0)*i/n+R(-amp,amp)) for i in range(n+1)]

# ---------- MOUNTAINS ----------
# peak
left=[(10,180),(40,140),(58,120),(72,96),(86,70),(98,44),(108,30)]
right=[(108,30),(118,44),(126,52),(138,70),(150,92),(168,112),(186,140),(210,180)]
body=poly(left+right)
cuts=[]
# snow cap edge: jagged line, and snow hatch (dense cuts on left/top)
snow=[(80,80),(88,74),(94,82),(100,70),(106,78),(112,64),(118,74),(126,66),(134,78)]
cuts.append(('M'+' L'.join(f'{x} {y}' for x,y in snow),2.2))
for i in range(22):
    x=86+i*2.2; cuts.append((f'M{x:.1f} {78-i*.4+R(-2,2):.1f} L{108+(x-108)*.25:.1f} {34+R(0,4):.1f}',R(.8,1.6)))
# shadow side: diagonal hatching on right flank (few cuts = dark)
for i in range(9):
    y=96+i*9; cuts.append((f'M{140+i*2:.1f} {y:.1f} l{R(14,24):.1f} {R(6,10):.1f}',R(.7,1.2)))
# lit side: long ridge cuts on left flank
for i in range(14):
    y=100+i*6; x=60-i*3.4
    cuts.append((f'M{x:.1f} {y:.1f} Q{x+20:.1f} {y-6:.1f} {x+36+R(0,10):.1f} {y-16+R(-3,3):.1f}',R(.9,1.7)))
el('mountain-peak',220,190,[body],cuts,title='Woodcut mountain: a single snow peak')

# range: three peaks, far ones carved lighter
fills=[];cuts=[]
peaks=[(70,60,90,0.9),(160,40,110,0.6),(240,72,80,0.3)]
for (px,py,half,dark) in [(160,40,110,.6),(70,64,90,.9),(250,76,80,.3)]:
    pts=[(px-half-60,200)]+jag(px-half-60,200,px,py,7,3)[1:]+jag(px,py,px+half+60,200,7,3)[1:]
    fills.append(poly(pts))
el('mountain-range-base',320,200,fills)
# build range as layered: back layer with many horizontal cuts (lighter), mid medium, front few
fills=[];cuts=[]
layers=[(170,30,130,26),(80,62,100,12),(260,78,90,6)]
for li,(px,py,half,ncut) in enumerate(layers):
    pts=[(px-half-50,200)]+jag(px-half-50,200,px,py,8,3)[1:]+jag(px,py,px+half+50,200,8,3)[1:]
    fills.append(poly(pts))
EL['mountain-range-base']=None
del EL['mountain-range-base']
# simpler approach: range drawn as one fill with internal contour cuts separating layers + horizontal mist cuts
outline=[(0,200)]+jag(0,200,80,62,6,3)[1:]+jag(80,62,120,110,4,3)[1:]+jag(120,110,170,30,7,3)[1:]+jag(170,30,215,100,6,3)[1:]+jag(215,100,262,78,4,3)[1:]+jag(262,78,320,200,7,3)[1:]+[(320,200)]
body=poly(outline)
cuts=[]
# contour of front ridges
cuts.append(('M80 66 Q70 120 40 200',2));cuts.append(('M170 34 Q160 110 120 200',2.2));cuts.append(('M262 82 Q250 140 230 200',1.8));cuts.append(('M120 112 Q126 150 150 200',1.4))
# mist bands (horizontal cuts), denser higher up
for i in range(18):
    y=70+i*7; x0=R(60,140); cuts.append((f'M{x0:.1f} {y:.1f} l{R(20,70):.1f} {R(-1,1):.1f}',R(.8,1.6)))
# snow on the tall peak
for i in range(12):
    cuts.append((f'M{170+R(-3,3):.1f} {34+R(0,4):.1f} L{150+i*3.6:.1f} {64+R(-4,4):.1f}',R(.8,1.4)))
el('mountain-range',320,200,[body],cuts,title='Woodcut mountains: a range with mist')

# mountain with moon/sun disc
body=poly([(0,200)]+jag(0,200,110,70,8,3)[1:]+jag(110,70,150,96,3,2)[1:]+jag(150,96,200,60,4,2)[1:]+jag(200,60,320,200,9,3)[1:]+[(320,200)])
cuts=[]
for i in range(16):
    y=96+i*6.5; cuts.append((f'M{R(10,60):.1f} {y:.1f} Q{140:.1f} {y-14:.1f} {R(250,300):.1f} {y+R(-4,4):.1f}',R(.7,1.5)))
disc=circ(262,34,22)
for r in range(5,22,4): cuts.append((circ(262,34,r).replace(' Z',''),1.2))
el('mountain-moon',320,200,[body,disc],cuts,title='Woodcut mountain with a rising moon')

# ---------- SWALLOWS ----------
# seen from above: wings spread, forked tail
body=('M100 38 C105 38 108 42 108 48 C120 46 138 36 158 24 C174 15 190 12 199 14 C192 30 176 48 152 60 '
      'C136 67 120 68 108 66 C108 72 108 80 110 92 L126 134 C114 124 106 108 102 96 L100 100 L98 96 '
      'C94 108 86 124 74 134 L90 92 C92 80 92 72 92 66 C80 68 64 67 48 60 C24 48 8 30 1 14 '
      'C10 12 26 15 42 24 C62 36 80 46 92 48 C92 42 95 38 100 38 Z')
cuts=[]
for side in (-1,1):
    for i in range(12):
        t=i/11; bx=100+side*(10+t*22); by=52+t*6
        tx=100+side*(92-t*30); ty=26+t*20
        cuts.append((f'M{bx:.1f} {by:.1f} Q{(bx+tx)/2:.1f} {(by+ty)/2-6:.1f} {tx:.1f} {ty:.1f}',R(.8,1.5)))
for i in range(5): cuts.append((f'M{97+i*1.5:.1f} {66+i*2:.1f} l0 {18+i*2:.1f}',1))

el('swallow-above',200,140,[body],cuts,title='Woodcut swallow seen from above, wings spread')

# perched on a branch
body=('M60 60 C60 48 70 40 82 42 C90 43 96 50 98 56 L104 57 L99 62 C104 76 106 90 104 102 '
      'L118 150 L108 152 L98 118 L92 152 L84 150 L88 112 C74 112 62 100 58 86 C56 76 58 66 60 60 Z')
branch='M10 118 C50 112 90 116 130 112 C150 110 170 112 190 108 L190 114 C170 118 150 116 130 118 C90 122 50 120 10 124 Z'
cuts=[('M64 76 Q76 96 96 104',1.6),('M68 70 Q80 88 98 96',1.2)]
for i in range(9): cuts.append((f'M{70+i*3:.1f} {86+i*2:.1f} q{4:.1f} {10:.1f} {12:.1f} {14:.1f}',R(.8,1.3)))
for i in range(6): cuts.append((f'M{20+i*30:.1f} {119+R(-1,1):.1f} l{R(10,20):.1f} {R(-1,1):.1f}',.9))
cuts.append(('M84 50 a2 2 0 1 0 .1 0',2))
el('swallow-perched',200,160,[body,branch],cuts,title='Woodcut swallow perched on a branch')

# bold: the brand swallow body as a graphic linocut, few strong cuts
SW=json.load(open('sw.json'))
body=SW['body']
cuts=[('M84 54 Q140 22 214 8',3.2),('M100 88 Q124 110 146 136',2.6),('M150 60 L222 40',2),('M160 70 L224 82',2),('M40 61.5 a2.4 2.4 0 1 0 .1 0',4)]
el('swallow-bold',248,150,[body],cuts,title='Swallow as a bold linocut, few strong cuts')

# ---------- LEAVES ----------
body='M100 10 C140 40 160 90 150 140 C142 176 120 196 100 200 C80 196 58 176 50 140 C40 90 60 40 100 10 Z'
cuts=[('M100 20 Q98 110 100 196',2.6)]
for i in range(9):
    y=40+i*17
    cuts.append((f'M{100:.1f} {y:.1f} Q{122:.1f} {y-4:.1f} {138-abs(i-4)*2:.1f} {y-16:.1f}',R(1.1,1.7)))
    cuts.append((f'M{100:.1f} {y+6:.1f} Q{78:.1f} {y+2:.1f} {62+abs(i-4)*2:.1f} {y-10:.1f}',R(1.1,1.7)))
stem='M98 196 L102 196 L104 228 L98 228 Z'
el('leaf-single',200,232,[body,stem],cuts,title='Woodcut leaf with veins')

# ginkgo fan
body='M100 150 C92 120 70 100 40 86 C20 76 10 60 14 46 C40 30 70 26 100 34 C130 26 160 30 186 46 C190 60 180 76 160 86 C130 100 108 120 100 150 Z'
body2='M97 150 L103 150 L104 196 L96 196 Z'
cuts=[('M100 34 L100 70',2.2)]
for i in range(24):
    a=math.radians(200+i*(140/23)); x=100+math.cos(a)*86; y=150+math.sin(a)*110
    cuts.append((f'M100 146 Q{(100+x)/2:.1f} {(146+y)/2+6:.1f} {x:.1f} {y:.1f}',R(.7,1.2)))
el('leaf-ginkgo',200,200,[body,body2],cuts,title='Woodcut ginkgo leaf')

# sprig: stem with five leaves
fills=['M96 230 C98 160 100 100 104 20 L108 20 C106 100 104 160 102 230 Z']
cuts=[]
def leaf_at(x,y,ang,L,W):
    a=math.radians(ang); ux,uy=math.cos(a),math.sin(a); px,py=-uy,ux
    tip=(x+ux*L,y+uy*L); m=(x+ux*L*.5,y+uy*L*.5)
    d=(f'M{x:.1f} {y:.1f} Q{m[0]+px*W:.1f} {m[1]+py*W:.1f} {tip[0]:.1f} {tip[1]:.1f} '
       f'Q{m[0]-px*W:.1f} {m[1]-py*W:.1f} {x:.1f} {y:.1f} Z')
    fills.append(d); cuts.append((f'M{x+ux*4:.1f} {y+uy*4:.1f} L{tip[0]-ux*6:.1f} {tip[1]-uy*6:.1f}',1.4))
    for k in range(1,5):
        t=k/5; bx,by=x+ux*L*t,y+uy*L*t
        for s in (1,-1): cuts.append((f'M{bx:.1f} {by:.1f} l{(ux*8+px*s*W*.5):.1f} {(uy*8+py*s*W*.5):.1f}',.9))
for (x,y,ang,L,W) in [(103,190,-150,70,18),(103,150,-30,74,18),(104,110,-155,64,16),(105,72,-28,62,15),(106,30,-95,50,13)]:
    leaf_at(x,y,ang,L,W)
el('leaf-sprig',210,236,fills,cuts,title='Woodcut sprig with five leaves')

# ---------- WIND ----------
inks=[]
def gust(y,amp,curl,w):
    d=f'M10 {y} C60 {y-amp} 110 {y+amp} 170 {y} C210 {y-amp*.6} 240 {y-curl} 236 {y-curl*1.6} C232 {y-curl*2.2} 214 {y-curl*2} 216 {y-curl*1.4}'
    return (d,w)
for i,(y,amp,curl,w) in enumerate([(40,10,14,5),(70,14,18,3.6),(100,9,12,6),(130,12,16,3),(160,8,10,4.4)]):
    inks.append(gust(y+R(-3,3),amp,curl,w))
    inks.append((f'M{R(20,60):.1f} {y+8:.1f} C80 {y+2} 120 {y+14} 160 {y+8}',w*.4))
el('wind-gusts',260,190,[],[],inks,title='Woodcut wind: curling gusts')

# wind with leaves carried
inks=[('M10 60 C70 40 130 90 190 60 C220 46 246 40 250 22 C252 10 236 6 232 16 C228 24 238 28 242 22',4.4),
      ('M10 100 C80 80 140 126 210 96 C230 88 248 92 252 104',3),
      ('M20 140 C90 124 150 160 240 130',2.2)]
fills=[];cuts=[]
for (x,y,ang) in [(86,52,-20),(150,78,30),(200,40,-60),(120,118,10),(226,112,50)]:
    a=math.radians(ang); ux,uy=math.cos(a),math.sin(a); px,py=-uy,ux; L=26; W=8
    tip=(x+ux*L,y+uy*L); m=(x+ux*L*.5,y+uy*L*.5)
    fills.append(f'M{x:.1f} {y:.1f} Q{m[0]+px*W:.1f} {m[1]+py*W:.1f} {tip[0]:.1f} {tip[1]:.1f} Q{m[0]-px*W:.1f} {m[1]-py*W:.1f} {x:.1f} {y:.1f} Z')
    cuts.append((f'M{x+ux*3:.1f} {y+uy*3:.1f} L{tip[0]-ux*4:.1f} {tip[1]-uy*4:.1f}',1.1))
el('wind-leaves',260,170,fills,cuts,inks,title='Woodcut wind carrying leaves')

# ---------- FRUITS ----------
apple='M100 60 C86 46 56 46 42 70 C26 98 38 150 66 170 C80 180 92 176 100 170 C108 176 120 180 134 170 C162 150 174 98 158 70 C144 46 114 46 100 60 Z'
stem='M98 62 C98 46 102 34 108 26 L112 28 C106 38 103 48 103 62 Z'
lf='M108 40 C120 22 146 18 162 26 C150 42 126 48 108 40 Z'
cuts=[('M60 80 Q50 110 62 146',3),('M70 74 Q62 100 70 130',1.6),('M110 42 Q134 34 158 27',1.4)]
for i in range(10): cuts.append((f'M{130+i*2:.1f} {84+i*7:.1f} l{R(6,12):.1f} {R(2,5):.1f}',R(.8,1.2)))
el('fruit-apple',200,190,[apple,stem,lf],cuts,title='Woodcut apple with leaf')

pear='M100 30 C110 30 116 44 118 64 C120 84 150 104 150 140 C150 172 126 190 100 190 C74 190 50 172 50 140 C50 104 80 84 82 64 C84 44 90 30 100 30 Z'
stem='M98 32 C98 22 100 14 106 6 L110 8 C104 16 103 24 103 32 Z'
cuts=[('M70 120 Q64 146 80 170',3),('M80 112 Q76 134 84 156',1.4)]
for i in range(30):
    a=R(0,2*math.pi); r=R(0,1)**.5; cuts.append((f'M{100+math.cos(a)*r*36:.1f} {144+math.sin(a)*r*32:.1f} l1.5 .5',R(1.6,2.4)))
el('fruit-pear',200,196,[pear,stem],cuts,title='Woodcut pear')

# pomegranate cut open: outer ring dark, inner white cuts as seeds
outer='M100 30 L92 14 L100 20 L108 14 L100 30 Z '+circ(100,110,80)
cuts=[(circ(100,110,70).replace(' Z',''),3)]
random.seed(44)
pts=[]
while len(pts)<70:
    x,y=R(36,164),R(46,174)
    if (x-100)**2+(y-110)**2<62**2 and all((x-a)**2+(y-b)**2>11**2 for a,b in pts): pts.append((x,y))
for x,y in pts:
    cuts.append((f'M{x-2.5:.1f} {y:.1f} q2.5 -4.5 5 0 q-2.5 4.5 -5 0',R(3,3.8)))

el('fruit-pomegranate',200,196,[outer],cuts,title='Woodcut pomegranate, cut open, full of seeds')

c1=circ(70,140,30); c2=circ(136,146,28)
stems='M70 110 C80 70 100 40 118 20 L121 23 C104 42 85 72 74 110 Z M136 118 C130 80 124 48 120 22 L124 21 C128 48 134 80 140 118 Z'
lf='M120 22 C138 8 166 8 180 18 C164 32 140 34 120 22 Z'
cuts=[('M54 128 Q50 142 58 156',2.6),('M122 132 Q118 146 126 160',2.4),('M124 22 Q150 18 176 18',1.3)]
el('fruit-cherries',200,180,[c1,c2,stems,lf],cuts,title='Woodcut cherries')

# ---------- PEOPLE IN A CIRCLE ----------
def seated(x,y,s,face):  # side view seated figure on chair, facing +1 right / -1 left; (x,y)=seat front-bottom of feet line
    f=face
    def P(px,py): return (x+f*(px-20)*s, y+(py-58)*s)
    def path(pts): return 'M'+' L'.join(f'{a:.1f} {b:.1f}' for a,b in (P(*p) for p in pts))+' Z'
    head=P(14,8); out=[circ(head[0],head[1],6*s)]
    out.append(path([(9,16),(19,15),(22,22),(24,33),(34,34),(36,40),(38,56),(33,57),(31,42),(18,42),(11,40),(8,28)]))
    out.append(path([(4,18),(7,18),(7,40),(30,40),(30,43),(27,43),(27,58),(25,58),(25,43),(9,43),(9,58),(7,58),(7,43),(4,43)]))
    return out
fills=[];cuts=[]
cx,cy,rx,ry=200,112,140,46
n=8
order=sorted(range(n),key=lambda i:math.sin(2*math.pi*i/n))  # far (top) first
for i in order:
    a=2*math.pi*i/n; x=cx+rx*math.cos(a); y=cy+ry*math.sin(a)
    depth=(math.sin(a)+1)/2; s=1.05+depth*.75
    face=-1 if math.cos(a)>0 else 1
    fills+=seated(x,y+20*s,s,face)
# dark carved ground under the circle, with a small fire at the centre
ground=f'M{cx-rx-46} {cy+44} C{cx-rx-40} {cy-40} {cx+rx+40} {cy-40} {cx+rx+46} {cy+44} C{cx+rx+40} {cy+120} {cx-rx-40} {cy+120} {cx-rx-46} {cy+44} Z'
figs=fills; fills=[ground]
cuts+=[(d,6) for d in figs]
for k in range(9): cuts.append((f'M{cx-rx-30+k*8} {cy+44+k*5} Q{cx} {cy+76+k*6} {cx+rx+30-k*8} {cy+44+k*5}',R(.9,1.6)))
for k in range(5):
    a=math.radians(-90+(k-2)*24); cuts.append((f'M{cx+math.cos(a)*6:.1f} {cy+40+math.sin(a)*6:.1f} L{cx+math.cos(a)*20:.1f} {cy+40+math.sin(a)*20:.1f}',2.2))
cuts.append((circ(cx,cy+40,5).replace(' Z',''),3))
inks=[]
el('circle-of-chairs',400,220,fills,cuts,inks,refills=figs,title='Woodcut: people sitting on chairs in a circle')

# from above: a dark floor disc, people and chairs carved into it
fills=[circ(150,150,140)];cuts=[]
cx,cy,r=150,150,96
for i in range(10):
    a=2*math.pi*i/10-math.pi/2; ux,uy=math.cos(a),math.sin(a); px,py=-uy,ux
    x=cx+r*ux; y=cy+r*uy
    def pt(u,v): return (x+ux*u+px*v, y+uy*u+py*v)
    seat=[pt(-13,-13),pt(13,-13),pt(13,13),pt(-13,13)]
    cuts.append((poly(seat),1.6))
    b0,b1=pt(19,-15),pt(19,15); cuts.append((f'M{b0[0]:.1f} {b0[1]:.1f} L{b1[0]:.1f} {b1[1]:.1f}',3.4))
    h=pt(1,0); cuts.append((circ(h[0],h[1],3.4).replace(' Z',''),6.6))
    s0,s1,sc=pt(9,-12),pt(9,12),pt(-3,0)
    cuts.append((f'M{s0[0]:.1f} {s0[1]:.1f} Q{sc[0]:.1f} {sc[1]:.1f} {s1[0]:.1f} {s1[1]:.1f}',3.2))
for k in range(5): cuts.append((circ(cx,cy,6+k*7).replace(' Z',''),1.4))
cuts.append((circ(cx,cy,132).replace(' Z',''),1.6))
el('circle-of-chairs-above',300,300,fills,cuts,title='Woodcut: a circle of people on chairs seen from above, around a centre')

def svg(name,e,bg=None,scale=3):
    w,h=e['w'],e['h']; uid=name
    m=''.join(f'<path d="{d}" fill="#fff"/>' for d in e['fills'])+''.join(f'<path d="{d}" stroke="#000" stroke-width="{wd:.2f}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>' for d,wd in e['cuts'])+''.join(f'<path d="{d}" fill="#fff"/>' for d in e['refills'])
    inks=''.join(f'<path d="{d}" stroke="currentColor" stroke-width="{wd:.2f}" stroke-linecap="round" fill="none"/>' for d,wd in e['inks'])
    fills=''.join(f'<path d="{d}"/>' for d in e['fills']+e['refills'])
    bgr=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w*scale}" height="{h*scale}" style="color:#1b1916">'
            f'<title>{e["title"]}</title><defs><filter id="r-{uid}" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="1" seed="5" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="2"/></filter>'
            f'<mask id="m-{uid}" maskUnits="userSpaceOnUse" x="-10" y="-10" width="{w+20}" height="{h+20}">{m}</mask></defs>{bgr}'
            f'<g filter="url(#r-{uid})">{inks}<g fill="currentColor" mask="url(#m-{uid})">{fills}</g></g></svg>')
os.makedirs(OUT,exist_ok=True)
for n,e in EL.items():
    open(f'{OUT}/{n}.svg','w').write(svg(n,e))
open('names.txt','w').write('\n'.join(EL))
# contact sheets (square, 3x3) for checking
names=list(EL)
for k in range(0,len(names),9):
    cells=''
    for j,n in enumerate(names[k:k+9]):
        e=EL[n]; x=(j%3)*300; y=(j//3)*300
        inner=svg(n,e).split('>',1)[1].rsplit('</svg>',1)[0]
        sc=min(260/e['w'],230/e['h'])
        cells+=f'<g transform="translate({x+20+(260-e["w"]*sc)/2:.1f} {y+15+(230-e["h"]*sc)/2:.1f}) scale({sc:.3f})">{inner}</g><text x="{x+150}" y="{y+288}" font-family="Helvetica" font-size="13" text-anchor="middle" fill="#5d584f">{n}</text>'
    open(f'sheet{k//9}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 900" width="1500" height="1500" style="color:#1b1916"><rect width="900" height="900" fill="#fbfaf6"/>{cells}</svg>')
print(len(EL))
