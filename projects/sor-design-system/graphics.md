# Woodcut graphics

Printmade marks, slightly rough at the edge. Black on light grounds, chalk on night. Never coloured, except the occasional red seed. Part of the [SoR design system](README.md); see them rendered in [guide.html](guide.html#graphics).

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
- Don't recolour them, outline them or add drop shadows.
- Don't mix in drawn suns or icon-set icons; the sun marks of an earlier version were rejected.

## The wider set

All twenty woodcuts (swallows, mountains, leaves, wind, fruit, people in a circle, seeds) are shown on any ground in **[woodcuts.html](woodcuts.html)**. The SVG files, the script that draws them and notes on each are in [system/woodcuts/](system/woodcuts/README.md); any file can be inlined as-is and takes the ink of its ground. Rebuild the page with `python3 system/build-woodcuts.py`. Only the symbols above are in the system sprite so far; add others to `system/graphics.svg` and run `python3 system/build-graphics.py`.

**Open:** hand-draw the woodcuts, or base them on public-domain prints?
