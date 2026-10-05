# Social media

Posts, announcements and posters for every social channel except YouTube's own channel art: Instagram, LinkedIn, Substack, X and Bluesky, link previews, and event announcements in any shape. Part of the [SoR design system](README.md); read [BUILD.md](BUILD.md) first. Status: [applications.md](applications.md) · beads `design-34t.15`.

**Stub.** Nothing built yet beyond the 16:9 gathering thumbnail in [examples/youtube/](examples/youtube/index.html), which is really an announcement and moves here.

## Organised by shape, not platform

One design, set on a few fixed artboards. The rules are the same on every platform; only the size changes.

| Shape | Size | Used for |
|---|---|---|
| Landscape 16:9 | 1920 × 1080 (or 1280 × 720) | Event announcements, Luma or Eventbrite banners, email headers, posts with a video feel |
| Link preview | 1200 × 630 | Open Graph image for the site and shared links, LinkedIn link posts, Substack post image |
| Portrait 4:5 | 1080 × 1350 | Instagram feed posts (the default), LinkedIn image posts |
| Square 1:1 | 1080 × 1080 | Instagram, LinkedIn, carousels |
| Story 9:16 | 1080 × 1920 | Instagram stories and reel covers, Shorts covers |
| Banners | LinkedIn 1584 × 396 · X 1500 × 500 · Bluesky 3000 × 1000 · Substack header | Profile headers |
| LinkedIn document | 1080 × 1350 pages as a PDF | Carousel-style explainers |

## What we need

1. **An announcement**: date, title, one photo or woodcut, logo on its disc. Designed once, set in 16:9, 4:5, 1:1 and 9:16.
2. **A quote card**: a line from the manifesto, a guest, an essay. Restora once it passes ~10 words.
3. **A text-only post** (Instagram template from the old website plan): a short statement on paper or sunlight.
4. **Text over photo**: one strong photo, a short Polyamine line, a scrim only if needed.
5. **A carousel**: a cover, three to six inner slides, a closing slide with the call to action.
6. **Profile banners** for LinkedIn, X, Bluesky and Substack, and the site's link preview image.

## Rules for social

- Everything in BUILD.md. Text must read on a phone at feed size: nothing under ~36px on a 1080-wide artboard.
- Keep to one idea per post. Five to ten words of Polyamine at most on the image; the rest goes in the caption.
- Respect platform safe areas: the top and bottom ~250px of a 9:16 story are covered by the interface.
- Sub-brand question: Over the Mountains, Mythos and others may get their own lockup (beads `design-34t.11`).

## Brief for a new session

Build fixed-size artboards the way the thumbnails were built (see [youtube.md](youtube.md): artboard, `--thumb-*` tokens, `.thumb-frame` scaling): add `--social-*` tokens and a "Social" block to `system/components.src.css`, and make `examples/social/index.html` showing every item above at full size and as it appears in a feed. Use real copy from [voice.md](voice.md). Finish: update this page and [applications.md](applications.md), beads, commit, push, republish.

**Prompt:** *Read projects/sor-design-system/social.md, section "Brief for a new session", and follow it.*
