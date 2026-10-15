# Woodcuts

Graphic elements for Seeds of Renaissance, drawn to look like woodcut or linocut prints: a black shape, white carved lines, and a slightly rough printed edge. See also [[design-system-plan]] and [[moodboard]].

Gallery with every file and a link to each: [graphics/woodcuts](../../../graphics/woodcuts.md) on the design system site, built with every set by `python3 system/build-galleries.py` from `elements.json` (which also makes the gitignored `thumbs/`).

![[preview-1.png]]
![[preview-2.png]]

## Files

| File | What it is |
|---|---|
| `swallow-flight.svg` | The main woodcut swallow, side view in flight (used on the website mockups) |
| `swallow-above.svg` | Swallow seen from above, wings spread |
| `swallow-perched.svg` | Swallow perched on a branch |
| `swallow-bold.svg` | The main swallow as a bold linocut with a few strong cuts |
| `mountain-peak.svg` | A single snow peak |
| `mountain-range.svg` | A range of peaks with mist |
| `mountain-moon.svg` | A mountain with a rising moon |
| `leaf-single.svg` | A leaf with its veins |
| `leaf-ginkgo.svg` | A ginkgo leaf |
| `leaf-sprig.svg` | A stem with five leaves |
| `wind-gusts.svg` | Curling gusts of wind |
| `wind-leaves.svg` | Wind carrying leaves |
| `fruit-apple.svg` | Apple with a leaf |
| `fruit-pear.svg` | Pear |
| `fruit-pomegranate.svg` | Pomegranate cut open, full of seeds |
| `fruit-cherries.svg` | A pair of cherries |
| `circle-of-chairs.svg` | People sitting on chairs in a circle, around a small fire |
| `circle-of-chairs-above.svg` | The same circle seen from above, carved into a dark floor |
| `seeds-red.svg` | The same seeds in the logo and link red (#E5201C) |
| `leaves-rising.svg` | Three leaves rising on the air, large to small, like the swallow flock |
| `leaves-falling.svg` | Five leaves tumbling down, some turned edge-on |
| `sprout-from-soil.svg` | A sprout breaking out of a mound of soil, with the seed, roots and buried shoot carved into it |
| `sprout-growing.svg` | The same sprout growing in five stages: seed, hooked shoot, closed leaves, open leaves, first true leaves |
| `seeds.svg` | The woodcut seeds and seed clusters (sunflower, bean, maple key, acorn, pumpkin, stone, wheat, dandelion; spiral, scatter, row) |

## Elements from the woodcuts mood board

The elements traced from [[moodboard/woodcuts/woodcuts-moodboard]] are now their own set: [[../prints/README|system/graphics/prints/]].

## Using them

- Every file is a vector SVG with a transparent background, so it sits on white, paper, pale yellow or night.
- The ink colour follows the CSS `color` of the page (`currentColor`), so the same file prints in ink on light grounds or chalk on night.
- The carved lines are real cut-outs, so the background shows through them, as in a print.
- The SVGs are in `elements/`, with black and white PNGs of the swallows. `wc.py` regenerates the set (`python3 wc.py elements`); `sw.json` holds the main swallow's shape.
- `swallow-flight.svg` is older: its cuts are drawn in paper colour (`#fbfaf6`) on a paper rectangle, so it needs a light ground. `seeds.svg` and `seeds-red.svg` also carry a paper rectangle behind them.

## Which to use

Drawn in code. The strongest are the mountain peak, the leaves, the sprig, the fruits, the bold swallow and the circle seen from above. The perched swallow reads more like a generic songbird and the swallow from above is a little moth-like: prefer the flight or bold swallow.
