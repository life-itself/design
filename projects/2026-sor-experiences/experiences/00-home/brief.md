# Home page: brief (draft)

Source: [raw/2026-09-29-arrival-feeling-and-beats.md](../../raw/2026-09-29-arrival-feeling-and-beats.md).

## What it is

The landing-page journey: a scroll that begins with the seeds and flows into the other experiences. **Movement: the leap** and **Courses: the book** are folded in as later beats. Each can also live on its own page (e.g. the leap on the join/movement page).

## Feeling

**Awe, excitement, beauty.** "Wow, this is cool." So good it provokes a little envy: beauty and depth.

- **Alive.** Constantly changing, moving. Something of the unknowable.
- **Rhythm with tension.** Like music: a steady beat stops being heard. Alternate between shiny, quick moments where people read, and slow moments where they sink in. Play dark against light, slow against a sudden "ding". Death and rebirth sit in the background; don't make them the subject.
- **Dynamic, not frantic.** Neither too fast nor too slow.
- **A journey, not one screen.** Each beat can have its own feeling and texture.
- **Experience over calls to action.** Invitations are light, and the next experience itself is the invitation.

## Medium

Most likely a scrollable web experience, where scrolling moves you through the beats. Open to it being a self-playing animation instead.

## Script

Five frames (sections of the page). Each frame can hold several beats.

**Rough sketch v1 (all five frames):** [sketch/index.html](sketch/index.html) · [artifact](https://claude.ai/artifact/KgQeyCfkyghWp3HPnJCRf3). Leap layers cut from the collage by `sketch/prep_assets.py` (rough; empty-road fill is smudgy).

**Build approach:** build and perfect one frame at a time as a standalone piece, then stitch them into the page. Each part has its own parallel folder (01-arrival … 05-flight) with its handoff; this brief is the whole-page view.

### Frame 1: Seeds

- **Background:** white.
- **Already mocked up** in a separate Claude Design session, fairly final. Good type, SoR seeds floating. Handover: HTML export into `../01-arrival/build/`; bind in at build time. (No link to frame 2 for now.)
- **Text:** *For all the living beings whose heart burns to see a new world emerge.*

### Frame 2: Dawn

- **Background:** black (sudden switch from white).
- **2a. Paragraph lights up like a dawn.** The whole paragraph starts off-dark grey, barely legible, and brightens evenly to white at the pace of a dawn: about 12s, quicker at first and lingering at the end. Not tied to scroll position.
  > *Human history has always been a story of transformation – of old worlds dying and new ones being born. Every great crisis carries within it the seed of rebirth. We are a movement called to bring forth a civilizational renaissance grounded in wisdom, interbeing, inner growth, revoligion (the evolution of religion), complexity and going beyond capitalism.*
- **2b. Six words:** stay plain text within the paragraph. They come alive later as the trees of frame 5.
- **Look** (static mockup: [../02-dawn/moodboard/frame-2-mockup-static.png](../02-dawn/moodboard/frame-2-mockup-static.png)): paragraph centred, statement below in a light, spaced, all-caps display face. The mockup shows key phrases in bold; that is dropped — body is one weight, no bold and no italic. Display face: [Polyamine](https://uicreative.net/products/polyamine-modern-classy-serif-font), unlicensed for sketching. Body face undecided.
- **Prototype v1:** [../02-dawn/prototype.html](../02-dawn/prototype.html) · [artifact](https://claude.ai/artifact/X6nxz5T2J9ykKvXFLiYbrY). Controls for dawn length and statement timing. Stand-in fonts until Polyamine is installed.
- **2c. Statement,** larger type: *We are a vision and movement for civilizational renewal.*
- **2d. Light invitation:** read the full manifesto, or keep going. Dawns together with the paragraph, same colour, not italic.

### Frame 3: The leap

- Own brief: [../03-leap/brief.md](../03-leap/brief.md). Plays once when it comes into view (not scroll-driven): the people in the collage walk up the road, the paper tears to reveal the yellow field, "Come join us".
- **The join offer lives here** (meetup), alongside a "keep learning" path onward to the book. Many won't join now, but they know the invitation is there.

### Frame 4: The book

- Own brief: [../04-book/brief.md](../04-book/brief.md). A heavy Kiefer-like lead book drops in from the top and falls open. Golden illuminated letters glow on the pages, rise and assemble above it: *Courses · Papers*. Caption below: *Sharing what we have learned on our journey over the past decades.* No page turning.

### Frame 5: Flight (closing)

The ending: a story of hope, authentic and credible. No further acknowledgement of darkness needed; frames 2–3 carry it.

- **Background:** white, high contrast. Swallows in black, like the logo. Spirit of a Japanese print (Hokusai-like treatment of space), or simply clean black on white.
- **5a. Logo.** The SoR logo (swallow in a ring of red fingerprints) with a short line. Wording to find: not "building a movement", not "a vision for civilizational renewal" (used in frame 2).
- **5b. Portal.** The swallow flies out of the logo and into the ring of fingerprints, now a portal. More swallows arrive and fly through. The portal keeps widening until it passes the edges of the screen and the red is gone: only swallows flying, in flocks.
- **5c. Trees.** From the bottom of the page, trees grow up. Each tree holds one of the principles in its letters (Wisdom, Interbeing, Inner growth, Revoligion, Complexity, Beyond capitalism). The seeds have become trees. (Flagged as possibly too much; try it.)
- **5d. Settle.** The swallows come to rest on the trees. End.

## Assets

- **Frame 1 design**: exists (Claude Design); HTML export to come.
- **Frame 2 static mockup**: [../02-dawn/moodboard/frame-2-mockup-static.png](../02-dawn/moodboard/frame-2-mockup-static.png).
- **SoR logo**: [ref/sor-logo-bird-prints.png](../../../../ref/sor-logo-bird-prints.png). Black swallow at the centre of a radiating burst of red fingerprints (the seeds).
- **Font**: Polyamine (link above) for display; needs installing locally / self-hosting for prototypes — today it is loaded via `local()` only, so anyone without it installed sees the Italiana fallback. Body face still to choose.
- **Sound**: wanted (ambient wind/birds, or music). Not defined yet.

## Open questions

- Book line: final wording.
- Colour: none needed yet, beyond maybe the six words and the book's patina.
- "Revoligion" chosen for now. Keep the gloss "(the evolution of religion)" on first use, since readers may take the word for a typo.
