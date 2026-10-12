# Podcast thumbnails: brief

A dedicated mini project: design the YouTube thumbnail (the 16:9 video cover) for Seeds of Renaissance podcast episodes, so each episode is easy to spot and click in a feed, and the series reads as one. Part of the [SoR design system](README.md); sits under [youtube.md](youtube.md) (kind 3, "Podcast episode cover") and [podcast.md](podcast.md). Started 2026-10-12.

## Context

- **The podcast** is *Seeds of Renaissance*: one name, one feed. Guest interviews (for example Iain McGilchrist, Dougald Hine, Roberto Mangabeira Unger) and Rufus–Sylvie conversations. Hosted on YouTube as video and on podcast apps as audio. See [podcast.md](podcast.md) for names and formats.
- **Why now.** The podcast is the main way new people meet the work, and on YouTube the thumbnail decides whether they click. Earlier passes were hard because the wider design system was still settling; the woodcut and botanical work of 2026-10-12 gives more to draw on.
- **Scope.** The episode thumbnail, 1280 × 720. Not channel art, not square podcast show art (3000²) and not Shorts, though decisions here should carry over to them later.

## What every version must have

1. **A significant text**: the episode's hook or a short quote from the guest. The biggest text on the image.
2. **The guest's name**, smaller.
3. **The logo** in a corner, the same corner every time.
4. **A large picture of the guest.**
5. Optionally **a background** that carries the brand and mood.

## What makes a good thumbnail (research summary)

1. **Design for feed size, not full size.** Most people see it at about 170–360 px wide, often on a phone. Anything under about 30 px tall on the 1280 × 720 artboard disappears. The name and logo are for recognition, not reading.
2. **One focal point, three elements at most.** The eye goes to the face, then the words, then the brand. Each extra element weakens the others.
3. **The face does most of the work.** Big (a third to half the height, cropped at the shoulders or tighter), expressive (mid-thought, intense, laughing; not a neutral headshot), eyes visible, ideally looking at the camera or towards the text. Cut out from its background so the background can carry the brand.
4. **Few words, big.** Three to five words, not a whole quote; a full quote rarely survives at feed size, so pull out its sharpest phrase. Bold, high contrast, no thin or light weights at small sizes.
5. **Thumbnail and title work as a pair.** Don't repeat the video title. The title can carry the topic ("Iain McGilchrist on the divided brain"), the thumbnail the hook ("We've lost the plot").
6. **Contrast and one strong colour.** Thumbnails sit among hundreds of others on white or near-black YouTube pages. Strong light-dark contrast between subject and ground matters more than palette; one saturated accent (logo red, sunlight yellow) makes it stand out. No busy texture behind the words.
7. **A series, with variety inside it.** Keep the logo corner, typeface and layout skeleton constant so viewers learn to spot an episode before they read it. Vary the face, the words and perhaps the ground colour by guest or theme.
8. **Keep the bottom-right corner clear**: YouTube puts the duration badge there. The logo goes top-left, or top-right on the side away from the face.
9. **Honest, not clickbait.** For this audience curiosity and depth beat shock. Good forms: an open question ("What comes after modernity?"), a claim with tension ("Hope isn't optimism"), a striking line from the guest. No arrows, shock faces or all caps.

## Starting proportions (1280 × 720)

| Element | Role | Size |
|---|---|---|
| Guest photo, cut out | Focal point | 50–60% of the height, one side |
| Hook or quote, 3–5 words | Second read | Text 80–140 px tall |
| Guest name | Recognition | About 36–48 px, near the face |
| Logo | Series signature | About 70–90 px, the same corner every time |
| Background | Brand and mood | Flat or quiet: night, sunlight, paper, or a faint woodcut, botanical or mountain element |

## Versions to test

- **A · Face-led**: a huge cropped face on one side, three big words on the other.
- **B · Quote-led**: the words dominate; the face smaller, in a circle or an arch.
- **C · Background-led**: one of the new elements (the brush mountain ridge, a botanical, a woodcut) as a quiet backdrop behind the face.
- **D · Colour-coded**: one layout, the ground colour changing by theme or guest.

Show each at full size **and** in a mocked YouTube feed at real size (360 px and 168 px, light and dark YouTube, with the duration badge), next to other channels' thumbnails. That is where a thumbnail succeeds or fails.

## What exists to start from

- **Current templates and the first guest cover** (`.thumb--guest`, dawn and valley backdrops): [examples/youtube/index.html](examples/youtube/index.html), live at https://sor-design-system-rufuspollock.flowershow.me/examples/youtube/index.html. Styles in `system/components.src.css` ("Thumbnails" block), tokens `--thumb-*` in `system/tokens.css`.
- **Known problems** (from [youtube.md](youtube.md#next)): at 168 px the duration badge covers the end of titles, and the "Podcast" label shrinks to about 5 px.
- **Grove covers**: six 16:9 podcast covers on sunlight with the speaker in the seed spiral, from structured to poetic: `examples/youtube/grove/podcast.html` (built by `build-podcast.py`; local, not yet committed).
- **A thumbnail workshop page**: `examples/youtube/workshop.html`, a field panel driving several artboards (local, not yet committed).
- **Earlier explorations**: Sylvie's original templates ([artifact](https://claude.ai/artifact/QEUjrhcpFTu5h9xjHP5Hco)); Uriel's channel directions round 4, with a podcast video cover per direction ([artifact](https://claude.ai/artifact/UyEW5burVcqNSzQj8GT2f1)).
- **Graphic elements to draw on**: woodcut elements in `system/woodcuts/elements/` ([gallery](https://claude.ai/artifact/6sqNWT9jeM3FJFXTGV8Guv)), blue mountain drawings in `system/mountains/elements/` (the brush ridge was liked on the About page), botanical elements in `moodboard/botanical-flower-illustration/elements/`. Most are traced from web images with no rights cleared: fine for drafts, re-source before publishing.
- **Placeholder guest photos**: `system/img/otm-guest-placeholder.jpg`, `otm-dawn-cloud.jpg`, `otm-valley.jpg`. Use a real guest photo and a real quote as soon as one is available.
- **Rules to follow**: [type.md](type.md) (Polyamine for short display text, Restora for the poetic italic), [colour.md](colour.md), [voice.md](voice.md) (title formulas), [logo.md](logo.md).

## Open questions

- Is the hook the episode title or a quote from the guest, or does it vary?
- Photo treatment: colour, greyscale, or duotone in a brand colour?
- One fixed ground for the whole series, or colour-coded by theme?
- Do Rufus–Sylvie conversations get the same layout with two faces, or a variant?

## Done when

Rufus and Sylvie pick one direction (or a combination), it is built as a reusable template in [examples/youtube/](examples/youtube/index.html) that reads at 168 px, and [youtube.md](youtube.md) and [podcast.md](podcast.md) say how to make a new episode's thumbnail.

**Prompt to start a session:** *Read projects/sor-design-system/podcast-thumbnails.md and follow it. Start by showing me the existing guest cover and the Grove covers at feed size, then build versions A to D.*
