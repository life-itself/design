# Build brief: The Leap

Copy everything below the line into a new session opened in the `life-itself/design` repo. Outside the repo (Claude Design, Open Design): paste this plus the contents of `00-home/common.md`, and attach the files it names. Suggested model: Opus 5.5. Asset work may also need image/video tools (see below).

---

You are building one standalone piece of an animated, poetic website for **Seeds of Renaissance (SoR)**, a movement and vision for civilizational renewal. First read `projects/sor-experiences-2026/experiences/00-home/common.md` for the shared fonts, colours, tone and words, and follow it.

## Your task

Build **The Leap** as a standalone page at `projects/sor-experiences-2026/experiences/03-leap/build/index.html` (assets in `build/assets/`). It animates a photo collage: people walk up a road that ends in empty sky, then the paper tears open onto a yellow field, and the visitor is invited to join the movement.

## The source image

`projects/sor-experiences-2026/experiences/03-leap/moodboard/leap-collage-walkers-torn-field.png` (512×512). A black-and-white photo collage: a line of people in dark coats walk away from us along a road into heavy grey clouds. Ahead of them, a torn-paper hole opens onto colour: a yellow flower field under a blue sky. **Animate this image itself**, using its own people; don't replace them with illustrations. Using the image is fine (fair use, nonprofit).

## Feeling

Walking into the unknown: scary, yet we hold the possibility of renewal. A leap of faith. Tension builds ("they're going to walk off the edge of the sky!"), then a gentle, not violent, opening into colour. It ends warm and concrete: come and meet us.

## What happens (scroll-driven)

The section is tall (about 6 viewports) with a sticky full-screen stage; scroll position scrubs the animation forwards and backwards. Deep links like `#leap-72` jump to a moment.

1. **The cliff.** Grey clouds and the road, which simply ends in sky like a cliff edge. **No people and no tear yet.** Text 1 fades in at the top, over the sky.
2. **Walking.** The people walk in from behind the viewer and up the road, one by one, towards the edge. Real walking movement if at all possible, not sliding cutouts. Text 1 fades out a moment before text 2, leaving a beat of just the walkers.
3. **The rip.** Just before the rip starts, text 2 appears at the top, where text 1 was, and holds through the rip. As the leading walkers near the edge, the paper tears **gently, from the top down**, as if someone is pulling it from the top. It reveals the yellow field and blue sky; the road now leads into it.
4. **Into the field.** The walkers step on towards and into the field. The grey scene lightens a little.
5. **Join.** Text 2 fades and the invitation appears over the image, in the lower third, on a soft dark gradient for legibility. It is the story's last beat, not a footer. If it doesn't read on phones, move it below the image at phone width only.

## Text

1. **The future may be dark and unknown.** (top, over the sky)
2. **But the unknown is also full of possibility.** (top, replacing line 1)
3. **COME JOIN US** (display capitals; this is the link), then small beneath: *Meet others on our Thursday calls*, then smaller still and secondary: *or keep learning ↓*

The join links to a page about the Thursday call (what, when, sign up), not straight to Zoom or a calendar. Use `#` until the URL exists.

## Look

- The background image runs **full width**, edge to edge (it looks better that way than a centred square). May need the high-res original photo.
- Text in warm white `#efebe4`, laid over the image: lines 1 and 2 at the top, the join in the lower third. Faces per `00-home/common.md`, by name only (shown where installed): Restora for lines 1–2, Polyamine for COME JOIN US, Bricolage Grotesque for the small lines.
- The tear is paper: rough white fibrous edge, slight depth and shadow, as in the source image.
- Colour stays inside the tear for now (whether it spills out is an open question; make it easy to try).
- Starts dark grey, ends on the field.

## Assets and production

What you need, and what exists:

1. **Clean plate**: road and clouds with no people and no tear. A rough one exists (`projects/sor-experiences-2026/experiences/00-home/sketch/assets/leap-plate.jpg`) but the area where the people were is a smudgy fill. Better: find the original photo (reverse image search on the collage) or retouch properly (Photoshop generative fill or an image model). If you can't, use the rough plate and say so.
2. **Walkers**: each person as its own transparent layer. A rough single layer of all walkers exists: `projects/sor-experiences-2026/experiences/00-home/sketch/assets/leap-people.png`. For walking motion: cutout puppetry (split legs/arms, bob), an image-to-video model on the stills, or After Effects/Rive.
3. **Tear layer**: the field and sky with the torn edge. Rough one: `projects/sor-experiences-2026/experiences/00-home/sketch/assets/leap-tear.png`.

The script that cut the rough layers: `projects/sor-experiences-2026/experiences/00-home/sketch/prep_assets.py`.

## Reference build

A rough working version exists in the whole-page sketch: `projects/sor-experiences-2026/experiences/00-home/sketch/index.html`, published at https://claude.ai/artifact/KgQeyCfkyghWp3HPnJCRf3#f3 (e.g. `#f3-72` jumps to the tear). Screenshots may be in `03-leap/screens/`. Improve on it; don't copy its shortcuts (walkers move as one block, zigzag tear edge).

## Rules

- One self-contained page; scope all CSS under `.x-leap`.
- Works at phone width and desktop. With `prefers-reduced-motion`, show the final state with the text.
- No sound.

## Done when

- `build/index.html` plays on its own, scroll-driven, and reads as the story above.
- Tell the user what's still rough (plate, walk cycles) and what would fix it.
- Record progress on beads task `design-323.4` (`bd update design-323.4 --notes "..."`; `bd close design-323.4` when done).
