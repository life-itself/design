# Website

Pages for the Seeds of Renaissance website, built in HTML and CSS from the system. Part of the [SoR design system](README.md); read [BUILD.md](BUILD.md) first for the rules that apply everywhere.

Examples: [examples/web/](examples.md#website).

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

2. **Keep the shell**: the `<head>` links, `<body class="sor">`, `graphics.js` first in the body, `sor.js` last, the site header and footer.

3. **Compose sections from the list below.** Each section is a full-width ground with the page gutter. Use only classes from `system/components.css`. If you need something the system lacks, add it to `system/components.src.css` (token-based, no page-specific colours), run `python3 system/build-css.py`, and say so.

4. **Write real copy.** Use [voice.md](voice.md) for how we sound (key lines, button text, titles) and [brand.md](brand.md) for who we are and what we offer; real page copy is in [content/](content/).

5. **Check against the list** at the bottom before you call it done.

## The page shell

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Page name · Seeds of Renaissance</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
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

Google Fonts loads Bricolage Grotesque, plus two fallbacks: Fraunces, for Polyamine and Restora (not yet licensed), and Hanken Grotesk, if Apfel Grotezk fails to load ([type.md](type.md#fallbacks-and-licences)). Adjust the `system/` paths to where the page sits. Woodcuts are inline SVG: `<svg class="seed-icon" viewBox="0 0 100 100" aria-hidden="true"><use href="#s-bean"/></svg>`.

## Sections

Each links to its HTML in [components.md](components.md); see them rendered in [guide.html](guide.html).

- [Header](components.md#site-header) (paper): every page; `--centred` over a photo hero.
- [Photo hero](components.md#photo-hero) (photograph, torn white edge): the one statement of a landing page.
- [Split hero](components.md#split-hero) (sunlight): when there's no strong landscape photo.
- [Page title](components.md#page-title) (sunlight): inner pages.
- [Statement](components.md#statement) (white): what we believe.
- [Pathways](components.md#pathways) (paper): four ways in, each with its seed.
- [Selected work](components.md#selected-work-night) (**night**): the page's one deep section.
- [Printed object](components.md#printed-object) (sunlight): magazine, book.
- [Calendar](components.md#calendar) (white) and [events](components.md#events) (paper): upcoming dates; gatherings with photos.
- [Band](components.md#band) and [interlude](components.md#interlude) (sunlight): one call to action; a single poetic line.
- [Engage](components.md#engage) (white): newsletter, join, support.
- [Long reading](components.md#long-reading) (white): articles, manifesto.
- [Footer](components.md#footer) (**night**): every page.

**A typical landing page:** header → photo hero → statement (white) → pathways (paper) → selected work (night) → printed object (sun) → calendar (white) → interlude (sun) → engage (white) → footer.

## Check before you finish

Everything in [BUILD.md](BUILD.md#check-before-you-finish), plus:

- [ ] Grounds alternate (white default, paper sometimes, sunlight at times); no two sunlight sections touch; at most one night section plus the footer.
- [ ] Torn edges join sections often: always between night and light (`.tear--top` inside the night section, `.tear--bottom` straight after).
- [ ] Every image is a `<figure>` with `<span class="fig-no">Fig. N</span>` and an italic caption, numbered in order down the page (heroes and pathway cards excepted).
- [ ] Section labels name the section ("Coming up"), not numbers.
- [ ] No page-specific colours or font sizes in inline styles; tokens only.
- [ ] Works at 400px wide with no sideways scroll.
