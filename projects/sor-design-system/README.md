# Seeds of Renaissance Design System

**The one home for SoR brand and design-system work.** Started 2026-09-30 with the typefaces.

[sor-brand/](sor-brand/) is the former `life-itself/sor-brand` repo (brand work: mockups, moodboards, logo, woodcuts, design-system plan), merged 2026-10-05 with history. Start from its [STATUS.md](sor-brand/STATUS.md) for the starred picks.

## The system — v0.1 (2026-10-05)

**Guide: [guide.html](guide.html)** · published at https://claude.ai/artifact/MtNi8BxiybVhuXZCzwo6it. Feel, principles, colour, type, graphics, photography, logo, live components, templates, open questions.

Extracted from the v7 home/manifesto mockup and the v2 four-page mockup in [sor-brand/](sor-brand/STATUS.md).

| Path | What |
|---|---|
| [system/tokens.css](system/tokens.css) | Every colour, face, size and space, with its role. Change the system here. |
| [system/components.src.css](system/components.src.css) | Components, readable source → `build-css.py` → `components.css` |
| `system/fonts.css` | Apfel Grotezk embedded (OFL); Polyamine and Restora by name only (unlicensed) → `build-fonts.py` |
| `system/graphics.svg` / `.js` | Woodcut swallow, seal, seeds, clusters → `build-graphics.py` |
| `system/sor.js` | Selected-work picker |
| `system/img/` | Placeholder photos from the mood board (not cleared) and the logo |
| [templates/](templates/) | Home and manifesto rebuilt from the system only |

Preview locally: run the `static` launch config (python http.server on 8790) from the repo root and open `/projects/sor-design-system/guide.html`.

Shared by the two SoR projects, and owned by neither:

- [../2026-sor-experiences/](../2026-sor-experiences/) — the poetic animated pieces
- [../2026-sor-website/](../2026-sor-website/) — the website

It lives here rather than inside either because both need it. Note that the website's own plan has a design system step *derived from the chosen direction*; type arrived earlier and from the other project, so it sits above that step rather than inside it.

Substance without visuals stays in [../2026-sor-website/brand.md](../2026-sor-website/brand.md). This file is for visual decisions only.

## Type — decided

Polyamine (billboard), Restora (heading), Bricolage Grotesque (body), Apfel Grotezk (eyebrow / meta).

**Canonical: [type.md](type.md)** for the decisions and how to apply them; [type/research-notes.md](type/research-notes.md) for the working and everything rejected; the two selection rounds archived in [type/](type/). Other files link here rather than restating the rules.

## Colour — not started

The experiences carry a working palette in [../2026-sor-experiences/experiences/00-home/common.md](../2026-sor-experiences/experiences/00-home/common.md#colour): warm blacks and whites, with colour arriving as events. It has not been tested against the website and is not promoted here yet.

## Not started

Spacing, scale, components, motion, iconography. All of it waits on the website direction being chosen.

## Open questions

- **Does the website direction get to override the type?** The website is starting fresh visually and its direction is unchosen. Type has been treated as brand-level, above direction, which is a reasonable call but was made from the experiences side only. If a chosen direction fights these faces, that conflict needs resolving rather than assuming.
- Is the experiences' colour palette a brand palette, or only right for those pieces?
- Where does the Book's illuminated display face belong — here, or only in the experiences?

Tracking: beads `design-34t`.
