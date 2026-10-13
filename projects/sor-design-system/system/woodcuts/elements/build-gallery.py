"""Build the woodcut elements gallery (one HTML page) from elements.json and the SVGs in this folder.
Usage: python3 build-gallery.py <output.html>. The page shell is gallery-shell.html."""
import json, re, html, sys, pathlib
here = pathlib.Path(__file__).parent
d = json.load(open(here / "elements.json"))
base = "projects/sor-design-system/system/woodcuts/elements/"
sym, cards = [], []
for e in d:
    tiles = []
    for v in e["variants"]:
        svg = (here / f"{v['file']}.svg").read_text()
        vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
        w, h = vb.split()[2:]
        paths = re.findall(r"<path[^>]*/>", svg)
        multi = len(paths) > 1
        sid = "s-" + (v["file"] if multi else e["slug"])
        if f'id="{sid}"' not in "".join(sym):
            inner = "".join(p if multi else re.sub(r'\sfill="[^"]*"', ' fill="currentColor"', p) for p in paths)
            sym.append(f'<symbol id="{sid}" viewBox="{vb}">{inner}</symbol>')
        ink = ' data-ink="1"' if v["hex"].lower() == "#1b1916" and not multi else ""
        sty = "" if multi else f' style="color:{v["hex"]}"'
        tiles.append(f'''<figure class="tile"><div class="stage"{ink}><svg role="img" aria-label="{html.escape(e["title"])}, {html.escape(v["colour"])}" viewBox="0 0 {w} {h}"{sty}><use href="#{sid}" width="{w}" height="{h}"/></svg></div>
<figcaption><span class="sw" style="background:{v["hex"]}"></span><span class="cn">{html.escape(v["colour"])}</span> <code>{v["hex"]}</code>
<button class="cp" data-copy="{base}{v["file"]}" title="Copy path without extension">Copy path</button><br><span class="fn">{v["file"]}<b>.svg</b> / <b>.png</b></span></figcaption></figure>''')
    key = (e["title"] + " " + e["desc"] + " " + e["slug"] + " " + " ".join(v["colour"] for v in e["variants"])).lower()
    cards.append(f'''<article class="el" data-search="{html.escape(key)}">
<header><h2>{html.escape(e["title"])}</h2><p>{html.escape(e["desc"])}</p><p class="meta">Mood board entry {e["entry"]} · {html.escape(e["source"])}</p></header>
<div class="tiles">{"".join(tiles)}</div></article>''')
page = (here / "gallery-shell.html").read_text()
page = page.replace("@@N_EL@@", str(len(d))).replace("@@N_V@@", str(sum(len(e["variants"]) for e in d)))
page = page.replace("@@CARDS@@", "".join(cards)).replace("@@SYM@@", "".join(sym))
open(sys.argv[1], "w").write(page)
print(f"{len(d)} elements, {len(page)//1024} KB")
