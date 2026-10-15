# Type

The typefaces, and where each one is used. Four faces, no more. Part of the shared [SoR design system](README.md), used by the [experiences](../sor-experiences-2026/) and the [website](website.md). Experience-only notes live in [common.md](../sor-experiences-2026/experiences/00-home/common.md#type). How the faces were chosen, and everything rejected: [type/research-notes.md](type/research-notes.md).

<iframe class="specimen" src="specimens/type.html" style="aspect-ratio:1000/1479" loading="lazy" title="Type, rendered"></iframe>

## The faces

Tokens in [system/tokens.css](system/tokens.css); specimens and scale in [guide.html](guide.html#type).

| Role | Token | Face | Used for |
|---|---|---|---|
| Display | `--font-display` | [Polyamine](https://uicreative.net/products/polyamine-modern-classy-serif-font) | Every headline and title up to ~10 words: hero, page titles, section headlines, card and list titles, wordmark |
| Quote | `--font-quote` | [Restora](https://www.myfonts.com/collections/restora-font-nasir-udin) | Display text past ~10 words: pull quotes (`.pull`), standout passages, long titles |
| Body | `--font-body` | [Bricolage Grotesque](https://fonts.google.com/specimen/Bricolage+Grotesque) | All reading; light (300) for statement paragraphs |
| Label | `--font-label` | [Apfel Grotezk](https://www.collletttivo.it/typefaces/apfel-grotezk) | Eyebrows, buttons, dates, captions, credits, figure numbers: 11–14px, uppercase, tracked .1–.16em |
| Poem | `--font-poem` | Restora italic | Dedications, a line set alone, one emphasised sentence |

## The rule: length decides

**Polyamine for almost all display.** Heroes, big titles, section headlines, card titles: if it is display text under about ten words, it is Polyamine.

**Restora beyond that.** Polyamine is not readable at length, so once display text runs past about ten words it moves to Restora: pull quotes, a bigger passage that should come through, a long title. The poetic italic is Restora too, not a fifth face.

**Bricolage for reading. Apfel Grotezk for small uppercase labels.**

Papers and other print follow their own type table: [print.md](print.md).

## Scale

| Token | Size (px) |
|---|---|
| `--t-hero` | 40–96 |
| `--t-title` | 40–84 |
| `--t-section` | 36–64 |
| `--t-card` | 24–32 |
| `--t-quote` | 26–38 |
| `--t-lead` | 20–28 |
| `--t-reading` | 19 |
| `--t-body` | 17 |
| `--t-caption` | 14 |
| `--t-label` | 12 |

## Fallbacks and licences

Bricolage Grotesque and Apfel Grotezk are free (SIL OFL). Apfel Grotezk (Regular, Mittel, Fett) is embedded in `system/fonts.css`, so it loads anywhere.

Polyamine and Restora are commercial and not yet licensed. Pages name them and they show only where installed; everyone else sees **Fraunces** (then Georgia) for display, quotes and the poetic italic. Fraunces is only the fallback, never a face of its own. If Apfel Grotezk fails to load, labels fall back to Hanken Grotesk.

## Using them

- **Polyamine** is a face for a statement, not a sentence. It has a single weight, so it does not step down: keep it at card-title size or larger.
- **Restora** has eight weights, thin to black, with matching italics. Build hierarchy from size and weight within Restora; there is no separate subheading face.
- **Bricolage**: no bold, no italic. Emphasis comes from rhythm and space.
- **Apfel Grotezk** covers the small interface chrome: section labels, eyebrows above headings, captions, credits, invitation lines.

Decisions: [planning 2608](https://github.com/life-itself/planning/blob/main/projects/2608-seeds-of-renaissance-rebrand.md) · [decision log](decisions.md)
