# Podcast thumbnails: brief (done, archived)

**Archived 2026-10-13.** The mini project is done: the chosen design is the swallows-and-fingerprints thumbnail, built as a Canva kit in [examples/youtube/canva-kit/](../../examples/youtube/canva-kit/README.md), with matching [Instagram posts](../../examples/social/instagram/README.md). What was tried is listed in [README.md](README.md). The brief below is kept as written, with its progress log.

A dedicated mini project: design the YouTube thumbnail (the 16:9 video cover) for Seeds of Renaissance podcast episodes, so each episode is easy to spot and click in a feed, and the series reads as one. Part of the [SoR design system](../../README.md); sits under [youtube.md](../../youtube.md) (kind 3, "Podcast episode cover") and [podcast.md](../../podcast.md). Started 2026-10-12.

## Context

- **The podcast** is *Seeds of Renaissance*: one name, one feed. Guest interviews (for example Iain McGilchrist, Dougald Hine, Roberto Mangabeira Unger) and Rufus–Sylvie conversations. Hosted on YouTube as video and on podcast apps as audio. See [podcast.md](../../podcast.md) for names and formats.
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

- **Current templates and the first guest cover** (`.thumb--guest`, dawn and valley backdrops): [examples/youtube/index.html](../../examples/youtube/index.html), live at https://sor-design-system-rufuspollock.flowershow.me/examples/youtube/index.html. Styles in `system/components.src.css` ("Thumbnails" block), tokens `--thumb-*` in `system/tokens.css`.
- **Known problems** (from [youtube.md](../../youtube.md#next)): at 168 px the duration badge covers the end of titles, and the "Podcast" label shrinks to about 5 px.
- **Grove covers**: six 16:9 podcast covers on sunlight with the speaker in the seed spiral, from structured to poetic: `examples/youtube/grove/podcast.html` (built by `build-podcast.py`; local, not yet committed).
- **A thumbnail workshop page**: `examples/youtube/workshop.html`, a field panel driving several artboards (local, not yet committed).
- **Earlier explorations**: Sylvie's original templates ([artifact](https://claude.ai/artifact/QEUjrhcpFTu5h9xjHP5Hco)); Uriel's channel directions round 4, with a podcast video cover per direction ([artifact](https://claude.ai/artifact/UyEW5burVcqNSzQj8GT2f1)).
- **Graphic elements to draw on**: woodcut elements in `system/graphics/prints/elements/` ([gallery](https://claude.ai/artifact/6sqNWT9jeM3FJFXTGV8Guv)), blue mountain drawings in `system/graphics/mountains/elements/` (the brush ridge was liked on the About page), botanical elements in `moodboard/botanical-flower-illustration/elements/`. Most are traced from web images with no rights cleared: fine for drafts, re-source before publishing.
- **Placeholder guest photos**: `system/img/otm-guest-placeholder.jpg`, `otm-dawn-cloud.jpg`, `otm-valley.jpg`. Use a real guest photo and a real quote as soon as one is available.
- **Rules to follow**: [type.md](../../type.md) (Polyamine for short display text, Restora for the poetic italic), [colour.md](../../colour.md), [voice.md](../../voice.md) (title formulas), [logo.md](../../logo.md).

## Progress

- **2026-10-12, versions A to D**: [examples/youtube/podcast-thumbnails.html](../../examples/youtube/podcast-thumbnails.html). Shows the current guest cover and the six Grove covers in the feed, then A (face-led, two hooks), B (quote-led, circle on paper and arch on night), C (brush ridge, linocut range, flowering branch) and D (sunlight, night, paper, white, plus cobalt as an out-of-palette test). Each is shown at full size and at 360 px and 168 px in light and dark feeds, then all together among stand-in thumbnails from other channels. The placeholder guest is cut out with macOS Vision (`system/img/otm-guest-placeholder-cut.png`).

- **2026-10-12, backgrounds**: the A–D grounds felt too flat (plain white, sunlight or night). [examples/youtube/thumbnail-backgrounds.html](../../examples/youtube/thumbnail-backgrounds.html) sets out what makes a good thumbnail background and the steps to design one, then mocks sixteen backgrounds in four families: light and depth (glow, dawn horizon, night glow, night before dawn), one big shape (sun disc, rays, fingerprint ring, ripples), landscape and drawing (layered ridges, brush ridge, linocut range, two-tone dawn photo) and light through things (leaf shadow, ink wash, watercolour halo, torn paper). A switch shows each alone, with a face and words, or blurred, plus a 168 px feed check. Finding: a face as big as A's hides any background, so the tests use a face about 70% of the height with the motif around the head.
- **2026-10-12, dawn ridge (2 + 10)**: Sylvie asked to combine the dawn horizon (2: gradient and band of light) with the brush ridge (10). Four variations at the top of the backgrounds page: dawn ridge, ridge from the mist, gold dawn ridge, two distances. Behind the head the ridge was hidden, so its peak stands between the words and the face, rising from the light band below the words.
- **2026-10-12, swallows flying in**: [examples/youtube/swallows-thumbnail.html](../../examples/youtube/swallows-thumbnail.html). Sylvie's layout on plain white: the woodcut swallow flock flying in from the top-left corner, the quote below it, the name under the quote, the guest on the right. Three versions (black, blue, larger flock). The logo moves to the bottom left, which raises the open question of the series logo corner. Sylvie preferred 1 (black swallows); versions 4–7 add two speakers (overlapping, or side by side) and the blue version with the words in the swallows' blue (#274191). Versions 8–11 add the logo's fingerprint ring, very faded, around the flock (red, grey, a wide arc from the corner, and with two speakers), cleared softly behind the quote so the words stay clean.
- **2026-10-12, chosen: version 8**, with the two-speaker variant. Built as a Canva kit for the team: [examples/youtube/canva-kit/](../../examples/youtube/canva-kit/README.md). Full-canvas PNG layers (background, swallows, fingerprints, logo, guest placement, guides), finished examples, and step-by-step Canva instructions with sizes and positions; `export.sh` rebuilds the PNGs.

## Next (agreed 2026-10-13, not yet done)

1. **Logo fix.** The logo changed on 13 October (same file names), so the kits are out of date. Rebuild both kits (`examples/youtube/canva-kit/build.py`, `examples/social/instagram/build.py`): fingerprints from `archive/logo-2026-10/parts/mark-prints-red.png` (prints only, red on transparent, 1130 px; no centre masking needed), at 20%. Drop the white disc. Use the lockup (mark + name, `system/logo/lockups/seeds-logo-horizontal-colour-*.png`) rather than the mark alone. Position it provisionally and settle it later: not top left, where the words go.
2. **Bottom left only.** The bottom-left layout is the one; archive top-left. Fill out the fingerprints in the bottom-left corner (the ring was placed for top left and leaves the corner thin).
3. **Retire** the old podcast and guest covers (`.thumb--guest`, the paper podcast template) from examples/youtube/index.html; gathering, manifesto and talk stay, marked for a later pass.
4. **Archive** the exploration concisely in `archive/podcast-thumbnails-2026-10/` (A–D, backgrounds, swallows versions, Grove, workshop), linking to artifacts rather than inlining: overview at https://claude.ai/artifact/MMNCAeF3gNzmpDSiB6aVDv.
5. **Docs: podcast first.** Open question from Rufus: organise docs by product (podcast: all its imagery, YouTube covers to social) or by channel? Recommended: by product for guidance (podcast.md holds every podcast image), with youtube.md and social.md keeping channel specs and non-podcast items.
6. Later, secondary: a soft colour or simple image ground instead of plain white.

## Open questions

- Is the hook the episode title or a quote from the guest, or does it vary?
- Photo treatment: colour, greyscale, or duotone in a brand colour?
- One fixed ground for the whole series, or colour-coded by theme?
- Do Rufus–Sylvie conversations get the same layout with two faces, or a variant?

## Done when

Rufus and Sylvie pick one direction (or a combination), it is built as a reusable template in [examples/youtube/](../../examples/youtube/index.html) that reads at 168 px, and [youtube.md](../../youtube.md) and [podcast.md](../../podcast.md) say how to make a new episode's thumbnail.

**Prompt to start a session:** *Read projects/sor-design-system/podcast-thumbnails.md and follow it. Start by showing me the existing guest cover and the Grove covers at feed size, then build versions A to D.*
