# Print

Papers and essays as printed or PDF documents, and later posters and magazine pages. Part of the [SoR design system](README.md); read [BUILD.md](BUILD.md) first. Status: [applications.md](applications.md) · beads `design-34t.17`.

**Stub, with a brief ready for its own session.**

## What we need

1. **A paper as PDF** (first): A4 and US Letter. Cover page, contents, running heads, page numbers, headings, footnotes, figures captioned as plates, pull quotes, references, a colophon.
2. **An A3 event poster**.
3. Later: a magazine page or spread, a printed flyer.

## How it's different from the web

- **Fixed sizes in points**, not fluid sizes: a print type scale as `--print-*` tokens (body around 10–11pt Bricolage, headings in Polyamine, pull quotes in Restora, labels in Apfel).
- **Pages**: margins, a baseline rhythm, widows and orphans, page breaks before chapters, figures that don't split.
- **Ink on paper**: check the logo red and the pale yellow on paper (sunlight may vanish on cheap stock; red may need a CMYK value). Paper grain is real on paper, so drop the grain overlay.
- **Woodcuts print beautifully**: use them for the cover and chapter openings.

## Brief for a new session

Build print with HTML and CSS paged media, so the same tokens and faces are reused:

1. Add `--print-*` tokens to `system/tokens.css` and a `system/print.css` (`@page` size and margins, running heads and page numbers via margin boxes, footnotes, break rules).
2. Make `examples/print/white-paper.html`: the white paper from [examples/web/white-paper.html](examples/web/white-paper.html) set for print, with a cover. Produce the PDF with a paged-media tool (Paged.js in the browser, or WeasyPrint) and commit both the HTML and a sample PDF.
3. Then an A3 poster: `examples/print/poster.html`.
4. Note any fonts issue: Polyamine and Restora must be installed or licensed for embedding in PDFs (beads `design-34t.2`).

Finish: update this page and [applications.md](applications.md), beads, commit, push, republish.

**Prompt:** *Read projects/sor-design-system/print.md, section "Brief for a new session", and follow it.*
