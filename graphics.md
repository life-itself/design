# Graphics

Printmade marks, slightly rough at the edge: woodcuts, animals, mountains, botanicals, washes, geometry, marks and prints. The woodcuts are black on light grounds, chalk on night, sometimes printed in one of the three [illustration inks](colour.md#illustration-inks-graphics-only) (blue, deep green, mustard), with the occasional red seed. Part of the [SoR design system](README.md); see them rendered in [guide.html](guide.html#graphics).

<iframe class="specimen" src="specimens/graphics.html" style="aspect-ratio:1000/1200" loading="lazy" title="Graphics, rendered"></iframe>

## The sets

| Set | What | Colours | Formats | Rights | Gallery |
|---|---|---|---|---|---|
| [Sprite](#the-sprite) | Swallow, seal, seeds and seed clusters | Ink of the ground; red seeds | Inline SVG symbols | Ours | [woodcuts.html](woodcuts.html) |
| [Woodcuts](#woodcuts) | 24 woodcuts: swallows, mountains, leaves, wind, fruit, people in a circle, seeds, sprouts | Ink of the ground; red seeds | SVG | Ours (drawn in code) | [woodcuts.html](woodcuts.html) |
| [Animals](#animals) | 21 animals: fox, swan, owls, bear, boar, swallow, hedgehog, snake, butterflies and more | Black and the three illustration inks | SVG and PNG | Not cleared | [animals](system/animals/gallery.html) |
| [Mountains](#mountains) | 8 pen, brush and linocut mountains | Drawn blues, cobalt, black | PNG; the linocut also SVG | Not cleared | [mountains](system/mountains/gallery.html) |
| [Botanicals](#botanicals) | 7 botanical illustrations | As painted | PNG | Not cleared | [botanicals](system/botanicals/gallery.html) |
| [Washes](#watercolour-washes) | 10 watercolour and ink washes | As painted, translucent | PNG | Not cleared | [washes](system/washes/gallery.html) |
| [Geometry](#geometry) | 4 line figures | Black (`--ink`) | PNG; SVG where small | Not cleared | [geometry](system/geometry/gallery.html) |
| [Marks](#marks-and-patterns) | 13 knot and interlaced marks, a kolam, two checkerboards | Black (`--ink`) | PNG; SVG where small | Not cleared | [marks](system/marks/gallery.html) |
| [Prints](#prints) | 17 prints in 30 versions: fruit, oak and acorns, pinecones, flowers, a mountain range, swallows | As printed | SVG and PNG | Not cleared; some drafts | [prints](system/prints/gallery.html) |

**Not cleared** means traced or cut from mood board images whose rights are not cleared: fine for mockups and drafts; redraw, re-source or clear them before anything goes public. Which colours each set may use: [colour.md](colour.md#which-colours-each-graphic-set-may-use).

## Rules for every set

- One graphic moment per section at most. They are punctuation, not wallpaper.
- Don't recolour them beyond what the set allows (above). Don't outline them or add drop shadows.
- One ink per graphic. Two or more on a page is fine if each graphic keeps to one.
- Don't mix in drawn suns or icon-set icons.
- Elements are cropped close to their edges, so add space in the layout instead of expecting it in the file.

## The sprite

Include `system/graphics.js` at the top of the body; it inlines the symbols. Then:

```html
<svg class="seed-icon" viewBox="0 0 100 100" aria-hidden="true"><use href="#s-wheat"/></svg>
```

Colour follows `currentColor`: the `.woodcut` class sets ink, and inside `.night` it turns chalk.

| Symbol | viewBox | Use |
|---|---|---|
| `#wsw` | 0 0 248 150 | The swallow. Single, or three in flight as a flock over a hero (`.flock`, see home.html). |
| `#seal` | 0 0 120 120 | Swallow seal. Closes a long text (`.seal`), or sits in the corner of the night section (`.seal-corner`). |
| `#s-sunflower` | 0 0 100 100 | Seed: **Gather** |
| `#s-wheat` | 0 0 100 100 | Seed: **Practise** |
| `#s-bean` | 0 0 100 100 | Seed: **Belong** |
| `#s-samara` | 0 0 100 100 | Seed (maple key): **Seed / Gardens of Change** |
| `#s-acorn`, `#s-pumpkin`, `#s-stone`, `#s-dandelion` | 0 0 100 100 | Other seeds, free to use |
| `#c-spiral` | 0 0 200 200 | Sunflower spiral, behind a page title (`.page-hero .spiral`) |
| `#c-scatter` | 0 0 280 170 | A handful scattered, above an interlude |
| `#c-row` | 0 0 290 120 | A sown row, as a divider (`.seed-row`) |

The four pathway seeds stay attached to their pathways everywhere: site, thumbnails, slides.

### Black and red

There is a set in black (ink) and a set in red (`system/woodcuts/seeds-red.svg`, the logo red). Spread them across a page to make it more dynamic and personal: to make a quote stand out, as a background, or to punctuate a section. Red woodcuts are the one place red is used as a graphic rather than a link; keep them occasional.

## Woodcuts

All twenty-four woodcuts are shown on any ground in **[woodcuts.html](woodcuts.html)**. The SVG files, the script that draws them and notes on each are in [system/woodcuts/](system/woodcuts/README.md); any file can be inlined as-is and takes the ink of its ground. Rebuild the page with `python3 system/build-woodcuts.py`. Only the symbols above are in the sprite; to add others, put them in `system/graphics.svg` and run `python3 system/build-graphics.py`.

## Animals

Animal woodcuts, linocuts and engravings, cut out of their paper. Each comes in black and the three illustration inks, as an SVG and a transparent 1000px PNG; the snake and the butterflies also in their original colours, PNG only. Files, sources and how to add one: [system/animals/](system/animals/README.md).

## Mountains

Blue pen, brush and linocut mountains, cut out of their paper: a high peak, a small peak, a peak above mist, a range with contour lines, a 1934 ridge sketch, a brush ridge, and a linocut of peaks over waves (also on its old map). Each comes in the blue it was drawn in, cobalt and black; the linocut also in three lighter blues. A candidate look for a sub-brand. Files, colours and how they were made: [system/mountains/](system/mountains/README.md).

The drawn blues are for the mountains only: don't retint them in other colours, and don't print other graphics in those blues. Pen and brush drawings are transparent PNGs whose transparency follows the ink, so light hatching stays light; only the linocut has an SVG.

## Botanicals

Botanical illustrations in colour, cut out of their paper: red alstroemeria, crimson flax, two tulips, spotted and star orchids and a scroll painting of peaches. Long side up to 1000px, PNG only (a trace would flatten the washes and hatching). They keep the colours they were painted in: don't retint them. Files and sources: [system/botanicals/](system/botanicals/README.md).

## Watercolour washes

Loose watercolour and ink washes: a red bloom, green and blue ink washes, blue flowers, a blue ring, a figure in red and in blue, red blooms, a green flower and a blue handprint. PNG only. The paint is translucent, so each wash takes the colour of its ground: **use them on light grounds** (white, paper, sunlight); on night they mostly disappear. Files: [system/washes/](system/washes/README.md).

## Geometry

Line figures in black: the exact Metatron's cube (rebuilt from geometry, so its SVG is tiny), the egg of life, a looser Metatron's cube and a seed rosette. 1000px PNGs, with SVGs where they are small. The files are fixed black (`--ink`), not `currentColor`, so they don't turn chalk on night: **use them on light grounds**, and don't tint them. Files: [system/geometry/](system/geometry/README.md).

## Marks and patterns

Interlaced and knot marks (rings, bands, loops, spirals, a radial wedge spiral, a wave ring, a circle rosette), a kolam line pattern and two checkerboards. 1000px PNGs, with SVGs where they are small and clean (under 150 KB). Like the geometry, fixed black: use them on light grounds, and don't tint them. Files: [system/marks/](system/marks/README.md).

## Prints

Woodcut, linocut and engraving prints traced from the [woodcuts mood board](moodboard/woodcuts/woodcuts-moodboard.md): pomegranates in black and red, oak leaves and acorns, pinecones, hanging fruit, round flowers, a lily, wildflowers, tulips, a flowering branch, a mountain range with and without a gold sun, and a flock of swallows. Each as an SVG and a transparent 1000px PNG. Files, colours and sources: [system/prints/](system/prints/README.md).

They **keep the colours they were printed in**: don't retint them to the illustration inks. They are often used under a transparency, which softens both the ink and the colour, so the exact colours matter; until the method is set, keep the transparency subtle. The gold sun and the pale-yellow branch are kept by choice, though drawn suns and yellow graphics are otherwise out. The oak set, the hanging fruit and the wildflowers are drafts: redraw or re-source them before they go on the live site.

Decisions: [planning 2608](https://github.com/life-itself/planning/blob/main/projects/2608-seeds-of-renaissance-rebrand.md) · [decision log](decisions.md)
