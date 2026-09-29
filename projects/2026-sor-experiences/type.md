# Type

Choosing the typefaces for the experiences. Frame 2 of [02-dawn](experiences/02-dawn/HANDOFF.md) is the test case, because it holds all the roles at once: a paragraph, a statement, and a small invitation line.

Shared constraints live in [experiences/00-home/common.md](experiences/00-home/common.md#type); this file is the reasoning behind them.

Tracking: beads `design-2pk`.

## Current output

- **[Heading faces](https://claude.ai/artifact/V3NjX27AqKMjKeiwxLSfgR)** — eleven candidates pre-rendered in the real frame, in three groups: a classical set, a weirder set, and commercial faces to look up. Rendered rather than described, so what you see is the real thing.
- Superseded: an interactive comparator with 33 faces and live controls. Too much choice, and a worse tool than the ones that already exist. Kept at [this link](https://claude.ai/artifact/2TkRgn44LBQdLedo1C5cr6), not maintained.

## The roles

| Role | Currently | State |
|---|---|---|
| Display / heading | Polyamine (Italiana fallback) | being chosen now |
| Body / long read | Crimson Text | undecided, waits for the heading |
| Eyebrow / meta | unowned; `system-ui` by default | not yet looked at |
| Illuminated | Cinzel Decorative | separate problem, Book only |

## Decisions

- **Heading first, body second.** The heading is the signature of the frame, and everything else gets judged against it. Body is the more expensive decision long-term, since one face carries all five experiences, but it is the wrong thing to settle first.
- **No bold, no italic in body.** One weight. Emphasis comes from rhythm and space.
- **The single-font plan is dead.** Polyamine was specified for display *and* body; that did not survive contact with 52 characters of running text. Two or three faces, deliberately.
- **Dawn stays black.** Inverting it would remove the ember-to-daylight mechanic, which is the whole frame.
- **The body face must hold on both grounds.** Dawn and the Book are black; Arrival and Flight are white. That is true whatever Dawn does, so it is a real constraint rather than a Dawn one.
- **Consistent system, variable voice.** One body face across the whole series — it is the reader's spine, and changing it per frame reads as broken. The display face may vary per experience, the way a magazine changes its feature openers but never its body text.

## The taste

Worth writing down, because it was not obvious and it redirected the search.

The two faces liked so far are [Polyamine](https://uicreative.net/products/polyamine-modern-classy-serif-font) (a high-contrast display serif with quirks) and [Restora](https://www.myfonts.com/collections/restora-font-nasir-udin) by Nasir Udin (an old-style roman with swashes, stylistic alternates and deliberately imperfect letterforms). Neither is an institutional classic. Both are independent or marketplace-tier, and both are liked *because* they are a bit strange.

So the target is **idiosyncratic display serifs**, not well-drawn historical ones. Cinzel, Italiana and Instrument Serif are the opposite axis and read as classical rather than alive.

Readability of the heading is not a problem — that was checked. Stroke thinning on black is a body-text concern only.

## Where to look

Google Fonts is largely the wrong place for the display face. Better sources:

- Free and open: [Velvetyne](https://velvetyne.fr/) (41 families, much of it genuinely strange), [Collletttivo](https://www.collletttivo.it/), [UNCUT.wtf](https://uncut.wtf/), [Fontshare](https://www.fontshare.com/).
- Commercial, matched to the taste above: Signifier (Klim), GT Sectra (Grilli), Ogg (Sharp), Reckless (Displaay), Swear Display (OH no), Migra (Pangram Pangram), Cardinal Fruit (Blaze), and Nasir Udin's other families.
- [Future Fonts](https://www.futurefonts.xyz/) for typefaces still in progress — cheap, and the best place to find something nobody else is using.

## Note on loading fonts

A published artifact may only pull stylesheets from Google Fonts and font files from Google's CDN; every other host is blocked silently, including jsDelivr for anything that is not a script.

This does **not** limit which faces can be shown. Download the file when building the page and embed it as a base64 data URI, and any face with a public download will render. That is how the Velvetyne and Collletttivo faces appear. The 16MB page limit is not a practical constraint — thirteen embedded faces came to under 600KB.

Velvetyne publishes on GitLab, Collletttivo on GitHub; default branches vary between `master` and `main`.

## Method

Render candidates in the real copy, at the real size, on the real ground, and look at them. Descriptions are unreliable: of a dozen weird faces pulled, one turned out to be a pictogram font, one only applies its effect to lowercase, and one puts a diamond between every word. None of that is visible from a specimen page.

Show a ranked recommendation with reasons rather than a configurator. The decision is a taste decision, and more options make it harder rather than easier.

## Open questions

- Is this type system for the experiences only, or shared with the [main website](../2026-sor-website/)?
- Is "light, widely spaced capitals" a real requirement, or an artefact of Polyamine being the face we happened to start from? The weirder candidates break it deliberately.
- Polyamine has no web font file and is loaded through `local()`, so everyone without it installed sees the fallback. Needs licensing and self-hosting if it stays.
