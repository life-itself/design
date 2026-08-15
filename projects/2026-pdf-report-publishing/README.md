# PDF report publishing — pipeline prototype

First pass at the "Markdown → elegant PDF" workflow tracked in
[life-itself/community#1269](https://github.com/life-itself/community/issues/1269)
and [rufuspollock/planning: 2026-pdf-report-publishing-from-markdown](https://github.com/rufuspollock/planning/blob/main/projects/2026-pdf-report-publishing-from-markdown.md).
Not a spec — a working build to see what each toolchain actually produces.

## Sample document

[`life-itself/2rbook`](https://github.com/life-itself/2rbook)'s `what-is-2r/essay.md`
— the "What is the Second Renaissance?" essay (~8,900 words, 12 sections + appendix).
Chosen because it's short-ish, representative, and — usefully — a real
Google-Docs export: escaped punctuation, a manual hyperlinked TOC, stray
empty heading page-breaks. Exactly the messy input the real pipeline has to
handle, not a clean hand-written Markdown file.

## What's here

```
source/               cleaned Markdown + copied image assets (input to both pipelines)
scripts/clean.py       Google-Docs-export -> clean Markdown (strips manual TOC,
                        un-escapes \. \- etc., drops empty page-break headers)
pandoc-latex/          Pandoc -> custom LaTeX template -> Tectonic -> PDF
typst/                 Pandoc -> Typst markup -> custom Typst template -> PDF
output/                built PDFs (both pipelines, gitignored — see below)
```

Run `pandoc-latex/build.sh` or `typst/build.sh` to rebuild. Both read from
the same `source/what-is-2r.md`.

## Toolchain (installed to `~/tools`, not system packages)

- **Pandoc 3.9** — Markdown → LaTeX or → Typst markup
- **Tectonic 0.15** — self-contained LaTeX engine (downloads its package
  bundle on first run instead of needing a multi-GB TeX Live install)
- **Typst 0.15** — native typesetting language + compiler, single binary

## Brand

No style guide exists yet (that's [#1276](https://github.com/life-itself/community/issues/1276),
still open). Palette and type treatment here are reverse-engineered from
`2rbook/assets/whitepaper-1-cover.webp` — the reference cover Rufus already
has in mind — and the Life Itself logotype: cream `#FFFFE3`, ink `#191512`,
gold `#B99A54`, sage `#445328`. Fonts are Liberation Serif / Liberation Sans
(only decent metric-compatible faces available in this sandbox — no network
access to Google Fonts from here). Swapping in real brand fonts (e.g. a serif
closer to the "Life Itself" wordmark) is a five-minute change once chosen —
one line in each template.

## Pandoc+LaTeX vs Typst — first impressions

Both produced a genuinely presentable report on the first real attempt, cover
included. Neither is a finished template — this is "does the workflow work
end to end", not "is the design done".

**Typst**
- Much faster to iterate: sub-second recompiles, clear error messages with
  source locations, no TeX package-download purgatory.
- Styling is direct: `show` rules for headings/images/emphasis read like
  normal code, not macro archaeology.
- Smaller ecosystem — fewer existing citation/bibliography styles, less
  prior art to copy from than LaTeX.
- 34 pages for this essay (looser default leading/spacing than the LaTeX run).

**Pandoc + LaTeX (Tectonic)**
- More ceremony (fontspec/titlesec/fancyhdr/hyperref plumbing) but it's the
  well-worn path — footnotes, bibliographies (biblatex), print-on-demand
  trim sizes, index generation all have mature, documented support if the
  reports need them later.
- Tectonic sidesteps the classic "install 4GB of TeX Live" pain — it fetches
  only the packages actually used, once, then caches them.
- 23 pages for the same content (denser default spacing).
- First build hit two real gremlins any custom template will hit:
  `\tightlist` undefined (pandoc emits it for every list, template must
  define it) and a Unicode arrow glyph missing from Liberation Serif —
  both easy fixes once you know to expect them.

**Read on this sample:** Typst is the faster path to a good-looking,
maintainable template, especially since Sylvie/other non-technical
collaborators are in scope — Typst's error messages and syntax are more
approachable than LaTeX's if anyone needs to touch the template. LaTeX earns
its keep if/when the reports need heavyweight bibliography management or
print-on-demand-specific packages. Worth prototyping a second, denser
source (more tables/citations) before deciding — this essay has no tables,
footnotes, or citations to stress-test either pipeline.

## Known gaps / next steps

- Fonts are placeholder system fonts, not final brand fonts.
- No Google Docs → Markdown step exercised yet (source was already
  Markdown) — that's the other half of the real pipeline and its own
  source of lossiness (esp. tables/footnotes/comments).
- No footnotes, tables, or bibliography in this sample essay — untested in
  both templates.
- `clean.py` is specific to this one export's quirks; a real pipeline needs
  a more general Google-Docs-export cleaner.
- Print-on-demand trim size / bleed not addressed (currently A4 for
  on-screen reading).
