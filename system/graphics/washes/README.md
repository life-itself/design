# Watercolour washes

Loose watercolour and ink washes for Seeds of Renaissance, cut out of their paper as transparent PNGs. Made from [[moodboard/botanical-flower-illustration/removal-candidates|the botanical flower mood board]], where each image was cut out, cropped to a tight box and renamed. See also [[animals/README|animals]], [[mountains/README|mountains]] and [[woodcuts/README|woodcuts]].

Gallery with every file and a link to each: [graphics/washes](../../../graphics/washes.md) on the design system site, built with every set by `python3 system/build-galleries.py` from `elements.json` (which also makes the gitignored `thumbs/`).

The paint stays **translucent**: transparency follows the density of the pigment, so each wash takes the colour of its ground. Use them on light grounds (white, paper, sunlight), where the pale areas stay quiet; on night they mostly vanish. PNG only. Painted colours, not retinted. See the colour rule in [[colour#Illustration inks (graphics only)|colour]].

## Elements

In [`elements/`](elements/). Names read `subject-style`. Long side up to 1000px. The green and blue ink washes run off the top and left of their source, so those two edges are straight. Transparent edges are cropped close, with about 2px of margin: add space around them in the layout.

| Name | What it is | Files | Source |
|---|---|---|---|
| `red-watercolour-flower` | Red watercolour flower: A loose red bloom on a thin stem. The washes stay translucent, so it takes the colour of its ground. | PNG | bfi-09 |
| `green-ink-wash` | Green ink wash: Abstract olive and moss green washes with dark pooled edges. Runs off the top and left. | PNG | bfi-14 |
| `blue-watercolour-flowers` | Blue watercolour flowers: Two translucent blue blooms with dark centres and a scatter of ink dots. | PNG | bfi-15 |
| `blue-ink-wash` | Blue ink wash: A deep blue ink bloom with lace-like edges. Runs off the top and left. Typography removed. | PNG | bfi-16 |
| `blue-watercolour-ring` | Blue watercolour ring: A soft blue ring with a halo and brush marks inside, open in the centre. | PNG | bfi-17 |
| `watercolour-figure-red` | Watercolour figure, red: A loose figure in pink-red wash with white gaps where the paper shows. | PNG | bfi-18 |
| `watercolour-figure-blue` | Watercolour figure, blue: The same figure with its colour shifted to blue. | PNG | bfi-18 |
| `red-watercolour-blooms` | Red watercolour blooms: Three red blooms with thin stems and a few drops. | PNG | bfi-19 |
| `blue-handprint` | Blue handprint: Five blue fingertips with a soft glow. Lettering removed. | PNG | bfi-20 |
| `green-watercolour-flower` | Green watercolour flower: A single green flower on a thin stem, in olive and moss washes with a touch of yellow. Signature and date removed. | PNG | bfi-32 |

Source images are `bfi-NN-*` files in the mood board folder (not committed, and not yet cleared for public use). Elements the owner chose not to ship are listed in [[moodboard/botanical-flower-illustration/removal-candidates|removal-candidates]].
