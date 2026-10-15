"""Build the graphics library: one gallery page per set, the hub cards and rules table in graphics.md,
and the logo files page. Usage: python3 system/build-galleries.py (thumbnails need ImageMagick `magick`, or `sips` on macOS).

Reads system/graphics/<set>/elements.json (one schema for every set, see system/graphics/README.md) and
system/graphics/gallery-shell.html. Writes:
  graphics/<set>.md          a Flowershow page (layout: plain) per set, with the site navbar
  graphics.md                the cards and the rules table, between their <!-- library:… --> markers
  logos.md                   every logo file on its ground
  system/graphics/<set>/thumbs/  600px PNG thumbnails (gitignored; CI builds them)
Pages use site-absolute paths (/system/graphics/...), so they work only on the published site."""
import html, json, pathlib, re, shutil, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
G = ROOT / "system" / "graphics"
e_ = html.escape

# Hub order: families, then sets within each
FAMILIES = [
    ("woodcut", "Woodcut and print", "Carved and printed marks: black shapes, white cuts, a rough printed edge.",
     ["sprite", "woodcuts", "animals", "prints"]),
    ("painted", "Painted", "Watercolour, ink and colour plates, kept in the colours they were painted in.",
     ["botanicals", "washes"]),
    ("line", "Line", "Geometry and interlaced marks in plain black line.", ["lines"]),
    ("landscape", "Landscape", "Pen, brush and linocut mountains in their drawn blues.", ["mountains"]),
]
GROUNDS = {"white": "White", "paper": "Paper", "sunlight": "Sunlight", "night": "Night"}
TINTS = [("blue", "Blue"), ("green", "Deep green"), ("mustard", "Mustard")]  # illustration inks, for inline sets
RIGHTS = {"ours": "Ours", "not-cleared": "Not cleared", "draft": "Draft"}
RIGHTS_NOTE = {
    "ours": "Ours to use anywhere.",
    "not-cleared": "Traced or cut from mood board images whose rights are not cleared: fine for mockups and drafts; redraw, re-source or clear before anything goes public.",
    "draft": "Draft: redraw or re-source before it goes on anything live.",
}
BRAND = [  # cards linking out of the library
    ("Logo files", "/logos", "Five colourways, five lockups, the mark at every size.", "SVG and PNG",
     [("system/logo/lockups/seeds-logo-horizontal-colour-1200.png", "g-paper")]),
    ("Signature", "/diagrams#the-signature", "The mark and URL that sign a figure or diagram.", "SVG and PNG",
     [("system/img/signature.svg", "g-white")]),
    ("Podcast ground", "/podcast#the-look-swallows-and-fingerprints", "Sunlight, the swallow flock and the fingerprints from the bottom left.", "PNG, built in code",
     [("examples/podcast/web/episode-art-background.jpg", "bleed")]),
]


def load(name):
    s = json.loads((G / name / "elements.json").read_text())
    s["name"] = name
    return s


def css():
    """System tokens scoped to .sg (so the site theme is untouched), then the library styles."""
    tokens = (ROOT / "system/tokens.css").read_text()
    root = re.search(r":root\s*\{(.*?)\n\}", tokens, re.S).group(1)
    root = re.sub(r"/\*.*?\*/", "", root, flags=re.S)
    root = " ".join(l.strip() for l in root.splitlines() if l.strip())
    lib = re.sub(r"/\*.*?\*/", "", (G / "library.css").read_text(), flags=re.S)
    lib = "\n".join(l for l in lib.splitlines() if l.strip())
    fonts = ('@import url("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700'
             '&family=Hanken+Grotesk:wght@400;500;700&family=Fraunces:ital,opsz,wght@0,9..144,300..500;1,9..144,300..500&display=swap");\n'
             '@import url("/system/fonts.css");')
    return f"{fonts}\n.sg {{ {root} }}\n{lib}"


