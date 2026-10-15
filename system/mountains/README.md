# Mountains

Blue pen, brush and linocut mountains for Seeds of Renaissance, a candidate look for a sub-brand. Each image from [[moodboard/mountains/mountains-moodboard]] is turned into a transparent element: the paper is removed and the ink kept. See also [[animals/README|animals]] and [[woodcuts/README|woodcuts]].

Gallery with every version and a link to each file: https://claude.ai/artifact/8bus8CMBYwRgsbSvxxJPSJ (source: `gallery.html`, built by `python3 build-gallery.py` from `elements.json` and `gallery-shell.html`, which also makes the gitignored `thumbs/`; publish it with `elements/` and `thumbs/`). On the design system site: `system/mountains/gallery.html`.

## Colours

Every mountain comes in **the blue it was drawn in**, **cobalt** (`--print-blue`) and **black** (`--ink`). The drawn blues were chosen by Sylvie to keep each drawing's character, and are used only for the mountains. They sit outside the system's [[colour#Illustration inks (graphics only)|illustration inks]]. The linocut also has three lighter blues for pale grounds and backgrounds. Don't retint them in other colours.

| Colour | Hex | Used on |
|---|---|---|
| Pen blue | `#10248a` | High peak, peaks and waves |
| Violet blue | `#1d14b8` | Small peak |
| Deep blue | `#0b2c8f` | Grid peak |
| Navy | `#14245f` | Contour range |
| Faded blue | `#2e3977` | 1934 ridge |
| Ultramarine | `#0f22b5` | Brush ridge |
| Mid blue, light blue, pale blue | `#2f5bc4`, `#6f93dc`, `#a9c0ea` | Peaks and waves only |
| Cobalt (`--print-blue`) | `#03296f` | All |
| Black (`--ink`) | `#1b1916` | All |

## Elements

In [`elements/`](elements/), named `subject-style-colour`, each a transparent 1000px-wide PNG. The linocut also has a traced `.svg`. Pen and brush drawings are PNG only: their transparency follows the density of the ink, so light hatching and wash stay light, which tracing would flatten into solid shapes.

| Element | What it is | Inks | Source |
|---|---|---|---|
| `high-peak-pen` | Steep single peak with clouds and pines, dense ballpoint hatching | blue, cobalt, black | mood board 01 |
| `small-peak-pen` | Compact peak in quick ballpoint strokes | violet, cobalt, black | mood board 04 |
| `peak-grid` | Tall peak above mist; grid paper removed, base faded out | blue, cobalt, black | mood board 03 |
| `range-contours-pen` | Whole range with contour lines in the sky | navy, cobalt, black | mood board 05 |
| `ridge-1934-pen` | Ridge in parallel hatching, 1934; handwritten note removed | blue, cobalt, black | mood board 06 |
| `ridge-brush` | Loose ridge in brush strokes and wash, cropped to the drawing | ultramarine, cobalt, black | mood board 02 |
| `peaks-waves-linocut` | Linocut peaks over curling waves, ink only (SVG + PNG) | blue, cobalt, black, mid-blue, light-blue, pale-blue | mood board 07 |
| `peaks-waves-linocut-map` | Same linocut keeping the old map, sky removed | blue, black (original print) | mood board 07 |

## Using them

Same rules as the [[graphics|woodcut graphics]]: one per section at most, punctuation, not wallpaper; no outlines or shadows. The busy ones (contour range, grid peak) work best large or as a quiet background.

## How they are made

```bash
magick SOURCE -channel R -separate +channel -negate -level LOW%,HIGH% mask.png
magick mask.png -fill "#10248a" -colorize 100 mask.png -alpha off -compose CopyOpacity -composite PNG32:OUT.png
pngquant --quality 80-100 --speed 1 --strip --force --skip-if-larger --output OUT.png OUT.png
```

The red channel measures how much blue ink is on the paper, so it becomes the alpha; the colour is then flat. On tinted or unevenly lit paper, flatten the paper first (`archive/mountains-2026-10/flatten-mask.sh`). The linocut SVG is traced from the same mask with `potrace` as in `../animals/make-element.sh`. Per-image notes (grid removal, the fade, the caption crop) are in `archive/mountains-2026-10/README.md`.

To add a mountain: put the source on the mood board, cut it as above in the drawn blue, cobalt and black, add a row to `elements.json` and this README, then run `python3 build-gallery.py`.

## Status

Sources are from the web, with no rights cleared. Fine for exploring the sub-brand; re-source or redraw before public use.
