# Podcast

Show art and episode artwork for Seeds of Renaissance podcasts, starting with *Over the Mountains*. Part of the [SoR design system](README.md); read [BUILD.md](BUILD.md) first. Status: [applications.md](applications.md) · beads `design-34t.16`.

**Stub.** The 16:9 guest cover for YouTube exists ([examples/youtube/](examples/youtube/index.html), `.thumb--guest`); square artwork doesn't yet.

## What we need

| Item | Size | Notes |
|---|---|---|
| Show art | 3000 × 3000, JPG or PNG, RGB | Spotify, Apple Podcasts and others. Must read at 55px in app lists |
| Episode art | 3000 × 3000 | Optional per episode: guest portrait, short title |
| Video cover | 1280 × 720 | The YouTube guest cover: see [youtube.md](youtube.md) |
| Audiogram or clip cover | 1080 × 1920 and 1080 × 1080 | Short clips for social: see [social.md](social.md) |

## Open: is Over the Mountains a sub-brand?

The biggest question for this page. Does *Over the Mountains* get its own name lockup and perhaps its own accent, or is it Seeds of Renaissance with a label? Same question for Sylvie's station. Decide in beads `design-34t.11` (sub-brands) before finalising show art; until then use the SoR lockup with "Over the Mountains" as the title.

## Direction so far

From the guest cover work: a dark mountain backdrop (the name), the guest's portrait in greyscale, a short Polyamine title, the logo on its disc. Show art could keep the mountain and swallow and drop the guest.

## Brief for a new session

Make `examples/podcast/index.html` with show art (two or three directions) and an episode art template, at full size and at app-list size (55px and 160px). Reuse tokens and the `.thumb` approach. Finish: update this page and [applications.md](applications.md), beads, commit, push, republish.

**Prompt:** *Read projects/sor-design-system/podcast.md and follow its brief.*
