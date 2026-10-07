# Examples

Whole pages and assets built only from the system: the test that the system is complete, and the thing to copy. To make something new, copy the closest example and follow [BUILD.md](BUILD.md). Part of the [SoR design system](README.md).

## Status

✅ done · 🚧 in progress · ⏳ to build. Each kind has a guide (how to make it) and, once built, examples to copy. Detail in beads under `design-34t` (IDs in the last column).

| Kind | What it covers | Guide | Examples | Status | Beads |
|---|---|---|---|---|---|
| **Website** | Pages: home, manifesto, gatherings, join, magazine, white paper | [website.md](website.md) | [below](#website) | ✅ **v0.1 done.** Sylvie's notes (white default, torn edges often) still to apply | `.14` |
| **Social media** | Announcements and posters in 16:9, 4:5, 1:1, 9:16; Instagram, LinkedIn, Substack, link previews, profile banners; the Canva kit | [social.md](social.md) | — | ⏳ **To build**, brief ready | `.15` |
| **YouTube** | Video thumbnails, channel banner, avatar, lower third, watermark | [youtube.md](youtube.md) | [below](#youtube) | 🚧 **First pass done**, polish in progress | `.5` `.6` |
| **Podcast** | Show art (3000²), episode art, the video guest cover | [podcast.md](podcast.md) | guest cover in [examples/youtube/](examples/youtube/index.html) | 🚧 **Stub**; 16:9 guest cover first pass done | `.16` `.8` |
| **Slides** | Talk and workshop decks | [slides.md](slides.md) | — | 🚧 **Brief ready**, in progress | `.12` |
| **Print** | Papers as PDF, A3 posters, later magazine pages | [print.md](print.md) | [below](#print) | ✅ **Papers approved**; Typst build in pdf-report-publishing; A3 poster later | `.22` `.28` |
| **Diagrams** | Figures, charts and frameworks, in papers and shared alone; the signature | [diagrams.md](diagrams.md) | [below](#diagrams) | ✅ **v0.1 done**: signature, type, drawing style, charts with data | `.20` `.25` `.26` |
| **Email** | The Greenhouse newsletter | [email.md](email.md) | — | ⏳ **To build** | `.18` |

Each kind has its own folder under `examples/`.

## Website

Pages for the Seeds of Renaissance website, one per register.

<iframe class="specimen" src="specimens/examples-web.html" style="aspect-ratio:1000/1400" loading="lazy" title="Website examples"></iframe>

| Example | Register |
|---|---|
| [Home](examples/web/home.html) | Landing page |
| [Manifesto](examples/web/manifesto.html) | Long reading |
| [Gatherings](examples/web/gatherings.html) | Events and community |
| [Join](examples/web/join.html) | Joining |
| [Magazine](examples/web/magazine.html) | Publication |
| [White paper](examples/web/white-paper.html) | Research |

## YouTube

Thumbnails, podcast covers and channel art. What we need, what exists and what's next: [youtube.md](youtube.md).

<iframe class="specimen" src="specimens/examples-youtube.html" style="aspect-ratio:1000/522" loading="lazy" title="YouTube examples"></iframe>

- [Thumbnails and podcast covers](examples/youtube/index.html), 1280×720, full size and in a feed.
- [Channel art](examples/youtube/channel.html): banner, avatar, lower third, watermark.

## Diagrams

Figures and frameworks, signed so they stay attributed when shared alone. Rules: [diagrams.md](diagrams.md).

- [The signature](examples/diagrams/index.html) on three real figures from the Wisdom paper and the framework, light and dark, at a 1600px export and at 400px in a feed.
- [Type for diagrams](examples/diagrams/fonts.html): the type scale on two redrawn figures.
- [Drawing style](examples/diagrams/style.html): panels against fine rules, in black and white, at 400px, and in context on a page of the paper and in a web article.
- [Charts with data](examples/diagrams/charts.html): lines, ranked bars, before and after, in the style (illustrative data).
- Built by `examples/diagrams/build.py`.

## Print

The inside of a paper at actual size, from the Wisdom paper, to decide how papers look before the Typst build: [a paper, page by page](examples/print/index.html). A plain typographic front cover, the title page with the imprint at its foot, annotated contents, a body spread (figure as plate, pull quote, footnotes), a chapter opening (epigraph, summary box) and the back cover. The page sequence is in [print.md](print.md#anatomy-of-a-paper). Print it (A4, no margins) for a paper proof. Sizes are the `--print-*` tokens.

## Open across all of them

- **Sub-brands (major).** Are *Over the Mountains*, *Mythos*, the papers, courses, *Gardens of Change* and *The Greenhouse* sub-brands with their own lockups and accents, or Seeds of Renaissance with a label? This shapes podcast, social, print and email. Beads `.11`.
- **Font licences.** Polyamine and Restora must be bought before anything public, PDFs and Canva included. Beads `.2`.
- **Logo.** A small version for avatars and favicons; possibly a redrawn swallow. See [logo.md](logo.md).
- **Photography.** Every photo so far is a placeholder. See [photography.md](photography.md).
