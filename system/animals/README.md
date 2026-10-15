# Animals

Woodcut and linocut animals for Seeds of Renaissance. Each image from [[moodboard/animals/animals-moodboard]] is turned into a transparent element: the paper is removed and the ink kept, then printed in four inks. See also [[woodcuts/README|woodcuts]] and [[mountains/README|mountains]].

Gallery with every version and a link to each file: https://claude.ai/artifact/Kq2WtpebTfHK4mme1m5mov (source: `gallery.html`, built by `python3 build-gallery.py` from `elements.json`, which also makes the gitignored `thumbs/`; publish it with `elements/` and `thumbs/`). On the design system site: `system/animals/gallery.html`. The blue, green and mustard are the system's [[colour#Illustration inks (graphics only)|illustration inks]]: for graphics only, one ink per graphic.

![[preview.png]]

## Elements

In [`elements/`](elements/). Every name has an `.svg` (vector, traced) and a 1000px-wide transparent `.png`. Names read `subject-style-colour`. Parts left uncut in the print (the fox's chest, the swan's feather lines) are transparent, so the ground shows through, as in a print.

| Colour | Hex |
|---|---|
| Black (`--ink`) | `#1b1916` |
| Blue (`--print-blue`) | `#03296f` |
| Deep green (`--print-green`) | `#1f3d2b` |
| Mustard yellow (`--print-mustard`) | `#c9a227` |

| Element | What it is | Source |
|---|---|---|
| `fox-sitting-linocut-{black,blue,green,mustard}` | Fox sitting, looking up | mood board 01 |
| `foxes-walking-engraving-{black,blue,green,mustard}` | Two foxes trotting, fine broken line. Draft: small watermarked source | mood board 02 |
| `swan-wings-open-linocut-{black,blue,green,mustard}` | Swan with wings spread | mood board 03 |
| `bird-flowering-stem-linocut-{black,blue,green,mustard}` | Bird diving with a flowering stem in its beak | mood board 04 |
| `snail-engraving-{black,blue,green,mustard}` | Snail reaching out, fine engraved shell. The source is small, so the finest lines thicken a little | mood board 05 |
| `barn-owl-framed-woodcut-{black,blue,green,mustard}` | Barn owl standing, with its double frame and "H·R" monogram | mood board 06 |
| `barn-owl-woodcut-{black,blue,green,mustard}` | Same owl on its own, frame and monogram removed | mood board 06 |
| `barn-owl-flying-stamp-{black,blue,green,mustard}` | Barn owl in flight seen from above, fine line | mood board 07 |
| `bear-standing-woodcut-{black,blue,green,mustard}` | Bear standing on its hind legs, looking up | mood board 08 |
| `wild-boar-linocut-{black,blue,green,mustard}` | Wild boar trotting, bristly coat in rows of short cuts | mood board 09 |
| `swallow-flight-linocut-{black,blue,green,mustard}` | Swallow swooping, bird only | mood board 10 |
| `swallow-flight-gouges-linocut-{black,blue,green,mustard}` | Same, keeping the gouge marks around it | mood board 10 |
| `hedgehog-curled-linocut-{black,blue,green,mustard}` | Hedgehog curled up asleep, fine sweeping spines | mood board 11 |
| `snake-coiled-watercolour-{black,blue,green,mustard}` | Coiled snake, two-tone: solid scales over a 22% tint of the same ink | mood board 12 |
| `snake-coiled-watercolour-colour` (PNG only) | Same snake in its original watercolour colours, plate number removed | mood board 12 |
| `butterfly-{dark-spotted,swallowtail-striped,pale-tailed,dark-edged,banded,spotted}-photo-{black,blue,green,mustard}` | Six butterflies, each a separate element, printed in three tones of the ink (solid, half and a light tint) | mood board 13 |
| `butterfly-…-photo-original` (PNG only) | Each butterfly in its original greys | mood board 13 |
| `loon-swimming-linocut-{black,blue,green,mustard}` | Loon swimming, with ripples | mood board 14 |

## How they are made

```bash
./make-element.sh SOURCE NAME [threshold%] [crop WxH+X+Y]
```

The paper is flattened (divided by a blurred local maximum) so uneven light does not turn grey (skip this with `NOFLAT=1` for clean white sources with large solid areas, like 04), then thresholded and traced with `potrace` (`brew install potrace`). Solid linocuts suit a threshold around 70–75; thin engraved lines around 65–70.

For a painted or photographic source (not a clean print), use `make-tonal.sh SOURCE NAME [crop] [edge%] [erase boxes]` instead. It keeps the original colours as `NAME-original.png` and prints each ink in three tones. It needs a dark edge round the animal; where a pale edge meets the paper the outline can come out a little ragged (the bottom of the spotted butterfly's hindwings).

To add an animal: put the source in [[moodboard/animals/animals-moodboard]], run `make-element.sh`, check the result on a light ground, add a row to `elements.json` and this README, optimise the PNGs, then run `python3 build-gallery.py`.

PNGs are optimised with `pngquant --quality 80-100 --strip`. They can be regenerated from the SVGs at any time (`magick -background none -density 72 X.svg -trim +repage -resize 1000x PNG32:X.png`). The exception is `snake-coiled-watercolour-colour.png`, which has no SVG and is kept lossless.