def thumb(name, f):
    src, dst = G / name / f"elements/{f}.png", G / name / f"thumbs/{f}.png"
    if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
        dst.parent.mkdir(exist_ok=True)
        if shutil.which("magick"):
            subprocess.run(["magick", str(src), "-resize", "600x600>", "-strip", f"PNG32:{dst}"], check=True)
        else:  # macOS without ImageMagick
            subprocess.run(["sips", "-Z", "600", str(src), "--out", str(dst)], check=True, capture_output=True)
    return f"/system/graphics/{name}/thumbs/{f}.png"


def kb(p):
    return f"{p.stat().st_size / 1024:,.0f} KB"


def inline_svg(path, label):
    """A woodcut SVG inlined so it takes the ink of its ground (currentColor), on one line."""
    s = path.read_text().strip()
    s = re.sub(r"<\?xml[^>]*>\s*", "", s)
    s = re.sub(r'\s(width|height)="[^"]*"', "", s, count=2)
    s = s.replace('style="color:#1b1916"', "", 1)
    if s.count("#fbfaf6") == 1:  # a paper background rect: drop it so the ground shows
        s = re.sub(r'<rect width="[\d.]+" height="[\d.]+" fill="#fbfaf6"/>', "", s, count=1)
    s = s.replace("<svg ", f'<svg role="img" aria-label="{e_(label)}" ', 1)
    return re.sub(r"\s*\n\s*", " ", s)


SPRITE = (ROOT / "system/graphics.svg").read_text()
VIEWBOX = dict(re.findall(r'<symbol id="([\w-]+)" viewBox="([^"]+)"', SPRITE))


def sprite_defs():
    return re.sub(r"\s*\n\s*", " ", SPRITE.strip())


def symbol(i, label):
    return f'<svg viewBox="{VIEWBOX[i]}" role="img" aria-label="{e_(label)}"><use href="#{i}"/></svg>'


def art(s, el, v, label):
    """What goes on the stage for one version: an inline SVG, a sprite symbol or a thumbnail."""
    f = v.get("file", f'{el["slug"]}-{v["ink"]}')
    if s.get("render") == "symbol":
        return symbol(f, label)
    if s.get("render") == "inline":
        return inline_svg(G / s["name"] / f"elements/{f}.svg", label)
    return f'<img src="{thumb(s["name"], f)}" alt="{e_(label)}" loading="lazy">'


def swatch(hexv, ink=None):
    if ink == "ground":
        return "linear-gradient(90deg,#1b1916 50%,#ece7dc 50%)"
    if not hexv:
        return "conic-gradient(#c25552,#dbb06a,#3b5a45,#03296f,#c25552)"
    cols = re.findall(r"#[0-9a-f]{6}", hexv, re.I)
    return cols[0] if len(cols) == 1 else f"linear-gradient(90deg,{cols[0]} 50%,{cols[1]} 50%)"


def files(s, el, v):
    """Links to a version's files, and the repo path to copy."""
    name, f = s["name"], v.get("file", f'{el["slug"]}-{v["ink"]}')
    if s.get("render") == "symbol":
        snippet = f'<svg viewBox="{VIEWBOX[f]}"><use href="#{f}"/></svg>'
        return f'<code>#{f}</code><button type="button" class="sg-cp" data-copy="{e_(snippet)}">Copy code</button>'
    out, d = [], G / name / "elements"
    for ext in ("png", "svg"):
        p = d / f"{f}.{ext}"
        if p.exists():
            out.append(f'<a href="/system/graphics/{name}/elements/{f}.{ext}" target="_blank" rel="noopener">{ext.upper()}</a> {kb(p)}')
    for p in sorted(d.glob(f"{f}-*.png")) if s.get("render") == "inline" else []:
        out.append(f'<a href="/system/graphics/{name}/elements/{p.name}" target="_blank" rel="noopener">PNG {p.stem[len(f) + 1:]}</a>')
    main = "svg" if s.get("render") == "inline" else "png"
    out.append(f'<button type="button" class="sg-cp" data-copy="projects/sor-design-system/system/graphics/{name}/elements/{f}.{main}">Copy path</button>')
    return " · ".join(out[:-1]) + " " + out[-1]


