# Arrival: frame handoffs

How to take one frame into its own working session (Claude Code, Claude Design, Open Design with Claude), and bring it back.

One HANDOFF file per frame. Each frame is first **completed standalone** (its own `build/`). **Integrating** frames into the home page is a separate exploration: [../00-home/HANDOFF.md](../00-home/HANDOFF.md).

**Progress lives in beads, not in these files:** `bd list --parent design-323`. Handoffs and briefs hold the what and how; beads hold where things stand.

Whole-page brief: [brief.md](brief.md). Rough sketch of all five frames: [sketch/index.html](sketch/index.html) · [artifact](https://claude.ai/artifact/KgQeyCfkyghWp3HPnJCRf3). Deep links jump to a moment, e.g. `#f3-70` = frame 3 at 70% of its scroll.

## Frames

| # | Frame | Handoff | Suggested model | Beads |
|---|---|---|---|---|
| 1 | Seeds | [frame-1/HANDOFF.md](frame-1/HANDOFF.md) | Sonnet 5.5 (import only) | `design-323.2` |
| 2 | Dawn | [frame-2/HANDOFF.md](frame-2/HANDOFF.md) | Sonnet 5.5 | `design-323.3` |
| 3 | The Leap | [../03-leap/HANDOFF.md](../03-leap/HANDOFF.md) | Opus 5.5 + image/video tools for assets | `design-323.4` |
| 4 | The Book | [../02-book/HANDOFF.md](../02-book/HANDOFF.md) | Opus 5.5 (+ 3D / motion tool) | `design-323.5` |
| 5 | Flight | [frame-5/HANDOFF.md](frame-5/HANDOFF.md) | Opus 5.5 | `design-323.6` |

**Model notes.** Opus 5.5 (`claude-opus-5-5`) for anything with real animation logic: scroll-scrubbed scenes, canvas/WebGL, 3D. Sonnet 5.5 (`claude-sonnet-5-5`) is enough for type-and-timing frames. Visual fine-tuning (spacing, type, colour) is best done where you can see and nudge things: Claude Design or Open Design. Asset production (clean plates, walk cycles, a 3D book) may need tools beyond a coding model; each handoff says where.

## Starting a session

Open the session in this repo (or attach the frame folder) and paste:

> Work on frame N of the Seeds of Renaissance Arrival page. Read `projects/2026-sor-experiences/experiences/<path>/HANDOFF.md` and everything it links. Build the frame as a standalone piece following the handoff rules. Save work into that folder's `build/`, and record progress on the frame's beads task (`bd update <id> --notes ...`, `bd close <id>`).

In Open Design / Claude Design without repo access: paste the HANDOFF text and attach the listed assets and screenshots. Export HTML back into the frame's `build/` folder.

## Handoff rules (provisional)

Loose on purpose: we reconcile and stitch after the frames exist, then write the formal frame contract in the [home page exploration](../00-home/HANDOFF.md) (`design-323.11`).

- **One standalone HTML page per frame**, playable on its own. Assets in a sibling `assets/` folder.
- **Scope styles** under one frame class (e.g. `.frame-leap`) so frames can later share a page without clashing.
- **Keep to the stated start and end background** (each handoff says, e.g. "starts black, ends black"); note any change in the bead.
- **State how it's driven:** scroll-scrubbed (tall section, sticky stage) or plays once reached.
- **Fonts:** Polyamine (display and body). Stand-ins are fine while sketching; name them.
- **No sound yet**, but leave room for it.

## Screenshots

Each handoff lists the moments to capture from the sketch (deep links above). Save them in the frame's `screens/` folder with the given names, as reference for the "before".
