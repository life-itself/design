# Logo v2: a hand-drawn swallow, rising

**Done, 13 October 2026, differently from this plan:** the original swallow was kept, given a cut-and-printed edge and made 30% bigger, and the full mark is used at every size (no small version). The result is in [logo.md](logo.md) and [logos.html](logos.html); how it was reached, in [archive/logo-2026-10/](archive/logo-2026-10/README.md). The plan below is kept as written.

A small project to replace the stock swallow at the centre of the SoR mark with our own drawn swallow, and to give the mark a small version that works at 48px and below. Part of the [SoR design system](README.md); current logo and its open questions: [logo.md](logo.md), [logo-notes.md](logo-notes.md). Task state lives in Beads (`design-34t.40` and its children), not here.

**The website launches with the current logo.** The logo is one file, so swapping it later is a cheap rollout.

## What we want (Rufus and Sylvie, 2026-10-12)

- **Our own swallow, with a hand-made woodcut or engraved feel**, in place of the stock silhouette.
- **Rising, flying left to right.** Body angled up (around 30–40°), wings raised so it reads as climbing, not gliding or diving.
- **Keep the ring of red fingerprints** (red `#e5201c`, decided 2026-10-12; see [colour.md](colour.md)).
- **One bird everywhere:** the mark, the small version, the seal (swallow in its ring, `#seal` in [graphics.md](graphics.md)), the video watermark, and on its own as decoration.

## What we learned from the first try

Comparison page: [archive/logo-2026-10/logo-v2-woodcut-swallows.html](archive/logo-2026-10/logo-v2-woodcut-swallows.html) (open it through a local server so the images load). It shows four code-drawn woodcut swallows mirrored into the ring at 320px; small-mark treatments at 176/98/48/24px on light and dark; the swallow on its own and in the seal.

- **The existing woodcuts are AI first drafts drawn in code**, not real cuts ([system/woodcuts/](system/woodcuts/) README says so). Fine for decoration, too weak for a logo.
- **Perched and above are out.** Perched isn't a flight pose; above reads as a moth.
- **Flight and bold are the right kind of side view, but the pose is wrong.** Mirrored, they face right, but the big wing sweeps back along the top and the lower wing hangs down and back, so the bird reads as gliding or diving. Rotating it (the page uses −14°) can't fix a pose, and flipping it vertically turns it upside down. We need a bird drawn in a rising pose.
- **At small sizes the fingerprints survive and the bird doesn't.** At 48 and 24px the red prints still read as a ring; any detailed bird turns to noise. The "swallow alone" and "solid red ring" treatments held at 24px; the 12-dot ring held to 48px.

## Where to find the bird

1. **Public-domain engravings (first choice to explore).** Real woodcuts and wood engravings, free to use. Start with Thomas Bewick, *A History of British Birds* (1797–1804): swallow, house martin, swift. Also 19th-century natural-history plates and engravings (Biodiversity Heritage Library, Wikimedia Commons, Internet Archive, Rawpixel's public-domain collection, Old Book Illustrations). Look for side views in flight, wings raised or mid-stroke. Record the source, date and licence for each.
2. **Sylvie draws one, or we commission a linocut artist.** Fully ours. An engraving found in step 1 can serve as the brief.
3. **Adapt rather than invent.** Whatever the source: mirror it to fly left to right, set the body rising, raise the wings if needed, clean it up and convert it to a vector (SVG) that keeps the cut texture.

## The small version

A logo with a simplified small version is normal practice. It's one mark at two sizes, not a second logo.

- **Full mark (about 96px and up):** the drawn swallow in the full fingerprint ring.
- **Small mark (48px and below):** fewer, larger fingerprints, and the bird as a **solid silhouette** of the same drawing (no inner detail), scaled up to fill the centre. Test against "prints only" and "swallow on a white disc".
- Uses: YouTube, Instagram and podcast avatars (shown in a circle, 24–176px), favicon, watermark.

## Rollout once chosen

Replace `system/img/logo.png` (and the inverted and 256px versions), the seal in `system/graphics.svg`, the YouTube avatar and watermark, the favicon, social avatars, and the website's copy. Then settle the dark-ground and one-colour variants (`design-34t.24`, `design-34t.21`).
