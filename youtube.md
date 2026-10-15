# YouTube

Thumbnails and channel art for the Seeds of Renaissance YouTube channel. Part of the [SoR design system](README.md); all examples by kind in [examples.md](examples.md).

**See them:** [thumbnails and podcast covers](examples/youtube/index.html) · [channel art](examples/youtube/channel.html).

<iframe class="specimen" src="specimens/examples-youtube.html" style="aspect-ratio:1000/985" loading="lazy" title="YouTube examples"></iframe>

**Scope:** this page covers what is specific to YouTube: video thumbnails (feed sizes, the duration badge), channel art, lower thirds. General 16:9 announcements and posters for any channel live in [social.md](social.md); podcast show art in [podcast.md](podcast.md).

## Kinds

| Kind | What it is | Make it from |
|---|---|---|
| **Landscape poster** | Announces a gathering or event: date, title, photograph. Also works as an event banner on other platforms. | The *gathering* template |
| **Video cover** | Generic videos (talks, essays, explainers), including a quote-card variant. | The *talk* and *manifesto* templates |
| **Podcast episode cover** | The guest, their name, the episode's hook, the logo with PODCAST, on the swallows-and-fingerprints ground. | [podcast.md](podcast.md) and the [podcast kit](examples/youtube/canva-kit/README.md) |
| **Channel art** | Banner with mobile crop, avatar, watermark, lower third. | [examples/youtube/channel.html](examples/youtube/channel.html) |

A vertical Shorts cover, if needed, is 1080 × 1920 (see [social.md](social.md)).

## Specs

| Asset | Size | Notes |
|---|---|---|
| Thumbnail | 1280 × 720 (16:9), JPG or PNG, under 2 MB | YouTube's duration badge covers the bottom-right corner; keep titles and faces out of it |
| Thumbnail in the feed | ~360px wide (desktop home), ~168px (desktop sidebar, "up next"), full width on mobile | Design for the 168px case: the title must still read |
| Channel banner | 2560 × 1440 upload; safe area 1546 × 423 centred | Desktops show a 2048 × 338 strip, phones a 1235 × 338 crop |
| Avatar | 800 × 800, shown as a circle at 176, 98, 48 and 24px | The logo: the full mark, drawn for each size, from `system/logo/mark/sizes/` ([logo.md](logo.md)) |
| Watermark | 150 × 150, shown bottom-right on videos | Export the circle on a transparent ground |

## Thumbnail rules

Tokens `--thumb-*` in [system/tokens.css](system/tokens.css) and the `.thumb` component in `components.src.css` (fixed 1280×720 artboard, `.thumb-frame` to scale it to fit).

- One idea per thumbnail: a Polyamine title of three to six words, one photograph or woodcut, the logo (on its white disc only over a busy photograph; see [logo.md](logo.md)).
- Grounds as on the site: paper, white, sunlight or night, joined to a photograph by a torn edge.
- Check every thumbnail at 360px and 168px with the duration badge in place. Long titles get cut off at 168px ("Find your peopl…"): shorten them or move them left.
- Labels are Apfel, uppercase. At feed size (×0.28) 24–28px labels shrink to about 7px and can't be read. Text that must be read goes to 40px and up on the artboard; anything smaller is decoration.
- Thumbnail text and video titles follow [voice.md](voice.md#youtube-and-podcast).
- Polyamine is not yet licensed, so export final PNGs from a machine that has it installed.

## Channel art rules

- **Handle:** `@SeedsOfRenaissance`. **Channel line:** the YouTube channel line in [voice.md](voice.md#the-media-house-line). **About text:** the description rung of the ladder in [voice.md](voice.md#the-media-house-line). YouTube allows 1,000 characters.
- **Banner:** the logo, name and line inside the 1546 × 423 safe area; the rest of the strip is for image (woodcut swallows, mountains). Paper banner for YouTube's light theme, night for dark.
- **Avatar and watermark:** the logo's mark, not a simplified version. Use the size file closest to each display size.
- **Lower third:** a torn white slip with the podcast in Apfel, the guest's name in Polyamine and one line about them.
- **Links:** Instagram @seedsofrenaissance · Facebook facebook.com/seeds0frenaissance · X @SeedRenaissance · LinkedIn linkedin.com/company/seedsofrenaissance · Linktree linktr.ee/seedsofrenaissance · Website secondrenaissance.net · YouTube and Substack. YouTube shows up to 14 links with custom titles.

Earlier channel directions (Uriel, round 4, before the current system): [archive/youtube-channel-directions-round-4.html](archive/youtube-channel-directions-round-4.html).

Decisions: [planning 2608](https://github.com/life-itself/planning/blob/main/projects/2608-seeds-of-renaissance-rebrand.md) · [decision log](decisions.md)
