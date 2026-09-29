# Build brief: Arrival (the seeds)

Copy everything below the line into a new session opened in the `life-itself/design` repo. Outside the repo (Claude Design, Open Design): paste this plus the contents of `00-home/common.md`, and attach the files it names. Suggested model: Sonnet 5.5.

---

You are building one standalone piece of an animated, poetic website for **Seeds of Renaissance (SoR)**, a movement and vision for civilizational renewal. First read `projects/2026-sor-experiences/experiences/00-home/common.md` for the shared fonts, colours, tone and words, and follow it.

## Your task

Bring the **Arrival** piece into the repo as a standalone web page. The design already exists and is close to final: it was made in Claude Design / Open Design. Your job is to get its HTML export into `projects/2026-sor-experiences/experiences/01-arrival/build/index.html` (assets in `build/assets/`), tidy it, and make it play correctly on its own. Don't redesign it.

If you don't have the export, ask the user for it (HTML export or a link) before doing anything else.

## What it is

The very first screen of the site. A white page, beautiful type, the SoR "seeds" (red fingerprint marks from the logo) floating gently. One line of text:

> For all the living beings whose heart burns to see a new world emerge.

Feeling: awe and beauty from the first second. Quiet, alive, a little mysterious. It is the calm before the next piece (which cuts hard to black), but you don't need to build that.

## Look

- White ground (`--paper` `#fbfaf7`), ink text (`--ink` `#121110`), seed red `#e11414`.
- Font: Polyamine (stand-in: Italiana). Keep whatever the existing design uses if it differs, and note it.
- Starts white, ends white. Full viewport height.

## Assets

- The Claude Design / Open Design export (from the user).
- SoR logo: `ref/sor-logo-bird-prints.png` (black swallow in a burst of red fingerprints).

## Rules

- One self-contained page; scope all CSS under `.x-arrival` so it can later sit on a page with other pieces.
- Works at phone width and desktop; respects `prefers-reduced-motion`.
- No sound.

## Done when

- `build/index.html` opens in a browser and matches the existing design.
- Tell the user what you changed during tidying, and whether the animation plays on load or is driven by scroll.
- Record progress on beads task `design-323.2` (`bd update design-323.2 --notes "..."`; `bd close design-323.2` when done).
