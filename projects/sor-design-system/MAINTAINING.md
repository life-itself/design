# Maintaining the design system

For whoever edits and publishes this folder. Readers start at [README.md](README.md); builders at [BUILD.md](BUILD.md).

## Where it lives

- **Source:** `life-itself/design`, folder `projects/sor-design-system/`. The single home for SoR brand and design-system work.
- **Published** at https://sor-design-system-rufuspollock.flowershow.me (Flowershow, CLI publishing). Preview copy as a Claude artifact: https://claude.ai/artifact/MtNi8BxiybVhuXZCzwo6it.
- **Tracking:** beads `design-34t`.

## How the site is put together

- **Markdown pages** hold the rules and the reasoning. Flowershow renders them with its own layout and the navbar from `config.json`. The sidebar is off. Each `.md` is also served raw at its `.md` URL, which is what agents read; [llms.txt](llms.txt) lists them in reading order.
- **[guide.html](guide.html)** holds the visuals: the whole system rendered with the real CSS, one chapter per topic. It is the only place the visuals are edited.
- **`specimens/<chapter>.html`** are cut from guide.html by `system/build-specimens.py` and embedded at the top of the topic pages and on the home with an `<iframe class="specimen">`. A group inside a chapter with an id like `<div id="examples-web">` also gets its own specimen (used on examples.md and youtube.md). Never edit them by hand. They hide each chapter's heading and "more" links, since the embedding page has its own.
- **`custom.css`** styles the specimen frames on Flowershow. Flowershow pages never load `components.css` (its generic class names would clash with the site theme); the system's CSS only runs inside the specimen frames, the guide and the examples.
- **Examples** are standalone HTML pages under `examples/<kind>/`, one folder per kind (web, youtube; next slides, print), each kind with an `index.html` gallery where it has several. [examples.md](examples.md) lists them all.

## Specimen heights

A specimen lays out at a virtual 1000px width and scales to its frame, so its height is a fixed ratio of its width. Each `<iframe>` carries `style="aspect-ratio:1000/H"`, where H is the specimen's height at 1000px plus about 10px. After changing a chapter in guide.html, re-measure: open any specimen locally, then in the browser console load each one into a 1000px-wide iframe and read `document.body.scrollHeight`. Update H wherever that specimen is embedded (`grep -n 'specimens/<name>' *.md`). Below 600px wide, frames fall back to a fixed height and scroll inside.

## Publish

From `projects/sor-design-system`:

```bash
python3 system/build-specimens.py && python3 system/build-site.py && fl --yes site
```

`build-site.py` assembles `site/` (gitignored): the docs, guide, specimens, woodcuts page, system code and images, examples and the loose files in archive. It leaves out `moodboard/` and the sub-folders of `archive/` (third-party screenshots, uncleared images, large PDFs) and rewrites `.md` links in HTML pages to Flowershow page URLs.

## Code

| Path | What |
|---|---|
| [system/tokens.css](system/tokens.css) | Every colour, face, size and space, with its role. Change the system here. |
| [system/components.src.css](system/components.src.css) | Components, readable source. Run `python3 system/build-css.py` to make `components.css`. |
| `system/fonts.css` | Apfel Grotezk embedded (OFL); Polyamine and Restora by name only (unlicensed). Built by `build-fonts.py`. |
| `system/graphics.svg` / `graphics.js` | Woodcut symbols for `<use>`. Built by `build-graphics.py`. |
| `system/woodcuts/` | All woodcut SVGs and the script that draws them. Gallery built by `build-woodcuts.py`. |
| `system/sor.js` | Small behaviours (selected-work picker) |
| `system/img/` | The logo, and placeholder photos from the mood board (not cleared) |
| `system/build-specimens.py` | Cuts guide.html into `specimens/` |
| `system/build-site.py` | Assembles `site/` for Flowershow |

Preview locally: run the `static` launch config (python http.server on 8790) from the repo root and open `/projects/sor-design-system/`. Markdown pages are not rendered locally; open the HTML pages and specimens directly.

## Where things came from

- The former `life-itself/sor-brand` repo, merged here 2026-10-05 with history and since folded in: [decisions.md](decisions.md) (design-system plan and decision log), [logo-notes.md](logo-notes.md), `moodboard/` (references and images, not published), `archive/sor-brand-mockups/` (the mockups the system was extracted from: Direction E v7 and the four-page v2) and `archive/sor-brand-STATUS.md`.
- The old website design project (`2026-sor-website`, directions and moodboard, 2026-09): `archive/website-2026-09/`. Its brand substance and page copy now live here as [brand.md](brand.md) and `content/`.
- [type/](type/): the two type selection rounds and research notes.
- Brand substance (who we are, offers, voice) stays in [brand.md](brand.md).

Shared by the SoR [experiences](../sor-experiences-2026/) and the website. The experiences carry their own working palette in [common.md](../sor-experiences-2026/experiences/00-home/common.md#colour), not yet reconciled with this system.
