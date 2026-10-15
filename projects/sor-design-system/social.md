# Social media

Posts, announcements and posters for every social channel except YouTube's own channel art: Instagram, LinkedIn, Substack, X and Bluesky, link previews, and event announcements in any shape. Part of the [SoR design system](README.md).

## Make one with your agent

Paste this into your AI agent, in whichever repo you're working in, and fill in the brackets. It finds what it needs in the design system and gives you the image, a caption and the steps to finish it in Canva.

```text
Make an Instagram post (4:5) for Seeds of Renaissance announcing [what], [when], [where].
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system (or, if that folder isn't there,
https://design.seedsofrenaissance.org/AGENTS.md). Follow its "Social post" route and
read only what it names. Don't change anything in the design repo.
Give me the PNG, a caption in our voice, and the steps to finish it in Canva.
Ask me for anything you need that you can't find. Then tell me what you checked
and what you guessed.
```

Instagram posts come from the [Instagram templates](examples/social/instagram/README.md): podcast episode, quote card, announcement, statement and carousel, in 4:5 and 1:1. For a 16:9 announcement, start from the gathering thumbnail in the [YouTube examples](examples/youtube/index.html).

<iframe class="specimen" src="specimens/examples-social.html" style="aspect-ratio:1000/523" loading="lazy" title="Social examples"></iframe>

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

## Kinds of post

1. **An announcement**: date, title, one photo or woodcut, the logo (on its disc over a busy photograph). Designed once, set in 16:9, 4:5, 1:1 and 9:16.
2. **A quote card**: a line from the manifesto, a guest, an essay. Restora once it passes ~10 words.
3. **A text-only post**: a short statement on paper or sunlight.
4. **Text over photo**: one strong photo, a short Polyamine line, a scrim only if needed.
5. **A carousel**: a cover, three to six inner slides, a closing slide with the call to action.
6. **Profile banners** for LinkedIn, X, Bluesky and Substack, and the site's link preview image.

## Rules for social

- Everything in BUILD.md. Text must read on a phone at feed size: nothing under ~36px on a 1080-wide artboard.
- Keep to one idea per post. Five to ten words of Polyamine at most on the image; the rest goes in the caption.
- Respect platform safe areas: the top and bottom ~250px of a 9:16 story are covered by the interface.
- A paper's cover is not a social image: make 1:1, 4:5 and 16:9 crops from its art, with the title and the mark on its disc inside the safe area ([logo.md](logo.md#which-mark-where)).
- The podcast has no lockup of its own: it is Seeds of Renaissance. Whether *Mythos* and others get their own lockups is not yet settled; until then, use the Seeds of Renaissance logo.
- Fixed-size artboards follow the thumbnail pattern in [youtube.md](youtube.md): an artboard, size tokens in `system/tokens.css`, a frame that scales it to fit. Use real copy from [voice.md](voice.md).

## Canva

For making on-brand graphics without code: the Canva brand kit and templates, recreating the coded versions.

**Kits to start from:**

- The [podcast thumbnail Canva kit](examples/youtube/canva-kit/README.md): full-canvas PNG layers and step-by-step instructions. The model for other templates.
- The [Instagram post kit](examples/social/instagram/README.md): podcast episode, quote card, announcement, statement and carousel in 4:5 and 1:1, on the swallows-and-fingerprints background, with free-standing elements and guides.

**Fonts:** Polyamine and Restora are not yet licensed, so they can't be uploaded to Canva. Bricolage Grotesque and Apfel Grotezk are free.

**The brand kit holds:**

1. The four faces (Polyamine and Restora once licensed), the colours with their names (white, paper, sunlight, night, ink, muted, chalk, logo red), the logo and its disc version, and the woodcuts as SVGs (from `system/graphics/woodcuts/`).
2. Templates matching the kinds above: announcement in 16:9, 4:5, 1:1 and 9:16; quote card; text post; carousel.
3. The rules from [BUILD.md](BUILD.md#rules-that-apply-everywhere), in plain words.

Keep font files and source assets in the shared Drive. Build a coded version first, then recreate it as a Canva template.

Decisions: [planning 2608](https://github.com/life-itself/planning/blob/main/projects/2608-seeds-of-renaissance-rebrand.md) · [decision log](decisions.md)
