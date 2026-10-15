# Woodcut graphics

Printmade marks, slightly rough at the edge. Black on light grounds, chalk on night. Sometimes printed in one of the three [illustration inks](colour.md#illustration-inks-graphics-only) (blue, deep green, mustard), and the occasional red seed. Part of the [SoR design system](README.md); see them rendered in [guide.html](guide.html#graphics).

<iframe class="specimen" src="specimens/graphics.html" style="aspect-ratio:1000/1200" loading="lazy" title="Graphics, rendered"></iframe>

## Using them

Include `system/graphics.js` at the top of the body; it inlines the symbols. Then:

```html
<svg class="seed-icon" viewBox="0 0 100 100" aria-hidden="true"><use href="#s-wheat"/></svg>
```

Colour follows `currentColor`: the `.woodcut` class sets ink, and inside `.night` it turns chalk.

## The set

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

## Black and red

There is a set in black (ink) and a set in red (`system/woodcuts/seeds-red.svg`, the logo red). Spread them across a page to make it more dynamic and personal: to make a quote stand out, as a background, or to punctuate a section. Red woodcuts are the one place red is used as a graphic rather than a link; keep them occasional.

## Rules

- One graphic moment per section at most. They are punctuation, not wallpaper.
- Don't recolour them beyond black, chalk, the illustration inks and the red set. Don't outline them or add drop shadows.
- One ink per graphic. Two or more on a page is fine if each graphic keeps to one.
- Don't mix in drawn suns or icon-set icons; the sun marks of an earlier version were rejected.

## The wider set

All twenty-four woodcuts (swallows, mountains, leaves, wind, fruit, people in a circle, seeds, leaves in the air, sprouts) are shown on any ground in **[woodcuts.html](woodcuts.html)**. The SVG files, the script that draws them and notes on each are in [system/woodcuts/](system/woodcuts/README.md); any file can be inlined as-is and takes the ink of its ground. Rebuild the page with `python3 system/build-woodcuts.py`. Only the symbols above are in the system sprite so far; add others to `system/graphics.svg` and run `python3 system/build-graphics.py`.

## Animals

Animal woodcuts, linocuts and engravings, cut out of their paper: fox, swan, owls, bear, boar, swallow, hedgehog, snake and more. Each comes in black and the three illustration inks, as an SVG and a transparent 1000px PNG. See every version and open each file in **[the animals gallery](system/animals/gallery.html)**; files, sources and how to add one are in [system/animals/](system/animals/README.md). They follow the same rules as the woodcuts above: one per section at most, punctuation, not wallpaper.

## Mountains

Blue pen, brush and linocut mountains, cut out of their paper: a high peak, a small peak, a peak above mist, a range with contour lines, a 1934 ridge sketch, a brush ridge, and a linocut of peaks over waves (also on its old map). Each comes in the blue it was drawn in, cobalt and black; the linocut also in three lighter blues. See every version in **[the mountains gallery](system/mountains/gallery.html)**; files, colours and how they were made are in [system/mountains/](system/mountains/README.md). A candidate look for a sub-brand.

The drawn blues are an exception for the mountains only (see [colour](colour.md#illustration-inks-graphics-only)): don't retint them in other colours, and don't print other graphics in those blues. Pen and brush drawings are transparent PNGs whose transparency follows the ink, so light hatching stays light; only the linocut has an SVG. Same rules as above: one per section at most.

## Botanicals

Botanical illustrations in colour, cut out of their paper: red alstroemeria, crimson flax, two tulips, spotted and star orchids and a scroll painting of peaches. Seven elements, long side up to 1000px, PNG only (a trace would flatten the washes and hatching). See them in **[the botanicals gallery](system/botanicals/gallery.html)**; files and sources in [system/botanicals/](system/botanicals/README.md). They keep the colours they were painted in: don't retint them (see [colour](colour.md#illustration-inks-graphics-only)).

## Watercolour washes

Loose watercolour and ink washes: a red bloom, green and blue ink washes, blue flowers, a blue ring, a figure in red and in blue, red blooms and a blue handprint. Nine elements, PNG only. The paint is translucent, so each wash takes the colour of its ground: **use them on light grounds** (white, paper, sunlight); on night they mostly disappear. See **[the washes gallery](system/washes/gallery.html)**; files in [system/washes/](system/washes/README.md).

## Geometry

Line figures in black: the exact Metatron's cube (rebuilt from geometry, so its SVG is tiny), the egg of life, a looser Metatron's cube and a seed rosette. Four elements as 1000px PNGs, with SVGs where they are small. They take the ink of their ground like the woodcuts. See **[the geometry gallery](system/geometry/gallery.html)**; files in [system/geometry/](system/geometry/README.md).

## Marks and patterns

Interlaced and knot marks (rings, bands, spirals, a radial wedge spiral, a wave ring), a kolam line pattern and two checkerboards, in black. Eleven elements as 1000px PNGs, with SVGs where they are small and clean (under 150 KB). See **[the marks gallery](system/marks/gallery.html)**; files in [system/marks/](system/marks/README.md).

## Prints

Woodcut, linocut and engraving prints traced from the [woodcuts mood board](moodboard/woodcuts/woodcuts-moodboard.md): pomegranates in black and red, oak leaves and acorns, pinecones, hanging fruit, round flowers, a lily, wildflowers, tulips, a flowering branch, a mountain range with and without a gold sun, and a flock of swallows. Seventeen elements in thirty versions, each as an SVG and a transparent 1000px PNG. See **[the prints gallery](system/prints/gallery.html)**; files, colours and sources in [system/prints/](system/prints/README.md).

They **keep the colours they were printed in** (see [colour](colour.md#illustration-inks-graphics-only)): don't retint them to the illustration inks. They are often used with a transparency over them, which softens both the ink and the colour, so the exact colours matter. How that transparency is applied is not settled yet (Beads `design-34t.52`). Same rules otherwise: one per section at most.

**Rules for these four sets** are the same as for the woodcuts: one per section at most, punctuation, not wallpaper. The geometry and marks are black line work, so don't tint them; the botanicals and washes keep their painted colours and are not retinted. Elements are cropped close to their edges, so add space in the layout instead of expecting it in the file.

**Open:** hand-draw the woodcuts, or base them on public-domain prints?
