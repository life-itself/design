# Build brief: Home page (joining the pieces)

Copy everything below the line into a new session opened in the `life-itself/design` repo. Outside the repo (Claude Design, Open Design): paste this plus the contents of `00-home/common.md`, and attach the files it names. Suggested model: Opus 5.5. Run it once one or more pieces have a standalone build; it can be repeated as more arrive.

---

You are assembling the home page of an animated, poetic website for **Seeds of Renaissance (SoR)**, a movement and vision for civilizational renewal. First read `projects/2026-sor-experiences/experiences/00-home/common.md` (shared fonts, colours, tone, words, and the start/end background of each piece) and `projects/2026-sor-experiences/experiences/00-home/brief.md` (the whole page: feeling and script).

## Your task

The home page is one long scroll made of five pieces, each built separately as a standalone page:

| # | Piece | Standalone build |
|---|---|---|
| 1 | Arrival (the seeds, white) | `projects/2026-sor-experiences/experiences/01-arrival/build/` |
| 2 | Dawn (text lights up on black) | `projects/2026-sor-experiences/experiences/02-dawn/build/` |
| 3 | The Leap (walkers, the tear, join us) | `projects/2026-sor-experiences/experiences/03-leap/build/` |
| 4 | The Book (lead book, gold letters) | `projects/2026-sor-experiences/experiences/04-book/build/` |
| 5 | Flight (swallows, portal, trees) | `projects/2026-sor-experiences/experiences/05-flight/build/` |

Check which builds exist (`bd list --parent design-323` also shows progress). Then:

1. **Write the frame contract** to `projects/2026-sor-experiences/experiences/00-home/CONTRACT.md`, based on what the builds actually do and extending `common.md`: shared tokens (fonts, colours, type scale), each piece's start/end background, how each is driven (scroll-scrubbed vs plays once reached), CSS scoping (`.x-<name>`), asset paths, how a piece is mounted on the page.
2. **Reconcile** the pieces to it with small edits in their `build/` folders, not rewrites. List anything that needs a bigger change for the user rather than doing it.
3. **Assemble** `projects/2026-sor-experiences/experiences/00-home/build/index.html`: all available pieces in order on one scroll, shared tokens loaded once, each piece's CSS and JS still scoped. For pieces without a build yet, use the corresponding section of the rough sketch (`projects/2026-sor-experiences/experiences/00-home/sketch/index.html`) as a placeholder.
4. **Tune the whole**: the cuts between pieces (white → black → dark grey → black → white), the scroll length of each piece, and the overall rhythm. The brief wants rhythm with tension: fast then slow, a sudden cut after a long build, nothing monotonous.

## Reference

The rough sketch of the whole page shows the intended order and rhythm: https://claude.ai/artifact/KgQeyCfkyghWp3HPnJCRf3 (source: `projects/2026-sor-experiences/experiences/00-home/sketch/index.html`).

## Done when

- `build/index.html` plays every available piece in one scroll, at phone width and desktop.
- `CONTRACT.md` written.
- Tell the user what you reconciled, what needs bigger changes, and how the rhythm feels.
- Record progress on beads task `design-323.11` (`bd update design-323.11 --notes "..."`), including which pieces are integrated.