def card(s, el):
    vs = el["versions"]
    rights = el.get("rights", s["rights"])
    q = " ".join([el["title"], el["slug"], el.get("kind", ""), el["desc"], el.get("source", "")] + [v["name"] for v in vs]).lower()
    stage, rows = [], []
    for i, v in enumerate(vs):
        label = el["title"] if len(vs) == 1 else f'{el["title"]}, {v["name"].lower()}'
        f = v.get("file", f'{el["slug"]}-{v["ink"]}')
        a = art(s, el, v, label)
        hid = " hidden" if i else ""
        if s.get("render") in ("inline", "symbol"):
            stage.append(f'<div data-v="{v["ink"]}"{hid}>{a}</div>')
        else:
            stage.append(f'<a data-v="{v["ink"]}" href="/system/graphics/{s["name"]}/elements/{f}.png" target="_blank" rel="noopener"{hid}>{a}</a>')
        hexv = f' <code>{e_(v["hex"])}</code>' if v.get("hex") else (f' <span class="sg-muted">{e_(v["note"])}</span>' if v.get("note") else "")
        rows.append(f'<div class="sg-row"><span class="sg-v" data-v="{v["ink"]}"><span class="sg-sw" style="background:{swatch(v.get("hex"), v["ink"])}"></span>{e_(v["name"])}</span>{hexv}'
                    f'<span class="sg-files">{files(s, el, v)}</span></div>')
    tag = f'<p class="sg-tag" title="{e_(RIGHTS_NOTE[rights])}">{RIGHTS[rights]}: {"redraw or re-source before public use" if rights == "draft" else "not cleared"}</p>' if rights != s["rights"] else ""
    kind = " · ".join(x for x in [el.get("kind", ""), el.get("source", "")] if x)
    wide = " sg-wide" if el.get("wide") else ""
    return (f'<article class="sg-el{wide}" id="{el["slug"]}" data-q="{e_(q)}">'
            f'<div class="sg-stage">{"".join(stage)}</div>'
            f'<div class="sg-cap"><p class="sg-kind sg-label">{e_(kind)}</p><h2>{e_(el["title"])}</h2><p class="sg-desc">{e_(el["desc"])}</p>{tag}'
            f'<div class="sg-vers">{"".join(rows)}</div></div></article>')


def facts(s):
    rows = [("Use for", s["use_for"]), ("Colour", s["colour_rule"]),
            ("Grounds", ", ".join(GROUNDS[g] for g in s["grounds"])),
            ("Registers", ", ".join(s["registers"])), ("Formats", s["formats"]),
            ("Rights", f'{RIGHTS[s["rights"]]}. {RIGHTS_NOTE[s["rights"]]}' if s["rights"] != "ours" else RIGHTS_NOTE["ours"])]
    return "".join(f"<dt>{k}</dt><dd>{e_(v)}</dd>" for k, v in rows)


def sets_nav(sets, current=None):
    groups = []
    for _, fam, _, names in FAMILIES:
        links = "".join(f'<li><a href="/graphics/{n}"{" aria-current=page" if n == current else ""}>{e_(sets[n]["title"])}</a></li>' for n in names)
        groups.append(f'<div><p class="sg-label sg-muted">{fam}</p><ul>{links}</ul></div>')
    groups.append('<div><p class="sg-label sg-muted">Brand marks</p><ul>'
                  + "".join(f'<li><a href="{h}">{e_(t)}</a></li>' for t, h, *_ in BRAND) + "</ul></div>")
    return '<p><a href="/graphics">All graphics</a></p>' + "".join(groups)


def n_versions(s):
    return sum(len(e["versions"]) for e in s["elements"])


def flat(text):
    """Flowershow ends an HTML block at a blank line, so the generated HTML has none."""
    return "\n".join(l for l in text.splitlines() if l.strip())


