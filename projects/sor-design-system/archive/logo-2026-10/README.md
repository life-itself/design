# Logo, October 2026: how the final mark and lockups were made

The working record behind the logo chosen on 13 October 2026 (Sylvie, with Claude). The result lives in [system/logo/](../../system/logo/README.md) and [the logo files page](../../logos.md); the rules in [logo.md](../../logo.md). Nothing here is current.

## The two working pages (Claude artifacts)

| Page | What it holds | Status |
|---|---|---|
| [Seeds Logo Variants](https://claude.ai/artifact/KckQRr1YDZunWiJZo4Pj9s) | The exploration, in order: three other swallows tried and dropped (an engraving, a photo silhouette, a pencil sketch), rough edges, bigger bird sizes, ways to keep the fingerprints around a bigger bird, the small-size simplification ladder | Record. Local copy: [seeds-logo-variants.html](seeds-logo-variants.html) (the page only; its images are on the artifact) |
| [Seeds Logo Set](https://claude.ai/artifact/2dYhoHf82ntvn2FQWFHcuE) | The chosen mark in every colourway, the lockup bench with live controls for the "of", saved settings ("Final version") | Superseded by logos.md; marked as moved. Local copy: [seeds-logo-set.html](seeds-logo-set.html) |

The earlier comparison of code-drawn woodcut swallows (12 October) is [logo-v2-woodcut-swallows.html](logo-v2-woodcut-swallows.html), moved here from `examples/logo/`.

## What was decided, step by step

1. **New birds tried and dropped.** A public-domain engraving (Rawpixel 6304685), a photo of three swallows and a pencil sketch, each filled solid, mirrored and set in the ring. None beat the original silhouette.
2. **Keep the original swallow, rising left to right**, but break its over-smooth, "commercial" edge. Of five treatments (knife-cut, ink bleed, cut and printed, carved line, grain), **cut and printed** was chosen.
3. **Bird 30% bigger.** Deleting the prints it touched thinned the ring, so the chosen method **pushes those prints out a little and cuts a thin white gap** for the rest. The ring stays as dense as before.
4. **No simplified small versions.** A ladder from 40 prints down to a solid ring was tried for small sizes and rejected: the full mark at every size.
5. **The name:** Polyamine capitals with an italic "of" in Fraunces, tuned toward Polyamine (contrast 101, softness 39, weight 350, 115% of cap height, raised 17%), capitals tracked +20, mark 2.7× cap height with a 0.35× gap. Saved as "Final version" on the Seeds Logo Set page.
6. **Sharp files.** The first exports came from the 600 px `logo.png` and looked soft. The final mark is rebuilt from the 1254 px original (`ref/sor-logo-bird-prints.png`), with the bird traced as a vector. Tracing the fingerprints as vectors was tried and rejected (blotchy ridges).

## Files here

- `build/`: the scripts that make `system/logo/`, in order:
  1. `make_hi.py ../parts/source-logo-600.png ../parts/source-logo-1254.png ../parts/bird-cutprint-2400.png <tmp>`: replays the print layout and traces the bird.
  2. `make_final.py <tmp> ../../../system/logo`: the mark in every colourway, and the parts the next steps use.
  3. `sizes.py ../parts ../../../system/logo/mark/sizes`: every size, and the favicon.
  4. `lockups.py <Polyamine.ttf> <Fraunces-Italic[SOFT,WONK,opsz,wght].ttf> ../parts ../../../system/logo/lockups`.
  `glyphs.py` makes `parts/wordmark-glyphs.json` for the lockup bench. They need Python with numpy, scipy, opencv, Pillow, fonttools, uharfbuzz, potracer and resvg-py; Polyamine installed (unlicensed, `design-34t.2`); Fraunces from Google Fonts (OFL). Rebuilt from scratch on 13 October 2026, identical to the kept files.
- `parts/`: inputs and pieces: the 600 and 1254 px originals, the rough bird mask at 2400 px, the fingerprint layers, the bird path, the Polyamine outlines.
- `exploration/`: the scripts behind the Seeds Logo Variants page (`make.py` to `make8.py`), as run. They read from a scratch folder, so they document the steps more than they rerun.
- `sources/`: the bird images tried (Rawpixel 6304685 is public domain; the other two are of unknown origin, not for use) and the wordmark reference screenshot.
