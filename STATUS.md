# Seeds of Renaissance brand: status and handoff

*Last updated: 2 October 2026.* Most recent work first. This page is the place to start a review.

## Where we are now

We're building the Seeds of Renaissance design system by mocking up real pages and pulling the rules out of what works. The feel is agreed, a first design system is in place and has been applied to six website pages and four YouTube thumbnails, and there's a first set of woodcut graphics.

**Most recent (2 October)**
- **Home page with a full-screen hero**, in the layout of the original mockup (centred header, photo full screen, title centred over it), now in the new system. [Seeds Polyamine Pages, v7](https://claude.ai/artifact/DuYLk3Qu3sSn6g1PKqBFqE)
- **Woodcut graphics folder** with a gallery: swallows, mountains, leaves, wind, fruits, people sitting in a circle, and seeds (in black and in red). [Woodcuts gallery](https://claude.ai/artifact/U3qepgEKdybBfPVu2YT3ny) · files in [`graphics/woodcuts/`](graphics/woodcuts/README.md)
- **Woodcut seeds**, single and in clusters, and the home and manifesto pages rebuilt in the current system (v6).

**What reviewers should look at first**
1. [Seeds Polyamine Pages](https://claude.ai/artifact/DuYLk3Qu3sSn6g1PKqBFqE): home and manifesto, the current state of the system.
2. [Seeds Website Pages](https://claude.ai/artifact/FdEdXJPhgzoX6thdzsgxwZ): four more page types (gatherings, join, magazine, white paper) and the graphic elements.
3. [Woodcuts gallery](https://claude.ai/artifact/U3qepgEKdybBfPVu2YT3ny): all the graphic elements on different grounds.
4. [YouTube thumbnails](https://claude.ai/artifact/QEUjrhcpFTu5h9xjHP5Hco): the system outside the website.

All photos in the mockups are placeholders from the mood board. Most can't be used publicly without rights.

## The design system so far

### Feel
- **Essence: Grounded hope.**
- **Supporting notes:** deep sourcing; crafted rigour (the potter's bowl, not Vogue); liminal integration (dawn, birth and death as one transition).
- **Character:** a little off-centre. Earthy, a bit muddy, a bit quirky; not mainstream, not chaotic.
- **Not:** wellness or new age, luxury, corporate or tech, hard selling, sleek and contemporary, merchandised spirituality.
- **Guiding image (open):** the doula, a caring presence at birth and at death.

Full reasoning: [design-system-plan.md](design-system-plan.md).

### Colour roles
| Role | Colour | Rule |
|---|---|---|
| Ground | White `#ffffff`, paper `#fbfaf6` | Most sections. Some sections pure white. |
| Pale yellow | `#fbefc4` | **Background only.** Sunlit sections. No bright yellow, no highlighting. |
| Ink | `#1b1916` | Text and **all buttons** (solid black or black outline). |
| Night | `#171613` with chalk text `#ece7dc` | At most one dark section per page. Meets light sections at a torn edge. |
| Red | `#E5201C` (the logo red) | **Only for occasional links in running text.** Optional for woodcut seeds. |
| Muted and rules | `#5d584f`, `#e0dacf` | Captions, labels, hairlines. |

Colour otherwise comes from photographs.

### Type
- **Polyamine:** headings and the wordmark. Restora is kept in reserve.
- **Bricolage Grotesque:** body text.
- **Appful Grotesque:** small uppercase labels, buttons, dates.
- **A soft italic serif** (Fraunces in the mockups): poems, quotes, interludes.

Polyamine and Appful Grotesque are only installed locally. Anyone without them sees Fraunces and Hanken Grotesk instead.

### Graphic devices
- **Torn edge** where dark and light meet (liked).
- **Woodcut graphics:** swallows (flight, flock, seal, divider), seeds, mountains, leaves, wind, fruits, people in a circle.
- **Figures numbered and captioned like plates** ("Fig. 2 · …"), for visible rigour.
- **Logo on a white disc or square tile** (liked).
- Light paper grain.

### Registers
The same skeleton is used at three levels of warmth:
- **Study** (white papers): rigour leads.
- **Conversation** (home, manifesto, magazine): balanced.
- **Gathering** (events, join): warmth leads.

## Open questions and next steps
- **Photography:** we need joyful photos with people and children. This would do more for joy than any colour.
- **Logo:** deepen the red? redraw the swallow? make a small version for favicons and avatars? See [logo.md](logo.md).
- **Woodcuts:** these are code-drawn first drafts. The perched swallow and the swallow from above are the weakest. Should a final set be hand-drawn, or based on public-domain prints?
- **Not yet tested:** slides and print (poster or magazine page).
- **Not yet written:** a type scale, the exact Polyamine and Restora split, and image rights and sourcing rules.
- **Guiding image:** decide whether the doula is part of the brand story.

## All artifacts (newest first)

Each artifact keeps its full version history in claude.ai. Source copies are in this repo.

### Seeds Woodcuts (gallery)
[Open](https://claude.ai/artifact/U3qepgEKdybBfPVu2YT3ny) · source: `graphics/woodcuts/gallery.html`
- v2: seeds in red added.
- v1: all 29 woodcuts with a switch for white, paper, pale yellow and night grounds.

### Seeds Polyamine Pages (home and manifesto)
[Open](https://claude.ai/artifact/DuYLk3Qu3sSn6g1PKqBFqE) · source: `mockups/direction-e/`
- v7: full-screen hero in the original layout (default), photo switcher, split hero still available.
- v6: rebuilt in the current system, with woodcut swallows and seeds.
- v5: Night to Dawn palette (didn't work; some ideas kept). Saved as `index-v5-night-to-dawn.html`.
- v4: #1F338A tested as a call-to-action colour (rejected).
- v1 to v3: before this work. Direction E, Restora against Polyamine, Polyamine chosen ("Warm Emergence").

### Seeds Website Pages (gatherings, join, magazine, white paper)
[Open](https://claude.ai/artifact/FdEdXJPhgzoX6thdzsgxwZ) · source: `mockups/pages/`
- v2: woodcut swallow and graphic elements sheet; pale yellow as background only.
- v1: joy layer with bright yellow, drawn suns and highlighting (bright yellow and highlighting rejected).

### Seeds YouTube Thumbnails
[Open](https://claude.ai/artifact/QEUjrhcpFTu5h9xjHP5Hco) · source: `mockups/youtube/`
- v2: photo fix.
- v1: four templates (gathering, podcast, manifesto, talk), full size and in light and dark feeds.

### Seeds Ink and Paper (home and manifesto, directions A, B and C)
[Open](https://claude.ai/artifact/R8YDUkZrsTMR3NUEq2cfEj) · source: `mockups/ink-and-paper/`
- v5: photo fix.
- v4: black buttons, red only for links. This decision became part of the system.
- v3: pure white sections; red buttons tried.
- v2: lighter, original photos back.
- v1: A (ink and paper only) and B (one extra ink: red, Prussian blue or gold). Too dark.

## Repo map
- [design-system-plan.md](design-system-plan.md): the working plan, feel, colour thinking and decision log.
- [moodboard.md](moodboard.md) and [moodboard-not-us.md](moodboard-not-us.md): images we like and don't, with notes and a synthesis.
- [logo.md](logo.md): logo notes and issues.
- [references/](references/): studies of Dark Mountain and Emergence Magazine.
- [graphics/woodcuts/](graphics/woodcuts/README.md): woodcut graphic elements and the script that draws them.
- [mockups/](mockups/): HTML source of every mockup.
- [assets/](assets/): mood board images (inspiration only, not cleared for use).
