# Common context

What every experience on the home page shares, so separately built pieces still feel like one work. Deliberately small: only what's already decided, and only what is specific to the experiences; type and colour come from the design system. The joining rules come later in the frame contract ([HANDOFF.md](HANDOFF.md)).

## Spirit

Awe, beauty, depth: "wow, this is cool". Alive, always moving, something of the unknowable. Rhythm with tension: fast then slow, dark then light, a sudden "ding" after a long build. Experience over calls to action. Usability is not the goal. Full page brief: [brief.md](brief.md).

## Type and colour: the SoR design system

The experiences use the shared [SoR design system](../../../sor-design-system/README.md). It is the source of truth; don't restate its rules here.

- **Type:** [type.md](../../../sor-design-system/type.md). Polyamine for display up to about ten words, Restora past that, Bricolage Grotesque for body (one weight, no bold, no italic), Apfel Grotezk for labels.
- **Colour:** [colour.md](../../../sor-design-system/colour.md), values in [tokens.css](../../../sor-design-system/system/tokens.css).

For now, name the faces in CSS and rely on them being installed locally; no web font loading. Bundling is decided later.

### Where the experiences differ, on purpose

The design system is written for the website. The experiences are a different register, so a few of its rules don't apply:

- **Colour arrives as events.** The red fingerprints, "heart burns" in red, the yellow field, the gold letters. The website keeps red for the odd link only; here it can be a moment.
- **More than one dark ground.** Dawn and Book are both black; the website allows one night section per page.
- **Extra colours, experiences only:** `--gold` `#e8c46a` (the Book's illuminated letters) and `--ember` `#2a2725` (barely-legible text at the start of the dawn).
- **The Book's rising letters** use an illuminated gold display face (sketch: Cinzel Decorative), outside the four faces.
- Body has to hold on both grounds: the black frames (Dawn, Book) and the white ones (Arrival, Flight).

### Still to reconcile

The pieces were built on an earlier palette whose values have drifted from the design system's tokens. Open question: move the pieces to the system values, or keep any of these on purpose? Until decided, pieces keep what they have.

| Pieces use | Value | System token | Value |
|---|---|---|---|
| `--paper` | `#fbfaf7` | `--paper` | `#fbfaf6` |
| `--ink` | `#121110` | `--ink` | `#1b1916` |
| `--night` | `#080707` | `--night` | `#171613` |
| `--daylight` | `#efebe4` | `--chalk` | `#ece7dc` |
| `--seed-red` | `#e11414` | `--red` | `#e5201c` |

## Sequence

| # | Experience | Starts | Ends | Driven by |
|---|---|---|---|---|
| 1 | Arrival | white | white | plays on load |
| 2 | Dawn | black | black | plays once reached |
| 3 | Leap | dark grey | the field | scroll |
| 4 | Book | black | black | scroll |
| 5 | Flight | white | white | scroll |

## Words

- **Revoligion**: keep, gloss "(the evolution of religion)" on first use.
- The six principles: Wisdom · Interbeing · Inner growth · Revoligion · Complexity · Beyond capitalism.
- **Papers**, not "white papers".

## Assets

- Logo: [ref/sor-logo-bird-prints.png](../../../../ref/sor-logo-bird-prints.png) (black swallow in a burst of red fingerprints). Split layers: [sketch/assets/swallow.png](sketch/assets/swallow.png), [sketch/assets/logo-ring.png](sketch/assets/logo-ring.png).
