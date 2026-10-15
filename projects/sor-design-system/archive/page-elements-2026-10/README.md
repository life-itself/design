# Elements on pages, working record (October 2026)

Sylvie's experiments placing woodcut, botanical and mountain elements on the website pages, 12–15 October 2026. Not final and not part of the system yet; kept so the tries and what came out of them aren't lost. Not published.

## The canvas

**SoR Website Page Mockups (Sylvie copy):** https://claude.ai/artifact/9ZFRMXLkpXLaS7ztyz8UAU

A Claude Design canvas, private to its owner: share it from the page's Share menu before sending the link to anyone. It is a copy of the colleague's page mockups (shared original: https://claude.ai/artifact/72AAYDbkez9TrCDh5pehsh). Its artboards:

| Artboard | What it is |
|---|---|
| About, Media House, Courses | The colleague's mockups as copied, unchanged |
| About · with woodcuts, Media House · with woodcuts, Courses · with woodcuts (second row) | First try: woodcuts drawn in code (see below), faint behind text and small beside photos. **Rejected:** they felt lifeless next to the mood board |
| About · elements v1 | Sylvie's placements with the traced [woodcut elements](../../system/woodcuts/elements/README.md): red round flowers under "Read our manifesto", a faded green pinecone under "We are not here to decorate the old paradigm", a large faded pomegranate (black and print red) under the "Why now?" text in place of the seed row |
| About · botanical v1 | Sylvie's placements with the botanical elements (`moodboard/botanical-flower-illustration/elements/`): the open tulip over a barely visible Metatron's cube in the hero (photo and spiral removed), Chinese peaches in place of the "Why now?" photo, the red watercolour flower under the manifesto button, mark 5312 and the green ink watercolour faded under their headings, and the [brush ridge](../../system/mountains/README.md) (ultramarine) in place of the last photo. The blue linocut mountains with a sun were tried there and swapped back |

The canvas's version history holds every step (labels such as "About with elements v1", "About botanical: back to brush ridge").

## What we learned

- **Woodcuts drawn in code feel dead.** Even, symmetrical, formula curves with a roughening filter don't carry the life of a hand-cut print. The mood board pieces feel alive because of the hand. Elements should start from hand-made marks (our own, public-domain prints, or carefully chosen sources) and use code only to clean and trace them.
- **The growing sprout idea worked** (`system/woodcuts/sprout-growing.svg`): growth over time reads as rebirth and renewal. Worth redrawing by hand.
- **Placement that works:** one element per section at most, in the empty space beside a heading or under a short text, faded when it sits near reading text; several sections stay bare.
- **Two directions to compare:** woodcut (About · elements v1) against botanical (About · botanical v1), on the same page and text.

## `woodcut-drafts/`

The code-drawn woodcuts from 12 October, moved here from `system/woodcuts/drafts/`. `review.html` shows round 1: leaves rising and falling, a sprout from the soil, the sprout growing in five stages. Sylvie kept all four, so their SVGs are now in the library (`system/woodcuts/`, see [woodcuts.html](../../woodcuts.html)); `wc_new.py` here is the script that drew them. Round 2, the same shapes in colour, was dropped and deleted.

## Open from this work

- Remove woodcut plates 1 and 4 (two swallows), 8–12 (leaves, wind), 13–16 (fruit) and 17 (circle of chairs) from the library page, as Sylvie asked on 12 October; leaves, wind and fruit to be redone.
- A written guide for graphic elements (feel, principles, when to use which, colour rules, how to make new ones), extending [graphics.md](../../graphics.md), once the woodcut or botanical direction is chosen.
