# Diagrams

Diagrams, figures, charts and frameworks: in papers, on slides, on the website, and above all shared on their own. Part of the [SoR design system](README.md); read [BUILD.md](BUILD.md) first. Status: [examples.md](examples.md#status).

**Stub: the signature is decided and made (2026-10-07, [reasoning](decisions.md#working-through-publication-branding-2026-10-07)); type and drawing style still to decide.** Examples: [examples/diagrams/](examples.md#diagrams).

## Why diagrams need their own rules

A diagram travels further than the paper it came from. People screenshot it, crop it, drop it into a deck or a post, and the credit and link are gone. So every diagram carries its own signature, inside the image.

## The signature

The standard pattern for published charts and figures (the Economist, the FT, Our World in Data): a small, consistent strip in the same place every time.

- **What:** the mark, then "SEEDS OF RENAISSANCE" and one optional slot on one line, **set in Apfel Grotezk**, not the Polyamine wordmark. Chosen over the full lockup and over text only after [mockups](examples/diagrams/index.html) (2026-10-07): the wordmark smudges at signature size and adds a second display face, and text alone leaves nothing recognisable once the image is shrunk. At thumbnail size no text survives; the mark does.
- **The slot after the name** holds the URL by default, or a publication line ("Wisdom · White paper No. 6"), or nothing. Drop it when the figure sits where the source is obvious.
- **Light grounds:** the mark on its white disc. **Dark grounds:** whatever the system settles as the mark on dark (white disc or an inverted mark, a general question in [logo.md](logo.md#open)). `signature-dark` uses a placeholder until then.
- **Where:** bottom right, **inside the diagram's margin**, not flush to the edge, so a loose crop keeps it. Same corner on every diagram.
- **Size:** on a 1600 px-wide export, the mark 64 px, the text 20 px, the whole signature about 540 px wide. Scale the diagram, not the signature: it stays the same size on every diagram.
- **Colour:** the mark as it is. Name and URL in the diagram's ink at 60% (ink on light, chalk on dark), so the signature signs without competing.
- **Too small for the mark** (a thumbnail, an inline icon-sized figure): drop the mark and keep the name and URL as text. Never shrink the mark until the fingerprints turn to noise.
- **Life Itself** is not shown on diagrams. Seeds is the brand ([logo.md](logo.md#which-mark-where)).
- **One version only.** The same signed file goes in the paper, on the site and in posts, so there is nothing to forget at export.

## Making it easy

Typing and styling text inside a diagram tool is fiddly, so the signature is a ready-made asset you drop in, not something you set each time.

| File | Use |
|---|---|
| `system/img/signature.svg`, `.png`, `@2x.png` | Light grounds |
| `system/img/signature-dark.svg`, `.png`, `@2x.png` | Dark grounds |
| `system/img/signature-name.svg`, `signature-name-dark.svg` (and PNGs) | Name only, no URL |
| `system/img/signature.excalidraw` | All four, as images at fixed size: open it, copy the one you need, paste into your diagram |

- Backgrounds are transparent. The 1x PNG and the SVG are sized for a 1600 px export (542 × 72 including a 4 px edge); use `@2x` for a 3200 px export.
- Place it bottom right with its right edge and bottom 72 px and 56 px in from the edges of the export.
- Excalidraw libraries don't reliably keep embedded images, so the signature ships as a scene to copy from rather than a library item.
- The URL depends on the domain, which is still open ([brand.md](brand.md#open)); the files carry a placeholder. When it is decided, change `URL` in `system/outline.py` and run `system/build-signature.py`. For a paper's figures, the paper's own page or a publication line can fill the slot: call `signature(theme, url=…)` in `outline.py`.

## Open

- **Type for diagrams** (beads `.25`), working direction 2026-10-08: **Apfel Grotezk only, no bold.** Not Polyamine: diagrams are working type, not billboard. Elegance from restraint, as in FT and Economist charts: the title in Apfel Regular, set apart by size only, a little larger than the labels, a grey subtitle saying what the figure shows, hierarchy from size and 60% ink rather than weight; uppercase only for tiny tags. Scale in [Type for diagrams](examples/diagrams/fonts.html). To confirm in context, beside running text.
- **Drawing style** (after the type, beads `.26`): how clean or hand-drawn, line weights, ink and the one accent, black-and-white print.
- Whether a small one-colour swallow (the woodcut seal in [graphics.md](graphics.md)) replaces the full mark at small sizes. Tied to the logo's open small version ([logo.md](logo.md#open), item 3).
