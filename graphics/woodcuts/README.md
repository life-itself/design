# Woodcuts

Graphic elements for Seeds of Renaissance, drawn to look like woodcut or linocut prints: a black shape, white carved lines, and a slightly rough printed edge. See also [[design-system-plan]] and [[moodboard]].

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
| `seeds.svg` | The woodcut seeds and seed clusters (sunflower, bean, maple key, acorn, pumpkin, stone, wheat, dandelion; spiral, scatter, row) |

## Using them

- Every file is a vector SVG with a transparent background, so it sits on white, paper, pale yellow or night.
- The ink colour follows the CSS `color` of the page (`currentColor`), so the same file prints in ink on light grounds or chalk on night.
- The carved lines are real cut-outs, so the background shows through them, as in a print.
- `wc.py` regenerates the set (`python3 wc.py <output folder>`); `sw.json` holds the main swallow's shape.

## Status

First drafts, drawn in code. Strongest: mountain peak, leaves, sprig, fruits, the bold swallow, the circle seen from above. Weakest: the perched swallow reads more like a generic songbird, and the swallow from above is still a little moth-like. For a final set, these could be redrawn by hand or based on public-domain woodcuts and engravings.
