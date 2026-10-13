# Mountains, working record (October 2026)

How the [mountain elements](../../system/mountains/README.md) were made, 12–13 October 2026. Not published. The current set is in `system/mountains/`.

- **Working gallery:** https://claude.ai/artifact/8bus8CMBYwRgsbSvxxJPSJ (Claude artifact; versions 1–5 are the drafts, later versions the built gallery). `gallery-draft.html` is the hand-written draft before the gallery was generated from `elements.json`.
- **Sources:** the original images are on the mood board, `moodboard/mountains/`, entries 01–07.
- **`elements/ridge-1934-pen-note-{blue,cobalt,black}.png`:** the 1934 sketch keeping the handwritten note "26 sept 34, 6h soir, Plateau de Paris". Left out of the main set.
- **`flatten-mask.sh`:** turns a drawing on tinted or unevenly lit paper into an ink mask, by dividing by a blurred local maximum of the red channel.

## Per image

| Entry | Mask | Notes |
|---|---|---|
| 01 high peak | red channel, level 2–92% | White paper, clean. |
| 02 brush ridge | red channel, shave 4px, level 13–88% | Cream paper. Cropped to the ink (the top third is empty paper). |
| 03 grid peak | red channel, level 14–80% | Silhouette from blurred ink density (holes filled), times the ink; straight grid lines found with 60×1 and 1×60 openings and removed only where ink is sparse; the base faded out over 200px, because line removal there also cut real hatching. |
| 04 small peak | `flatten-mask.sh` 6–75% | White paper with a grey vignette. |
| 05 contour range | `flatten-mask.sh` 8–75%, bottom 30px cut | Cream paper, darker bottom edge. |
| 06 1934 ridge | `flatten-mask.sh` 8–65% | Note removed by blacking out the box 905,570–1135,690 of the source. |
| 07 peaks and waves | grey, negate, level 52–85% | Black ink over a map. The sky mask is a flood fill from the top corners, eroded 6px to drop the grey glow of the source's earlier cut-out; the ink is cut to it. SVG: mask ×2, blur 1.5, threshold 50%, `potrace -s -t 6 -a 1.0 -O 0.4`. The map versions keep the source pixels inside the sky mask; the blue one lays `#10248a` over the ink. |

## Decisions

- 13 Oct 2026: keep each drawing's own blue (Sylvie's choice) alongside cobalt and black, mountains only, and no other tints. The tension with the illustration-ink rule is tracked in Beads.
- Pen and brush drawings stay PNG only; the linocut gets SVG too.
