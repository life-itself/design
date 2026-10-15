# Colour

Colours have roles, not just values. Four grounds, three inks and one accent, used in that order of frequency, plus three illustration inks for graphics only. Values live in [system/tokens.css](system/tokens.css); see them rendered in [guide.html](guide.html#colour). Part of the [SoR design system](README.md).

<iframe class="specimen" src="specimens/colour.html" style="aspect-ratio:1000/622" loading="lazy" title="Colour, rendered"></iframe>

## Grounds (backgrounds only)

| Token | Value | Role |
|---|---|---|
| `--white` | `#ffffff` | Pure white sections: the page at its most open. Statements, calendars, engage, long reading. |
| `--paper` | `#fbfaf6` | The default page, warm near-white, under the paper grain. Headers, collections. |
| `--sunlight` | `#fbefc4` | Pale yellow, for joy. **A whole section's background only**: never text, never a highlight. |
| `--night` | `#171613` | At most **one** section per page, plus the footer. Depth: selected work, reflection. |

## Inks

| Token | Value | Role |
|---|---|---|
| `--ink` | `#1b1916` | All text on light grounds, rules that matter, and **every button**. |
| `--muted` | `#5d584f` | Captions, labels, secondary text. |
| `--rule` | `#e0dacf` | Hairlines on light grounds. |
| `--chalk` | `#ece7dc` | Text on night. |
| `--night-muted` | `#a49e93` | Secondary text on night. |
| `--night-rule` | `#38342e` | Hairlines on night. |

## The accent

| Token | Value | Role |
|---|---|---|
| `--red` | `#e5201c` | The logo red. **Only** an occasional link in running text (`.link`) and footnote marks. |

## Illustration inks (graphics only)

| Token | Value | Role |
|---|---|---|
| `--print-blue` | `#03296f` | Cobalt. A woodcut printed in blue. |
| `--print-green` | `#1f3d2b` | Deep green. A woodcut printed in green. |
| `--print-mustard` | `#c9a227` | Mustard yellow. A woodcut printed in mustard. |

These are the colours a woodcut or animal graphic may be printed in besides black (and chalk on night). They are **only** for graphics: never text, buttons, rules or backgrounds. One illustration ink per graphic, and keep them occasional: black stays the default.

### Which colours each graphic set may use

The illustration inks are for the woodcuts and the animals. Painted and printed sets keep the colours they were made in: never retint them, and never use their colours on other graphics. The geometry and marks are plain ink. Every set: [graphics.md](graphics.md).

| Graphic set | Colours | Rule |
|---|---|---|
| [Woodcuts](system/woodcuts/README.md), [animals](system/animals/README.md) | Black (chalk on night) and the three illustration inks; woodcut seeds also in the logo red | One ink per graphic. Every animal comes in all four |
| [Mountains](system/mountains/README.md) | The blue each was drawn in (six blues from navy to violet), cobalt and black; the linocut also in three lighter blues | The drawn blues are for the mountains only |
| [Botanicals](system/botanicals/README.md), [washes](system/washes/README.md) | The colours they were painted in: reds, blues, greens, olive and ochre | Not retinted |
| [Prints](system/prints/README.md) | The colours they were made in: black, the logo red and a softer print red, a faded green, a faded dark blue, cobalt, a swallow blue, ochre, pale yellow and a gold sun | Not retinted. Often used under a transparency that softens ink and colour together, so the exact colours matter; until the method is set, keep it subtle |
| [Geometry](system/geometry/README.md), [marks](system/marks/README.md) | `--ink` only | Plain black line work: don't tint |

## Proportion

By area on the home page, leaving out photographs: about 64% white and paper, 14% sunlight, 16% night, 5% ink, 1% red. Photographs carry most of the colour.

## Do

- Let a photograph be the most colourful thing on the screen.
- Alternate white, paper and sunlight sections to give rhythm without colour.
- Use red for one link in a paragraph, at most.

## Don't

- Make a red button, red heading or red background.
- Highlight words in yellow, or use a bright yellow anywhere (tried: rejected).
- Add a second dark section, or a gradient other than the hero scrim.
- Use blue for action (#1F338A was tried and rejected as too cool and corporate). The illustration blue is for graphics only.
- Use an illustration ink for text, a button or a background.

Decisions: [planning 2608](https://github.com/life-itself/planning/blob/main/projects/2608-seeds-of-renaissance-rebrand.md) · [decision log](decisions.md) (black buttons and red-only-for-links came from the Ink and Paper exploration; the pigment palette of Night to Dawn did not work).
