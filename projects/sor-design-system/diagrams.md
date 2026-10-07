# Diagrams

Diagrams, figures, charts and frameworks: in papers, on slides, on the website, and above all shared on their own. Part of the [SoR design system](README.md); read [BUILD.md](BUILD.md) first. Status: [examples.md](examples.md#status).

**Stub: signing rules decided 2026-10-07 ([reasoning](decisions.md#working-through-publication-branding-2026-10-07)); diagram style still to write.**

## Why diagrams need their own rules

A diagram travels further than the paper it came from. People screenshot it, crop it, drop it into a deck or a post, and the credit and link are gone. So every diagram carries its own signature, inside the image.

## The signature

The standard pattern for published charts and figures (the Economist, the FT, Our World in Data): a small, consistent strip in the same place every time.

- **What:** the mark on its white disc (the stamp), then the name and the URL **set as text in the diagram's own label face**, Apfel Grotezk, not the Polyamine wordmark. The wordmark is for display sizes; at signature size it doesn't render well, and set text can be moved to suit each diagram. Mockups to confirm (beads).
- **Where:** bottom right, **inside the diagram's margin**, not flush to the edge, so a loose crop keeps it. Same corner on every diagram.
- **Size:** the mark at least 64 px on a 1600 px-wide export (about 4% of the width). Scale the diagram, not the signature: it stays the same size on every diagram.
- **Colour:** the mark as it is, on its disc. Name and URL in the diagram's ink at about 60%, so the signature signs without competing.
- **Too small for the mark** (a thumbnail, an inline icon-sized figure): drop the mark and keep the name and URL as text. Never shrink the mark until the fingerprints turn to noise.
- **Life Itself** is not shown on diagrams. Seeds is the brand ([logo.md](logo.md#which-mark-where)).
- **One version only.** The same signed file goes in the paper, on the site and in posts, so there is nothing to forget at export.

## Making it easy

Typing and styling text inside a diagram tool is fiddly, so the signature is a ready-made asset you drop in, not something you set each time.

- `system/img/signature.svg` and `.png`: the signature as one image, on light and on dark grounds. **To make** (beads).
- An Excalidraw library item of the same, at a fixed size.
- The URL depends on the domain, which is still open ([brand.md](brand.md#open)). Until then, use the paper's or project's own page.

## Open

- The diagram style itself: line weight, type (Apfel Grotezk labels? Bricolage?), ink and the one accent, hand-drawn against clean.
- Whether a small one-colour swallow (the woodcut seal in [graphics.md](graphics.md)) replaces the full mark at small sizes. Tied to the logo's open small version ([logo.md](logo.md#open), item 3).
