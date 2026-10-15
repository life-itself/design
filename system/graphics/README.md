# Graphics library

Every graphic set of the Seeds of Renaissance design system, one folder each. The rules for using them, and a card per set: [graphics.md](../../graphics.md). Each set has a gallery page on the site at `/graphics/<set>`.

| Folder | Set | Family |
|---|---|---|
| `sprite/` | The symbols in `system/graphics.svg` (only `elements.json` lives here) | Woodcut and print |
| `woodcuts/` | Woodcuts drawn in code (`wc.py`) | Woodcut and print |
| `animals/` | Animal woodcuts, linocuts and engravings | Woodcut and print |
| `prints/` | Prints traced from the woodcuts mood board | Woodcut and print |
| `botanicals/` | Botanical illustrations in colour | Painted |
| `washes/` | Watercolour and ink washes | Painted |
| `lines/` | Line geometry and printed marks | Line |
| `mountains/` | Pen, brush and linocut mountains | Landscape |

Each set folder holds `elements/` (the files), `elements.json` (the set and its elements), a `README.md` (sources, colours, how they were made) and, once built, `thumbs/` (600px previews, gitignored).

## Build

```bash
python3 system/build/build-galleries.py
```

From `projects/sor-design-system`. It writes `graphics/<set>.md` (one gallery page per set), the cards and the rules table in `graphics.md` (between the `<!-- library:… -->` markers) and `logos.md`, and makes the thumbnails (ImageMagick `magick`, or `sips` on macOS). The pages are Flowershow pages with `layout: plain`, so they keep the site navbar; their behaviour (ground and ink switchers, search, copy path) is `library.js`, loaded as a page script, and their look is `library.css` with the system tokens, inlined into each page and scoped to `.sg`. The frame of a gallery page is `gallery-shell.html`. Never edit the generated pages by hand.

## elements.json

```json
{
  "title": "Animals",
  "family": "woodcut",
  "lede": "One paragraph: what the set is.",
  "use_for": "One line: where it goes.",
  "colour_rule": "Which colours it may be used in.",
  "grounds": ["white", "paper", "sunlight"],
  "registers": ["Conversation", "Gathering"],
  "formats": "SVG and PNG",
  "rights": "not-cleared",
  "notes": "Optional: one more rule for this set.",
  "render": "img",
  "cover": ["fox-sitting-linocut", "swan-wings-open-linocut"],
  "elements": [
    {
      "slug": "fox-sitting-linocut",
      "title": "Fox sitting",
      "kind": "linocut",
      "desc": "One or two sentences.",
      "source": "Mood board 01",
      "rights": "draft",
      "versions": [
        {"ink": "black", "name": "Black", "hex": "#1b1916"},
        {"ink": "colour", "name": "Original colours", "hex": null, "note": "watercolour", "file": "fox-sitting-linocut-colour"}
      ]
    }
  ]
}
```

- **Set.** `family` is one of `woodcut`, `painted`, `line`, `landscape` (the groups on the hub). `grounds` are the grounds the set may sit on, from `white`, `paper`, `sunlight`, `night`; the gallery offers only those. `registers` are from Study, Conversation, Gathering ([feel.md](../../feel.md#rigour-and-warmth)). `rights` is `ours` or `not-cleared`. `render` is `img` (thumbnails of PNGs, the default), `inline` (the SVG inlined so it takes the ink of its ground) or `symbol` (a sprite symbol). `cover` picks up to six elements for the hub card; without it, the first six.
- **Element.** `rights` only when it differs from the set (`draft`: redraw or re-source before public use); the gallery tags it. `wide: true` gives the plate two columns.
- **Version.** One per colour. The file stem is `file`, or `<slug>-<ink>` without it; the builder links the `.png` and `.svg` it finds in `elements/`. `hex` is the ink colour (`#1b1916 + #e5201c` for two), or `null` with a `note`.

## Add an element

1. Put the files in the set's `elements/`: a transparent PNG, 1000px on the long side, and an SVG where it is small and clean.
2. Add it to the set's `elements.json` and a row to its README.
3. Run `python3 system/build/build-galleries.py` and check the gallery page.

A new set: a new folder with the same parts, then add it to `FAMILIES` in `system/build/build-galleries.py`.