def gallery(s, sets, shell, style):
    name = s["name"]
    fam = next(f for k, f, _, _ in FAMILIES if k == s["family"])
    inks = []
    if s.get("render") in ("inline", "symbol"):
        if s["name"] == "woodcuts":
            inks = [("ground", "Ground")] + TINTS
    else:
        seen = {}
        for el in s["elements"]:
            for v in el["versions"]:
                seen.setdefault(v["ink"], v["name"])
        if len(seen) > 1 and len(seen) <= 6:
            inks = list(seen.items())
    ink_html = ""
    if inks:
        first = inks[0][0]
        ink_html = ('<div class="sg-grp" role="group" aria-label="Ink"><span class="sg-label">Ink</span>'
                    + "".join(f'<button type="button" class="sg-btn" data-ink-btn="{k}" aria-pressed="{str(k == first).lower()}">{e_(n)}</button>' for k, n in inks) + "</div>")
    grounds = "".join(f'<button type="button" class="sg-btn" data-ground-btn="{g}" aria-pressed="{str(i == 0).lower()}">{GROUNDS[g]}</button>' for i, g in enumerate(s["grounds"]))
    notes = f'<p class="sg-note">{e_(s["notes"])}</p>' if s.get("notes") else ""
    count = f'{len(s["elements"])} elements' + (f', {n_versions(s)} files' if n_versions(s) != len(s["elements"]) else "")
    finds = ", ".join(e["title"].split(",")[0].split()[-1].lower() for e in s["elements"][:2]) + "…"
    page = shell
    for k, v in {"@@TITLE@@": e_(s["title"]), "@@DESCRIPTION@@": e_(f'{s["title"]}: {count}. {s["use_for"]}'),
                 "@@CSS@@": style, "@@SET@@": name, "@@GROUND@@": s["grounds"][0], "@@RENDER@@": s.get("render", "img"),
                 "@@FAMILY@@": e_(fam), "@@LEDE@@": e_(s["lede"]), "@@FACTS@@": facts(s), "@@NOTES@@": notes,
                 "@@GROUNDS@@": grounds, "@@INKS@@": ink_html, "@@FIND@@": e_(finds),
                 "@@SPRITE@@": sprite_defs() if s.get("render") == "symbol" else "",
                 "@@CARDS@@": "".join(card(s, el) for el in s["elements"]), "@@SETS@@": sets_nav(sets, name),
                 "@@DIR@@": f"system/graphics/{name}/"}.items():
        page = page.replace(k, v)
    out = ROOT / "graphics" / f"{name}.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(flat(page) + "\n")
    return out


