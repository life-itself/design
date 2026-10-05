# Build brief: Flight

Copy everything below the line into a new session opened in the `life-itself/design` repo. Outside the repo (Claude Design, Open Design): paste this plus the contents of `00-home/common.md`, and attach the files it names. Suggested model: Opus 5.5.

---

You are building one standalone piece of an animated, poetic website for **Seeds of Renaissance (SoR)**, a movement and vision for civilizational renewal. First read `projects/sor-experiences-2026/experiences/00-home/common.md` for the shared fonts, colours, tone and words, and follow it.

## Your task

Build **Flight** as a standalone, scroll-driven page at `projects/sor-experiences-2026/experiences/05-flight/build/index.html` (assets in `build/assets/`). The swallow leaves the SoR logo, flocks of swallows pour through the logo's ring of fingerprints as it opens like a portal, six trees grow from the ground, and the birds come to rest on them. It is the closing scene of the site.

## The logo

`ref/sor-logo-bird-prints.png`: a black swallow in flight at the centre of a radiating burst of red fingerprints (the fingerprints are the "seeds"). Split layers already cut: `projects/sor-experiences-2026/experiences/00-home/sketch/assets/swallow.png` (the swallow, black on transparent, facing up-right) and `.../00-home/sketch/assets/logo-ring.png` (the red fingerprints on transparent).

## Feeling

Authentic, credible hope. Lightness and release after heavier scenes. High contrast: black swallows on white, in the spirit of a Japanese print (Hokusai-like use of empty space), or simply clean black on white.

## What happens (scroll-driven)

The section is tall (about 6 viewports) with a sticky full-screen white stage; scroll scrubs the animation. Percentages are suggested scroll progress.

1. **Logo (0–10%).** The logo, centred, with a short line of text beneath.
2. **Take-off (8–25%).** The swallow flies out of the logo, loops, and flies back into the ring of fingerprints, now a portal.
3. **Portal (20–62%).** More and more swallows fly in from the edges of the screen and through the portal. The ring keeps widening until it passes the edges of the screen and the red is gone: only swallows, flying in flocks.
4. **Trees (62–86%).** From the bottom of the screen, six trees grow up, each holding one principle: **Wisdom · Interbeing · Inner growth · Revoligion · Complexity · Beyond capitalism**. The seeds have become trees. (This may be too much; build it and let the user judge.)
5. **Settle (86–100%).** The swallows come to rest on the branches. End.

## Text

- Under the logo: **line to be decided**. Use *Seeds of Renaissance* as a placeholder. Don't use "building a movement".
- The six tree words as above (spelling exact; *Revoligion* is deliberate).

## Look

- White ground `#fbfaf7`, ink `#121110` for swallows and trees, the ring in its own red.
- Swallows: ideally with a wingbeat (a few drawn frames or a simple procedural flap) and natural flocking, not static stamps.
- Trees: brush or ink style rather than plain lines; the word carried in the tree (canopy or trunk) rather than as a label under it, if you can make it readable.
- Words in Polyamine display capitals (stand-in: Italiana).
- Starts white, ends white.

## Reference build

A rough working version exists in the whole-page sketch: `projects/sor-experiences-2026/experiences/00-home/sketch/index.html`, published at https://claude.ai/artifact/KgQeyCfkyghWp3HPnJCRf3#f5 (e.g. `#f5-40`, `#f5-100` to jump). Screenshots may be in `05-flight/screens/`. It uses canvas for birds and trees; improve on it.

## Rules

- One self-contained page; scope all CSS under `.x-flight`.
- Works at phone width and desktop. With `prefers-reduced-motion`, show the final state (trees with birds).
- No sound.

## Done when

- `build/index.html` plays on its own, scroll-driven, and ends on the birds settled in the trees.
- Tell the user what's still rough and any wording you need.
- Record progress on beads task `design-323.6` (`bd update design-323.6 --notes "..."`; `bd close design-323.6` when done).
