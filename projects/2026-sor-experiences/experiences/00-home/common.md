# Common context

What every experience on the home page shares, so separately built pieces still feel like one work. Deliberately small: only what's already decided. The joining rules come later in the frame contract ([HANDOFF.md](HANDOFF.md)).

## Spirit

Awe, beauty, depth: "wow, this is cool". Alive, always moving, something of the unknowable. Rhythm with tension: fast then slow, dark then light, a sudden "ding" after a long build. Experience over calls to action. Usability is not the goal. Full page brief: [brief.md](brief.md).

## Type

Polyamine (billboard), Restora (heading), Bricolage Grotesque (body), Apfel Grotezk (eyebrow / meta). Rules for each: [type.md](../../../2026-sor-design-system/type.md) in the shared design system. Don't restate them here.

For now, name the faces in CSS and rely on them being installed locally; no web font loading. Bundling is decided later.

Experience-only notes:

- Body has to hold on both grounds: the black frames (Dawn, Book) and the white ones (Arrival, Flight).
- Exception: the Book's rising letters use an illuminated, gold display face (sketch: Cinzel Decorative).

## Colour

Mostly black and white; colour arrives as events (the yellow field, the gold letters, the red fingerprints).

| Token | Value | Use |
|---|---|---|
| `--paper` | `#fbfaf7` | white grounds (Arrival, Flight) |
| `--ink` | `#121110` | text and swallows on white |
| `--night` | `#080707` | black grounds (Dawn, Book) |
| `--ember` | `#2a2725` | barely-legible dark text (start of the dawn) |
| `--daylight` | `#efebe4` | warm white text on black |
| `--seed-red` | `#e11414` | the logo's fingerprints / seeds |
| `--gold` | `#e8c46a` | the Book's illuminated letters |

## Sequence

| # | Experience | Starts | Ends | Driven by |
|---|---|---|---|---|
| 1 | Arrival | white | white | tbc (existing design) |
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
