"""Assemble ../site/ (gitignored): the publishable design system, for `fl --yes site`.
Docs, guide, specimens, graphics galleries, system code and images, examples. Leaves out moodboard/ and archive/
(the working record, linked on GitHub)."""
import pathlib, re, shutil
root = pathlib.Path(__file__).resolve().parent.parent
site = root / "site"
keep = site / ".flowershow"
saved = keep.read_text() if keep.exists() else None
if site.exists():
    shutil.rmtree(site)
site.mkdir()
if saved:
    keep.write_text(saved)
for f in list(root.glob("*.md")) + list(root.glob("*.html")) + [root / "config.json", root / "custom.css", root / "llms.txt"]:
    shutil.copy2(f, site / f.name)
for d in ["examples", "specimens", "content", "graphics"]:
    shutil.copytree(root / d, site / d)
# No .gitignore: the sets ignore thumbs/ in the repo, but the site branch must commit them for the galleries
shutil.copytree(root / "system", site / "system", ignore=shutil.ignore_patterns("*.py", "*.sh", "*-shell.html", ".gitignore", "fonts", "textures.txt", "__pycache__", "preview-*.png", "sw.json"))
(site / "type").mkdir()
shutil.copy2(root / "type" / "research-notes.md", site / "type" / "research-notes.md")
# archive/ is not published: it is the working record, read on GitHub. Links to it from pages go there.
ARCHIVE = "https://github.com/life-itself/design/blob/main/projects/sor-design-system/archive/"
for f in list(site.rglob("*.md")) + list(site.rglob("*.html")):
    t = f.read_text()
    t2 = re.sub(r'(\]\(|href=")(?:\.\./)*archive/', lambda m: m.group(1) + ARCHIVE, t)
    if t2 != t:
        f.write_text(t2)
# HTML pages are served raw: point their links to .md files at the rendered Flowershow pages
for f in site.rglob("*.html"):
    t = f.read_text()
    t2 = re.sub(r'href="((?:\.\./)*)(?:README|index)\.md(#[^"]*)?"', r'href="\1./\2"', t)
    t2 = re.sub(r'href="((?:\.\./)*[\w/-]+)\.md(#[^"]*)?"', r'href="\1\2"', t2)
    if t2 != t:
        f.write_text(t2)
# The guide and the examples are standalone pages with no site navbar: give each a way back (not when framed)
BACK = ('<a id="sor-back" href="{href}" style="display:none;position:fixed;left:12px;bottom:12px;z-index:2147483647;'
        'background:#1b1916;color:#fbfaf6;font:500 11px/1 system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;'
        'padding:9px 11px;text-decoration:none">&larr; {text}</a><script>if(window.top===window.self)'
        'document.getElementById("sor-back").style.display="block"</script>')
for f, href, text in [(site / "guide.html", "/", "SoR design system")] + [
        (p, "/examples", "Examples &middot; SoR design system") for p in (site / "examples").rglob("*.html")]:
    t = f.read_text()
    link = BACK.format(href=href, text=text)
    m = re.search(r"<body[^>]*>", t)
    f.write_text(t[:m.end()] + link + t[m.end():] if m else t + link)
# Old addresses of pages that moved: a redirect stub at each
MOVED = {"woodcuts.html": "/graphics/woodcuts", "logos.html": "/logos",
         **{f"system/{s}/gallery.html": f"/graphics/{s}" for s in ["animals", "mountains", "botanicals", "washes", "prints"]},
         "system/geometry/gallery.html": "/graphics/lines", "system/marks/gallery.html": "/graphics/lines",
         "system/woodcuts/gallery.html": "/graphics/woodcuts"}
for old, new in MOVED.items():
    (site / old).parent.mkdir(parents=True, exist_ok=True)
    (site / old).write_text(f'<!doctype html><meta charset="utf-8"><title>Moved</title><meta http-equiv="refresh" content="0; url={new}">'
                            f'<link rel="canonical" href="{new}"><p>Moved to <a href="{new}">{new}</a>.</p>\n')
print("built", site, sum(1 for _ in site.rglob("*") if _.is_file()), "files")
