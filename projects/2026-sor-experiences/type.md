# Type

Choosing the typefaces for the experiences. Frame 2 of [02-dawn](experiences/02-dawn/HANDOFF.md) is the test case, because it holds all the roles at once: a paragraph, a statement, and a small invitation line.

Shared constraints live in [experiences/00-home/common.md](experiences/00-home/common.md#type); this file is the reasoning behind them.

Tracking: beads `design-2pk`.

## Current output

- **Round one: heading faces** — nineteen candidates in the real frame, each carrying the verdict it got. Kept as a record so a later round does not re-propose what was turned down.
  - To read or share: **[artifact](https://claude.ai/artifact/V3NjX27AqKMjKeiwxLSfgR)**.
  - In the repo: [type/round-01-headings.html](type/round-01-headings.html), which opens straight from disk. `type/build-round-01.py` regenerates both copies; the publishable one is derived and gitignored.
- **Round two: body and eyebrow faces** — the two chosen body faces, then three eyebrow candidates, with the four rejected bodies collapsed at the bottom. One variable per block.
  - To read or share: **[artifact](https://claude.ai/artifact/Gr3K5DYxpoB6hP4XZ1nR9L)**.
  - In the repo: [type/round-02-body.html](type/round-02-body.html). `type/build-round-02.py` regenerates it.
- Superseded and unmaintained: an interactive comparator with 33 faces and live controls ([link](https://claude.ai/artifact/2TkRgn44LBQdLedo1C5cr6)). Too much choice, and a worse tool than the ones that already exist.

## The roles

Five roles, four faces. Billboard and heading are split because they are different jobs at different optical sizes, not two flavours of the same thing.

| Role | Where it appears | Currently | State |
|---|---|---|---|
| **Billboard** | Heroes and the experience pages. Used sparingly. | Polyamine | effectively settled |
| **Heading** | Ordinary headings in ordinary text. Web now, print later. | Restora | effectively settled |
| **Body** | Long reading, 52 characters and up | Crimson Text, disliked | **open — being researched** |
| **Eyebrow / meta** | Labels, captions, the invitation line | unowned; `system-ui` by default | **open — being researched** |
| Subheading | — | — | not a face. Size and weight within the heading family |
| Illuminated | The Book's rising gold letters | Cinzel Decorative | separate problem, Book only |

**Billboard and heading rarely share a page.** Billboard is reserved for heroes and the experience pages; everywhere else, headings in running text use the heading face. That is why the two do not need to harmonise closely — they need to belong to the same world, not the same family, and the usual objection to running two display faces does not apply here.

**Optical size is the reason for the split.** A face drawn for 120px carries hairlines, tight fitting and fine detail that collapse at 28px; a face drawn for 28px has sturdier strokes and looser spacing that look inflated at 120px. The specs bear this out: Polyamine ships no weight range at all, so it cannot run a hierarchy and is billboard-only. Restora has eight weights thin to black with matching italics, which is a real heading family and covers subheads without a fifth face.

**Subheading is not a separate face.** Hierarchy comes from size, weight and spacing inside the heading family. Adding a face for it would be a mistake.

## Decisions

- **Heading before body.** The heading is the signature of the frame and everything else gets judged against it. Settled first, and it was the right order: the body brief only became clear once the heading taste was known.
- **No bold, no italic in body.** One weight. Emphasis comes from rhythm and space.
- **The single-font plan is dead.** Polyamine was specified for display *and* body; that did not survive contact with 52 characters of running text. Two or three faces, deliberately.
- **Dawn stays black.** Inverting it would remove the ember-to-daylight mechanic, which is the whole frame.
- **The body face must hold on both grounds.** Dawn and the Book are black; Arrival and Flight are white. That is true whatever Dawn does, so it is a real constraint rather than a Dawn one.
- **Consistent system, variable voice.** One body face across the whole series — it is the reader's spine, and changing it per frame reads as broken. The display face may vary per experience, the way a magazine changes its feature openers but never its body text.

## What we are looking for

Distilled from the round-one review. This is the brief for every later round, headings and body alike.

> "Weightiness is important, this grounded weightiness. We are saying something relatively significant, but at the same time it wants to have a bit of an edge, a bit of novelty. It wants life — life and groundedness and wholeness — without becoming just organic kitsch."

**Wants:** groundedness and weight, because the thing being said is significant. An edge, a novelty, something genuinely new. Life and wholeness. Organic *and* elegant at once. Luxurious and sleek without going dead.

**Rejects**, each one learned from a specific face:

| Failure | Where it showed up |
|---|---|
| Boring, no personality | Bluu Next, Instrument Serif, Italiana, Fraunces, Reckless, Signifier |
| Backward-looking — runes, revivals, the *last* Renaissance | Basteleur, Cinzel, and the reason Bagnard is a no |
| Organic kitsch, woo-woo, new-age | Cantique |
| Fat, heavy, inelegant | Coconat Bold |
| Too sharp, feels like it will cut you | GT Sectra |
| Newspaper | Ogg |
| Barber shop or pub signage | Migra |
| Crazy — video game, disco ball | Flor de Ruina |

The second failure is the important one and the least obvious. This is a *new* rebirth emerging forwards, not a return to an earlier one, so historical revival reads as going backwards even when it is beautifully drawn. That single rule explains most of the rejections at once.

## The contrast principle

The other thing that came out of round one, and it sets the body brief:

> "I end up liking Restora and Polyamine because they have something a little organic and elegant, but they are both fonts that do feel quite luxurious and sleek. The thing is, if you take that, then you have to compensate with something more weighty and grounded in the body."

So the system is a deliberate **contrast**, not a match. A sleek, elegant, faintly luxurious display face over a body face that supplies the weight and groundedness the heading does not. That rules out the obvious move of pairing the display serif with a quiet neutral workhorse: neutral is not the same as grounded, and a neutral body would leave the page with no ballast at all.

## The body brief, and how it resolved

Round two settled it: **Bricolage Grotesque** first, **Bespoke Serif** second, against Polyamine. Bespoke Slab, Hoover, Sentient and Literata are out.

The brief that produced them:

- **Weighty and grounded.** The body supplies the ballast the sleek display faces do not. Neutral is not grounded; a quiet workhorse would leave the page with no weight anywhere.
- Alive rather than kitsch, holds on both grounds, one weight, long-form at 52 characters and up.

**What the result taught us, which the brief did not predict.** A sans came first, and every serif but one was rejected — including the slab that was recommended as the most genuinely weighty option. So the contrast wanted between display and body is a **change of kind, not of degree**: not more weight inside the same family of shapes, but a different skeleton altogether. Ink traps and contemporary grotesque construction pass the "not backward-looking" test in a way that even a well-drawn low-contrast serif does not.

That also reframes the paid options worth trialling. Arizona Mix (Dinamo) and Right Serif (Pangram Pangram) are both nearer to Bricolage than to the serifs, so they are the sensible commercial comparisons now that the direction is known.

## The eyebrow

Still open. Three candidates in round two: Apfel Grotezk, Azeret Mono, Ysabeau Office, now shown against Bricolage Grotesque.

One constraint decided more than taste did: the invitation line ends in a down arrow, and several otherwise good faces carry no arrow glyph at all. Check the character map before shortlisting anything for this role.

## Where to look

Google Fonts is largely the wrong place for the display face. Better sources:

- Free and open: [Velvetyne](https://velvetyne.fr/) (41 families, much of it genuinely strange), [Collletttivo](https://www.collletttivo.it/), [UNCUT.wtf](https://uncut.wtf/), [Fontshare](https://www.fontshare.com/).
- Commercial: worth noting that six of the commercial faces put up in round one were rejected, so foundry reputation is not doing the work here. Nasir Udin's other families are the exception, being the source of Restora.
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
- Does Restora actually hold up at working heading size, among body copy? It has been judged only as a billboard line so far, and swashes and imperfect letterforms can read busier at 24px than at 45px.
- Which way round for a Restora / Restora Neue pair, if Polyamine is ever dropped? Neue is higher contrast, which usually suits the larger size.
- Is "light, widely spaced capitals" a real requirement, or an artefact of Polyamine being the face we happened to start from? The weirder candidates break it deliberately.
- Polyamine has no web font file and is loaded through `local()`, so everyone without it installed sees the fallback. Needs licensing and self-hosting if it stays.
