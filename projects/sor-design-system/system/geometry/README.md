# Geometry elements

Line geometry for Seeds of Renaissance: sacred-geometry figures as transparent black line work. Made from [[moodboard/botanical-flower-illustration/removal-candidates|the botanical flower mood board]], where each image was cut out, cropped to a tight box and renamed. See also [[animals/README|animals]], [[mountains/README|mountains]] and [[woodcuts/README|woodcuts]].

Gallery with every file and a link to each: `system/geometry/gallery.html` on the design system site (built by `python3 system/build-element-galleries.py` from `elements.json`; it also makes the gitignored `thumbs/`).

Drawn in black ink (`--ink`, `#1b1916`) on a transparent ground. The colour is fixed in the files, so use them on light grounds; they don't turn chalk on night. The Metatron's cube is rebuilt from geometry, so it is exact and its SVG is tiny; the others are traced from small sources. SVGs are kept only where they are small (under 150 KB); the finest line work is PNG only.

## Elements

In [`elements/`](elements/). Names read `subject`. PNGs 1000px on the long side. Transparent edges are cropped close, with about 2px of margin: add space around them in the layout.

| Name | What it is | Files | Source |
|---|---|---|---|
| `metatron-cube` | Metatron’s cube: The full cube: thirteen circles joined by every line between their centres, in even black lines. Rebuilt from geometry, so it is exact. | PNG, SVG | bfi-07 |
| `egg-of-life` | Egg of life: Seven circles around a central one. | PNG, SVG | bfi-13 |
| `metatron-cube-circles` | Metatron’s cube with circles: Metatron’s cube drawn with its circles, for a looser look than the exact one. | PNG, SVG | bfi-13 |
| `seed-rosette` | Seed rosette: Overlapping circles forming a rosette. PNG only: a trace of the fine lines is heavier than the image. | PNG | bfi-11 |

Source images are `bfi-NN-*` files in the mood board folder (not committed, and not yet cleared for public use). Elements the owner chose not to ship are listed in [[moodboard/botanical-flower-illustration/removal-candidates|removal-candidates]].
