# Building with the SoR design system

**Start here** if you are making a new page, thumbnail or slide for Seeds of Renaissance, whether you are a person or an AI agent. Read this file, copy the closest example, then build. Detail lives in the topic pages linked below; you rarely need them for a first draft.

## The brief in one paragraph

The feel is **grounded hope**: ink and paper, a little off-centre, with the hand visible (paper grain, torn edges, woodcut seeds and swallows). Pages are mostly white, paper and ink, and colour comes from photographs. Buttons are black. The logo red is only for an occasional link in running text. Pale yellow is a background, never text or highlight. One night section per page, plus the footer, meeting the light at a torn edge. Headings are Polyamine, reading is Bricolage Grotesque, labels are small uppercase Apfel Grotezk, and the poetic voice is a soft italic serif.

## How to build a page

1. **Pick the closest example** and copy it:

   | Making… | Copy |
   |---|---|
   | A landing or home page | [examples/web/home.html](examples/web/home.html) |
   | A long text (manifesto, essay) | [examples/web/manifesto.html](examples/web/manifesto.html) |
   | An events or community page | [examples/web/gatherings.html](examples/web/gatherings.html) |
   | A sign-up or "how to join" page | [examples/web/join.html](examples/web/join.html) |
   | A publication page (magazine, podcast) | [examples/web/magazine.html](examples/web/magazine.html) |
   | A research paper | [examples/web/white-paper.html](examples/web/white-paper.html) |
   | A YouTube thumbnail | [examples/youtube/index.html](examples/youtube/index.html) |

2. **Keep the shell**: the `<head>` links, `<body class="sor">`, `graphics.js` first in the body, `sor.js` last, the site header and footer.

3. **Compose sections from the menu below.** Each section is a full-width ground with the page gutter. Use only classes from `system/components.css`. If you need something the system lacks, add it to `system/components.src.css` (token-based, no page-specific colours), run `python3 system/build-css.py`, and say so.

4. **Write real copy.** Use [../2026-sor-website/brand.md](../2026-sor-website/brand.md) for who we are, what we offer and how we sound; real page copy is in [../2026-sor-website/content/](../2026-sor-website/content/).

5. **Check against the list** at the bottom before you call it done.

## The page shell

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Page name · Seeds of Renaissance</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700&family=Hanken+Grotesk:wght@400;500;700&family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..500,100;1,9..144,300..500,100&display=swap">
<link rel="stylesheet" href="system/fonts.css">
<link rel="stylesheet" href="system/tokens.css">
<link rel="stylesheet" href="system/components.css">
</head>
<body class="sor">
<script src="system/graphics.js"></script>   <!-- woodcut symbols -->

<header class="site-header gutter">…</header>
<section class="section gutter ground-white">
  <span class="label">Section name</span>
  …
</section>
…
<footer class="site-footer gutter"><span class="tear"></span>…</footer>

<script src="system/sor.js"></script>
</body>
</html>
```

Adjust the `system/` paths to where the page sits. Woodcuts are inline SVG: `<svg class="seed-icon" viewBox="0 0 100 100" aria-hidden="true"><use href="#s-bean"/></svg>`.

## Section menu

| Section | Class | Ground | Use for |
|---|---|---|---|
| Header | `.site-header` (or `--centred` over a photo hero) | paper | every page |
| Photo hero | `.hero-photo` | photograph, torn white edge | the one statement of a landing page |
| Split hero | `.hero-split` + `.print` | sunlight | when there's no strong landscape photo |
| Page title | `.page-hero` | sunlight | inner pages: title, dedication, a plate |
| Statement | `.statement` | white | what we believe, a short manifesto paragraph |
| Pathways | `.pathways` | paper | four ways in, each with its seed |
| Selected work | `.night` + `.selected` | **night** | podcast, essays, art: the page's one deep section |
| Printed object | `.object-feature` | sunlight | magazine, book |
| Calendar | `.calendar` | white | upcoming dates |
| Events | `.events` | paper | gatherings with photos |
| Band | `.band` | sunlight | one call to action across the page |
| Interlude | `.interlude` | sunlight | a single poetic line with a seed cluster |
| Engage | `.engage` | white | newsletter, join, support |
| Long reading | `.reading` (`.drop`, `.pull`, `.verse`, `.litany`) | white | articles, manifesto |
| Footer | `.site-footer` | **night** | every page |

The full list, with HTML to copy, is in [components.md](components.md). See every component rendered in [guide.html](guide.html).

**A typical landing page:** header → photo hero → statement (white) → pathways (paper) → selected work (night) → printed object (sun) → calendar (white) → interlude (sun) → engage (white) → footer.

## Check before you finish

- [ ] Grounds alternate; no two sunlight sections touch; at most one night section plus the footer.
- [ ] Night meets light only through a torn edge (`.tear--top` inside the night section, `.tear--bottom` straight after).
- [ ] Every button is `.btn` or `.btn--solid`. No coloured buttons.
- [ ] Red appears only as `.link` inside running text, at most once a paragraph.
- [ ] No yellow text or highlight. No bright yellow. No gradients except the hero scrim.
- [ ] Polyamine lines are short (about ten words at most). Pull quotes use `.pull` (Restora).
- [ ] Every image is a `<figure>` with `<span class="fig-no">Fig. N</span>` and an italic caption, numbered in order down the page (heroes and pathway cards excepted).
- [ ] Section labels name the section ("Coming up"), not numbers.
- [ ] No page-specific colours or font sizes in inline styles; tokens only.
- [ ] Works at 400px wide with no sideways scroll.
- [ ] Copy is real and in our voice; photos marked as placeholders if not cleared.

## Topic pages

- [feel.md](feel.md): grounded hope, what we are not, the three registers
- [colour.md](colour.md): roles, proportion, do and don't
- [type.md](type.md): the faces, scale, and how to apply them
- [layout.md](layout.md): grounds, rhythm, torn edges, grid and spacing
- [graphics.md](graphics.md): woodcut swallow, seal, seeds and clusters
- [photography.md](photography.md): what to choose and avoid
- [logo.md](logo.md): versions and placement
- [components.md](components.md): every component with HTML
