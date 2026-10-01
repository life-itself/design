# Type

The typefaces, and where each one is used. Settled over two rounds in September 2026; the reasoning, and everything rejected, is in [type/research-notes.md](type/research-notes.md).

Part of the shared [SoR design system](README.md), used by the [experiences](../2026-sor-experiences/) and the [website](../2026-sor-website/). Experience-only notes live in [common.md](../2026-sor-experiences/experiences/00-home/common.md#type).

Tracking: beads `design-2pk` (closed).

## The rounds

| | What | Read and share | Archived here |
|---|---|---|---|
| **One** | Heading and billboard faces, nineteen candidates | [artifact](https://claude.ai/artifact/V3NjX27AqKMjKeiwxLSfgR) | [type/round-01-headings.html](type/round-01-headings.html) |
| **Two** | Body faces, then eyebrow faces | [artifact](https://claude.ai/artifact/Gr3K5DYxpoB6hP4XZ1nR9L) | [type/round-02-body.html](type/round-02-body.html) |

Both pages are **archived in this repo** as standalone HTML with the fonts embedded, so they open offline and do not depend on the artifacts surviving. The artifact links are for reading and sharing. No need to archive them again. Each page carries the verdict every candidate got, so a later round can check what has already been turned down. Rebuild either with its `build-round-0N.py`.

## The four faces

| Role | Face | Licence |
|---|---|---|
| **Billboard** | [Polyamine](https://uicreative.net/products/polyamine-modern-classy-serif-font) | commercial, UICreative — $36 personal, $189 business |
| **Heading** | [Restora](https://www.myfonts.com/collections/restora-font-nasir-udin), Nasir Udin | commercial, ~$139 |
| **Body** | [Bricolage Grotesque](https://fonts.google.com/specimen/Bricolage+Grotesque), Mathieu Triay | free, SIL OFL |
| **Eyebrow / meta** | [Apfel Grotezk](https://www.collletttivo.it/typefaces/apfel-grotezk), Collletttivo | free, SIL OFL |

Two paid, two free. Neither paid face is licensed yet — see [Before shipping](#before-shipping).

## How to apply them

Provisional. The patterning below is what we believe now; it gets worked out properly against real page layouts in a later session, from exemplars rather than in the abstract.

### Polyamine — billboard only

The hero, and display type on landing pages and the experience pages. Used **sparingly**: it is the loudest thing in the system and loses its force if it appears often.

Three limits, all learned from looking at it rather than from theory:

- **Five to ten words maximum** at any given size. It is a face for a statement, not for a sentence.
- **Not for pull quotes.** It does not hold at that length or in that position.
- **Not for small headings.** It ships no weight range at all, so there is nothing to step down to. It only works large.

In an ordinary article, Polyamine appears in the hero and nowhere else. H1 to H4 in running text are Restora.

### Restora — headings, and the larger quotes

The working heading face: headings and subheadings inside running text, pull quotes, and larger quotations. Eight weights thin to black with matching italics, so hierarchy comes from size and weight within Restora rather than from bringing in another face.

There is **no separate subheading face**. Subheads are Restora, smaller or at a different weight.

### Bricolage Grotesque — body

All long reading. One weight, no bold, no italic: emphasis comes from rhythm and space.

### Apfel Grotezk — eyebrows and meta

Section labels, eyebrows above headings, captions, credits, small interface chrome, invitation lines. Typically 11–14px, uppercase, letterspaced around 0.08–0.14em.

## Why this combination

Two ideas did the work, and both came out of reactions to real samples rather than being planned.

**The display faces are sleek, so the body supplies the ballast.** Stated during the first round: *"if you take that, then you have to compensate with something more weighty and grounded in the body."* The body is not a neutral container. That rules out pairing the display serifs with a quiet workhorse — neutral is not the same as grounded, and a neutral body would leave the page with no weight anywhere.

**The contrast is a change of kind, not of degree.** Round two tested that principle and corrected it. Every serif but one was rejected, including the slab put forward as the most genuinely weighty option, and a **sans** came first. The answer was not more weight inside the same family of shapes but a different skeleton.

**Nothing may look backwards.** The most-used rejection across both rounds: *"it looks like you're going backwards rather than forwards — we're rebirthing, emerging forwards. We're not talking about the last Renaissance, we're talking about a new one."* This killed several beautifully drawn faces. Bricolage's ink traps help here, since ink traps only exist in faces drawn recently.

## Before shipping

- **Licence Polyamine and Restora.** Neither is bought. For now pages name the faces and they show only where installed; anyone else sees a fallback. Tracked as `design-34t.2`.
- **Self-host all four.** Bricolage and Apfel are OFL and can be served directly; the two paid faces need web licences.
- **Test Restora at working heading size.** Everything reviewed so far was judged as a *billboard* — one line at around 45px. Restora has never been seen at 24px among body copy, which is where it will actually live, and swashes and imperfect letterforms can read busier small than large.

## Open questions

- Is "light, widely spaced capitals" (in [common.md](../2026-sor-experiences/experiences/00-home/common.md#type)) a real requirement, or an artefact of Polyamine being the face we started from?
- The Book's illuminated gold letters are a separate problem, still on Cinzel Decorative as a sketch.
