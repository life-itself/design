# Home page: stitching the frames — handoff

The integration exploration: takes the standalone frames and assembles them into the one scrolling home (Arrival) page. Kept separate from the frames on purpose: **completing a frame standalone** and **integrating it** are two different jobs.

Page brief: [../01-arrival/brief.md](../01-arrival/brief.md). Frame handoffs: [../01-arrival/HANDOFFS.md](../01-arrival/HANDOFFS.md). Rough sketch v1 of the whole page (the reference for order and rhythm): [../01-arrival/sketch/index.html](../01-arrival/sketch/index.html) · [artifact](https://claude.ai/artifact/KgQeyCfkyghWp3HPnJCRf3).

Suggested model: **Opus 5.5**.

## Frame status

| # | Frame | Standalone | Integrated |
|---|---|---|---|
| 1 | Seeds | Done elsewhere (Claude Design); not yet in repo | No |
| 2 | Dawn | Prototype v1 (timing agreed); polish to do | No |
| 3 | The Leap | Rough sketch only | No |
| 4 | The Book | Rough sketch only | No |
| 5 | Flight | Rough sketch only | No |

A frame is ready to integrate when its `build/` plays on its own and its HANDOFF Status records start/end background and how it's driven.

## Goal

1. Write the **frame contract** from what the finished frames actually do: shared tokens (fonts, core colours, type scale), start/end backgrounds, scroll-driven vs plays-once, scoping, asset paths.
2. Reconcile the frames to it (small edits in each frame's `build/`, not rewrites).
3. Assemble them into `build/index.html` here: one scroll, frames in order, transitions between them tuned as a whole (rhythm, lengths, cuts).
4. Integrate frames as they become ready; it doesn't need all five at once.

## Done when

- `build/index.html` plays all five frames in one scroll.
- Frame contract written to `CONTRACT.md` here.
- Table above updated.

## Status

Not started. Waits for standalone frames (frame 1 is the first candidate).
