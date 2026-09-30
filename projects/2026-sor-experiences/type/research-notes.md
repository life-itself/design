# Type research notes

Backup for [../type.md](../type.md), which holds the decisions. This file holds the working: what was looked at, what was rejected and why, where things came from, and the techniques that made the rounds possible.

Two rounds, both September 2026. Every candidate was rendered in the real frame at real size on the real ground before being judged.

## The rounds

| | What | Read it |
|---|---|---|
| **Round one** | Heading and billboard faces. Nineteen candidates. | [artifact](https://claude.ai/artifact/V3NjX27AqKMjKeiwxLSfgR) · [round-01-headings.html](round-01-headings.html) · `build-round-01.py` |
| **Round two** | Body faces, then eyebrow faces. | [artifact](https://claude.ai/artifact/Gr3K5DYxpoB6hP4XZ1nR9L) · [round-02-body.html](round-02-body.html) · `build-round-02.py` |

Superseded, unmaintained: an [interactive comparator](https://claude.ai/artifact/2TkRgn44LBQdLedo1C5cr6) with 33 faces and live controls. Abandoned because it offered choice instead of judgement, and was a worse tool than the ones that already exist. The lesson is in [Method](#method) below.

Both build scripts download their font files at build time and embed them; `fonts/` is a gitignored cache, so a clean checkout rebuilds from nothing.

## What was rejected, and why

Each rejection is quoted, because the phrasing carried more information than a rating would have.

### Round one — headings

| Face | Source | Why not |
|---|---|---|
| Bluu Next | Velvetyne | "A bit boring. Interesting, but not interesting enough." |
| Bagnard | Velvetyne | "More groundedness — but very masculine." In the general direction, but a no against Polyamine or Restora. |
| Cinzel | Google | "Too much like a chiselled monument. Clean, classic Roman." |
| Fraunces | Google | "You can adjust it a great deal… but it does not have real personality. It is nothing new. You do not feel alive." |
| Instrument Serif | Google | "Just a bit boring." |
| Italiana | Google | "Classic and elegant, but with no originality." |
| Coconat Bold | Collletttivo | "It looks fat and heavy. Maybe it has to not be bold." |
| Basteleur Moonlight | Velvetyne | "Too much of a reference to Nordic. It looks like runes… going backwards rather than forwards." |
| Cantique | Velvetyne | "Woo-woo, new-agey." |
| Flor de Ruina | Velvetyne | "It looks like I am in a video game, or a disco ball." |
| Signifier | Klim | "Kind of boring. It could be used for body text." |
| GT Sectra | Grilli Type | "Too cutty, too sharp. Makes you feel you are going to be cut." |
| Ogg | Sharp Type | "Has a bit more to it. But it makes me think newspaper." |
| Reckless | Displaay | "Kind of boring. Does not really have any personality." |
| Migra | Pangram Pangram | "Looks too much like a barber or a pub." |

### Round two — body

| Face | Source | Why not |
|---|---|---|
| Bespoke Slab | ITF / Fontshare | Out. Was the recommended pick; the slabs were too much. |
| Hoover | Gaëtan Baehr / Fontshare | Out. Most personality of the six, and still no. |
| Sentient | ITF / Fontshare | Out, as predicted — it sat in the display register, so it read as a smaller cousin of the heading rather than a counterweight. Shown deliberately as that failure mode. |
| Literata | TypeTogether | Out. Included as the restraint baseline; a brief that keeps rejecting things for being boring was never going to keep it. |
| Recia | Carlos de Toro / Fontshare | Cut before showing: conventional, high boring risk. |

### Cut before being shown

From the eyebrow research: **Fraunces** (already rejected outright in round one — a rejected face does not get a second life in a new role), **Spectral SC** (its own risk note was "newspaper", which had already killed Ogg), **Familjen Grotesk** and **Amulya** (polite, friendly-UI, high boring risk).

### Considered commercially, never shown

These could not be embedded, so they were excluded for a mechanical reason rather than an aesthetic one. Both sit nearer to Bricolage than to the serifs, which makes them the sensible trials now the direction is known:

- **Arizona Mix** — [ABC Dinamo](https://abcdinamo.com/typefaces/arizona). Chunky, low-contrast, between serif and sans.
- **Right Serif** — [Pangram Pangram](https://pangrampangram.com/products/right-serif). Grew out of a sans; moderate contrast, large x-height, seven widths.

## Where the candidates came from

Google Fonts turned out to be largely the wrong place for display type — almost everything from it was rejected as boring. More useful:

- **Free:** [Velvetyne](https://velvetyne.fr/) (41 families, much of it genuinely strange), [Collletttivo](https://www.collletttivo.it/), [UNCUT.wtf](https://uncut.wtf/), [Fontshare](https://www.fontshare.com/) (Indian Type Foundry, free for commercial use), [Fontsource](https://fontsource.org/) for anything self-hostable.
- **Commercial:** Klim, Grilli Type, Displaay, Pangram Pangram, Sharp Type, Blaze Type, OH no Type, ABC Dinamo. Worth noting that six commercial faces were put up in round one and all six were rejected — foundry reputation did no work here.
- **[Future Fonts](https://www.futurefonts.xyz/)** for typefaces still in progress: cheap, and the best place to find something nobody else is using.

## Verified sources for the two free faces

Direct files, confirmed to return HTTP 200 with `wOF2` magic bytes:

```
Bricolage Grotesque  https://cdn.jsdelivr.net/fontsource/fonts/bricolage-grotesque@latest/latin-400-normal.woff2
Apfel Grotezk        https://raw.githubusercontent.com/collletttivo/apfel-grotezk/main/fonts/ApfelGrotezk-Mittel.woff2
```

Both are OFL and should be self-hosted rather than hot-linked in production.

## Technique: rendering any typeface in an artifact

A published artifact may only pull stylesheets from Google Fonts and font files from Google's CDN. Every other host is blocked silently — including jsDelivr for anything that is not a script.

This does **not** limit which faces can be shown. Download the file when building the page and embed it as a base64 data URI, and any face with a public download renders. The 16MB page limit is not a practical constraint: thirteen embedded faces came to under 600KB.

Practical notes:

- Velvetyne publishes on GitLab, Collletttivo on GitHub. Default branches vary between `master` and `main`; the GitLab and GitHub tree APIs are the quick way to find the real file paths.
- Fontshare serves hashed URLs that can rot. Regenerate them from `https://api.fontshare.com/v2/css?f[]=<slug>@400`.
- System Python is externally managed on this machine, so `fontTools` needs a virtualenv. Worth it — reading the character map is the only reliable way to check glyph coverage.

## Method

Things that cost time to learn, worth not relearning.

**Render and look. Descriptions lie.** Of a dozen "weird" faces pulled in one batch, one turned out to be a pictogram font, one only applied its effect to lowercase so capitals got nothing, one put a diamond between every word, and one was past legibility. None of that is visible from a specimen page.

**Check the rendering, not the screenshot.** In one round every block was silently falling back to the body font, because the font stacks contained double quotes which terminated the `style="…"` attribute. It looked plausible. Comparing computed styles caught it; the screenshot did not.

**Change one thing per block.** Vary the heading and hold the body, or vary the body and hold the heading. Otherwise a reaction cannot be attributed.

**Show a ranked recommendation, not a configurator.** The first attempt was an interactive comparator with 33 faces and eight sliders. It was rejected as overwhelming, and rightly: this is a taste decision, and more options make it harder.

**Glyph coverage can decide a role.** The invitation line ends in a down arrow, and several otherwise good eyebrow faces carry no arrow glyph at all. That narrowed the field more than taste did.

**A face rejected in one role stays rejected.** Proposing Fraunces for the eyebrow after it had been turned down for headings would have wasted a round.

## What was not tested

Everything in round one was judged as a **billboard** — one line at around 45px on black. Restora has never been seen at working heading size among body copy, which is where it will actually live. "Restora is more readable" remains a reasonable hypothesis rather than an observation.
