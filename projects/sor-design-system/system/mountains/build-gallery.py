"""Build the mountains gallery (gallery.html) from elements.json.
Usage: python3 build-gallery.py. Also makes thumbs/ (gitignored). Images load from
elements/ and thumbs/ next to the page, so publish those folders with it."""
import json, html, pathlib, subprocess
here = pathlib.Path(__file__).parent
d = json.load(open(here / "elements.json"))
base = "projects/sor-design-system/system/mountains/elements/"
e_ = html.escape

def thumb(f):
    # thumbs/ is generated, not committed: 480px copies so the gallery loads quickly
    src, dst = here / f"elements/{f}.png", here / f"thumbs/{f}.png"
    if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
        dst.parent.mkdir(exist_ok=True)
        subprocess.run(["magick", str(src), "-resize", "480x480", "-strip", f"PNG32:{dst}"], check=True)

def kb(p):
    return f"{(here / p).stat().st_size / 1024:.0f} KB"

def sw(hexv):
    return hexv if hexv.startswith("#") else "conic-gradient(#1b1916,#e8dcc0,#1b1916)"

overview, cards, toc, n_v = [], [], [], 0
for e in d:
    s = e["slug"]
    toc.append(f'<a href="#{s}">{e_(e["title"])}</a>')
    inks = e["inks"]
    # overview: rows of three, so the lighter blues get a row of their own
    for i in range(0, len(inks), 3):
        chunk = inks[i:i + 3]
        sub = e["kind"] if i == 0 else "lighter blues"
        overview.append(f'<div class="all-name"><a href="#{s}">{e_(e["title"])}</a><span>{e_(sub)}</span></div>')
        for c, name, _ in chunk:
            f = f"{s}-{c}"; thumb(f)
            overview.append(f'<a class="all-tile" href="#{s}"><img src="thumbs/{f}.png" alt="{e_(e["title"])}, {e_(name.lower())}" loading="lazy"></a>')
        overview += ['<div class="all-empty"></div>'] * (3 - len(chunk))
    tiles = []
    for c, name, hexv in inks:
        f = f"{s}-{c}"; n_v += 1
        has_svg = (here / f"elements/{f}.svg").exists()
        svg = f'<a href="elements/{f}.svg" target="_blank" rel="noopener">SVG</a> <span class="kb">{kb(f"elements/{f}.svg")}</span>' if has_svg else '<span class="kb">PNG only</span>'
        tiles.append(f'''<figure class="tile">
<a class="stage" href="elements/{f}.png" target="_blank" rel="noopener" aria-label="Open {e_(e["title"])}, {e_(name)}, PNG"><img src="thumbs/{f}.png" alt="{e_(e["title"])} in {e_(name.lower())}" loading="lazy"></a>
<figcaption><span class="sw" style="background:{sw(hexv)}"></span><b>{e_(name)}</b> <code>{e_(hexv)}</code>
<span class="links"><a href="elements/{f}.png" target="_blank" rel="noopener">PNG</a> <span class="kb">{kb(f"elements/{f}.png")}</span> · {svg} <button type="button" class="cp" data-copy="{base}{f}">Copy path</button></span></figcaption></figure>''')
    cards.append(f'''<article class="el" id="{s}">
<header><p class="meta">Mood board {e["entry"]} · {e_(e["kind"])}</p><h2>{e_(e["title"])}</h2><p>{e_(e["desc"])}</p></header>
<div class="tiles">{"".join(tiles)}</div></article>''')

page = (here / "gallery-shell.html").read_text()
for k, v in {"@@N_EL@@": str(len(d)), "@@N_V@@": str(n_v), "@@ALL@@": "".join(overview),
             "@@CARDS@@": "".join(cards), "@@TOC@@": "".join(toc)}.items():
    page = page.replace(k, v)
(here / "gallery.html").write_text(page)
print(f"{len(d)} elements, {n_v} files, {len(page)//1024} KB")
