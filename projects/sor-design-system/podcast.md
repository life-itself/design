# Podcast

Show art and episode artwork for the Seeds of Renaissance podcast. Part of the [SoR design system](README.md); read [BUILD.md](BUILD.md) first. Status: [examples.md](examples.md#status) · beads `design-34t.16`.

**Stub.** The 16:9 guest cover for YouTube exists ([examples/youtube/](examples/youtube/index.html), `.thumb--guest`); square artwork doesn't yet.

## What we need

| Item | Size | Notes |
|---|---|---|
| Show art | 3000 × 3000, JPG or PNG, RGB | Spotify, Apple Podcasts and others. Must read at 55px in app lists |
| Episode art | 3000 × 3000 | Optional per episode: guest portrait, short title |
| Video cover | 1280 × 720 | The YouTube guest cover: see [youtube.md](youtube.md) |
| Audiogram or clip cover | 1080 × 1920 and 1080 × 1080 | Short clips for social: see [social.md](social.md) |

## One brand, no named shows

The podcast is **Seeds of Renaissance**: one name, one feed, no named stations. *Over the Mountains* is retired as a show name (2026-10-05, see [brand.md](brand.md#names)). Kinds of episode (guest interviews, Rufus–Sylvie conversations) are formats, shown by playlist and an artwork tag such as "Podcast" or "Conversation", not by separate lockups. Use the SoR lockup.

## Direction so far

From the guest cover work: a dark mountain backdrop, the guest's portrait in greyscale, a short Polyamine title, the logo on its disc. Show art could keep the mountain and swallow and drop the guest.

## Brief for a new session

Make `examples/podcast/index.html` with show art (two or three directions) and an episode art template, at full size and at app-list size (55px and 160px). Reuse tokens and the `.thumb` approach. Finish: update this page and [examples.md](examples.md#status), beads, commit, push, republish.

**Prompt:** *Read projects/sor-design-system/podcast.md and follow its brief.*
