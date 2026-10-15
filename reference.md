---
title: "Reference"
description: "Everything in the Seeds of Renaissance design system, one row each: graphics, logo files, fonts, colours, sizes, components, kits and examples, with where the files are."
---

For when and how to use a thing, follow its link to the rules.

Paths are in the `life-itself/design` repo, inside `projects/sor-design-system/`. The same paths work on this site, after `design.seedsofrenaissance.org/`, except the font files, which are in the repo only.

[Graphics](#graphics) · [Logo](#logo) · [Fonts](#fonts) · [Colours](#colours) · [Type sizes](#type-sizes) · [Spacing](#spacing) · [Fixed sizes](#fixed-sizes) · [Components](#components) · [Kits](#kits) · [Examples](#examples) · [Code](#code)

## Graphics

Each set has a gallery of every file, on each ground it may use, with its path to copy. Rules for using them: [Graphics](graphics.md).

<!-- reference:graphics -->

| Set | Elements | Formats | Rights | Files |
|---|---|---|---|---|
| [Sprite](graphics/sprite.md) | 13 | Inline SVG symbols | Free to use | `system/graphics.svg`, listed in [elements.json](system/graphics/sprite/elements.json) |
| [Woodcuts](graphics/woodcuts.md) | 24 | SVG | Free to use | `system/graphics/woodcuts/elements/`, listed in [elements.json](system/graphics/woodcuts/elements.json) |
| [Animals](graphics/animals.md) | 21 (91 versions) | SVG and PNG | Not cleared: drafts only | `system/graphics/animals/elements/`, listed in [elements.json](system/graphics/animals/elements.json) |
| [Prints](graphics/prints.md) | 17 (30 versions) | SVG and PNG | Not cleared: drafts only | `system/graphics/prints/elements/`, listed in [elements.json](system/graphics/prints/elements.json) |
| [Botanicals](graphics/botanicals.md) | 7 | PNG | Not cleared: drafts only | `system/graphics/botanicals/elements/`, listed in [elements.json](system/graphics/botanicals/elements.json) |
| [Watercolour washes](graphics/washes.md) | 10 | PNG | Not cleared: drafts only | `system/graphics/washes/elements/`, listed in [elements.json](system/graphics/washes/elements.json) |
| [Line figures and marks](graphics/lines.md) | 17 | PNG; SVG where small | Not cleared: drafts only | `system/graphics/lines/elements/`, listed in [elements.json](system/graphics/lines/elements.json) |
| [Mountains](graphics/mountains.md) | 8 (26 versions) | PNG; the linocut also SVG | Not cleared: drafts only | `system/graphics/mountains/elements/`, listed in [elements.json](system/graphics/mountains/elements.json) |

117 elements in 8 sets.

<!-- /reference:graphics -->

## Logo

Every file shown on its ground: [Logo files](logos.md). Which version goes where: [Logo](logo.md). Each version comes in five colourways: `colour`, `colour-dark` (for dark grounds), `black`, `white` and `red`.

<!-- reference:logos -->

| Version | Colourways (SVG) | Formats | Path |
|---|---|---|---|
| Horizontal, the main logo | [colour](system/logo/lockups/seeds-logo-horizontal-colour.svg) · [colour-dark](system/logo/lockups/seeds-logo-horizontal-colour-dark.svg) · [black](system/logo/lockups/seeds-logo-horizontal-black.svg) · [white](system/logo/lockups/seeds-logo-horizontal-white.svg) · [red](system/logo/lockups/seeds-logo-horizontal-red.svg) | SVG; PNG 1200 and 2400px | `system/logo/lockups/seeds-logo-horizontal-<colourway>.svg` |
| Two lines, left | [colour](system/logo/lockups/seeds-logo-two-lines-left-colour.svg) · [colour-dark](system/logo/lockups/seeds-logo-two-lines-left-colour-dark.svg) · [black](system/logo/lockups/seeds-logo-two-lines-left-black.svg) · [white](system/logo/lockups/seeds-logo-two-lines-left-white.svg) · [red](system/logo/lockups/seeds-logo-two-lines-left-red.svg) | SVG; PNG 1200 and 2400px | `system/logo/lockups/seeds-logo-two-lines-left-<colourway>.svg` |
| Two lines, right | [colour](system/logo/lockups/seeds-logo-two-lines-right-colour.svg) · [colour-dark](system/logo/lockups/seeds-logo-two-lines-right-colour-dark.svg) · [black](system/logo/lockups/seeds-logo-two-lines-right-black.svg) · [white](system/logo/lockups/seeds-logo-two-lines-right-white.svg) · [red](system/logo/lockups/seeds-logo-two-lines-right-red.svg) | SVG; PNG 1200 and 2400px | `system/logo/lockups/seeds-logo-two-lines-right-<colourway>.svg` |
| Stacked | [colour](system/logo/lockups/seeds-logo-stacked-colour.svg) · [colour-dark](system/logo/lockups/seeds-logo-stacked-colour-dark.svg) · [black](system/logo/lockups/seeds-logo-stacked-black.svg) · [white](system/logo/lockups/seeds-logo-stacked-white.svg) · [red](system/logo/lockups/seeds-logo-stacked-red.svg) | SVG; PNG 1200 and 2400px | `system/logo/lockups/seeds-logo-stacked-<colourway>.svg` |
| Wordmark, the name alone | [colour](system/logo/lockups/seeds-logo-wordmark-colour.svg) · [colour-dark](system/logo/lockups/seeds-logo-wordmark-colour-dark.svg) · [black](system/logo/lockups/seeds-logo-wordmark-black.svg) · [white](system/logo/lockups/seeds-logo-wordmark-white.svg) · [red](system/logo/lockups/seeds-logo-wordmark-red.svg) | SVG; PNG 1200 and 2400px | `system/logo/lockups/seeds-logo-wordmark-<colourway>.svg` |
| The mark alone | [colour](system/logo/mark/seeds-mark-colour.svg) · [colour-dark](system/logo/mark/seeds-mark-colour-dark.svg) · [black](system/logo/mark/seeds-mark-black.svg) · [white](system/logo/mark/seeds-mark-white.svg) · [red](system/logo/mark/seeds-mark-red.svg) | SVG; PNG 1130px | `system/logo/mark/seeds-mark-<colourway>.svg` |
| The mark drawn for each size | 16, 24, 32, 48, 64, 96, 128, 180, 256, 512, 1024px | PNG; @2x up to 128 | `system/logo/mark/sizes/seeds-mark-<colourway>-<px>.png` |
| Favicon | [favicon.ico](system/logo/favicon.ico) | ICO: 16, 32, 48px | `system/logo/favicon.ico` |

<!-- /reference:logos -->

## Fonts

Four faces. Which one to use: [Type](type.md). Fallbacks: Fraunces for Polyamine and Restora, Hanken Grotesk for Apfel Grotezk, both from Google Fonts.

<!-- reference:fonts -->

| Face | Token and role | Weights | Files | Licence |
|---|---|---|---|---|
| [Polyamine](https://uicreative.net/products/polyamine-modern-classy-serif-font) | `--font-display`: headlines, titles, wordmark: anything up to ~10 words | One weight (Regular) | `Polyamine-Regular.woff2` in `system/fonts/` (repo only) | Commercial, not yet licensed: drafts only. Shows only where installed; elsewhere Fraunces. |
| [Restora](https://www.myfonts.com/collections/restora-font-nasir-udin) | `--font-quote`: display text that runs longer than ~10 words: pull quotes, standout passages; `--font-poem`: the poetic voice: Restora italic | Eight weights, thin to black, with italics | `Restora-ExtraLight.woff2`, `Restora-ThinItalic.woff2` in `system/fonts/` (repo only) | Commercial, not yet licensed: drafts only. Shows only where installed; elsewhere Fraunces. |
| [Bricolage Grotesque](https://fonts.google.com/specimen/Bricolage+Grotesque) | `--font-body`: everything you read | 300 to 700 (variable); light 300 for statements | None in the repo: [Google Fonts](https://fonts.google.com/specimen/Bricolage+Grotesque) | Free (SIL OFL). Loaded from Google Fonts. |
| [Apfel Grotezk](https://www.collletttivo.it/typefaces/apfel-grotezk) | `--font-label`: eyebrows, buttons, dates, captions numbers | Regular 400, Mittel 500, Fett 700 | `ApfelGrotezk-Regular.otf`, `ApfelGrotezk-Mittel.otf`, `ApfelGrotezk-Fett.otf` in `system/fonts/` (repo only) | Free (SIL OFL). Embedded in `system/fonts.css`, so it loads anywhere. |

<!-- /reference:fonts -->

## Colours

From [system/tokens.css](system/tokens.css). Use the token, not the hex, wherever CSS is available. Rules: [Colour](colour.md).

<!-- reference:colours -->

|  | Token | Hex | Group | Use |
|---|---|---|---|---|
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#ffffff;border:1px solid rgb(0 0 0 / .18)"></span> | `--white` | `#ffffff` | Grounds | Pure white sections: openness, the page at its most awake |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#fbfaf6;border:1px solid rgb(0 0 0 / .18)"></span> | `--paper` | `#fbfaf6` | Grounds | The default page: warm near-white |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#fbefc4;border:1px solid rgb(0 0 0 / .18)"></span> | `--sunlight` | `#fbefc4` | Grounds | Pale yellow: background only, never text, never highlight |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#171613;border:1px solid rgb(0 0 0 / .18)"></span> | `--night` | `#171613` | Grounds | At most one night section per page, plus the footer |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#1b1916;border:1px solid rgb(0 0 0 / .18)"></span> | `--ink` | `#1b1916` | Ink | All text on light grounds, and every button |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#5d584f;border:1px solid rgb(0 0 0 / .18)"></span> | `--muted` | `#5d584f` | Ink | Secondary text, captions, labels |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#e0dacf;border:1px solid rgb(0 0 0 / .18)"></span> | `--rule` | `#e0dacf` | Ink | Hairlines on light grounds |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#ece7dc;border:1px solid rgb(0 0 0 / .18)"></span> | `--chalk` | `#ece7dc` | On night | Text on night |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#a49e93;border:1px solid rgb(0 0 0 / .18)"></span> | `--night-muted` | `#a49e93` | On night | Secondary text on night |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#38342e;border:1px solid rgb(0 0 0 / .18)"></span> | `--night-rule` | `#38342e` | On night | Hairlines on night |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#e5201c;border:1px solid rgb(0 0 0 / .18)"></span> | `--red` | `#e5201c` | Accent | The logo red: only an occasional link in running text, and footnote marks |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#03296f;border:1px solid rgb(0 0 0 / .18)"></span> | `--print-blue` | `#03296f` | Illustration inks | Cobalt |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#1f3d2b;border:1px solid rgb(0 0 0 / .18)"></span> | `--print-green` | `#1f3d2b` | Illustration inks | Deep green |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#c9a227;border:1px solid rgb(0 0 0 / .18)"></span> | `--print-mustard` | `#c9a227` | Illustration inks | Mustard yellow |
| <span style="display:inline-block;width:2.2em;height:1.4em;vertical-align:middle;background:#ffffff;border:1px solid rgb(0 0 0 / .18)"></span> | `--print-page` | `#ffffff` | Print | Pages are white, unfilled: the PDF is read on screen, and if printed the stock gives any warmth |

<!-- /reference:colours -->

## Type sizes

Fluid sizes scale with the width of their container (`cqi`) between the smallest and largest values. Print sizes are under [Fixed sizes](#fixed-sizes).

<!-- reference:type -->

| Token | Value | Use |
|---|---|---|
| `--t-hero` | `clamp(40px, 7cqi, 96px)` | One statement per page, 5–10 words |
| `--t-title` | `clamp(40px, 6cqi, 84px)` | Page title on inner pages |
| `--t-section` | `clamp(36px, 5cqi, 64px)` | A section headline |
| `--t-band` | `clamp(30px, 4.4cqi, 56px)` |  |
| `--t-card` | `clamp(24px, 2.5cqi, 32px)` | Card and pathway titles |
| `--t-item` | `26px` | List item titles (calendar, contents) |
| `--t-interlude` | `clamp(26px, 3.4cqi, 42px)` | A poetic line set alone |
| `--t-quote` | `clamp(26px, 3.4cqi, 38px)` | Pull quote |
| `--t-lead` | `clamp(20px, 2.4cqi, 28px)` | Statement paragraphs, light weight |
| `--t-intro` | `clamp(17px, 1.9cqi, 21px)` | Hero standfirst |
| `--t-reading` | `19px` | Long-form article text |
| `--t-body` | `17px` |  |
| `--t-small` | `15px` |  |
| `--t-caption` | `14px` |  |
| `--t-button` | `13px` |  |
| `--t-label` | `12px` |  |
| `--t-meta` | `11px` |  |
| `--lh-display` | `.95` |  |
| `--lh-heading` | `1.1` |  |
| `--lh-body` | `1.55` |  |
| `--lh-reading` | `1.65` |  |
| `--track-label` | `.16em` | Uppercase labels |
| `--track-button` | `.12em` |  |
| `--track-meta` | `.14em` |  |

<!-- /reference:type -->

## Spacing

<!-- reference:spacing -->

| Token | Value | Use |
|---|---|---|
| `--gutter` | `clamp(16px, 4cqi, 56px)` | Page side padding |
| `--section` | `clamp(44px, 7cqi, 96px)` | Vertical padding of a section |
| `--gap-s` | `12px` |  |
| `--gap-m` | `clamp(16px, 2.6cqi, 32px)` | Between cards |
| `--gap-l` | `clamp(24px, 5cqi, 72px)` | Between columns |
| `--measure` | `680px` | Long-form reading width |
| `--tear-height` | `22px` |  |
| `--shadow-print` | `0 18px 40px -22px rgb(27 25 22 / .55)` | A photograph laid on the page |
| `--shadow-object` | `0 30px 50px -30px rgb(27 25 22 / .7)` | A printed object: magazine, book |
| `--tilt` | `1.6deg` | Prints sit slightly off-square |
| `--grain-opacity` | `.14` |  |

<!-- /reference:spacing -->

## Fixed sizes

Thumbnails, channel art and papers are fixed artboards, so their sizes are fixed too: px at the artboard's full size, and pt and mm on paper.

<!-- reference:fixed -->

**Thumbnails**

| Token | Value | Use |
|---|---|---|
| `--thumb-w` | `1280px` |  |
| `--thumb-h` | `720px` |  |
| `--thumb-title-xl` | `110px` | Podcast: short title in the paper column (three lines at most) |
| `--thumb-title-l` | `122px` | Talk: title over a photo |
| `--thumb-title` | `104px` | Gathering: title on the torn white strip |
| `--thumb-title-m` | `96px` | Manifesto: a sentence-length quote |
| `--thumb-byline` | `52px` | "with Guest Name", Polyamine |
| `--thumb-label` | `28px` | Apfel labels: series, date |
| `--thumb-label-s` | `24px` | Footer labels beside the logo |
| `--thumb-meta` | `20px` | Figure number on a photo |
| `--thumb-pad` | `64px` | Outer margin for text |
| `--thumb-inset` | `46px` | Corner inset for logo and marks |
| `--thumb-logo` | `116px` | Logo on white or paper |
| `--thumb-tear` | `34px` | Torn edge depth at artboard scale |

**Podcast guest thumbnail**

| Token | Value | Use |
|---|---|---|
| `--thumb-label-l` | `40px` | A label that must read at feed size: the podcast name |
| `--thumb-name` | `64px` | Guest name, Bricolage semibold |
| `--thumb-guest-w` | `680px` | Width of the greyscale portrait on the right |
| `--thumb-disc` | `92px` | Logo on its white disc, bottom left |

**YouTube channel art**

| Token | Value | Use |
|---|---|---|
| `--yt-banner-w` | `2560px` |  |
| `--yt-banner-h` | `1440px` |  |
| `--yt-strip-h` | `423px` | The desktop strip, full width |
| `--yt-safe-w` | `1546px` | The safe area: what phones show |
| `--yt-avatar` | `800px` |  |
| `--yt-watermark` | `150px` |  |
| `--yt-video-w` | `1920px` |  |
| `--yt-video-h` | `1080px` |  |
| `--yt-wordmark` | `112px` | "Seeds of / Renaissance" on the banner, Polyamine, two lines |
| `--yt-tagline` | `50px` | Banner tagline, the poem voice |
| `--yt-banner-logo` | `236px` | Logo on the banner |
| `--yt-l3-label` | `30px` | Lower third: series label |
| `--yt-l3-name` | `76px` | Lower third: guest name, Polyamine |
| `--yt-l3-role` | `36px` | Lower third: role or one line about the guest |

**Print**

| Token | Value | Use |
|---|---|---|
| `--print-w` | `210mm` | A4. US Letter is 215.9 × 279.4mm with the same margins |
| `--print-h` | `297mm` |  |
| `--print-m-top` | `22mm` | To the top of the text block; running head sits in it |
| `--print-m-bottom` | `26mm` | Folio sits in it |
| `--print-m-inner` | `24mm` |  |
| `--print-m-outer` | `20mm` | Text block 166mm wide at A4: two-thirds of it is the measure |
| `--print-measure` | `118mm` | About 70 characters at body size |
| `--print-margin-col` | `38mm` | Side column beside the measure: notes on figures, pull quotes hang into it |
| `--print-cover-title` | `46pt` | Polyamine, the cover only |
| `--print-title` | `30pt` | Polyamine: cover, title page, contents and chapter titles. Nowhere else inside |
| `--print-h2` | `19pt` | Restora, sentence case: section heads in the run of text (all-caps Polyamine tires at length) |
| `--print-h3` | `14pt` | Restora medium: sub-sections in the run of text |
| `--print-standfirst` | `13pt` | Restora: subtitle, chapter summary |
| `--print-quote` | `15pt` | Restora italic: pull quotes |
| `--print-epigraph` | `11.5pt` | Restora italic |
| `--print-body` | `10.5pt` | Bricolage, light-regular |
| `--print-lh` | `14.5pt` | The baseline: everything sits on multiples of it |
| `--print-summary` | `9.5pt` | Section summary box |
| `--print-caption` | `8.5pt` |  |
| `--print-note` | `8pt` | Footnotes, line height 11pt |
| `--print-label` | `7pt` | Apfel uppercase: running heads, folios, figure numbers, series line |
| `--print-track` | `.16em` |  |

<!-- /reference:fixed -->

## Components

The HTML to copy for each one is in [Components](components.md); all of them rendered in [the whole system on one page](guide.html#components).

<!-- reference:components -->

| Component | Class | When |
|---|---|---|
| [Base and type roles](components.md#base-and-type-roles) | `.sor`, `.gutter`, `.section`, `.ground-white`, `.display`, `.label` and 2 more | Listed in a table on the page |
| [Buttons, links, fields](components.md#buttons-links-fields) | `.btn` | One solid button per section for the main action; outline for secondary actions; `.text-link` inside lists |
| [Site header](components.md#site-header) | `.site-header` | Every page |
| [Photo hero](components.md#photo-hero) | `.hero-photo` | The one statement of a landing page, over a strong landscape photograph |
| [Split hero](components.md#split-hero) | `.hero-split` | A landing page without a strong landscape photo |
| [Page title](components.md#page-title) | `.page-hero` | Inner pages |
| [Statement](components.md#statement) | `.statement` | What we believe |
| [Pathways](components.md#pathways) | `.pathways` | The four ways to take part |
| [Selected work (night)](components.md#selected-work-night) | `.selected` | The page's one deep section: podcast, essays, art |
| [Printed object](components.md#printed-object) | `.object-feature` | The magazine or a book |
| [Calendar](components.md#calendar) | `.calendar` | Upcoming dates, text only |
| [Events](components.md#events) | `.events` | Gatherings with photographs |
| [Band](components.md#band) | `.band` | One call to action across the page, on sunlight |
| [Interlude](components.md#interlude) | `.interlude` | A single poetic line between sections |
| [Engage](components.md#engage) | `.engage` | Newsletter, join, support, near the end of a page |
| [Long reading](components.md#long-reading) | `.reading` | Articles, the manifesto |
| [Contents](components.md#contents) | `.contents` | A magazine's table of contents, or any numbered list of works |
| [Footer](components.md#footer) | `.site-footer` | Every page |
| [More components](components.md#more-components) | `.actions`, `.prints`, `.swallows`, `.table-wrap`, `.hero-banner`, `.steps` and 7 more | Copy the markup from the example pages named |

<!-- /reference:components -->

## Kits

Files ready to drop into Canva or a build, with the steps.

| Kit | What's in it | Path |
|---|---|---|
| [Instagram kit](examples/social/instagram/README.md) | Five post templates, 4:5 and 1:1: backgrounds, the logo lockup, layers, guides and finished examples. [Download all (zip)](examples/social/instagram/sor-instagram-kit.zip) | `examples/social/instagram/png/` |
| [Podcast thumbnail kit](examples/youtube/canva-kit/README.md) | The episode cover for YouTube in Canva: background, layers, guides and positions, 2560 × 1440 | `examples/youtube/canva-kit/png/` |
| [Podcast show art](examples/podcast/README.md) | Show art, episode art ground and guides, 3000 × 3000 | `examples/podcast/png/` |
| [Diagram helpers](diagrams.md) | Python functions for type, panels, arrows and the signature; build a figure as SVG | `examples/diagrams/build.py` |
| [Slide decks](slides.md) | The deck CSS and script, and two decks to copy | `examples/slides/` |
| [Signature](diagrams.md#the-signature) | The mark and URL that sign a figure, light and dark, SVG and PNG | `system/img/signature*.svg` |

## Examples

Whole pages built only from the system, to copy. Grouped with their guides in [Examples](examples.md).

<!-- reference:examples -->

| Kind | Page | Path |
|---|---|---|
| Website | [Gatherings template](examples/web/gatherings.html) | `examples/web/gatherings.html` |
| Website | [Home template](examples/web/home.html) | `examples/web/home.html` |
| Website | [Join template](examples/web/join.html) | `examples/web/join.html` |
| Website | [Magazine template](examples/web/magazine.html) | `examples/web/magazine.html` |
| Website | [Manifesto template](examples/web/manifesto.html) | `examples/web/manifesto.html` |
| Website | [White paper template](examples/web/white-paper.html) | `examples/web/white-paper.html` |
| YouTube | [YouTube thumbnails](examples/youtube/index.html) | `examples/youtube/index.html` |
| YouTube | [YouTube channel art](examples/youtube/channel.html) | `examples/youtube/channel.html` |
| Social | [Instagram Post Templates](examples/social/instagram/index.html) | `examples/social/instagram/index.html` |
| Slides | [Slides](examples/slides/index.html) | `examples/slides/index.html` |
| Slides | [Slides: Gathering](examples/slides/gathering.html) | `examples/slides/gathering.html` |
| Slides | [Slides: Study](examples/slides/study.html) | `examples/slides/study.html` |
| Diagrams | [Diagram examples](examples/diagrams/index.html) | `examples/diagrams/index.html` |
| Print | [Print examples](examples/print/index.html) | `examples/print/index.html` |

<!-- /reference:examples -->

## Code

| File | What | Path |
|---|---|---|
| [tokens.css](system/tokens.css) | Every colour, face, size and space, with its role | `system/tokens.css` |
| [components.css](system/components.css) | Every component (link this one). Readable source: [components.src.css](system/components.src.css) | `system/components.css` |
| [fonts.css](system/fonts.css) | Apfel Grotezk embedded; Polyamine and Restora by name only. Link it, don't read it: it is long | `system/fonts.css` |
| [graphics.svg](system/graphics.svg) | The sprite symbols, for `<use href="#id">`; [graphics.js](system/graphics.js) puts them in a page | `system/graphics.svg` |
| [sor.js](system/sor.js) | Small behaviours: the selected-work picker | `system/sor.js` |
| [The whole system on one page](guide.html) | Every chapter rendered with the real CSS | `guide.html` |
| [Photographs](photography.md) | Mood board placeholders, not cleared for public use | `system/img/*.jpg` |
