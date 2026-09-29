# Build brief: Dawn

Copy everything below the line into a new session opened in the `life-itself/design` repo. Outside the repo (Claude Design, Open Design): paste this plus the contents of `00-home/common.md`, and attach the files it names. Suggested model: Sonnet 5.5 (fine-tune visuals in Claude Design / Open Design if you like).

---

You are building one standalone piece of an animated, poetic website for **Seeds of Renaissance (SoR)**, a movement and vision for civilizational renewal. First read `projects/2026-sor-experiences/experiences/00-home/common.md` for the shared fonts, colours, tone and words, and follow it.

## Your task

Build **Dawn** as a polished, near-final standalone page at `projects/2026-sor-experiences/experiences/02-dawn/build/index.html`. A working prototype already exists at `projects/2026-sor-experiences/experiences/02-dawn/prototype.html`: start from it (its timing is agreed), remove its tuning panel, and bring the look up to the mockup.

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

Paragraph (centred serif; the phrases in bold are bold; *Revoligion* in italics):

> Human history has always been a story of transformation – of **old worlds dying and new ones being born**. Every great crisis carries within it the **seed of rebirth**. We are a movement called to bring forth a civilizational renaissance grounded in Wisdom, Interbeing, Inner growth, *Revoligion*, Complexity and beyond capitalism.

Statement (larger, light, widely spaced capitals):

> WE ARE A VISION AND MOVEMENT FOR CIVILIZATIONAL RENEWAL.

Invitation (same size and colour as the paragraph, not italic; it brightens together with the paragraph):

> [Read the full manifesto](https://docs.google.com/document/d/13ClquJ8mXP2njNb0qGr2yJjbn6p23_f28J7yVvvBSDo/edit) · or continue ↓

## Look

- Match the static mockup: `projects/2026-sor-experiences/experiences/02-dawn/moodboard/frame-2-mockup-static.png`.
- Font: Polyamine for both paragraph and statement (stand-ins: Libre Caslon Text for the paragraph, Italiana for the statement).
- Paragraph about 52 characters wide, generous line height. Big vertical space between paragraph, statement and invitation.
- Starts black, ends black. At least one full viewport high.

## Rules

- One self-contained page; scope all CSS under `.x-dawn`.
- Works at phone width and desktop. With `prefers-reduced-motion`, show the text at full brightness immediately.
- No sound.

## Done when

- `build/index.html` plays on its own, looks like the mockup, and the 12s dawn feels right.
- Tell the user which fonts you used and anything you changed from the prototype.
- Record progress on beads task `design-323.3` (`bd update design-323.3 --notes "..."`; `bd close design-323.3` when done).