def hub(sets, style):
    """The cards and the rules table in graphics.md, between the library markers."""
    fams = []
    for _, fam, blurb, names in FAMILIES:
        cards = []
        for n in names:
            s = sets[n]
            pick = s.get("cover") or [e["slug"] for e in s["elements"][:6]]
            by = {e["slug"]: e for e in s["elements"]}
            thumbs = []
            for slug in pick[:6]:
                el = by[slug]
                v = el["versions"][0]
                a = art(s, el, v, el["title"])
                thumbs.append(f"<div>{a}</div>")
            count = f'{len(s["elements"])} elements' + (f' · {n_versions(s)} files' if n_versions(s) != len(s["elements"]) else "")
            cards.append(f'<a class="sg-card" href="/graphics/{n}"><div class="sg-thumbs">{"".join(thumbs)}</div>'
                         f'<h3>{e_(s["title"])}</h3><p>{e_(s["use_for"])}</p>'
                         f'<p class="sg-meta"><span class="sg-label">{count}</span><span class="sg-label">{e_(s["formats"])}</span><span class="sg-label">{RIGHTS[s["rights"]]}</span></p></a>')
        fams.append(f'<section class="sg-fam"><header><h2 class="sg-label">{fam}</h2><p>{e_(blurb)}</p></header><div class="sg-cards">{"".join(cards)}</div></section>')
    brand = []
    for t, h, use, fmt, imgs in BRAND:
        th = "".join(f'<div class="{c}"><img src="/{p}" alt="" loading="lazy"></div>' for p, c in imgs)
        brand.append(f'<a class="sg-card" href="{h}"><div class="sg-thumbs one">{th}</div><h3>{e_(t)}</h3><p>{e_(use)}</p>'
                     f'<p class="sg-meta"><span class="sg-label">{e_(fmt)}</span><span class="sg-label">Ours</span></p></a>')
    fams.append('<section class="sg-fam"><header><h2 class="sg-label">Brand marks</h2><p>The logo and the marks built from it. Rules in their own guides.</p></header>'
                f'<div class="sg-cards">{"".join(brand)}</div></section>')
    has_sprite = any(sets[n].get("render") == "symbol" for _, _, _, ns in FAMILIES for n in ns)
    cards_html = flat(f'<style>{style}</style>\n<div class="sg not-prose" style="padding-inline:0;background:none">'
                      + (sprite_defs() if has_sprite else "") + "\n" + "\n".join(fams) + "\n</div>")
    rows = ["| Set | Colour | Grounds | Registers | Formats | Rights |", "|---|---|---|---|---|---|"]
    for _, _, _, names in FAMILIES:
        for n in names:
            s = sets[n]
            rows.append(f'| [{s["title"]}](graphics/{n}.md) | {s["colour_rule"]} | {", ".join(GROUNDS[g] for g in s["grounds"])} | '
                        f'{", ".join(s["registers"])} | {s["formats"]} | {RIGHTS[s["rights"]]} |')
    md = (ROOT / "graphics.md").read_text()
    for key, block in (("cards", cards_html), ("rules", "\n".join(rows))):
        md, n = re.subn(rf"(<!-- library:{key} -->\n)(?:.*?\n)?(<!-- /library:{key} -->)", lambda m: m.group(1) + block + "\n" + m.group(2), md, flags=re.S)
        assert n == 1, f"graphics.md needs <!-- library:{key} --> and <!-- /library:{key} --> markers"
    (ROOT / "graphics.md").write_text(md)


# ── Logo files ─────────────────────────────────────────────────────────────
WAYS = [("colour", "Colour", "g-paper", "on white, paper, pale yellow"),
        ("colour-dark", "Colour, dark", "g-night", "on night, dark photographs"),
        ("black", "Black", "g-white", "on light grounds, and on red"),
        ("white", "White", "g-night", "on night, and on red"),
        ("red", "Red", "g-white", "on light grounds")]
LOCKUPS = [("horizontal", "Horizontal", "the main logo: header, letterhead, email signature"),
           ("two-lines-left", "Two lines, mark left", "narrow headers, social profiles"),
           ("two-lines-right", "Two lines, mark right", "the name leads, the mark closes"),
           ("stacked", "Stacked", "footer, covers, posters"),
           ("wordmark", "Wordmark alone", "where the mark is already nearby")]
PX = [512, 256, 128, 96, 64, 48, 32, 24, 16]


