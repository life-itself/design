# Print

Papers and essays as printed or PDF documents, and later posters and magazine pages. Part of the [SoR design system](README.md); read [BUILD.md](BUILD.md) first. Status: [examples.md](examples.md#status) · beads `design-34t.17`.

**Mockups for approval:** [the Wisdom paper, page by page](examples/print/index.html) (`design-34t.22`). Sizes are drafted as `--print-*` tokens in `system/tokens.css`.

## What we need

1. **A paper as PDF** (first): A4 and US Letter. Cover page, contents, running heads, page numbers, headings, footnotes, figures captioned as plates, pull quotes, references, a colophon.
2. **An A3 event poster**.
3. Later: a magazine page or spread, a printed flyer.

## How it's different from the web

- **Fixed sizes in points**, not fluid sizes: a print type scale as `--print-*` tokens (body around 10–11pt Bricolage, headings in Polyamine, pull quotes in Restora, labels in Apfel).
- **Pages**: margins, a baseline rhythm, widows and orphans, page breaks before chapters, figures that don't split.
- **Ink on paper**: check the logo red and the pale yellow on paper (sunlight may vanish on cheap stock; red may need a CMYK value). Paper grain is real on paper, so drop the grain overlay.
- **Woodcuts print beautifully**: use them for the cover and chapter openings.

## Covers and credits

Decided 2026-10-07 ([reasoning](decisions.md#working-through-publication-branding-2026-10-07)). Which mark goes where: [logo.md](logo.md#which-mark-where).

- **Papers are the Seeds of Renaissance series**, numbered on from the Second Renaissance series (*Wisdom and Wanting What's Good* is No. 6).
- **Front cover, top to bottom:** series line ("Seeds *of* Renaissance · No. 6", small, wordmark face); title; subtitle; part line if any ("Wisdom · Part 1", small); cover art; optional one-line blurb; authors with the Life Itself credit in text.
- **No logo on the front cover** until a one-colour mark exists. The mark and the Life Itself logo go on the back cover or colophon.
- **Cover art may bring its own palette** (Wisdom's is blue and gold). The series line takes the cover's ink, not the logo red.
- **Export covers at print resolution**: A4 at 300 dpi is 2480 × 3508 px. Social images are crops made from the art, not the cover itself ([social.md](social.md#rules-for-social)).
- **Figures** carry the signature ([diagrams.md](diagrams.md)), so they stay attributed when shared alone.

## How papers are built

Decided 2026-10-07: papers are rendered with **Typst** in the sibling repo [`pdf-report-publishing`](https://github.com/life-itself/pdf-report-publishing) (issue [#6](https://github.com/life-itself/pdf-report-publishing/issues/6)), not with HTML and CSS paged media. Typst handles footnotes, running heads, page breaks and long documents more reliably, and the pipeline already builds the 2R essay.

This page stays the spec: sizes, faces, covers, figures and the rules above. The Typst `sor` style takes its values from `system/tokens.css`, so change a value here and in the tokens, then rebuild there.

Still to do here (`design-34t.17`): confirm the drafted `--print-*` tokens once the mockups are approved, check the red and pale yellow on paper, and an A3 poster.
