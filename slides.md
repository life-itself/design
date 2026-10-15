# Slides

Slide decks in the Seeds of Renaissance system: talks, calls, workshops, pitches. Part of the [SoR design system](README.md).

## Make a deck with your agent

Paste this into your AI agent, in whichever repo you're working in, and fill in the brackets. It gives you a deck to present from the browser and a PDF.

```text
Make a slide deck for Seeds of Renaissance: [the talk, the event and date, the speakers].
Here is the outline: [the outline or text, or a path to it].
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system (or, if that folder isn't there,
https://design.seedsofrenaissance.org/AGENTS.md). Follow its "Slides" route and
read only what it names. Don't change anything in the design repo.
Give me the deck as an HTML page I can present from, and a PDF.
Ask me for anything you need that you can't find. Then tell me what you checked
and what you guessed.
```

**See them:** [example decks](examples/slides/index.html): [Study](examples/slides/study.html), fifteen slides on the Wisdom paper, and [Gathering](examples/slides/gathering.html), ten slides for a community call. By hand, copy the closer one; open it in Chrome and print it to save a PDF, one slide per page.

## Two registers

Both on a fixed 1920 × 1080 artboard, sharing one set of slide types.

- **Study**, for white papers and research talks: claims as sentences in Restora, evidence below (figures, short lists, tables, quotes), Polyamine on the cover only.
- **Gathering**, for calls, community and art: Polyamine titles, sunlight and night grounds, photographs torn into the page, woodcuts.

## Slide types

| Slide | What it holds |
|---|---|
| Title | Talk title (Polyamine), speaker, date or event, the logo |
| Section | A chapter break: one or two words of Polyamine on a ground, perhaps a woodcut |
| Content | A heading and up to five short points, or a short paragraph |
| Quote | A pull quote in Restora with attribution (the length rule: past ~10 words it's Restora) |
| Image | A full-bleed photograph with a caption as a plate (`Fig. N`) |
| Image + text | Plate on one side, heading and text on the other |
| Numbers or list | A calendar-style list of dates, or a short numbered list |
| Closing | Call to action (e.g. "Come to a call"), links, logo |

## Rules for slides

- A fixed scale, not the fluid web scale: the `--slide-*` tokens in [examples/slides/slides.css](examples/slides/slides.css) for the 1920 × 1080 artboard (title, section, heading, quote, points, labels, captions).
- Text must read from the back of a room: nothing under 28px on the artboard.
- White is the default ground, paper and sunlight sometimes, at most one night slide per section.
- Red only as the logo's own red, a red seed or woodcut, and the house diagrams.
- Polyamine under ~10 words, Restora beyond; four faces only.
- Photographs flat and square. Reuse the system's grounds, torn edges, woodcuts, plates and logo.
- Real SoR copy, from [Voice](voice.md), [Brand](brand.md) and the manifesto.
- The HTML decks are the reference. A deck made another way (for example the Claude Slides artifact type, which exports .pptx and PDF) follows the same rules.

Decisions: [planning 2608](https://github.com/life-itself/planning/blob/main/projects/2608-seeds-of-renaissance-rebrand.md) · [decision log](decisions.md)
