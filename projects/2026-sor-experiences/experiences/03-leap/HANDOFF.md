# Build brief: The Leap

Copy everything below the line into a new session opened in the `life-itself/design` repo. Outside the repo (Claude Design, Open Design): paste this plus the contents of `00-home/common.md`, and attach the files it names. Suggested model: Opus 5.5. Asset work may also need image/video tools (see below).

---

You are building one standalone piece of an animated, poetic website for **Seeds of Renaissance (SoR)**, a movement and vision for civilizational renewal. First read `projects/2026-sor-experiences/experiences/00-home/common.md` for the shared fonts, colours, tone and words, and follow it.

## Your task

Build **The Leap** as a standalone, scroll-driven page at `projects/2026-sor-experiences/experiences/03-leap/build/index.html` (assets in `build/assets/`). It animates a photo collage: people walk up a road that ends in empty sky, then the paper tears open onto a yellow field, and the visitor is invited to join the movement.

## The source image

`projects/2026-sor-experiences/experiences/03-leap/moodboard/leap-collage-walkers-torn-field.png` (512×512). A black-and-white photo collage: a line of people in dark coats walk away from us along a road into heavy grey clouds. Ahead of them, a torn-paper hole opens onto colour: a yellow flower field under a blue sky. **Animate this image itself**, using its own people; don't replace them with illustrations. Using the image is fine (fair use, nonprofit).

## Feeling

Walking into the unknown: scary, yet we hold the possibility of renewal. A leap of faith. Tension builds ("they're going to walk off the edge of the sky!"), then a gentle, not violent, opening into colour. It ends warm and concrete: come and meet us.

## What happens (scroll-driven)

The section is tall (about 6 viewports) with a sticky full-screen stage; scroll position scrubs the animation forwards and backwards. Percentages are suggested scroll progress.

1. **The cliff (0–10%).** Grey clouds and the road, which simply ends in sky like a cliff edge. **No people and no tear yet.** Text 1 fades in.
2. **Walking (10–55%).** The people walk in from behind the viewer and up the road, one by one, towards the edge. Real walking movement if at all possible, not sliding cutouts. Text 1 gives way to text 2.
3. **The rip (52–74%).** As the leading walkers near the edge, the paper tears **gently, from the top down**, as if someone is pulling it from the top. It reveals the yellow field and blue sky; the road now leads into it.
4. **Into the field (74–90%).** The walkers step on towards and into the field. The grey scene lightens a little.
5. **Join (80–100%).** The invitation appears.

## Text (placeholders; final wording to come)

1. *Walking into the unknown can be frightening.*
2. *But as we walk, we hold the possibility of renewal.*
3. **COME JOIN US** (display capitals), then smaller: *Meet others on our Thursday calls* (link: `#` for now) · *or keep learning ↓*

## Look

- Stage background around the image: very dark grey `#161616`. The image fills most of the screen (square, about `min(92vw, 78vh)`).
- Text in warm white `#efebe4`, Polyamine (stand-ins: Libre Caslon Text for lines, Italiana for COME JOIN US), below the image.
- The tear is paper: rough white fibrous edge, slight depth and shadow, as in the source image.
- Colour stays inside the tear for now (whether it spills out is an open question; make it easy to try).
- Starts dark grey, ends on the field.

## Assets and production

What you need, and what exists:

1. **Clean plate**: road and clouds with no people and no tear. A rough one exists (`projects/2026-sor-experiences/experiences/00-home/sketch/assets/leap-plate.jpg`) but the area where the people were is a smudgy fill. Better: find the original photo (reverse image search on the collage) or retouch properly (Photoshop generative fill or an image model). If you can't, use the rough plate and say so.
2. **Walkers**: each person as its own transparent layer. A rough single layer of all walkers exists: `projects/2026-sor-experiences/experiences/00-home/sketch/assets/leap-people.png`. For walking motion: cutout puppetry (split legs/arms, bob), an image-to-video model on the stills, or After Effects/Rive.
3. **Tear layer**: the field and sky with the torn edge. Rough one: `projects/2026-sor-experiences/experiences/00-home/sketch/assets/leap-tear.png`.

The script that cut the rough layers: `projects/2026-sor-experiences/experiences/00-home/sketch/prep_assets.py`.

## Reference build

A rough working version exists in the whole-page sketch: `projects/2026-sor-experiences/experiences/00-home/sketch/index.html`, published at https://claude.ai/artifact/KgQeyCfkyghWp3HPnJCRf3#f3 (e.g. `#f3-72` jumps to the tear). Screenshots may be in `03-leap/screens/`. Improve on it; don't copy its shortcuts (walkers move as one block, zigzag tear edge).

## Rules

- One self-contained page; scope all CSS under `.x-leap`.
- Works at phone width and desktop. With `prefers-reduced-motion`, show the final state with the text.
- No sound.

## Done when

- `build/index.html` plays on its own, scroll-driven, and reads as the story above.
- Tell the user what's still rough (plate, walk cycles) and what would fix it.
- Record progress on beads task `design-323.4` (`bd update design-323.4 --notes "..."`; `bd close design-323.4` when done).
