# Logo

A black swallow in a radiating circle of red fingerprints: many hands around a bird in flight. **Provisional.** Part of the [SoR design system](README.md). Full notes and issues: [logo-notes.md](logo-notes.md).

<iframe class="specimen" src="specimens/logo.html" style="aspect-ratio:1000/262" loading="lazy" title="Logo, rendered"></iframe>

## Terms

- **Mark** (logomark, the stamp): the swallow in fingerprints.
- **Wordmark** (logotype): "Seeds *of* Renaissance" lettered in Polyamine, with "of" as a lowercase italic in Fraunces (light, 300). Polyamine has only capitals and no italic, so a Polyamine "of" (slanted or small) looks wrong (decided 2026-10-08 on the Wisdom cover). Fraunces rather than Restora: its italic "of" looks better in the wordmark (Rufus, 2026-10-08). Fraunces is otherwise only a fallback; this one word is the exception to "four faces only". For display sizes only.
- **Lockup**: mark and wordmark fixed together, as in the site header.
- Below display size, the name is not the wordmark: it is set as text in the system's small face, Apfel Grotezk ([diagrams.md](diagrams.md#the-signature)).

## Using it

- File: `system/img/logo.png` (the current mark). `logo-inverted.png` is a scripted placeholder for dark grounds, used only by the dark diagram signature until the question below is settled (beads `.24`).
- Set it on a **white disc** (`.logo-disc`) or a **white square tile**, so it sits on any ground, including night and sunlight.
- In the header it sits beside the wordmark, set in Polyamine with "of" in Fraunces italic (the site CSS still slants a Polyamine "of"; to update, bead `rbook-8k3.34`):

```html
<a class="wordmark" href="/"><img src="system/img/logo.png" alt=""><span>Seeds <em>of</em> Renaissance</span></a>
```

- In the footer it sits on the white disc above the name.
- Don't recolour it, stretch it, or put it straight onto a photograph without its disc. One exception: the **one-colour mark**, the whole mark in a single ink (the swallow solid, the fingerprints lighter), made by turning darkness into alpha. Approved for covers whose palette the red would fight (2026-10-08). Recipe: an SVG `feColorMatrix` on `logo.png`, rows `0 0 0 0 R / 0 0 0 0 G / 0 0 0 0 B / -0.7 -0.7 -0.7 0 2`, with `color-interpolation-filters="sRGB"` (without it the ink comes out pale). Example: the Wisdom cover, `life-itself/2rbook` `wisdom/cover/cover.html`.

## Which mark where

Seeds is the brand. Life Itself, its steward and the authors' home, is credited in text. At most one logo on any surface. Reasoning: [decisions.md](decisions.md#working-through-publication-branding-2026-10-07).

| Surface | Seeds | Life Itself |
|---|---|---|
| Paper or essay cover | Series line in the wordmark face and the cover's ink, small, at the top: "Seeds *of* Renaissance · White Paper No. 6" (a bare "No. 6" doesn't say what it counts). Optionally the one-colour mark in the cover's ink, small, centred in the bottom margin | Text, one line, one size, with the authors at the foot: "Rufus Pollock & Rosie Bell · Life Itself Sensemaking Studio" |
| Title page | The same series line | The same text credit |
| Back cover, colophon | Mark on its disc with the wordmark | Its logo may appear here |
| Diagram, figure, chart | The signature: the mark (on its disc on light; on dark, see Open item 4), name and URL set in Apfel Grotezk, bottom right inside the margin ([diagrams.md](diagrams.md#the-signature)) | Not shown |
| Social crops of a cover | Mark on its disc, inside the safe area | Not shown; in the caption if needed |

## Open

1. A deeper, ink-like red instead of the clean screen red.
2. A hand-drawn or printmade swallow instead of the stock silhouette.
3. A small version that survives a favicon or YouTube avatar (the fingerprints turn to noise).
4. A full set: colour, one colour (black on light, light on dark; a first one-colour version exists as a filter recipe, see [Using it](#using-it)), inverted, small. Open: on dark grounds, the white-disc cutout or an inverted mark (with red fingerprints the swallow alone reads; the fingerprints may need to go white) (beads `.24`).
