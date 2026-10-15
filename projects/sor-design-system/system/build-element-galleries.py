"""Build gallery.html for the graphic sets (botanicals, washes, geometry, marks, prints)
from each set's elements.json and element-gallery-shell.html.
Usage: python3 system/build-element-galleries.py. Also makes thumbs/ (gitignored) in each set.
Images load from elements/ and thumbs/ next to each page, so publish those folders with it."""
import json, html, pathlib, subprocess
here = pathlib.Path(__file__).parent
e_ = html.escape
SETS = ["botanicals", "washes", "geometry", "marks", "prints"]
shell = (here / "element-gallery-shell.html").read_text()

def kb(p):
    return f"{p.stat().st_size / 1024:.0f} KB"

for name in SETS:
    d = json.load(open(here / name / "elements.json"))
    base = f"projects/sor-design-system/system/{name}/elements/"
    cards = []
    for e in d["elements"]:
        s = e["slug"]
        src, dst = here / name / f"elements/{s}.png", here / name / f"thumbs/{s}.png"
        if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
            dst.parent.mkdir(exist_ok=True)
            subprocess.run(["magick", str(src), "-resize", "600x600>", "-strip", f"PNG32:{dst}"], check=True)
        svg_p = here / name / f"elements/{s}.svg"
        svg = (f'<a href="elements/{s}.svg" target="_blank" rel="noopener">SVG</a> <span class="kb">{kb(svg_p)}</span>'
               if svg_p.exists() else '<span class="kb">PNG only</span>')
        cards.append(f'''<figure class="tile">
<a class="stage" href="elements/{s}.png" target="_blank" rel="noopener" aria-label="Open {e_(e["title"])}, PNG"><img src="thumbs/{s}.png" alt="{e_(e["title"])}" loading="lazy"></a>
<h2>{e_(e["title"])}</h2><p class="kind">{e_(e["kind"])}</p><p class="desc">{e_(e["desc"])}</p>
<div class="links"><a href="elements/{s}.png" target="_blank" rel="noopener">PNG</a> <span class="kb">{kb(src)}</span> · {svg} <button type="button" class="cp" data-copy="{base}{s}">Copy path</button></div></figure>''')
    sets_nav = " · ".join(f'<a href="../{n}/gallery.html"{" aria-current=page" if n == name else ""}>{n.capitalize()}</a>' for n in SETS)
    page = shell
    for k, v in {"@@TITLE@@": d["title"], "@@H1@@": d["title"], "@@LEDE@@": e_(d["lede"]), "@@SETS@@": sets_nav,
                 "@@CARDS@@": "".join(cards), "@@SET@@": name}.items():
        page = page.replace(k, v)
    (here / name / "gallery.html").write_text(page)
    print(f"{name}: {len(d['elements'])} elements, {len(page)//1024} KB")
