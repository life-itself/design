"""Split guide.html into specimens/<chapter>.html: one standalone page per chapter, for
embedding in the markdown pages with an <iframe>. guide.html stays the single source;
rerun after editing it. Specimens hide each chapter's heading and "more" links: the
pages that embed them have their own.

Each specimen lays out at a virtual 1000px and scales to its frame (CSS zoom), so its height
is a fixed ratio of its width: embed with aspect-ratio 1000 / height (heights printed by
measuring in a browser; see MAINTAINING.md). Below 600px it lays out natively and scrolls."""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "guide.html").read_text()
out = root / "specimens"
out.mkdir(exist_ok=True)

head = src[:src.index('<div class="sor">')].replace('<meta charset="utf-8">', "").strip()
sections = {"cover": re.search(r'<header class="g-cover">.*?</header>\s*<span class="tear tear--bottom"[^>]*></span>', src, re.S).group(0)}
for m in re.finditer(r'<section class="g-ch[^"]*" id="([a-z]+)">.*?</div></section>', src, re.S):
    sections[m.group(1)] = m.group(0)
# groups within a chapter (<div id="examples-web">…</div></div>) get their own specimen too
for m in re.finditer(r'<div id="(examples-[a-z]+)">.*?</div></div>', src, re.S):
    sections[m.group(1)] = f'<section class="g-ch"><div class="g-wrap"><div class="g-body">{m.group(0)}</div></div></section>'

def fix(html):
    # one folder down: rebase relative paths; open links in the parent page, not the frame
    html = re.sub(r'(href|src)="(?![a-z]+:|#|/|\.\./)', r'\1="../', html)
    return re.sub(r'<a ((?:class="[^"]*" )?)href="(?!#)', r'<a \1target="_top" href="', html)

extra = """<style>
html, body { overflow-x: hidden }
.g-ch { padding-block: 28px; border: 0 !important }
.g-cover { padding-block: clamp(32px, 6cqi, 72px) }
.g-head, .g-more { display: none }
.g-body { margin-left: 0 }
</style>"""
tail = """<script>
function fit() { document.documentElement.style.zoom = innerWidth >= 600 ? innerWidth / 1000 : 1 }
fit(); addEventListener('resize', fit);
document.querySelectorAll('.hex[data-token]').forEach(function (el) {
  var v = getComputedStyle(document.documentElement).getPropertyValue(el.dataset.token).trim();
  if (v) el.textContent = el.dataset.token + ' · ' + v;
});
</script>
<script src="../system/sor.js"></script>"""
for name, body in sections.items():
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Generated from guide.html by system/build-specimens.py. Do not edit. -->
{fix(head)}
{extra}
</head>
<body>
<div class="sor">
<script src="../system/graphics.js"></script>
{fix(body)}
</div>
{tail}
</body>
</html>
"""
    (out / f"{name}.html").write_text(page)
print("specimens:", ", ".join(sections))
