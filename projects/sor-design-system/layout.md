# Layout and rhythm

A page is a stack of grounds. Rhythm comes from changing the ground, not from boxes, borders or colour. Part of the [SoR design system](README.md); see the diagram in [guide.html](guide.html#rhythm).

<iframe class="specimen" src="specimens/rhythm.html" style="aspect-ratio:1000/536" loading="lazy" title="Rhythm, rendered"></iframe>

## Sections

- Every section runs full width, with the page gutter as side padding (`.gutter`, 16–56px) and vertical padding of 44–96px (`.section`).
- Each section opens with a small muted label (`<span class="label">Coming up</span>`), then its content. Labels **name** the section; they are not numbered.
- Give each section a ground: `.ground-white`, `.ground-paper`, `.ground-sun` or `.night`.

## Rhythm of grounds

- **White is the default ground.** **Paper** (off-white) is used sometimes, to feel like paper, as in the Take part section; **sunlight** (baby yellow) at times, to bring in a little colour.
- **Torn edges between sections often**, not only around the night section: a balance, not every boundary.
- Never put two sunlight sections next to each other.
- **One night section** per page, roughly two thirds of the way down, where the page goes deep (selected work, a reading). The footer is the only other night.

The home page runs: paper header → photo hero → white → paper → **night** → sun → white → sun → white → **night** footer.

## Torn edges

Night and light meet at a torn paper edge, never a straight line or gradient. A photograph also tears into the page below it.

| Where | Markup |
|---|---|
| Top of a night section | `<span class="tear tear--top"></span>` as its first child |
| Straight after a night section | `<span class="tear tear--bottom" style="background:var(--night)"></span>` |
| Foot of a photo hero | `<span class="tear tear--overlay" style="background:var(--white)"></span>` (colour of the next section) |
| Top of the footer | `<span class="tear"></span>` as its first child |

Rule: give the tear the colour of the ground it tears **out of**.

## Grid and spacing

| Token | Value | Use |
|---|---|---|
| `--gutter` | 16–56px | page side padding |
| `--section` | 44–96px | section vertical padding |
| `--gap-m` | 16–32px | between cards |
| `--gap-l` | 24–72px | between columns |
| `--measure` | 680px | long-form reading width |

- Calm grids of two, three or four columns, falling to one (or two for pathways) under 800px.
- Two-column sections set text against a plate, usually 1 : 1 to 1.2 : 1.
- Rigour shows in structure: hairline rules between list rows, numbered figures, a contents list, footnotes.
- Sizes are fluid in `cqi` (container width), so a component previewed in a narrow frame behaves as it would on a narrow screen.

## Material

- **Paper grain** sits over the whole page (`.sor::after`, multiply, 14%).
- **Prints**: photographs laid on the page sit on a white mount, slightly rotated (`.print`, 1.6°), with a soft shadow.
- **Printed objects** (magazine, book) get a deeper shadow (`--shadow-object`).
- No rounded corners, no card shadows, no borders around sections.
