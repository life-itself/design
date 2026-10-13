# Colour

Colours have roles, not just values. Four grounds, three inks and one accent, used in that order of frequency, plus three illustration inks that only woodcut graphics may use. Values live in [system/tokens.css](system/tokens.css); see them rendered in [guide.html](guide.html#colour). Part of the [SoR design system](README.md).

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

The red is decided: `#e5201c`, the logo red, kept as the site's red (decided 2026-10-12; see the [planning record](https://github.com/life-itself/planning/blob/main/projects/2608-seeds-of-renaissance-rebrand.md)).

## Illustration inks (graphics only)

| Token | Value | Role |
|---|---|---|
| `--print-blue` | `#03296f` | Cobalt. A woodcut printed in blue. |
| `--print-green` | `#1f3d2b` | Deep green. A woodcut printed in green. |
| `--print-mustard` | `#c9a227` | Mustard yellow. A woodcut printed in mustard. |

These are the colours a woodcut graphic may be printed in besides black (and chalk on night). They are **only** for graphics: never text, buttons, rules or backgrounds. One illustration ink per graphic, and keep them occasional: black stays the default. Every animal in [system/animals/](system/animals/README.md) comes in all four (decided 2026-10-13).

**Exception, mountains only:** the [mountain elements](system/mountains/README.md) also come in the blue each was drawn in (six blues from navy to violet), plus three lighter blues on the linocut, chosen to keep each drawing's character. They are not illustration inks: don't use them on any other graphic. This is an open tension with the rule above, to be settled with the sub-brand question (decided 2026-10-13, Beads `design-34t.43`).

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

## History

Black buttons and red-only-for-links were decided in the Ink and Paper exploration (v4). Pale yellow as background only, no bright yellow and no highlighting, on 2026-10-01. The pigment palette of Night to Dawn (lapis, vermilion, gold, plum) did not work. Decision log: [decisions.md](decisions.md#decision-log).
