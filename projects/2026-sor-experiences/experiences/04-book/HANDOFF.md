# Build brief: The Book

Copy everything below the line into a new session opened in the `life-itself/design` repo. Outside the repo (Claude Design, Open Design): paste this plus the contents of `00-home/common.md`, and attach the files it names. Suggested model: Opus 5.5 (the book may be best made in 3D with Three.js, or as motion graphics).

---

You are building one standalone piece of an animated, poetic website for **Seeds of Renaissance (SoR)**, a movement and vision for civilizational renewal. First read `projects/2026-sor-experiences/experiences/00-home/common.md` for the shared fonts, colours, tone and words, and follow it.

## Your task

Build **The Book** as a standalone, scroll-driven page at `projects/2026-sor-experiences/experiences/04-book/build/index.html` (assets in `build/assets/`). A huge, heavy book made of lead falls out of the darkness, opens, and golden letters rise from its pages to spell what SoR offers: courses and papers.

## Reference

`projects/2026-sor-experiences/experiences/04-book/moodboard/kiefer-lead-book-open.webp`: one of Anselm Kiefer's lead books. Open, with heavy, rippled lead pages, an oxidised patina with streaks of rust red, verdigris blue and pale yellow, lit on black. This is the look to aim for.

Two routes, your choice (say which and why):
- **Animate the photo** (quickest; fine to use, fair use): it can only fall already open.
- **Recreate the book** in 3D (Three.js) or motion graphics, textured from the photo: can fall closed and heave itself open.

## Feeling

Weight, age, treasure: decades of hard-won learning, offered up. Magical rather than informational. The first priority is the book itself: its beauty and its arrival.

## What happens (scroll-driven)

The section is tall (about 4–5 viewports) with a sticky full-screen black stage; scroll scrubs the animation. Percentages are suggested scroll progress.

1. **The fall (0–16%).** Black space. The book drops in heavily from the top, accelerating, and lands with weight: a small settle, maybe a puff of dust. Ideal: it lands closed, then heaves itself open. Fallback: it lands already open.
2. **Illumination (20–40%).** Golden, illuminated-manuscript letters begin to glow on the open pages. The book itself gains a faint golden glow.
3. **Rising (44–75%).** The letters lift off the pages, float up and assemble in the black space above the book into two words, **COURSES · PAPERS**. They stay there.
4. **Caption (78%+).** A line fades in below the book.

No page turning. Don't try to print the words onto the pages themselves (it looks fake): the letters rise into clean black space instead.

## Text

- **COURSES · PAPERS**: each word is a link (use `#` for now; destinations to come).
- Caption, below the book, italic serif: *Sharing what we have learned on our journey over the past decades.*

## Look

- Black ground `#080707`. Gold `#e8c46a` with a soft glow for the letters.
- Gold letters in an illuminated display face (stand-in: Cinzel Decorative, bold). Caption in Polyamine (stand-in: Libre Caslon Text, italic), warm white `#efebe4`.
- If you use the photo, fade its edges into black (the photo's museum-case background isn't pure black).
- Starts black, ends black.

## Reference build

A rough working version exists in the whole-page sketch: `projects/2026-sor-experiences/experiences/00-home/sketch/index.html`, published at https://claude.ai/artifact/KgQeyCfkyghWp3HPnJCRf3#f4 (e.g. `#f4-35`, `#f4-95` to jump). Screenshots may be in `04-book/screens/`. It animates the photo (lands open); improve on it.

## Rules

- One self-contained page; scope all CSS under `.x-book`.
- Works at phone width and desktop. With `prefers-reduced-motion`, show the final state.
- No sound.

## Done when

- `build/index.html` plays on its own, scroll-driven, and the book feels heavy and beautiful.
- Tell the user which route you took and what would take it further.
- Record progress on beads task `design-323.5` (`bd update design-323.5 --notes "..."`; `bd close design-323.5` when done).
