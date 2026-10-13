"""Build the animals gallery (gallery.html) from elements.json.
Usage: python3 build-gallery.py. Also makes thumbs/ (gitignored). Images load from
elements/ and thumbs/ next to the page, so publish those folders with it."""
import json, html, pathlib, subprocess
here = pathlib.Path(__file__).parent
d = json.load(open(here / "elements.json"))
INKS = [("black", "Black", "#1b1916"), ("blue", "Blue", "#03296f"),
        ("green", "Deep green", "#1f3d2b"), ("mustard", "Mustard", "#c9a227")]
base = "projects/sor-design-system/system/animals/elements/"
e_ = html.escape

def thumb(f):
    # thumbs/ is generated, not committed: 480px copies so the gallery loads quickly
    src, dst = here / f"elements/{f}.png", here / f"thumbs/{f}.png"
    if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
        dst.parent.mkdir(exist_ok=True)
        subprocess.run(["magick", str(src), "-resize", "480x480", "-strip", f"PNG32:{dst}"], check=True)

def kb(p):
    return f"{(here / p).stat().st_size / 1024:.0f} KB"

cards, rows, toc = [], [], []
for e in d:
    s = e["slug"]
    toc.append(f'<a href="#{s}">{e_(e["title"])}</a>')
    tiles = []
    for c, name, hexv in INKS + [tuple(x) for x in e.get("extra", [])]:
        f = f"{s}-{c}"
        thumb(f)
        has_svg = (here / f"elements/{f}.svg").exists()
        svg_link = f'<a href="elements/{f}.svg" target="_blank" rel="noopener">SVG</a>' if has_svg else ""
        svg_cell = f'{svg_link} <span class="kb">{kb(f"elements/{f}.svg")}</span>' if has_svg else '<span class="kb">PNG only</span>'
        tiles.append(f'''<figure class="tile" data-ink="{c}">
<a class="stage" href="elements/{f}.png" target="_blank" rel="noopener" aria-label="Open {e_(e["title"])}, {name}, PNG"><img src="thumbs/{f}.png" alt="{e_(e["title"])} in {name.lower()}" loading="lazy"></a>
<figcaption><span class="sw" style="background:{hexv if hexv.startswith('#') else 'conic-gradient(#2f4a44,#e8cf8f,#2f4a44)'}"></span><span class="cn">{name}</span> <code>{hexv}</code>
<span class="links"><a href="elements/{f}.png" target="_blank" rel="noopener">PNG</a>{svg_link}<button type="button" class="cp" data-copy="{base}{f}">Copy path</button></span></figcaption></figure>''')
        rows.append(f'''<tr data-search="{e_((e["title"] + " " + s + " " + name).lower())}"><td>{e["entry"]}</td><td><a href="#{s}">{e_(e["title"])}</a></td><td><span class="sw" style="background:{hexv if hexv.startswith('#') else 'conic-gradient(#2f4a44,#e8cf8f,#2f4a44)'}"></span>{name}</td><td class="fn">{f}</td><td><a href="elements/{f}.png" target="_blank" rel="noopener">PNG</a> <span class="kb">{kb(f"elements/{f}.png")}</span></td><td>{svg_cell}</td></tr>''')
    key = (e["title"] + " " + e["desc"] + " " + s + " " + e["source"]).lower()
    cards.append(f'''<article class="el" id="{s}" data-search="{e_(key)}">
<header><p class="meta">Mood board {e["entry"]} · {e_(e["source"])}</p><h2>{e_(e["title"])}</h2><p>{e_(e["desc"])}</p></header>
<div class="tiles">{"".join(tiles)}</div></article>''')

page = (here / "gallery-shell.html").read_text()
for k, v in {"@@N_EL@@": str(len(d)), "@@N_V@@": str(sum(len(INKS) + len(e.get("extra", [])) for e in d)), "@@CARDS@@": "".join(cards),
             "@@ROWS@@": "".join(rows), "@@TOC@@": "".join(toc)}.items():
    page = page.replace(k, v)
(here / "gallery.html").write_text(page)
print(f"{len(d)} elements, {len(page)//1024} KB")
