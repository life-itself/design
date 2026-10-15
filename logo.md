# Logo

A black swallow rising through a radiating circle of red fingerprints: many hands around a bird in flight. Every file, shown on its ground with links: **[logo files](logos.md)**. Part of the [SoR design system](README.md).

<iframe class="specimen" src="specimens/logo.html" style="aspect-ratio:1000/262" loading="lazy" title="Logo, rendered"></iframe>

## Terms

- **Mark** (logomark, the stamp): the swallow in fingerprints.
- **Wordmark** (logotype): "Seeds *of* Renaissance" lettered in Polyamine, with "of" as a lowercase italic in Fraunces (Polyamine has no lowercase or italic, and Fraunces' "of" reads better than Restora's). This one word is the exception to "four faces only". For display sizes only.
- **Lockup**: mark and wordmark fixed together, as in the site header.
- Below display size, the name is not the wordmark: it is set as text in the system's small face, Apfel Grotezk ([diagrams.md](diagrams.md#the-signature)).

## The logo

- **The mark:** the swallow, rising left to right, with a cut-and-printed edge, a thin white gap around it, and the ring of fingerprints kept full.
- **The full mark at every size.** No simplified small version: the same mark from 16 px up (smaller sizes are drawn for their size, not shrunk).
- **The wordmark:** Polyamine capitals tracked +20 (font units); "of" in Fraunces italic at weight 350, optical size 101, softness 39, 115% of the cap height, raised 17% of the cap height, with 0.8 of a word space on each side. The capitals and "of" are outlines in the files, so no fonts are needed to use them.
- **The horizontal lockup** is the main logo: the mark at 2.7× the cap height, 0.35× cap height from the name. Two-line and stacked lockups are for spaces it doesn't fit.
- **Polyamine is not yet licensed** ([type.md](type.md#fallbacks-and-licences)). The wordmark, files included, needs that licence before public use. Where the wordmark is live text and Polyamine isn't installed, it falls back to Fraunces.

## Files

All in [system/logo/](system/logo/README.md); see them on the **[logo files](logos.md)** page.

| Use | File |
|---|---|
| The main logo | `lockups/seeds-logo-horizontal-<colourway>.svg` (or `-1200.png`, `-2400.png`) |
| Other lockups | `lockups/seeds-logo-{two-lines-left, two-lines-right, stacked, wordmark}-<colourway>` |
| The mark alone | `mark/seeds-mark-<colourway>.svg` / `.png` (1130 px) |
| Avatars, icons | `mark/sizes/seeds-mark-<colourway>-<px>.png`, 16 to 1024 px; `favicon.ico` |
| Pages and code | `mark/sizes/seeds-mark-colour-512.png` (or `-256`), the colour mark; `seeds-mark-colour-dark-<px>.png` on dark grounds |

SVGs scale freely; the fingerprints inside them are sharp up to about 1130 px, enough for screens and A4 print. For anything larger than A4 (posters, banners), ask for the original fingerprint artwork.

## Colourways

| Colourway | Prints, bird, name | Use on |
|---|---|---|
| `colour` | red, black, black | white, paper, sunlight |
| `colour-dark` | red, white, white | night, dark photographs |
| `black` | all black | light grounds, and the logo red; where the red would fight the page |
| `white` | all white | night, the logo red, photographs |
| `red` | all red | light grounds |

On night, use `colour-dark` or `white`; no disc needed.

## Using it

- Use the files as they are. Don't recolour, stretch, rotate or redraw them, or add effects. Choose the colourway for the ground from the table above.
- **Clear space:** at least one cap height of the wordmark on every side, and the same between the logo and the edge of the page or frame.
- **Minimum size:** below about 32 px of mark height, the name can't be read; use the mark alone.
- On a busy photograph, the **white disc** (`.logo-disc`) or a **white tile** is fine.
- In the site header it sits beside the wordmark, set in Polyamine with "of" in Fraunces italic (`.wordmark em` in `components.css`). Match the wordmark settings above, or use the lockup file:

```html
<a class="wordmark" href="/"><img src="system/logo/mark/sizes/seeds-mark-colour-512.png" alt=""><span>Seeds <em>of</em> Renaissance</span></a>
```

- In the footer it sits above the name.
- Use the current files everywhere the mark appears (avatars, watermarks, social and Canva exports); older exports carry the old mark.

## Which mark where

Seeds is the brand. Life Itself, its steward and the authors' home, is credited in text. At most one logo on any surface. Reasoning: [design system plan](https://github.com/life-itself/design/blob/main/projects/sor-design-system/archive/design-system-plan-2026-10.md#working-through-publication-branding-2026-10-07).

| Surface | Seeds | Life Itself |
|---|---|---|
| Paper or essay cover | Series line in the wordmark face and the cover's ink, small, at the top: "Seeds *of* Renaissance · White Paper No. 6" (a bare "No. 6" doesn't say what it counts). Optionally the one-colour mark (`black`, `white` or `red`) in the cover's ink, small, centred in the bottom margin | Text, one line, one size, with the authors at the foot: "Rufus Pollock & Rosie Bell · Life Itself Sensemaking Studio" |
| Title page | The same series line | The same text credit |
| Back cover, colophon | The stacked or horizontal lockup | Its logo may appear here |
| Diagram, figure, chart | The signature: the mark (on its disc on light, `colour-dark` on dark), name and URL set in Apfel Grotezk, bottom right inside the margin ([diagrams.md](diagrams.md#the-signature)) | Not shown |
| Social crops of a cover | The mark, inside the safe area | Not shown; in the caption if needed |

Decisions: [planning 2608](https://github.com/life-itself/planning/blob/main/projects/2608-seeds-of-renaissance-rebrand.md) · [decision log](decisions.md)
