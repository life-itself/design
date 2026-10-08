# YouTube

Thumbnails and channel art for the Seeds of Renaissance YouTube channel: what exists, the specs, and what's next. Part of the [SoR design system](README.md); all examples by kind in [examples.md](examples.md).

**See them:** [thumbnails and podcast covers](examples/youtube/index.html) · [channel art](examples/youtube/channel.html).

<iframe class="specimen" src="specimens/examples-youtube.html" style="aspect-ratio:1000/522" loading="lazy" title="YouTube examples"></iframe>

**Scope:** this page covers what is specific to YouTube: video thumbnails (feed sizes, the duration badge), channel art, lower thirds. General 16:9 announcements and posters for any channel live in [social.md](social.md); podcast show art in [podcast.md](podcast.md).

## What we need: four kinds

| Kind | What it is | Status |
|---|---|---|
| **1 · Landscape poster** | Announces a gathering or event: date, title, photograph. Also works as an event banner on other platforms. | Have it: the *gathering* template |
| **2 · Video cover** | Generic videos (talks, essays, explainers), including a quote-card variant. | Have it: the *talk* and *manifesto* templates |
| **3 · Podcast episode cover** | Podcast episodes: the **guest's portrait**, their name, the episode title or a quote, the podcast and SoR lockup. | **First pass done** (`.thumb--guest`, dawn and valley backdrops) in [examples/youtube/](examples/youtube/index.html); needs polish. Composition from the rough mockup in `archive/otm-thumbnail-rough.html` |
| **4 · Channel art** | Banner with mobile crop, avatar, watermark, lower third. | **First pass done** in [examples/youtube/channel.html](examples/youtube/channel.html): banner (paper and night, desktop/mobile/TV views, safe-area guides), channel page mocks, avatar options (swallow-on-white recommended; the logo fails under 48px), lower third, watermark, About panel |

Later, if needed: a vertical Shorts cover (1080 × 1920).

## What exists

