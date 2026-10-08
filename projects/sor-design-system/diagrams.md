# Diagrams

Diagrams, figures, charts and frameworks: in papers, on slides, on the website, and above all shared on their own. Part of the [SoR design system](README.md); read [BUILD.md](BUILD.md) first. Status: [examples.md](examples.md#status).

**v0.1, 2026-10-08:** the signature, type and drawing style are decided ([reasoning](decisions.md#working-through-publication-branding-2026-10-07)). Examples: [examples/diagrams/](examples.md#diagrams).

## Why diagrams need their own rules

A diagram travels further than the paper it came from. People screenshot it, crop it, drop it into a deck or a post, and the credit and link are gone. So every diagram carries its own signature, inside the image.

## The look in one paragraph

References: the FT, the Economist, Tufte. Restraint over decoration. One face, Apfel Grotezk, with no bold. Ink lines, solid arrowheads, no outlines on boxes: groups are panels in a pale red tint, and that same tint marks the area that is the point of the figure. A title and a grey subtitle top left, the signature bottom right. Built to read at 400 px in a feed and in a black-and-white print. See it in [Drawing style](examples/diagrams/style.html), including on a page of a paper and in a web article.

## Type

Apfel Grotezk only, and no Fett (bold). Not Polyamine: a diagram is working type, not billboard. In the paper or on a page, Apfel sets the figure apart from the Bricolage of the running text while staying in the family. Sizes at a 1600 px export ([specimen](examples/diagrams/fonts.html)):

| Role | Face | Size | Use |
|---|---|---|---|
| Title | Apfel Regular | 46 px | Top left. Title case ("The Wisdom Gap"); ideally the claim, not the topic. Set apart by size, never weight |
| Subtitle | Apfel Regular, 60% ink | 28 px | One line under the title: what the figure shows |
| Heading | Apfel Mittel | 32 px | Panel and group headings |
| Group label | Apfel Mittel | 34 px | Bracket and group labels |
| Label | Apfel Regular | 29 px | Annotations and bullets, sentence case, set on the thing they name |
| Secondary | Apfel Regular, 60% ink | 26 px | Second lines inside panels |
| Tag | Apfel Mittel, uppercase, tracked .1em | 21 px | Axis names and one-to-three-word tags only |

Nothing smaller than about 26 px at 1600, so the smallest text is still about 7 px in a feed. No legends: label lines and areas directly.

In a paper the figure keeps its own title (it travels alone); the caption below gives "Fig. 1" and a sentence of explanation, not the title again.

## Drawing style

Called **panels**, after the FT and the Economist; chosen over fine Tufte-style rules (too faint at 400 px) and a hand-drawn wobble (looks generated: the hand is our texture around a figure, not a filter on its lines).

- **Lines:** ink, solid, round caps. 4 px for what the figure is about (curves, main arrows), 2 px for scaffolding (axes, brackets, connectors). No dashes.
- **Arrowheads:** solid triangles, never open chevrons. The line stops at the base of the head.
- **Groups:** panels with no outline, square corners, in the **red tint**. As wide as their longest line plus padding, never stretched to fill the canvas. Padding the same on all four sides: 40 px from the edge to the top of the heading's capitals, to the text at the left, and from the last baseline to the bottom.
- **The red tint:** the logo red at 16% on white (`#fbdbdb`), 40% on night (`#6b1a17`; weaker vanishes on dark). For panels and for the one area that is the point (the wisdom gap). Red **text** only for the label of that one area. This is the one place the system allows a red ground ([BUILD.md](BUILD.md#rules-that-apply-everywhere)).
- **Labelling an area:** centre the label in the area, with equal space between it and the edges on either side (in the wisdom gap: midway between the curves, and between the upper curve and the shading's edge), then nudged a touch right if exact centre reads as off: trust the eye over the arithmetic. One line.
- **Black and white:** the tint prints as a light grey, so panels and areas survive a mono printer. Never let colour alone carry a meaning.
- **Ground:** transparent in the drawing, so it takes the ground of the page it sits on; white for a figure shared on its own (see Exports). On dark grounds ink becomes chalk and the tint its night value.
- **Canvas:** draw on 1600 px wide for a figure that fills it, with a 72 px margin; a narrower figure gets a narrower canvas, as wide as its content plus the margin, so the signature sits under the figure. The margin is for the shared export only: the embedded file is cropped to the drawing (see Exports). **The content spans margin to margin:** its right edge (an axis end, a text column, a panel) sits at the right margin, so the signature's right edge lines up with it. Don't lay a figure out on a fixed grid that stops short of the margin: the signature then floats off to the right of the drawing.

## Charts with data

**v0.1, 2026-10-08** ([Charts with data](examples/diagrams/charts.html), illustrative data). The same type, ink and red, after the FT and the Economist: colour is emphasis, not decoration.

- **One series in red,** the one the title is about. The rest: lines in a warm grey (`#8a847a`, on night `#8f897f`), bars and areas in the red tint. Ink when two things are compared as equals. Checked: the grey clears 3:1 on the ground and stays distinct from the red for colour-blind readers; in black and white the red prints darker than the rest.
- **The title says what to see** ("Gatherings have grown fastest since the pandemic"); the subtitle says what is measured, in what units.
- **Label directly:** line names at their ends, values at bar tips, the newer value beside each dot. A key only when unavoidable (two dots per row). Never a number on every point.
- **Scaffolding is quiet:** hairline gridlines in one direction only, the zero line in ink, ticks in Apfel at 60% ink with figures that line up. An event is a pale band behind the data, labelled at its top.
- **Forms:** lines for change over time, ranked bars for comparison, two dots per row for before and after. One axis only, never two.
- **Source line** bottom left, level with the signature: "Source: …". Source left and brand right is the FT and Economist convention; the signature already follows it. Publish the data beside the figure.

## The signature

The standard pattern for published charts and figures (the Economist, the FT, Our World in Data): a small, consistent strip in the same place every time.

- **What:** the mark, then "SEEDS OF RENAISSANCE" and one optional slot on one line, **set in Apfel Grotezk**, not the Polyamine wordmark. Chosen over the full lockup and over text only after [mockups](examples/diagrams/index.html) (2026-10-07): the wordmark smudges at signature size and adds a second display face, and text alone leaves nothing recognisable once the image is shrunk. At thumbnail size no text survives; the mark does.
- **The slot after the name** holds the URL by default, or a publication line ("Wisdom · White paper No. 6"), or nothing. Drop it when the figure sits where the source is obvious.
- **Light grounds:** the mark on its white disc. **Dark grounds:** whatever the system settles as the mark on dark (white disc or an inverted mark, a general question in [logo.md](logo.md#open)). `signature-dark` uses a placeholder until then.
- **Where:** bottom right, its right edge on the drawing's right edge. In the shared export it sits inside the margin, so a loose crop keeps it. Same corner on every diagram.
- **Size:** on a 1600 px-wide export, the mark 64 px, the text 20 px, the whole signature about 540 px wide. Scale the diagram, not the signature: it stays the same size on every diagram.
- **Colour:** the mark as it is. Name and URL in the diagram's ink at 60% (ink on light, chalk on dark), so the signature signs without competing.
- **Too small for the mark** (a thumbnail, an inline icon-sized figure): drop the mark and keep the name and URL as text. Never shrink the mark until the fingerprints turn to noise.
- **Life Itself** is not shown on diagrams. Seeds is the brand ([logo.md](logo.md#which-mark-where)).
- **One drawing, signed once.** Both exports (embedded and shared) come from the same signed drawing, so there is nothing to forget at export.

## Making it easy

Typing and styling text inside a diagram tool is fiddly, so the signature is a ready-made asset you drop in, not something you set each time.

| File | Use |
|---|---|
| `system/img/signature.svg`, `.png`, `@2x.png` | Light grounds |
| `system/img/signature-dark.svg`, `.png`, `@2x.png` | Dark grounds |
| `system/img/signature-name.svg`, `signature-name-dark.svg` (and PNGs) | Name only, no URL |

- Backgrounds are transparent. The 1x PNG and the SVG are sized for a 1600 px export (542 × 72 including a 4 px edge); use `@2x` for a 3200 px export.
- Place it bottom right with its right edge and bottom 72 px and 56 px in from the edges of the export.
- The URL depends on the domain, which is still open ([brand.md](brand.md#open)); the files carry a placeholder. When it is decided, change `URL` in `system/outline.py` and run `system/build-signature.py`. For a paper's figures, the paper's own page or a publication line can fill the slot: call `signature(theme, url=…)` in `outline.py`.

## Drawing them

- **How:** sketch the figure (on paper, a whiteboard, anything), then build it as SVG with Claude, from the code in `examples/diagrams/build.py`: its helpers set the type, panels, arrows and signature to this spec. No diagram tool to configure.
- **Exports: draw tight, add the margin on export** (decided 2026-10-08). The margin and white ground are what a figure needs when it travels alone, not when it sits in a page, so they belong to the export, not the drawing. `write_figure()` in `system/outline.py` writes both from one drawing:
  - **Embedded** (papers, web pages): `name.svg`, cropped to the drawing (plus 8 px so nothing clips), transparent, text outlined (Apfel is not on readers' machines). The page supplies the space around it, as for any other block, and its edges line up with the text. Commit this one; the paper's Markdown links it.
  - **Shared alone** (Substack, social, slides, Docs): `name.share.png` and `name.share@2x.png`, the full canvas with its 72 px margin on white (dark-mode apps would hide ink on transparent). Built on demand with headless Chrome; not committed.
- **Alt text** says what the figure claims, not what it looks like.

## Check before you publish

- [ ] Apfel only, no bold; title, grey subtitle, labels on the things they name.
- [ ] Solid lines, solid arrowheads, no outlines on panels, panels sized to their text with even padding.
- [ ] Red tint on panels and the one key area only; red text only for that area's label.
- [ ] Reads at 400 px and in black and white.
- [ ] Signature bottom right; the content's right edge lines up with the signature's.
- [ ] Exported with `write_figure()`: tight transparent SVG for the page, padded white PNG for sharing.

## Open

- **The red tint at full size** may be a touch strong on large panels (fine at 400 px and in pages). If so, try 12% for panels and keep 16% for the key area. Low priority (beads).
- **Charts with data:** more forms as real charts need them (stacked bars, small multiples, maps).
- Whether a small one-colour swallow (the woodcut seal in [graphics.md](graphics.md)) replaces the full mark at small sizes. Tied to the logo's open small version ([logo.md](logo.md#open), item 3).
