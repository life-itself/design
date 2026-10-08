# Social media

Posts, announcements and posters for every social channel except YouTube's own channel art: Instagram, LinkedIn, Substack, X and Bluesky, link previews, and event announcements in any shape. Part of the [SoR design system](README.md); read [BUILD.md](BUILD.md) first. Status: [examples.md](examples.md#status) · beads `design-34t.15`.

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
- A paper's cover is not a social image: make 1:1, 4:5 and 16:9 crops from its art, with the title and the mark on its disc inside the safe area ([logo.md](logo.md#which-mark-where)).
- Sub-brand question: *Mythos* and others may get their own lockup (beads `design-34t.11`). The podcast does not: it is Seeds of Renaissance.

## Canva

For making on-brand graphics without code: the Canva brand kit and templates, recreating the coded versions above. Beads `design-34t.19`.

**Stub.** Waits on the font licences (beads `design-34t.2`).

### What we need

1. **Brand kit**: the four faces (upload Polyamine and Restora once licensed; Bricolage Grotesque and Apfel Grotezk are free), the colours with their names (white, paper, sunlight, night, ink, muted, chalk, logo red), the logo and its disc version, and the woodcuts as SVGs (from `system/woodcuts/`).
2. **Templates** matching [social.md](above): announcement in 16:9, 4:5, 1:1 and 9:16; quote card; text post; carousel.
3. **A one-page "how to stay on brand in Canva"** note: the rules from [BUILD.md](BUILD.md#rules-that-apply-everywhere) in plain words.
4. Store the font files and source assets in the shared Drive.

Build the coded versions first (above), then recreate them as Canva templates.

## Brief for a new session

Build fixed-size artboards the way the thumbnails were built (see [youtube.md](youtube.md): artboard, `--thumb-*` tokens, `.thumb-frame` scaling): add `--social-*` tokens and a "Social" block to `system/components.src.css`, and make `examples/social/index.html` showing every item above at full size and as it appears in a feed. Use real copy from [voice.md](voice.md). Finish: update this page and [examples.md](examples.md#status), beads, commit, push, republish.

**Prompt:** *Read projects/sor-design-system/social.md, section "Brief for a new session", and follow it.*
