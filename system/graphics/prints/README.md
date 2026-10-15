# Print elements

Woodcut, linocut and engraving prints for Seeds of Renaissance: fruit, oak leaves and acorns, pinecones, flowers, a mountain range (with and without a gold sun) and a flock of swallows. Each was traced from an image on [[moodboard/woodcuts/woodcuts-moodboard]]: the paper is removed and the ink kept. See also [[woodcuts/README|woodcuts]], [[animals/README|animals]] and [[mountains/README|mountains]].

Gallery with every file and a link to each: [graphics/prints](../../../graphics/prints.md) on the design system site, built with every set by `python3 system/build-galleries.py` from `elements.json` (which also makes the gitignored `thumbs/`).

## Colours: kept as printed

These elements **keep the colours they were made in** and are not retinted to the system tokens (see [[colour#Illustration inks (graphics only)|colour]]). They are often used with a transparency over them, which takes the edge off both the ink and the colour (for example the red and black of the pomegranates), so the exact colours matter. Until the system sets how, keep the transparency subtle.

| Colour | Hex | Used on |
|---|---|---|
| Black (`--ink`) | `#1b1916` | Most elements |
| Logo red | `#e5201c` | Pomegranates, second layer |
| Print red | `#c25552` | Pomegranates (red sampled from the print), round flowers |
| Faded green | `#3b5a45` | Acorns, oak leaves, pinecones |
| Faded dark blue | `#2f4465` | Hanging fruit |
| Cobalt (`--print-blue`) | `#03296f` | Tulips, mountain range |
| Swallow blue | `#274191` | Flock of swallows (sampled from the engraving) |
| Ochre | `#b49856` | Flowering branch |
| Pale yellow (`--sunlight`) | `#fbefc4` | Flowering branch |
| Gold | `#dbb06a` | The sun over the mountain range |

## Elements

In [`elements/`](elements/). Every name has an `.svg` and a 1000px-wide transparent `.png`. Names read `subject-style-colour`.

| File (.svg and .png) | What it is | Colour | Mood board | Source |
|---|---|---|---|---|
| `swallows-flock-engraving-blue` | Flock of swallows | Blue (original) (`#274191`) | 22 | Pinterest engraving |
| `swallows-flock-engraving-black` | Flock of swallows | Black (`#1b1916`) | 22 | Pinterest engraving |
| `pomegranates-linocut-black-red-logo` | Pomegranates | Black + logo red (`#1b1916 + #e5201c`) | 01 | Pinterest linocut |
| `pomegranates-linocut-black-red-print` | Pomegranates | Black + print red (`#1b1916 + #c25552`) | 01 | Pinterest linocut |
| `oak-leaf-acorn-twig-linocut-black` | Oak leaf and acorn on a twig | Black (`#1b1916`) | 11 | Pinterest linocut |
| `acorn-single-linocut-black` | Acorn | Black (`#1b1916`) | 10 | Stock linocut set (watermarked, draft) |
| `acorn-single-linocut-green` | Acorn | Faded green (`#3b5a45`) | 10 | Stock linocut set (watermarked, draft) |
| `oak-leaf-linocut-a-black` | Oak leaf, down-right | Black (`#1b1916`) | 10 | Stock linocut set (watermarked, draft) |
| `oak-leaf-linocut-a-green` | Oak leaf, down-right | Faded green (`#3b5a45`) | 10 | Stock linocut set (watermarked, draft) |
| `oak-leaf-linocut-b-black` | Oak leaf, up-right | Black (`#1b1916`) | 10 | Stock linocut set (watermarked, draft) |
| `oak-leaf-linocut-b-green` | Oak leaf, up-right | Faded green (`#3b5a45`) | 10 | Stock linocut set (watermarked, draft) |
| `acorns-pair-oak-leaf-linocut-black` | Two acorns with an oak leaf | Black (`#1b1916`) | 10 | Stock linocut set (watermarked, draft) |
| `acorns-pair-oak-leaf-linocut-green` | Two acorns with an oak leaf | Faded green (`#3b5a45`) | 10 | Stock linocut set (watermarked, draft) |
| `pinecone-linocut-black` | Pinecone, bold | Black (`#1b1916`) | 20 | Pinterest linocut |
| `pinecone-linocut-green` | Pinecone, bold | Faded green (`#3b5a45`) | 20 | Pinterest linocut |
| `pinecone-hanging-twig-pen-black` | Pinecone hanging from a twig | Black (`#1b1916`) | 19 | Pinterest pen drawing |
| `pinecone-hanging-twig-pen-green` | Pinecone hanging from a twig | Faded green (`#3b5a45`) | 19 | Pinterest pen drawing |
| `hanging-fruit-silhouette-black` | Hanging fruit and leaves | Black (`#1b1916`) | 12 | Craft-shop stencil (draft) |
| `hanging-fruit-silhouette-blue` | Hanging fruit and leaves | Faded dark blue (`#2f4465`) | 12 | Craft-shop stencil (draft) |
| `round-flowers-stem-ink-black` | Round flowers on a branching stem | Black (`#1b1916`) | 13 | Pinterest ink drawing |
| `round-flowers-stem-ink-red` | Round flowers on a branching stem | Print red (`#c25552`) | 13 | Pinterest ink drawing |
| `tulips-brush-blue` | Tulips in loose brush line | Cobalt blue (`#03296f`) | 14 | Pinterest (AI-generated) |
| `lily-stem-brush-black` | Lily stem | Black (`#1b1916`) | 17 | Pinterest ink study |
| `wildflowers-pen-black` | Wildflowers | Black (`#1b1916`) | 18 | Pinterest clip-art preview (draft) |
| `flowering-branch-silhouette-ochre` | Flowering branch, cropped | Ochre (`#b49856`) | 15 | Pinterest silhouette |
| `flowering-branch-silhouette-pale-yellow` | Flowering branch, cropped | Pale yellow (sunlight) (`#fbefc4`) | 15 | Pinterest silhouette |
| `mountain-range-linocut-black-sun` | Mountain range with a gold sun | Black + gold sun (`#1b1916 + sun #dbb06a`) | 21 | Pinterest linocut with gold leaf |
| `mountain-range-linocut-blue-sun` | Mountain range with a gold sun | Cobalt blue + gold sun (`#03296f + sun #dbb06a`) | 21 | Pinterest linocut with gold leaf |
| `mountain-range-linocut-black` | Mountain range | Black (`#1b1916`) | 21 | Pinterest linocut with gold leaf |
| `mountain-range-linocut-blue` | Mountain range | Cobalt blue (`#03296f`) | 21 | Pinterest linocut with gold leaf |

## Notes

- **Drafts:** the oak set (watermarked stock), the hanging fruit (craft-shop stencil) and the wildflowers (clip-art preview) are drafts; redraw or re-source them before they go on the live site. The tulips were traced from an AI-generated image.
- **Heavy files:** the swallows' SVGs are about 650 KB and the bold pinecone's 164 KB, because of the fine line; prefer the PNG on the web and use them large.
- **Cropped branch:** the flowering branch runs off its frame on purpose: use it as a tile or full-bleed texture, not a free-standing element.
- The pale-yellow branch and the gold sun are exceptions to the usual rules (sunlight is a background colour; drawn suns were rejected for the earlier sun marks). Kept by choice for these prints.
- Each element was traced with potrace from the mood-board image, so curves are close to the original but slightly smoothed.
