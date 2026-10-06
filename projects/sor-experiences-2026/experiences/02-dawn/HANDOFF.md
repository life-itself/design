# Build brief: Dawn

## Iterating on this frame

To keep working on what exists, open a new session in this repo and start with:

> Let's iterate on frame 2, Dawn: `projects/sor-experiences-2026/experiences/02-dawn/build/index.html`. For context read `projects/sor-experiences-2026/experiences/00-home/common.md` and `projects/sor-experiences-2026/experiences/02-dawn/HANDOFF.md`. Open it in the browser pane (the `static` preview) so we can look at it together. First change: …

No need to paste the brief below for that. The brief is for starting the frame afresh, or for working on it outside the repo.

## Starting afresh, or outside the repo

Copy everything below the line into a new session: in the `life-itself/design` repo, or outside it (Claude Design, Open Design). Outside the repo, also paste `00-home/common.md` and attach the starting file `projects/sor-experiences-2026/experiences/02-dawn/build/index.html` with its `assets/` folder, plus any files named below. Suggested model: Sonnet 5.5.

**Bringing work back:** export the HTML with its assets (a zip is fine), drop it in `inbox/` at the repo root, and ask for it to be moved into the repo.

---

You are building one standalone piece of an animated, poetic website for **Seeds of Renaissance (SoR)**, a movement and vision for civilizational renewal. First read `projects/sor-experiences-2026/experiences/00-home/common.md` for the shared fonts, colours, tone and words, and follow it.

**Where this fits.** This piece is one of five that will later be joined, in order, into one long scrolling home page. That joining is done separately; you don't need to handle it. Just keep the piece self-contained: styles scoped under its class, asset paths relative (`assets/...`), and no rules on `html` or `body` beyond a margin reset.

## Your task

Polish **Dawn**, starting from the current build: `projects/sor-experiences-2026/experiences/02-dawn/build/index.html` (scoped under `.x-dawn`; timing agreed). Bring the look up to the mockup. The earlier `prototype.html` has a tuning panel for dawn length and statement timing if you need to revisit them.

## What it is

A full-screen black section. On it, a paragraph that starts almost invisible and slowly becomes readable, like first light at dawn. Below it, a short statement in large capitals, and a quiet invitation.

Feeling: calm, deep, a little mysterious. The reader shouldn't notice the text brightening until they realise they can read it. On the site it follows a white opening screen, so it lands as a sudden cut to black; built alone, just start on black.

## What happens

1. The section is black (`#080707`).
2. When most of the section is on screen, the **dawn** starts (it plays once; it is not tied to scroll position):
   - The paragraph and the invitation start in an off-dark grey (`#2a2725`), barely legible.
   - They brighten evenly to warm white (`#efebe4`) over **12 seconds**, quicker at first and lingering at the end. The prototype uses `transition: color 12s cubic-bezier(.25, .6, .35, 1)`.
3. The statement is visible in warm white throughout.

## Text (exact)

Paragraph (centred; one weight, no bold, no italic, as the body face rule says; the mockup's bold is dropped):

> Human history has always been a story of transformation – of old worlds dying and new ones being born. Every great crisis carries within it the seed of rebirth. We are a movement called to bring forth a civilizational renaissance grounded in Wisdom, Interbeing, Inner growth, Revoligion, Complexity and beyond capitalism.

Statement (larger, light, widely spaced capitals):

> WE ARE A VISION AND MOVEMENT FOR CIVILIZATIONAL RENEWAL.

Invitation (same size and colour as the paragraph, not italic; it brightens together with the paragraph):

> [Read the full manifesto](https://docs.google.com/document/d/13ClquJ8mXP2njNb0qGr2yJjbn6p23_f28J7yVvvBSDo/edit) · or continue ↓

## Look

- Match the static mockup: `projects/sor-experiences-2026/experiences/02-dawn/moodboard/frame-2-mockup-static.png`.
- Paragraph and invitation in Bricolage Grotesque (body), statement in Polyamine. Faces per `00-home/common.md`, named in CSS and shown where installed (no web font loading for now).
- Paragraph about 52 characters wide, generous line height. Big vertical space between paragraph, statement and invitation.
- Starts black, ends black. At least one full viewport high.

## Rules

- Works at phone width and desktop. With `prefers-reduced-motion`, show the text at full brightness immediately.
- No sound.

## Done when

- `build/index.html` plays on its own, looks like the mockup, and the 12s dawn feels right.
- Tell the user which fonts you used and anything you changed from the prototype.
- Record progress on beads task `design-323.3` (`bd update design-323.3 --notes "..."`; `bd close design-323.3` when done).
