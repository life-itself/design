# Type research notes

Backup for [../type.md](../type.md), which holds the decisions. This file holds the working: what was looked at, what was rejected and why, where things came from, and the techniques that made the rounds possible.

Two rounds, both September 2026. Every candidate was rendered in the real frame at real size on the real ground before being judged.

## The rounds

| | What | Read it |
|---|---|---|
| **Round one** | Heading and billboard faces. Nineteen candidates. | [artifact](https://claude.ai/artifact/V3NjX27AqKMjKeiwxLSfgR) · [round-01-headings.html](round-01-headings.html) · `build-round-01.py` |
| **Round two** | Body faces, then eyebrow faces. | [artifact](https://claude.ai/artifact/Gr3K5DYxpoB6hP4XZ1nR9L) · [round-02-body.html](round-02-body.html) · `build-round-02.py` |

Both pages are **archived in this repo** as standalone HTML with the fonts embedded, so they open offline and do not depend on the artifacts surviving. The artifact links are for reading and sharing. No need to archive them again.

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

## Moved from type.md

Reasoning and history that used to sit on [the type page](../type.md), kept here so the page can state only the rules.

### Why this combination

Two ideas did the work, and both came out of reactions to real samples rather than being planned.

**The display faces are sleek, so the body supplies the ballast.** Stated during the first round: *"if you take that, then you have to compensate with something more weighty and grounded in the body."* The body is not a neutral container. That rules out pairing the display serifs with a quiet workhorse — neutral is not the same as grounded, and a neutral body would leave the page with no weight anywhere.

**The contrast is a change of kind, not of degree.** Round two tested that principle and corrected it. Every serif but one was rejected, including the slab put forward as the most genuinely weighty option, and a **sans** came first. The answer was not more weight inside the same family of shapes but a different skeleton.

**Nothing may look backwards.** The most-used rejection across both rounds: *"it looks like you're going backwards rather than forwards — we're rebirthing, emerging forwards. We're not talking about the last Renaissance, we're talking about a new one."* This killed several beautifully drawn faces. Bricolage's ink traps help here, since ink traps only exist in faces drawn recently.

### Licences and prices

| Role | Face | Licence |
|---|---|---|
| Display | [Polyamine](https://uicreative.net/products/polyamine-modern-classy-serif-font), UICreative | commercial: $36 personal, $189 business |
| Quote and poem | [Restora](https://www.myfonts.com/collections/restora-font-nasir-udin), Nasir Udin | commercial, ~$139 |
| Body | [Bricolage Grotesque](https://fonts.google.com/specimen/Bricolage+Grotesque), Mathieu Triay | free, SIL OFL |
| Label | [Apfel Grotezk](https://www.collletttivo.it/typefaces/apfel-grotezk), Collletttivo | free, SIL OFL |

Two paid, two free. All four should be self-hosted: Bricolage and Apfel are OFL and can be served directly; the two paid faces need web licences. Until then, `system/build-fonts.py` embeds Apfel only and declares the paid faces as `local()`, so they show only where installed.

### The rounds archive

Each archived round page carries the verdict every candidate got, so a later round can check what has already been turned down. Rebuild either with its `build-round-0N.py`.

### How the rule changed

- **The first plan (September 2026)** used Polyamine as a billboard face only: the hero and landing-page display, used sparingly, five to ten words at most, never for pull quotes or small headings. In an ordinary article Polyamine appeared in the hero and nowhere else, and H1 to H4 in running text were Restora.
- **The length rule (2026-10-05, Rufus and Sylvie)** replaced it, from the approved mockups: Polyamine for almost all display under about ten words, Restora beyond that and for the poetic italic. Four faces only; Fraunces is only the fallback.
- **The "Appful Grotesque" fix (2026-10-05).** The mockups named "Appful Grotesque", which matched no font, so labels showed in the fallback (Hanken Grotesk). The system now embeds Apfel Grotezk.
- Labels were first specified as letterspaced around 0.08–0.14em; the system uses .1–.16em.

### Still unexamined

- Restora at working heading size among body copy (see [What was not tested](#what-was-not-tested)). Swashes and imperfect letterforms can read busier small than large. Open-licence stand-ins to compare: [Restora alternatives](../examples/type/restora-alternatives.html).
- Whether "light, widely spaced capitals" (in [common.md](../../sor-experiences-2026/experiences/00-home/common.md#type)) is a real requirement, or an artefact of Polyamine being the face we started from.
- The Book's illuminated gold letters are a separate problem, still sketched in Cinzel Decorative.
