"""Fill the generated tables in reference.md, between its <!-- reference:… --> markers.
Usage: python3 system/build/build-reference.py (from projects/sor-design-system).

Reads system/tokens.css, system/graphics/<set>/elements.json, system/logo/, system/fonts/, the headings of
components.md and the pages in examples/. The words around the tables are edited in reference.md itself."""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
REPO = "https://github.com/life-itself/design/tree/main/projects/sor-design-system/"
RIGHTS = {"ours": "Free to use", "public-domain": "Free to use", "not-cleared": "Not cleared: drafts only", "draft": "Draft"}
SETS = ["sprite", "woodcuts", "animals", "prints", "botanicals", "washes", "lines", "mountains"]  # the order of graphics.md
COLOURWAYS = ["colour", "colour-dark", "black", "white", "red"]
LOCKUPS = [("horizontal", "Horizontal, the main logo"), ("two-lines-left", "Two lines, left"),
           ("two-lines-right", "Two lines, right"), ("stacked", "Stacked"), ("wordmark", "Wordmark, the name alone")]
# Faces: what tokens.css can't say. The role comes from the token's comment.
FONTS = [
    ("Polyamine", ["--font-display"], "One weight (Regular)", "Polyamine-",
     "Commercial, not yet licensed: drafts only. Shows only where installed; elsewhere Fraunces.",
     "https://uicreative.net/products/polyamine-modern-classy-serif-font"),
    ("Restora", ["--font-quote", "--font-poem"], "Eight weights, thin to black, with italics", "Restora-",
     "Commercial, not yet licensed: drafts only. Shows only where installed; elsewhere Fraunces.",
     "https://www.myfonts.com/collections/restora-font-nasir-udin"),
    ("Bricolage Grotesque", ["--font-body"], "300 to 700 (variable); light 300 for statements", None,
     "Free (SIL OFL). Loaded from Google Fonts.", "https://fonts.google.com/specimen/Bricolage+Grotesque"),
    ("Apfel Grotezk", ["--font-label"], "Regular 400, Mittel 500, Fett 700", "ApfelGrotezk-",
     "Free (SIL OFL). Embedded in `system/fonts.css`, so it loads anywhere.", "https://www.collletttivo.it/typefaces/apfel-grotezk"),
]
EXAMPLE_KINDS = [("web", "Website"), ("youtube", "YouTube"), ("social", "Social"), ("slides", "Slides"),
                 ("diagrams", "Diagrams"), ("print", "Print")]
USE = {"--night-muted": "secondary text on night", "--night-rule": "hairlines on night"}  # tokens.css leaves these bare
GENERIC = {"section", "gutter", "night", "label", "muted", "woodcut", "seal-corner"}
SWATCH = ('<span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;'
          'background:{};border:1px solid rgb(0 0 0 / .18)"></span>')


def cell(s):
    s = s.replace("|", "\\|").strip()
    return s[:1].upper() + s[1:]


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def tokens():
    """[(block title, [(group, name, value, use)])] for each :root block of tokens.css."""
    src = (ROOT / "system/tokens.css").read_text()
    blocks, pos = [], 0
    for m in re.finditer(r":root\s*\{(.*?)\n\}", src, re.S):
        before = src[pos:m.start()]
        heads = re.findall(r"/\*\s*──\s*([^─\n]+?)\s*─", before)
        title = heads[-1] if heads else ""
        group, rows = title, []
        for line in m.group(1).splitlines():
            h = re.match(r"\s*/\*\s*──\s*(.+?)\s*─", line)
            if h:
                group = h.group(1)
                continue
            t = re.match(r"\s*(--[\w-]+):\s*(.+?);\s*(?:/\*\s*(.*?)\s*\*/)?\s*$", line)
            if t:
                rows.append((group, t.group(1), t.group(2), t.group(3) or ""))
        blocks.append((title, rows))
        pos = m.end()
    return blocks


def is_colour(v):
    return re.fullmatch(r"#[0-9a-fA-F]{3,8}", v) is not None


def colours():
    rows = []
    for _, block in tokens():
        for group, name, value, use in block:
            if is_colour(value):
                g = re.sub(r"\s*\(.*|^The one ", "", group)
                rows.append((SWATCH.format(value), f"`{name}`", f"`{value}`", g, use or USE.get(name, "")))
    return table(["", "Token", "Hex", "Group", "Use"], rows)


def type_sizes():
    rows = [(f"`{n}`", f"`{v}`", u) for _, b in tokens()[:1] for g, n, v, u in b
            if n.startswith(("--t-", "--lh-", "--track-"))]
    return table(["Token", "Value", "Use"], rows)


def spacing():
    rows = [(f"`{n}`", f"`{v}`", u) for _, b in tokens()[:1] for g, n, v, u in b
            if g.startswith(("Space", "Material"))]
    return table(["Token", "Value", "Use"], rows)


def fixed():
    out = []
    for title, block in tokens()[1:]:
        name = re.sub(r"\s*\(.*", "", title)
        rows = [(f"`{n}`", f"`{v}`", u) for g, n, v, u in block if not is_colour(v)]
        out.append(f"**{name}**\n\n" + table(["Token", "Value", "Use"], rows))
    return "\n\n".join(out)


