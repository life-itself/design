# Seeds of Renaissance Design System

The brand and design system for Seeds of Renaissance: how it looks and why, with the code and examples to build from. **Version 0.1, 5 October 2026.** The single home for SoR brand and design-system work.

**Building something? Start with [BUILD.md](BUILD.md).** It is the brief for people and AI agents alike: the rules in one paragraph, the page shell, a menu of sections, the examples to copy and a checklist.

**Want to see it?** [guide.html](guide.html) shows the whole system rendered, set in its own style. Published at https://claude.ai/artifact/MtNi8BxiybVhuXZCzwo6it.

## The system

| Page | What |
|---|---|
| [feel.md](feel.md) | Grounded hope, what we are not, rigour and warmth, the three registers |
| [colour.md](colour.md) | Grounds, inks and the one accent, with roles and rules |
| [type.md](type.md) | The faces, the scale, and the research behind them |
| [layout.md](layout.md) | Grounds and rhythm, torn edges, grid and spacing |
| [graphics.md](graphics.md) | The woodcut swallow, seal, seeds and clusters |
| [photography.md](photography.md) | What to choose and avoid; placeholders |
| [logo.md](logo.md) | Versions and placement (provisional) |
| [components.md](components.md) | Every component, with HTML to copy |

## Examples

Whole pages built only from the system. Copy the closest one.

| Example | Register |
|---|---|
| [examples/web/home.html](examples/web/home.html) | Landing page |
| [examples/web/manifesto.html](examples/web/manifesto.html) | Long reading |
| [examples/web/gatherings.html](examples/web/gatherings.html) | Events and community |
| [examples/web/join.html](examples/web/join.html) | Joining |
| [examples/web/magazine.html](examples/web/magazine.html) | Publication |
| [examples/web/white-paper.html](examples/web/white-paper.html) | Research |
| [examples/youtube/](examples/youtube/index.html) | YouTube thumbnails, 1280×720 |

Slides and print are next.

## Code

| Path | What |
|---|---|
| [system/tokens.css](system/tokens.css) | Every colour, face, size and space, with its role. Change the system here. |
| [system/components.src.css](system/components.src.css) | Components, readable source. Run `python3 system/build-css.py` to make `components.css`. |
| `system/fonts.css` | Apfel Grotezk embedded (OFL); Polyamine and Restora by name only (unlicensed). Built by `build-fonts.py`. |
| `system/graphics.svg` / `graphics.js` | Woodcut symbols. Built by `build-graphics.py`. |
| `system/sor.js` | Small behaviours (selected-work picker) |
| `system/img/` | The logo, and placeholder photos from the mood board (not cleared) |

Preview locally: run the `static` launch config (python http.server on 8790) from the repo root and open `/projects/sor-design-system/`.

## Where things came from

- [sor-brand/](sor-brand/STATUS.md): the former `life-itself/sor-brand` repo (mockups, moodboards, logo, woodcuts, design-system plan and decision log), merged here 2026-10-05 with history. The system was extracted from its Direction E v7 home and manifesto and its four-page v2 mockup.
- [type/](type/): the two type selection rounds and research notes.
- Brand substance (who we are, offers, voice) stays in [../2026-sor-website/brand.md](../2026-sor-website/brand.md).

Shared by the SoR [experiences](../2026-sor-experiences/) and the website. The experiences carry their own working palette in [common.md](../2026-sor-experiences/experiences/00-home/common.md#colour), not yet reconciled with this system.

## Open questions

See the last chapter of [guide.html](guide.html#open). In short: Polyamine or Restora for headings, font licences, the logo, photography, woodcut sourcing, the scale for slides and print, sub-brand colours. Also: where the Book's illuminated display face belongs.

Tracking: beads `design-34t`.
