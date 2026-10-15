# Podcast: show art and episode art

The square artwork for the Seeds of Renaissance podcast, 3000 × 3000. Rules: [podcast.md](../../podcast.md).

| File | What it is | Use |
|---|---|---|
| `png/show-art.png` | The show art: the mark, SEEDS of RENAISSANCE big, PODCAST small, swallows and fingerprints on sunlight | Upload once to the podcast host (Spotify for Podcasters, Apple Podcasts Connect, etc.) |
| `png/show-art-wash.png` | The same on the paper-to-sunlight wash | Alternative |
| `png/episode-art-example.png` | Square episode art: hook, guest's name, logo with PODCAST, guest | An example. Make a real one from the Instagram 1:1 podcast template (below) |
| `png/episode-art-background.png`, `png/episode-art-guides.png` | The ground and the placement guides at 3000 × 3000 | For making episode art in Canva at full size |

**Episode art in Canva.** Make the Instagram 1:1 podcast post from the [Instagram kit](../social/instagram/README.md) (1080 × 1080). Download it as PNG; in the download panel, set the size to about 2.78× (3000 × 3000), or resize a copy of the design to 3000 × 3000 (Canva Pro). Upload it with the episode.

**Rebuilding.** `./export.sh` runs `build.py` (the show art, a 1000 × 1000 artboard rendered at 3×) and renders the Instagram 1:1 podcast template at 3000 × 3000. The ground comes from `system/swallows.py`, shared with the YouTube and Instagram kits. Polyamine must be licensed before the art is published.