def graphics():
    rows, total = [], 0
    for name in SETS:
        s = json.loads((ROOT / "system/graphics" / name / "elements.json").read_text())
        n = len(s["elements"])
        files = sum(len(e.get("versions", [])) for e in s["elements"])
        total += n
        count = f"{n}" if files == n else f"{n} ({files} versions)"
        where = "`system/graphics.svg`" if name == "sprite" else f"`system/graphics/{name}/elements/`"
        rows.append((f"[{s['title']}](graphics/{name}.md)", count, s["formats"], RIGHTS[s["rights"]],
                     f"{where}, listed in [elements.json](system/graphics/{name}/elements.json)"))
    return table(["Set", "Elements", "Formats", "Rights", "Files"], rows) + f"\n\n{total} elements in {len(SETS)} sets."


def logos():
    L = ROOT / "system/logo"
    rows = []
    for slug, what in LOCKUPS:
        ways = " · ".join(f"[{c}](system/logo/lockups/seeds-logo-{slug}-{c}.svg)" for c in COLOURWAYS
                          if (L / f"lockups/seeds-logo-{slug}-{c}.svg").exists())
        rows.append((what, ways, "SVG; PNG 1200 and 2400px", f"`system/logo/lockups/seeds-logo-{slug}-<colourway>.svg`"))
    ways = " · ".join(f"[{c}](system/logo/mark/seeds-mark-{c}.svg)" for c in COLOURWAYS if (L / f"mark/seeds-mark-{c}.svg").exists())
    rows.append(("The mark alone", ways, "SVG; PNG 1130px", "`system/logo/mark/seeds-mark-<colourway>.svg`"))
    sizes = sorted({int(m.group(1)) for p in (L / "mark/sizes").glob("*.png") if (m := re.search(r"-(\d+)(?:@2x)?\.png$", p.name))})
    rows.append(("The mark drawn for each size", ", ".join(map(str, sizes)) + "px",
                 "PNG; @2x up to 128", "`system/logo/mark/sizes/seeds-mark-<colourway>-<px>.png`"))
    rows.append(("Favicon", "[favicon.ico](system/logo/favicon.ico)", "ICO: 16, 32, 48px", "`system/logo/favicon.ico`"))
    return table(["Version", "Colourways (SVG)", "Formats", "Path"], rows)


def fonts():
    toks = {n: u for _, b in tokens()[:1] for g, n, v, u in b}
    rows = []
    for face, names, weights, prefix, licence, src in FONTS:
        role = "; ".join(f"`{n}`: " + toks.get(n, "").split(". ")[0] for n in names)
        if prefix:
            order = ["Regular", "Mittel", "Fett"]  # by weight
            fs = sorted((p.name for p in (ROOT / "system/fonts").glob(prefix + "*")),
                        key=lambda f: next((i for i, w in enumerate(order) if w in f), len(order)))
            files = ", ".join(f"`{f}`" for f in fs) + " in `system/fonts/` (repo only)"
        else:
            files = "None in the repo: [Google Fonts](" + src + ")"
        rows.append((f"[{face}]({src})", role, weights, files, licence))
    return table(["Face", "Token and role", "Weights", "Files", "Licence"], rows)


def components():
    text = (ROOT / "components.md").read_text()
    rows = []
    for m in re.finditer(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", text, re.S | re.M):
        name, body = m.group(1).strip(), m.group(2)
        anchor = re.sub(r"[^\w\s-]", "", name.lower()).strip().replace(" ", "-")
        code = re.search(r"```html\n(.*?)```", body, re.S)
        if code:  # the first class that names the component, not a ground or a shared helper
            names = [c for a in re.findall(r'class="([^"]+)"', code.group(1)) for c in a.split()
                     if c not in GENERIC and not c.startswith(("ground-", "tear", "btn--"))]
            cls = f"`.{names[0]}`" if names else ""
        else:  # a table of classes
            names = re.findall(r"^\| `\.([\w-]+)`", body, re.M)
            cls = ", ".join(f"`.{c}`" for c in names[:6]) + (f" and {len(names) - 6} more" if len(names) > 6 else "")
        when = re.search(r"^When: (.+?)(?:\.\s|\.?$)", body, re.M) or re.search(r"^(\w[^\n]+?)\.?$", body, re.M)
        rows.append((f"[{name}](components.md#{anchor})", cls, when.group(1) if when else "Listed in a table on the page"))
    return table(["Component", "Class", "When"], rows)


def examples():
    rows = []
    for kind, label in EXAMPLE_KINDS:  # the order of examples.md; examples/type/ is a type study, not an example
        pages = sorted((ROOT / "examples" / kind).rglob("*.html"), key=lambda p: (p.name != "index.html", p.as_posix()))
        for p in pages:
            t = re.search(r"<title>([^<]*)", p.read_text())
            title = re.sub(r"^Seeds of Renaissance · ", "", t.group(1)).strip() if t else p.stem
            rel = p.relative_to(ROOT).as_posix()
            rows.append((label, f"[{title}]({rel})", f"`{rel}`"))
    return table(["Kind", "Page", "Path"], rows)


BLOCKS = {"graphics": graphics, "logos": logos, "fonts": fonts, "colours": colours, "type": type_sizes,
          "spacing": spacing, "fixed": fixed, "components": components, "examples": examples}

page = ROOT / "reference.md"
t = page.read_text()
for name, fn in BLOCKS.items():
    t, n = re.subn(rf"(<!-- reference:{name} -->\n).*?(<!-- /reference:{name} -->)",
                   lambda m: m.group(1) + "\n" + fn() + "\n\n" + m.group(2), t, flags=re.S)
    if n != 1:
        raise SystemExit(f"reference.md: no <!-- reference:{name} --> block")
page.write_text(t)
print("reference.md:", ", ".join(BLOCKS))
