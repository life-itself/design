# How we build a paper

How a Seeds of Renaissance paper goes from finished text to a PDF and a web page. Read this first if you're briefed to build one. Part of the [SoR design system](README.md).

## The aim

A paper should read as typeset and crafted, not word-processed, on paper and on screen. One text, marked once, gives every output: the PDF, the web page, the launch images.

## Three layers and a pipeline

| Layer | Question it answers | Where it lives |
|---|---|---|
| **Design system** | What does it look like? Colours, faces, components, what a pull quote or summary box looks like | This system: [colour](colour.md), [type](type.md), [components](components.md), [diagrams](diagrams.md) |
| **Paper anatomy** | What is a paper made of, and in what order? Title page, imprint, contents, chapters, back matter; how often a pull quote may appear | [print.md](print.md#anatomy-of-a-paper), with [mockups](examples/print/index.html) |
| **Editorial craft** | Given this text, what do we pull out and emphasise? Standfirsts, pull quotes, summary boxes, epigraphs, emphasis | A skill in [`pdf-report-publishing`](https://github.com/life-itself/pdf-report-publishing) (`skills/pdf-report`, step 5) |
| **Pipeline** | How do marked text and a style become a PDF or a page? | Typst, in `pdf-report-publishing` |

Take a pull quote. The design system says how it looks and how often it may appear. The craft says which sentence to pick: verbatim, 12 to 30 words, a claim. The pipeline turns the mark into a page.

## Steps

1. **Final text in Markdown.** One master per paper (for 2R papers, `2rbook/<topic>/essay.md`). Title page fields live only in its front matter.
2. **Editorial pass.** Mark what the text needs to read well. If the authors already marked summaries and quotes, add only the obvious.
3. **Figures.** Redraw in house style and sign them ([diagrams.md](diagrams.md)).
4. **Cover.** Designed separately from the cover art, built as HTML ([print.md](print.md#covers-and-credits)). Promo crops come from the art, not from the cover.
5. **Render.** The PDF follows the anatomy of a paper, in the Typst `sor` style; the cover goes in as page 1. The web page goes on secondrenaissance.net.
6. **Check.** Compare against the anatomy, the mockups and the front matter.

Then publish and announce: for 2R papers, see `2rbook/docs/publishing-a-white-paper.md`.

## Open work

Tracked in beads, not here: `bd list --label area:print` in this repo, `bd ready` in `pdf-report-publishing`.
