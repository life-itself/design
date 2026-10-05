# YouTube

Thumbnails and channel art for the Seeds of Renaissance YouTube channel: what exists, the specs, and what's next. Part of the [SoR design system](README.md).

## What we need: four kinds

| Kind | What it is | Status |
|---|---|---|
| **1 · Landscape poster** | Announces a gathering or event: date, title, photograph. Also works as an event banner on other platforms. | Have it: the *gathering* template |
| **2 · Video cover** | Generic videos (talks, essays, explainers), including a quote-card variant. | Have it: the *talk* and *manifesto* templates |
| **3 · Podcast episode cover** | Over the Mountains episodes: the **guest's portrait**, their name, the episode title or a quote, the podcast and SoR lockup. | **Missing, and important.** Uriel's round 4 has a version in older styles; an earlier, better mockup may exist |
| **4 · Channel art** | Banner with mobile crop, avatar, watermark, lower third. | Uriel's round 4, in older styles: to redo in the current system |

Later, if needed: a vertical Shorts cover (1080 × 1920).

## What exists

| Work | By | Status | Where |
|---|---|---|---|
| **Thumbnail templates** (gathering, podcast, manifesto, talk) in the current system | Sylvie, ported to the system 2026-10-05 | Current; needs an accuracy pass | [examples/youtube/](examples/youtube/index.html) · original [artifact](https://claude.ai/artifact/QEUjrhcpFTu5h9xjHP5Hco), source `sor-brand/mockups/youtube/` |
| **Channel directions, round 4**: banner, mobile crop, channel page, podcast video cover, lower third and watermark, About text and links | Uriel | Earlier exploration, before the current system | [artifact](https://claude.ai/artifact/UyEW5burVcqNSzQj8GT2f1) · archived copy [archive/youtube-channel-directions-round-4.html](archive/youtube-channel-directions-round-4.html) |

### Uriel's round 4: three directions

Each direction shows a desktop banner, the mobile crop, the channel page header, a podcast video cover (1280×720, guest portrait and quote as placeholders) and a lower third with watermark.

| Option | Idea | Palette | Type |
|---|---|---|---|
| **1 · Warm Emergence** (from Direction E) | A simple lockup on a soft neutral: logo, wordmark, tagline, no photos. Podcast cover puts the guest in an arch in front of the sun. | stone sage `#D6DACD`, ink `#231D1A`, mulberry `#6E3450`, ember `#F25F00` (background swatches: stone sage, fog, sand, dove) | Fraunces light (stand-in for Restora), Italiana small caps, Newsreader italic |
| **2 · Dusk & Dawn** (from Direction D) | The dark-blue eclipse as sky, the logo as the sun rising beside the name. Guest portrait as a small eclipse with a first-light rim. | night `#0E1222`, moon `#ECE6DA`, first light `#F0A868`, logo red `#F91F29` | Castoro Titling, Castoro italic, Albert Sans |
| **3 · Grove** (new) | The logo taken apart: each fingerprint becomes a seed, the seeds become the leaves of a tree growing across the banner. | forest `#0F1A14`, bone `#EDE8DC`, print red `#F91F29`, moss `#7E8F73` | Fraunces light, Newsreader italic, Karla caps |

Uriel's own warnings: option 1 sits close to Emergence Magazine without photos; option 2 can drift into mystical cliché and its eclipse artwork is low resolution; option 3 needs the logo as a clean file.

**What carries over into the current system:** the set of channel assets to make (banner with mobile safe area, podcast cover, lower third, watermark), the podcast cover idea of guest portrait plus a large plain quote, the "Over the Mountains · presented by Seeds of Renaissance" lockup, Grove's idea of the fingerprints becoming seeds (it rhymes with our woodcut seeds), and the About text and links below. **What doesn't:** the three palettes and typefaces, which predate the decisions on ink, paper, sunlight and Polyamine (see [colour.md](colour.md), [type.md](type.md)).

### Channel About text (from round 4)

> Seeds of Renaissance (SoR) is a place for seekers who sense the impending death of old paradigms and long for the ideas, the practice, and the company to help birth the new.
>
> We are a media house and space of belonging, offering mythos and language for what we already feel. Our content gives people a place to encounter and make sense of this new mythos and provides places of belonging where practice, sense-making, and creating together move society towards an emerging vision of a wiser, weller world.
>
> Together we will make the art, ideas and actions for what comes next.
>
> Join our newsletter to never miss an episode of the Seeds of Renaissance Podcast and to stay up to date on what's happening at SoR and in the broader community of seekers ushering in what's to come.

776 characters of YouTube's 1,000. Handle `@SeedsOfRenaissance`; channel line "Over the Mountains podcast, gatherings, magazine"; tagline "Vision and movement for civilisational renewal".

**Links:** Instagram @seedsofrenaissance · Facebook facebook.com/seeds0frenaissance · X @SeedRenaissance · LinkedIn linkedin.com/company/seedsofrenaissance · Linktree linktr.ee/seedsofrenaissance · Website secondrenaissance.net · YouTube and Substack links still to fill. YouTube shows up to 14 links with custom titles.

## Specs

| Asset | Size | Notes |
|---|---|---|
| Thumbnail | 1280 × 720 (16:9), JPG or PNG, under 2 MB | YouTube's duration badge covers the bottom-right corner; keep titles and faces out of it |
| Thumbnail in the feed | ~360px wide (desktop home), ~168px (desktop sidebar, "up next"), full width on mobile | Design for the 168px case: title must still read |
| Channel banner | 2560 × 1440 upload; safe area 1546 × 423 centred | Uriel's mocks show the visible desktop strip (2048 × 338) and mobile crop (1235 × 338) |
| Avatar | 800 × 800, shown as a circle down to ~24px | The current logo fails small (fingerprints turn to noise); see [logo.md](logo.md) |
| Watermark | 150 × 150, shown bottom-right on videos | |

## Thumbnail rules in the system

Tokens `--thumb-*` in [system/tokens.css](system/tokens.css) and the `.thumb` component in `components.src.css` (fixed 1280×720 artboard, `.thumb-frame` to scale it to fit).

- One idea per thumbnail: a Polyamine title of three to six words, one photograph or woodcut, the logo on its disc.
- Grounds as on the site: paper, white, sunlight or night, joined to a photograph by a torn edge.
- Labels are Apfel, uppercase. **Known problem:** at feed size (×0.28) the 24–28px labels shrink to about 7px and can't be read. Either they are decoration, or they go to 40px and up.
- Titles render in Polyamine only where it is installed (not yet licensed), so export final PNGs from a machine that has it.

## Next

1. **Thumbnail accuracy pass**: check each template at real feed sizes (360px and 168px) with the duration badge in place; fix label sizes; use real episode titles and guests; decide which labels must be readable.
2. **Channel art in the current system**: banner and mobile crop, avatar (needs the small logo), podcast video cover, lower third and watermark, using the asset list from round 4.