def logos(sets, style):
    L = "/system/logo/"
    a = lambda h, t: f'<a href="{h}">{t}</a>'
    lock = []
    for k, n, use in LOCKUPS:
        plates = []
        for w, wn, g, on in WAYS:
            f = f"{L}lockups/seeds-logo-{k}-{w}"
            plates.append(f'<figure class="sg-lp"><div class="sg-la {g}"><img src="{f}-1200.png" alt="{n} logo, {wn.lower()}" loading="lazy"></div>'
                          f'<figcaption><b>{wn}</b><span>{on}</span><span class="sg-lfiles">{a(f + ".svg", "SVG")}{a(f + "-1200.png", "PNG 1200")}{a(f + "-2400.png", "PNG 2400")}</span></figcaption></figure>')
        lock.append(f'<h3 class="sg-label">{n} <span class="sg-muted">· {use}</span></h3><div class="sg-lgrid wide">{"".join(plates)}</div>')
    marks = "".join(f'<figure class="sg-lp"><div class="sg-la {g}"><img src="{L}mark/seeds-mark-{w}.png" alt="The mark, {wn.lower()}" loading="lazy"></div>'
                    f'<figcaption><b>{wn}</b><span>{on}</span><span class="sg-lfiles">{a(f"{L}mark/seeds-mark-{w}.svg", "SVG")}{a(f"{L}mark/seeds-mark-{w}.png", "PNG 1130")}</span></figcaption></figure>'
                    for w, wn, g, on in WAYS)
    sizes = []
    for w, wn, g, _ in WAYS:
        figs = []
        for px in PX:
            f = f"{L}mark/sizes/seeds-mark-{w}-{px}"
            show = f"{f}@2x.png" if px <= 128 else f"{f}.png"
            d = min(px, 256)
            figs.append(f'<figure><a href="{f}.png"><img src="{show}" width="{d}" height="{d}" alt="{wn} mark at {px} px" loading="lazy"></a><figcaption>{a(f + ".png", f"{px} px")}</figcaption></figure>')
        sizes.append(f'<h3 class="sg-label">{wn}</h3><div class="sg-sizes {g}">{"".join(figs)}</div>')
    body = f'''<style>{style}</style>
<div class="sg" data-sg="logos">
<div class="sg-in">
<header class="sg-head">
<nav class="sg-crumbs sg-label" aria-label="Breadcrumb"><a href="/graphics">Graphics</a> · Brand marks</nav>
<h1>Logo files</h1>
<p class="sg-lede">Every version of the logo, shown on the ground it is made for, with its files: SVG for any size, PNG with a transparent background.</p>
<dl class="sg-facts"><dt>Rules</dt><dd>Where it goes and how big: <a href="/logo">logo</a>. All files and how they are rebuilt: <code>system/logo/</code>.</dd>
<dt>Colourways</dt><dd><b>Colour</b> on white, paper or pale yellow. <b>Colour, dark</b> (white bird and name) on night and dark photographs. <b>Black</b> and <b>white</b> where colour fights the page; both also work on the logo red. <b>Red</b> on light grounds.</dd></dl>
</header>
<section class="sg-lg"><h2>Mark and name</h2><p>The horizontal lockup is the main logo. The others are for spaces it doesn't fit.</p>{"".join(lock)}</section>
<section class="sg-lg"><h2>The mark</h2><p>The swallow in its ring of fingerprints, on its own. PNG at 1130 px.</p><div class="sg-lgrid">{marks}</div></section>
<section class="sg-lg"><h2>The mark at every size</h2><p>The same full mark, drawn for each size, shown at real size. Use these for avatars and icons rather than shrinking the big file. Each size links to its PNG; <code>@2x</code> files (up to 128 px) are in the same folder. Favicon: <a href="{L}favicon.ico">favicon.ico</a>.</p>{"".join(sizes)}</section>
<nav class="sg-sets" aria-label="All graphics">{sets_nav(sets)}</nav>
</div>
</div>'''
    (ROOT / "logos.md").write_text('---\ntitle: "Logo files"\ndescription: "Every Seeds of Renaissance logo file, on the ground it is made for: five colourways, five lockups, the mark at every size."\nlayout: plain\n---\n'
                                   "<!-- GENERATED by system/build-galleries.py. Edit the logo tables there. -->\n" + flat(body) + "\n")


if __name__ == "__main__":
    sets = {n: load(n) for _, _, _, names in FAMILIES for n in names}
    shell = (G / "gallery-shell.html").read_text()
    style = css()
    for s in sets.values():
        out = gallery(s, sets, shell, style)
        print(f'{out.relative_to(ROOT)}: {len(s["elements"])} elements, {out.stat().st_size // 1024} KB')
    hub(sets, style)
    logos(sets, style)
    print("graphics.md (cards, rules) and logos.md")
