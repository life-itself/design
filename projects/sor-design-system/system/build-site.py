"""Assemble ../site/ (gitignored): the publishable design system, for `fl --yes site`.
Docs, guide, specimens, woodcuts page, system code and images, examples, archive. Leaves out moodboard/, raw/ and the
sub-folders of archive/ (third-party screenshots, uncleared images, large PDFs)."""
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
for d in ["examples", "specimens", "content"]:
    shutil.copytree(root / d, site / d)
shutil.copytree(root / "system", site / "system", ignore=shutil.ignore_patterns("*.py", "fonts", "textures.txt", "__pycache__", "preview-*.png", "sw.json"))
(site / "type").mkdir()
shutil.copy2(root / "type" / "research-notes.md", site / "type" / "research-notes.md")
shutil.copytree(root / "archive", site / "archive", ignore=lambda d, names: [n for n in names if (pathlib.Path(d) / n).is_dir()])
# HTML pages are served raw: point their links to .md files at the rendered Flowershow pages
for f in site.rglob("*.html"):
    t = f.read_text()
    t2 = re.sub(r'href="((?:\.\./)*)(?:README|index)\.md(#[^"]*)?"', r'href="\1./\2"', t)
    t2 = re.sub(r'href="((?:\.\./)*[\w/-]+)\.md(#[^"]*)?"', r'href="\1\2"', t2)
    if t2 != t:
        f.write_text(t2)
print("built", site, sum(1 for _ in site.rglob("*") if _.is_file()), "files")
