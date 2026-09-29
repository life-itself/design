# Frame 3: The Leap — handoff

Frame 3 of the Arrival page ([Arrival brief](../01-arrival/brief.md), [all handoffs](../01-arrival/HANDOFFS.md)); can also stand alone on a join/movement page. Full brief: [brief.md](brief.md).

Suggested model: **Opus 5.5** for the scroll scene. Asset work (clean plate, walk cycles) needs image/video tools: Photoshop generative fill or an image model for the plate; cutout puppetry (After Effects, Rive) or an image-to-video model for walking figures.

## Goal

Turn the collage into a scroll-driven scene: people walk up an empty road towards a cliff of sky, the paper tears open onto a yellow field, and the invitation to join appears.

## Feeling

Walking into the unknown: scary, yet we hold the possibility of renewal. Tension ("they'll walk off the edge!"), then a gentle opening into colour. Ends warm and concrete.

## Beats (scroll-driven)

1. **The cliff.** Grey clouds, empty road ending in sky. No people, no tear. Text 1.
2. **Walking.** People walk in from behind the viewer and up the road, one by one. Real walking figures if possible. Text 2.
3. **The rip.** As the leaders near the edge, the paper tears **gently, top down**, as if pulled from the top. Reveals the yellow field and blue sky. Walkers step on into it.
4. **Join.** Invitation to join.
5. **Onward** to the Book.

## Text (placeholders; final to come)

1. *Walking into the unknown can be frightening.*
2. *But as we walk, we hold the possibility of renewal.*
4. **COME JOIN US** · *Meet others on our Thursday calls* (link to come) · *or keep learning ↓*

## Assets

- Source collage: [moodboard/leap-collage-walkers-torn-field.png](moodboard/leap-collage-walkers-torn-field.png) (512×512; higher-res or the original photo would help a lot: try a reverse image search).
- Rough layers cut by script ([../01-arrival/sketch/prep_assets.py](../01-arrival/sketch/prep_assets.py)) in [../01-arrival/sketch/assets/](../01-arrival/sketch/assets/): `leap-plate.jpg` (empty road; the people-area fill is smudgy), `leap-tear.png`, `leap-people.png` (all walkers as one layer).
- Font: Polyamine.

## Current state

In the sketch at `#f3`. Works end to end but rough: smudgy empty road, walkers slide as one group, tear edge is a simple zigzag clip.

Screenshots to capture into `screens/`: `sketch-v1-f3-05.png` (`#f3-5`), `-45` (`#f3-45`), `-72` (`#f3-72`), `-95` (`#f3-95`).

## Main production tasks

1. Clean plate: road and sky with no people and no tear.
2. Each walker as its own layer, with a walk cycle.
3. A convincing paper tear: fibrous white edge, slight depth and shadow, opening top down.

## Open questions

- Does colour spill out of the tear into the frame, or stay contained?
- Join wording and link.

## Done when

- `build/index.html` plays on its own, scroll-driven, and reads as the brief.
- Status records: starts dark grey, ends with the field; scroll-driven.

## Status

Rough sketch v1 only.
