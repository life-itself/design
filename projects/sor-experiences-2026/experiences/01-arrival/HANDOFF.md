# Build brief: Arrival (the seeds)

Copy everything below the line into a new session: in the `life-itself/design` repo, or outside it (Claude Design, Open Design). Outside the repo, also paste `00-home/common.md` and attach the starting file `projects/sor-experiences-2026/experiences/01-arrival/build/index.html` with its `assets/` folder, plus any files named below. Suggested model: Sonnet 5.5, or Opus 5.5 for the fingerprint seeds.

**Bringing work back:** export the HTML with its assets (a zip is fine), drop it in `inbox/` at the repo root, and ask for it to be moved into the repo.

---

You are building one standalone piece of an animated, poetic website for **Seeds of Renaissance (SoR)**, a movement and vision for civilizational renewal. First read `projects/sor-experiences-2026/experiences/00-home/common.md` for the shared fonts, colours, tone and words, and follow it.

**Where this fits.** This piece is one of five that will later be joined, in order, into one long scrolling home page. That joining is done separately; you don't need to handle it. Just keep the piece self-contained: styles scoped under its class, asset paths relative (`assets/...`), and no rules on `html` or `body` beyond a margin reset.

## Your task

Polish **Arrival**, starting from the current build: `projects/sor-experiences-2026/experiences/01-arrival/build/index.html` (brought in from Claude Design; CSS already scoped under `.x-arrival`). Keep its choreography: six seeds sit clumped like a full stop, burst, swirl and each settle on a letter. Two changes:

1. **Seeds become fingerprints.** Replace the round ink dots with the actual red fingerprints from the SoR logo (`ref/sor-logo-bird-prints.png`; the ring of fingerprints is already cut out at `projects/sor-experiences-2026/experiences/00-home/sketch/assets/logo-ring.png`). Cut individual prints, keep them small, and let them turn as they fly.
2. **"heart burns" in red.** The two words are currently an orange accent. Make them the SoR red, the same red as the fingerprints. The exact red is still being chosen (beads `design-34t.1`): use `--seed-red` `#e11414` as a token so it is a one-line change later.

## What it is

The very first screen of the site. A white page, beautiful type, the seeds settling on one line of text:

> For all the living beings whose heart burns to see a new world emerge.

Feeling: awe and beauty from the first second. Quiet, alive, a little mysterious. It is the calm before the next piece (which cuts hard to black), but you don't need to build that.

## Look

- White ground (`--paper` `#fbfaf7`; the build currently uses pure white, move it to the token), ink text (`--ink` `#121110`), seed red as above.
- Headline in Polyamine. Faces per `00-home/common.md`, named in CSS and shown where installed (no web font loading for now).
- Starts white, ends white. Full viewport height.

## Rules

- Works at phone width and desktop; respects `prefers-reduced-motion`.
- No sound.

## Done when

- The seeds are fingerprints, "heart burns" is red, and nothing else about the motion has changed unless agreed.
- Tell the user what you changed.
- Record progress on beads task `design-323.12` (`bd update design-323.12 --notes "..."`; `bd close design-323.12` when done).
