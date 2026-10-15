# Slides

Slide decks in the Seeds of Renaissance system: talks, calls, workshops, pitches. Part of the [SoR design system](README.md). Status lives in beads (`bd show design-34t.12`).

## What we need

A deck template with these slide types, built only from the system:

| Slide | What it holds |
|---|---|
| Title | Talk title (Polyamine), speaker, date or event, logo on its disc |
| Section | A chapter break: one or two words of Polyamine on a ground, perhaps a woodcut |
| Content | A heading and up to five short points, or a short paragraph |
| Quote | A pull quote in Restora with attribution (the length rule: past ~10 words it's Restora) |
| Image | A full-bleed photograph with a caption as a plate (`Fig. N`) |
| Image + text | Plate on one side, heading and text on the other |
| Numbers or list | A calendar-style list of dates, or a short numbered list |
| Closing | Call to action (e.g. "Come to a call"), links, logo |

## Brief for a new session

**Read first:** [BUILD.md](BUILD.md), [voice.md](voice.md), [type.md](type.md) (top section), [colour.md](colour.md), [layout.md](layout.md), [graphics.md](graphics.md), and [youtube.md](youtube.md) for how the fixed-size thumbnails were done (artboard + `--thumb-*` tokens + `.thumb-frame` scaling): slides work the same way.

**Build**

1. A fixed slide scale: `--slide-*` tokens in `system/tokens.css` for a 1920 × 1080 artboard (title, heading, body, label, quote sizes). The web scale is fluid and doesn't transfer. Body text must read from the back of a room: nothing under ~28px on the artboard.
2. `.slide` components in a commented "Slides (fixed 1920×1080)" block in `system/components.src.css` (rebuild with `python3 system/build-css.py`). Reuse grounds, torn edges, woodcuts, plates, the logo disc.
3. `examples/slides/index.html`: every slide type above with real SoR copy (from voice.md, brand.md and the manifesto), scaled to fit the page, plus a strip of thumbnails as a deck overview.
4. Rules from the system: white default ground, paper and sunlight sometimes, at most one night slide per section; red only as the logo's own red or red woodcuts; Polyamine under ~10 words, Restora beyond; four faces only.

**Then decide with Rufus** whether to also produce the deck through the Claude Slides artifact type (exports .pptx and PDF) using these rules. Keep this HTML version as the reference either way.

**Finish:** add the example to BUILD.md's "copy" table and the README examples table, update beads, commit, `git push`, republish (`python3 system/build-site.py && fl --yes site` from this folder).

**Prompt to start a session:** *Read projects/sor-design-system/slides.md, section "Brief for a new session", and follow it.*
