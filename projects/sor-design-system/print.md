# Print

Papers and essays as printed or PDF documents, and later posters and magazine pages. Part of the [SoR design system](README.md); read [BUILD.md](BUILD.md) first. Status: [examples.md](examples.md#status) · beads `design-34t.22` (papers, done), `design-34t.28` (poster).

**Approved 2026-10-08:** [a paper, page by page](examples/print/index.html) and the [anatomy](#anatomy-of-a-paper) below (`design-34t.22`). Sizes are the `--print-*` tokens in `system/tokens.css`. The Wisdom paper is the first paper built this way; its PDF is published with the paper, not kept here, and rebuilt with `typst/build-paper.sh wisdom` in `pdf-report-publishing`.

## What we need

1. **A paper as PDF** (first): A4 only (decided 2026-10-08, [below](#one-pdf-for-reading-on-screen)). Cover page, contents, running heads, page numbers, headings, footnotes, figures captioned as plates, pull quotes, references, a colophon.
2. **An A3 event poster**.
3. Later: a magazine page or spread, a printed flyer.

## How it's different from the web

- **Fixed sizes in points**, not fluid sizes: a print type scale as `--print-*` tokens (body around 10–11pt Bricolage, headings in Polyamine, pull quotes in Restora, labels in Apfel).
- **Pages**: margins, a baseline rhythm, widows and orphans, page breaks before chapters, figures that don't split.
- **Ink on paper**: paper grain is real on paper, so drop the grain overlay.
- **Woodcuts print beautifully**: use them for the cover and chapter openings.

## Anatomy of a paper

Proposed from the Wisdom paper; mockups of the interior in [examples/print/](examples/print/index.html). In page order. Every part starts on a new page. There is no recto rule and so no blank pages: the paper is one PDF read on screen (decided 2026-10-08, [below](#settled-while-building-the-first-paper)). The *Starts on* column is kept for a printed run.

| Part | Holds | Starts on | Optional |
|---|---|---|---|
| Front cover | Series line, title, subtitle, part line, blurb, authors with the text credit ([below](#covers-and-credits)). By default plain and typographic, ink on paper with a woodcut; a paper with its own art gets a bespoke cover | — | |
| Inside front cover | Blank. Printed runs only; not in the PDF | verso | |
| Title page | Series line, title, subtitle, part line, authors, the Life Itself credit in text. No logo. Quieter than the cover: no art, no blurb | recto (i) | |
| Imprint | On the back of the title page, set small at the foot with the rest left empty: a line about the series, edition and publisher, authors, acknowledgements, credits (figures, woodcuts, typefaces), copyright and licence (CC BY 4.0) in full, how to cite, URL | verso (ii) | |
| Summary | The paper in a few paragraphs | recto | yes |
| Annotated contents | Parts and sections with page numbers, a one-line summary under each section | recto | plain contents if no summaries |
| Preface | Where the paper sits in the series and why it was written | recto | yes |
| Introduction | Unnumbered; first page of arabic numbering | recto (1) | |
| Chapters | Numbered. Opening: number, title, optional epigraph, then the first section with its summary box. Body: running heads, footnotes, figures as plates, pull quotes | recto | epigraph and summary box optional |
| Conclusion | Unnumbered | recto | |
| Further reading | Short annotated list | new page | yes |
| Bibliography | References cited | new page | |
| Appendices | Lettered or numbered, each titled | new page | yes |
| Back cover | The one night: a hook line, about 120 words on what the paper argues (its summary will do), the inverted SoR mark (the seed ring, no disc) with the wordmark, a colophon (series, part, version, year, URL) and the Life Itself Sensemaking Studio logo in its night colours | — | |

One ground throughout the inside: white, unfilled ([below](#one-pdf-for-reading-on-screen)). Polyamine stays for the cover, title page, contents and chapter titles. Inside the text, heads are Restora: sections at 19pt, sub-sections at 14pt medium. Markdown levels map as `##` chapter, `###` section, `####` sub-section.

Running heads: the same on every page, the width of the text column: the paper's title at its left edge, the chapter and folio at its right. No running head on the title page, imprint and openings; openings carry the folio at the foot, at the text's right edge. Prelims numbered in roman, the text in arabic from the introduction.

## One PDF, for reading on screen

Decided 2026-10-08. Each paper ships as **one PDF**, made for reading on screen, which also prints cleanly at home. No separate print edition.

- **White pages, no fill.** A tinted page looks dingy on the grey of a PDF viewer, and at home it prints as a full-page wash inside a white border. The off-white `--paper` is the screen's stand-in for paper; on paper, the stock does that job.
- **Links live and red**, footnotes linked to their notes, the contents linked to the sections, and PDF bookmarks for chapters.
- **A4 only.** Most readers read on screen, where page size doesn't matter, and a reader in the US who prints it chooses "fit to page" and loses about 6% of the size. A Letter edition would double every check for very little. Revisit if a US partner distributes the paper.
- **Covers inside the same file**: the front cover is page one, the night back cover the last page.
- **If we ever print a run**, use the same file on a natural or cream uncoated stock (e.g. Munken Premium Cream) for the warmth, with bleed added for the covers.

## Settled while building the first paper

Decided 2026-10-08, building the Wisdom paper in Typst. The approved mockups didn't settle these, or settled them for print and we changed our minds for the screen.

- **Paragraphs are spaced, not indented**: half a line between them, no first-line indent. Indents are the book convention; spacing suits a sans body read on screen.
- **No recto rule, no blank pages.** Every part starts on a new page.
- **One running-head layout on every page** (above), not mirrored for spreads: on screen there is no outer corner.
- **Figures are cropped to their drawn content** at build time, so the margin a figure carries for sharing alone doesn't push it in from the text edge.
- **Footnotes stay 8/11pt Bricolage** (`--print-note`), numbers in Apfel. 7.5pt was tried and was too small; Apfel is a label face and doesn't read at length.
- **The version** (e.g. 1.0) is in the imprint and the back-cover colophon.

- **Figures sit bare on the page, aligned with the text.** No rules above or below. A figure is the width of the text column and starts at its left edge, so the title drawn into the figure lines up with the prose; then its number and caption.
- **The summary box is drawn fine**: a 0.4pt rule in `--muted`, not 0.6pt ink, so it reads as an aside and not a warning.
- **Long quotations drop a size.** A displayed quotation is Restora italic at 15pt (`--print-quote`); past about 60 words it drops to the epigraph size, 11.5pt.
- **Bricolage gets an oblique for emphasis.** The body face has no italic, but papers use emphasis (titles of works, a stressed word), and the mockups showed the browser's slanted Bricolage. Papers use the same thing, made properly: the upright slanted 11°.
- **Openings carry no running head**, including the contents page (the mockup showed one): only the folio, at the foot.
- **Tables**: 8.5pt between hairlines, header row semibold, no fills.
- **Footnotes are numbered from 1** in each paper, whatever the source document's numbering.
- **Figures carry their own signature** in the image, so the plate doesn't add one.

## Covers and credits

Decided 2026-10-07 ([reasoning](decisions.md#working-through-publication-branding-2026-10-07)). Which mark goes where: [logo.md](logo.md#which-mark-where).

- **Papers are the Seeds of Renaissance series**, numbered on from the Second Renaissance series (*Wisdom and Wanting What's Good* is No. 6).
- **Keep the cover simple.** Let the art carry it. The Wisdom cover (2026-10-08) carries too much: series line, title, subtitle, part line, art, blurb, credit and mark all compete. Its 16:9 social image (art, title, mark) is the better model. Start from art, title, series line and credit; add a subtitle only if the title needs it. Part line and blurb are optional and can move inside.
- **Front cover, top to bottom:** series line ("Seeds *of* Renaissance · White Paper No. 6", small, wordmark face, with "of" in Fraunces italic as in the wordmark); title; subtitle; part line if any ("Wisdom · Part 1", small); cover art at full size; optional one-line blurb, set smaller than the credit; authors with the Life Itself credit in text, on one line at one size; optionally the one-colour mark, small, centred in the bottom margin.
- **On the front, only the one-colour mark** in the cover's ink ([logo.md](logo.md#using-it)), never the red one. The Life Itself logo and the colour mark with its wordmark go on the back cover or colophon.
- **Cover art may bring its own palette** (Wisdom's is blue and gold). The series line takes the cover's ink, not the logo red.
- **Export covers at print resolution**: A4 at 300 dpi is 2480 × 3508 px. Social images are crops made from the art, not the cover itself ([social.md](social.md#rules-for-social)).
- **Figures** carry the signature ([diagrams.md](diagrams.md)), so they stay attributed when shared alone.

## How papers are built

Decided 2026-10-07: papers are rendered with **Typst** in the sibling repo [`pdf-report-publishing`](https://github.com/life-itself/pdf-report-publishing) (bead `prp-4ls`), not with HTML and CSS paged media. Typst handles footnotes, running heads, page breaks and long documents more reliably, and the pipeline already builds the 2R essay.

The whole process, from text to PDF and web page, is in [How we build a paper](publishing.md). This page stays the spec: sizes, faces, covers, figures and the rules above. The Typst `sor` style takes its values from `system/tokens.css`, so change a value here and in the tokens, then rebuild there.

The `--print-*` tokens are approved (2026-10-08). Still to do, when an event needs it (`design-34t.28`): an A3 poster.