| Work | By | Status | Where |
|---|---|---|---|
| **Thumbnail templates** (gathering, podcast, manifesto, talk) in the current system | Sylvie, ported to the system 2026-10-05 | Current; needs an accuracy pass | [examples/youtube/](examples/youtube/index.html) · original [artifact](https://claude.ai/artifact/QEUjrhcpFTu5h9xjHP5Hco), source `archive/sor-brand-mockups/youtube/` |
| **Channel directions, round 4**: banner, mobile crop, channel page, podcast video cover, lower third and watermark, About text and links | Uriel | Earlier exploration, before the current system | [artifact](https://claude.ai/artifact/UyEW5burVcqNSzQj8GT2f1) · archived copy [archive/youtube-channel-directions-round-4.html](archive/youtube-channel-directions-round-4.html) |

### Uriel's round 4: three directions

Each direction shows a desktop banner, the mobile crop, the channel page header, a podcast video cover (1280×720, guest portrait and quote as placeholders) and a lower third with watermark.

| Option | Idea | Palette | Type |
|---|---|---|---|
| **1 · Warm Emergence** (from Direction E) | A simple lockup on a soft neutral: logo, wordmark, tagline, no photos. Podcast cover puts the guest in an arch in front of the sun. | stone sage `#D6DACD`, ink `#231D1A`, mulberry `#6E3450`, ember `#F25F00` (background swatches: stone sage, fog, sand, dove) | Fraunces light (stand-in for Restora), Italiana small caps, Newsreader italic |
| **2 · Dusk & Dawn** (from Direction D) | The dark-blue eclipse as sky, the logo as the sun rising beside the name. Guest portrait as a small eclipse with a first-light rim. | night `#0E1222`, moon `#ECE6DA`, first light `#F0A868`, logo red `#F91F29` | Castoro Titling, Castoro italic, Albert Sans |
| **3 · Grove** (new) | The logo taken apart: each fingerprint becomes a seed, the seeds become the leaves of a tree growing across the banner. | forest `#0F1A14`, bone `#EDE8DC`, print red `#F91F29`, moss `#7E8F73` | Fraunces light, Newsreader italic, Karla caps |

Uriel's own warnings: option 1 sits close to Emergence Magazine without photos; option 2 can drift into mystical cliché and its eclipse artwork is low resolution; option 3 needs the logo as a clean file.

**What carries over into the current system:** the set of channel assets to make (banner with mobile safe area, podcast cover, lower third, watermark), the podcast cover idea of guest portrait plus a large plain quote, Grove's idea of the fingerprints becoming seeds (it rhymes with our woodcut seeds), and the About text and links below. **What doesn't:** the three palettes and typefaces, which predate the decisions on ink, paper, sunlight and Polyamine (see [colour.md](colour.md), [type.md](type.md)).

### Channel About text (from round 4)

> Seeds of Renaissance (SoR) is a place for seekers who sense the impending death of old paradigms and long for the ideas, the practice, and the company to help birth the new.
>
> We are a media house and space of belonging, offering mythos and language for what we already feel. Our content gives people a place to encounter and make sense of this new mythos and provides places of belonging where practice, sense-making, and creating together move society towards an emerging vision of a wiser, weller world.
>
> Together we will make the art, ideas and actions for what comes next.
>
> Join our newsletter to never miss an episode of the Seeds of Renaissance Podcast and to stay up to date on what's happening at SoR and in the broader community of seekers ushering in what's to come.

776 characters of YouTube's 1,000. Handle `@SeedsOfRenaissance`; channel line "Podcast, gatherings, magazine"; tagline "Vision and movement for civilisational renewal".

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

1. **Known:** at 168px the duration badge covers the end of the gathering title ("Find your peopl…"); the podcast label is ~5px there.
2. **Thumbnail accuracy pass**: check each template at real feed sizes (360px and 168px) with the duration badge in place; fix label sizes; use real episode titles and guests; decide which labels must be readable.
3. **Channel art review**: banner and mobile crop, avatar (needs the small logo), podcast video cover, lower third and watermark, using the asset list from round 4.

## Brief: polishing the YouTube work in a new session

For a fresh Claude session (or a person) picking up the YouTube work. Current state and what's done live in beads (`bd show design-34t.5 design-34t.8 design-34t.6`), not here; this is what to do and how.

**Read first, in order:** [BUILD.md](BUILD.md), this file, [voice.md](voice.md) (titles and thumbnail text), [type.md](type.md) top section (Polyamine for display under ~10 words, Restora beyond that and for the poetic italic; four faces only), [colour.md](colour.md), [graphics.md](graphics.md).

**Where to work**

- Thumbnails and the podcast guest cover (`.thumb--guest`): [examples/youtube/index.html](examples/youtube/index.html)
- Channel art (banner, avatar, lower third, watermark, About): [examples/youtube/channel.html](examples/youtube/channel.html)
- Styles: `system/components.src.css`, in the "Thumbnails" and "YouTube channel art" blocks. Rebuild with `python3 system/build-css.py`; never edit `components.css`. Tokens: `--thumb-*` and `--yt-*` in `system/tokens.css`.
- Composition reference for the podcast cover: `archive/otm-thumbnail-rough.html`. Keep its idea (dark mountain backdrop, guest portrait greyscale on the right, title and guest name on the left), not its styling. Placeholder images: `system/img/otm-*.jpg`.

**Start from these known problems**

1. At 168px (the "up next" size) the duration badge covers the end of the gathering title.
2. The "Podcast" label is about 5px at 168px; the guest name only just reads. Decide which text must be readable at 168px and size it (roughly 40px+ on the 1280×720 artboard), or drop it.
3. Use real episode titles and guests where Rufus provides them; follow the title formulas in voice.md.
4. Review the channel art with Rufus: banner, avatar choice (swallow on white is the current recommendation; the logo fails under 48px), lower third.

**How**

- Preview: run the `static` launch config (python http.server on 8790 from the repo root), open `/projects/sor-design-system/examples/youtube/`. Check every template in the feed preview at 360px and 168px.
- Keep changes inside the YouTube examples and their CSS blocks. If something belongs in the wider system (a new rule or token), make it and note it in this file.
- Record progress in beads notes, not in markdown.
- Finish: update this file's tables, close or update the beads, commit, `git push`, then republish: `python3 system/build-site.py && fl --yes site` (from this folder).

**Prompt to start a session:** *Read projects/sor-design-system/youtube.md, section "Brief: polishing the YouTube work in a new session", and follow it. Then show me the podcast cover and thumbnails at feed size and propose fixes.*
