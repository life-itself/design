# Seeds of Renaissance design system: the roadmap for agents

You're making something for Seeds of Renaissance, or changing this design system. Find your job below, read only what its route names, copy its example, and check against its list before you hand it back.

Paths are relative to this folder: `projects/sor-design-system/` in the `life-itself/design` repo, usually checked out at `~/src/life-itself/design`. Without a checkout, the same paths are on the site: `https://design.seedsofrenaissance.org/<path>`, with pages as raw markdown at `<page>.md`. Python scripts are in the repo only.

Working in another repo? Its own rules win where they differ (how it builds, what you may edit). Don't write into this repo unless your job is to change the system.

## Rules everywhere

1. **Four faces.** Polyamine for headlines and titles under ~10 words; Restora for longer display text and the poetic italic; Bricolage Grotesque for reading; Apfel Grotezk for small uppercase labels.
2. **Ink and paper first.** White, paper and sunlight (pale yellow) grounds; one night section per piece; colour comes from photographs.
3. **Buttons and marks are ink.** Red only as the logo, an occasional link in running text, or a red woodcut.
4. **No bright yellow, no highlighting, no gradients**, except a scrim to make text readable on a photo. Sunlight is a ground, never text.
5. **The hand is our texture:** torn edges, paper grain, woodcuts. No filters, no stock textures.
6. **Images are clean:** a photograph sits flat and square, full-bleed or in its column. No white mount, tilt or drop shadow.
7. **Real copy in our voice** (`voice.md`). Use the tokens in `system/tokens.css`; no colours or sizes of your own.

## Jobs

| You're making… | Route |
|---|---|
| A social post: Instagram, LinkedIn, an event announcement | [Social post](#social-post) |
| A page on the website, or a change to one | [Website page](#website-page) |
| A podcast or YouTube cover, thumbnail or show art | [Episode cover](#episode-cover) |
| Slides | [Slides](#slides) |
| A diagram, figure or chart | [Diagram](#diagram) |
| A paper (PDF) | [Paper](#paper) |
| The newsletter | [Email](#email) |
| The logo, a graphic, a font or a colour, as a file or a value | [Assets](#assets) |
| A check that something is on brand | [Check](#check) |
| A change to the design system itself | [Maintain](#maintain) |

Don't read `system/fonts.css` (fonts embedded as data, very long), `archive/` or `briefs/`. Progress and open questions are in beads, not here.

## Social post

Instagram feed posts (4:5, 1:1) from the Instagram kit. Other shapes (16:9, link preview, story, banners) are in `social.md`.

- **Read:** `examples/social/instagram/README.md`, the row for your template (podcast episode, quote card, announcement, statement, carousel); in `voice.md`, "The voice in one line", "Register by place" and "Calls to action" (for the words on the image and the caption).
- **Use:** the whole background in one image, `examples/social/instagram/png/bg-4x5.png` (or `bg-1x1.png`; `-quiet` for text-heavy posts); the logo lockup `png/element-logo-lockup.png`; text in ink `#1b1916`, secondary lines muted `#5d584f`; everything left-aligned at x 90.
- **Copy:** the template's entry in `T` in `examples/social/instagram/build.py`, with the helpers above it (`label`, `poly`, `brico`, `resto`, `logo`): together they give fonts, weights, sizes, letter-spacing and positions (x, baseline y; for the logo, y is its top). They are the spec. Without the repo, `png/guides-<template>-<format>.png` (e.g. `guides-announcement-4x5.png`) shows the same boxes, labelled with font and size, and `png/example-<template>-<format>.png` shows the result: measure baselines from it. Labels are Apfel Grotezk 500, uppercase, letter-spacing 0.12em.
- **Make it:** an HTML page in your own repo or a scratch folder, the background as a full-size image and the words as text on top at the template's positions (SVG `<text>` uses the same baselines). Fonts: copy the `@font-face` lines and the Google Fonts link from `PAGE` in `build.py`. Without the repo, link `system/fonts.css` as a stylesheet (don't read it) and Bricolage Grotesque from Google Fonts; the Polyamine and Restora files are in the repo only, so say the type needs checking or finish in Canva. Screenshot at the post's size with headless Chrome: `--headless=new --hide-scrollbars --force-device-scale-factor=1 --window-size=1080,1350 --screenshot=post.png file:///path/post.html` (as in `export.sh`). For Canva, hand the person the background, the logo and the words, and the steps in the kit README ("Make a post in Canva").
- **Ask the person for:** what it announces, the date and place, the one line they want on the image, if they haven't said.
- **Check:** `social.md#rules-for-social` (its "Everything in BUILD.md" is the rules above). One idea; five to ten words on the image, the rest in the caption; nothing under ~36 px except the template's 30 px label; the logo under the words. Dates match their weekday.
- **Watch out:** the announcement exists in 4:5 only; a 1:1 needs the 1:1 background and positions scaled from `statement-1x1`. Polyamine and Restora are not yet licensed: say so if the post is going out.

## Website page

The website is the `sor-website` repo: Flowershow Markdown pages, with the CSS, fonts and scripts synced from this folder at a pinned commit. So a plain Markdown page is already on brand; what you add is the words, the images and the order. That repo's `AGENTS.md` wins where it differs.

First read that repo's `AGENTS.md` and `README.md` (how it builds, what you may edit, how it marks TODOs), and open the page if it exists. Then, which of three cases are you in?

- **Writing or changing a page** (most jobs, including section pages such as Podcast or Events): plain Markdown with `title` and `description` in the frontmatter. No HTML (other than that repo's TODO comments), classes or inline styles.
  - **Read:** in `voice.md`, "The voice in one line", "Register by place", "Calls to action", "Words" and any section on the page's subject (for Podcast, "YouTube and podcast"); `brand.md` for who we are, what we offer and who we speak to. The key lines in `voice.md` are the approved copy to build from.
  - **Use:** short sections with plain headings, short paragraphs, links with button text from "Calls to action". Images are clean (rule 6), one idea each; every current photograph is a placeholder (`photography.md`), so leave a TODO rather than an uncleared image.
  - **Ask the person for:** facts only they have (dates, names, links, the feed or player). Don't name guests until they are confirmed.
- **A new kind of page** (an episode, a type of post, a page with its own layout, not one page): don't hand-write component HTML into the page. The content goes in the site's `src/` with frontmatter, and its build script (`scripts/build-content.py`) renders it. A new layout starts here, as a mockup in `examples/web/` built from `components.md` (see `website.md`), then becomes a template in that script.
- **Changing how the site looks** (a colour, the type, a section): change it here (see [Maintain](#maintain)), then bump the pin in `sor-website`. CSS for the site alone goes in its `scripts/site-overrides.css`.
- **Check:** the copy is real and in our voice, with anything unconfirmed marked as that repo marks TODOs; images are clean; no inline styles or colours; that repo's own checks pass (`scripts/check-links.py` and `scripts/prepublish-scan.py`). For a mockup here, the list at the end of `website.md`.
- **Watch out:** the site only has what exists at its pin, which can be behind this folder: check with `git show <pin>:projects/sor-design-system/<path>` in this repo. Woodcuts need the sprite, which only Home has.

## Episode cover

A podcast episode goes out as a YouTube video, so its thumbnail (1280 × 720) is the episode cover. Show art and square episode art: `podcast.md`, "Show art" and "Episode art". A thumbnail for any other video (a talk, an essay): copy the `thumb--talk` or `thumb--manifesto` artboard in `examples/youtube/index.html` and follow "Thumbnail rules" in `youtube.md`. Channel art: `youtube.md`.

- **Read:** `examples/youtube/canva-kit/README.md`, "Make a thumbnail" (every position and size) and "Rules in short"; in `voice.md`, "YouTube and podcast" (the hook, the video title, the description's opening lines).
- **Use:** the whole background in one image, `examples/youtube/canva-kit/png/02-background-with-logo.png` (2560 × 1440, drawn at 2×: the sunlight ground, swallows, fingerprints and the logo with PODCAST, all in place). Nothing else to place but the guest and the words.
- **Copy:** the layout at the top of `examples/youtube/canva-kit/build.py` (`Q`, `NAME`) and `words()`, `face_one()` and `face_two()`: the hook in Polyamine 112 px, ink `#1b1916`, at x 80 on baselines 185 and 297, two lines no wider than 520 px; the guest's name in Apfel Grotezk 500 at 48 px (42 for "Name & Name"), baseline 375; one guest as an 800 × 800 image at x 560, y 10. Without the repo, the README's step list gives the same numbers and `png/example-with-guides.png` shows them.
- **Make it:** an HTML page in your own repo or a scratch folder, with a 1280 × 720 SVG: the background as an `<image>` at width 1280, height 720, the guest, then the words as `<text>` at those baselines. Fonts: copy the font lines of `PAGE` in `build.py`, with its relative paths made absolute (`file:///…/projects/sor-design-system/system/…`); its `{defs}` is a mask for two guests only, so leave it out for one. Without the repo, link `system/fonts.css` from the site (don't read it); Polyamine is in the repo only, so say the type needs checking or finish in Canva. Screenshot with headless Chrome: `--headless=new --hide-scrollbars --force-device-scale-factor=1 --window-size=1280,720 --screenshot=cover.png file:///path/cover.html`.
- **The guest:** cut out (a transparent PNG), black and white (`style="filter:grayscale(1)"` on the image), head about three-quarters of the height, shoulders running off the bottom. If the photo isn't cut out, don't try: make the cover without the guest and give the person the README's Canva steps for adding them (BG Remover, saturation −100, the `06-guest-example.png` size guide).
- **Ask the person for:** the hook (a phrase the guest actually says, three to five words, not the topic), the guest's name, their photo (ideally already cut out), and one line on what the episode is about, for the title and description.
- **Check:** "Before you publish" in `podcast.md`. The hook is the biggest text and isn't the video title; no words or face in the bottom-right corner, where YouTube shows the video length (the guest's shoulder may run into it); at 168 px wide (YouTube's "Up next") the face and the hook still read; no arrows, extra colours or episode numbers. Hand back the PNG, a video title (40–60 characters) and the description's opening lines from `voice.md`.
- **Watch out:** Polyamine is not yet licensed, and the swallow engraving is not cleared: say so if the cover is going out.

## Slides

A deck is an HTML page of 1920 × 1080 slides: presented from the browser, saved as a PDF.

- **Read:** `slides.md`, all of it (short): the two registers, the slide types and the rules. For the words, in `voice.md`, "The voice in one line", "Calls to action" and "Key lines" (the line under the logo, the closing slide). Pick the register: **Study** for a paper or research talk, **Gathering** for a call, community talk or art evening.
- **Copy:** the whole deck for your register, `examples/slides/study.html` or `examples/slides/gathering.html`. Each slide is a `<figure>` in `#slides`: a `.slide-frame` holding one `.slide slide--<type>`, then a `<figcaption>` naming it. Keep the slide types and their markup; change the words and pictures, drop the slides you don't need, repeat the ones you do. Take the closing slide's address and handles, and the line under the logo, from `voice.md`, not from the example. Every class and size is in `examples/slides/slides.css` (the `--slide-*` tokens): add none of your own and no inline styles beyond the examples' `object-position`.
- **Make it:** save the copy in your own repo or a scratch folder and point its links at the design system: `../../system/…`, `slides.css`, `deck.css`, `deck.js` and `img/` become `https://design.seedsofrenaissance.org/…` (same paths), so the deck works on any computer; absolute `file:///…/projects/sor-design-system/…` paths into a checkout work only on that machine. Keep `<script src="…/system/graphics.js">` straight after `<body>`: it brings the woodcuts the slides `<use>`. Above the slides, keep only a short intro (the deck's title, one line, the Present button): drop the example's nav and its notes on the register. Open it in a browser: Present shows it full screen (arrows, Esc). PDF, one slide per page: `"<Chrome>" --headless=new --no-pdf-header-footer --allow-file-access-from-files --virtual-time-budget=5000 --print-to-pdf=deck.pdf file:///path/deck.html` (or Print, Save as PDF, in Chrome). Look at every page (`mkdir -p check && pdftoppm -r 20 -png deck.pdf check/p`) before you hand it back. The PDF carries the photographs at full size: for email, resize them first (`sips -Z 1920`).
- **Fonts:** Polyamine and Restora load only where they are installed (`system/fonts.css` names them; don't read it). If titles come out in a fallback face, say the type needs checking.
- **Ask the person for:** the title, the speakers, the event and date, the outline or text of the talk, and their photographs. Without photographs, keep the example's (placeholders from `system/img/`) and say which slides need real ones.
- **Check:** "Rules for slides" in `slides.md`. Nothing under 28 px on the artboard (the `--slide-*` sizes keep to it); Polyamine only for titles under ~10 words (in Study, the cover only), Restora beyond; white by default, at most one night slide per section; red only as the logo, a red seed or a woodcut; one idea a slide, five points at most. A section title is one or two short words: Polyamine capitals are wide, and the woodcut beside it is large, so break a longer one over two lines (`<br>`) or shorten it, and check it doesn't touch the woodcut.
- **Watch out:** the example photographs are placeholders, not cleared; Polyamine and Restora are not yet licensed: say so if the deck is going out. A .pptx (for example from the Claude Slides artifact type) follows the same rules but can't use these classes.

## Diagram

A figure is built as SVG by a short Python script, not drawn in a tool: text set as outlines in Apfel Grotezk, signed bottom right, exported tight for a page and padded for sharing.

- **Read:** `diagrams.md` from "The look in one paragraph" to the end ("Charts with data" only for a chart). The sizes, line weights, red and tint, panel padding and signature rules are all there.
- **Copy:** `examples/diagrams/figure.py` into your own repo or a scratch folder: a whole figure (title, subtitle, panels, arrows, signature) with the house style's values and helpers (`text`, `tag`, `arrow`, `panel`). Change `FIGURE`; for another shape (a cycle, a grid), write your own `draw()` with the same helpers (the file's docstring says what `outline.py` gives you). For curves with a shaded gap (`gap_svg`), layers with brackets (`poly_svg`) or charts (`chart_line`, `chart_bars`, `chart_dumbbell`), borrow the geometry from `examples/diagrams/build.py`, but set the text with `text()` from `figure.py`: `build.py` sets it as CSS-styled `<text>` for its gallery page, which doesn't travel.
- **Make it:** `python3 -m venv .venv && .venv/bin/pip install fonttools uharfbuzz`, then `.venv/bin/python figure.py <name>`: it writes `<name>.svg` (tight, transparent: for a paper or a page) and `<name>.share.png` and `@2x` (the full canvas on white: for sharing alone). It finds the design system at `~/src/life-itself/design`, or set `SOR_SYSTEM` to its `projects/sor-design-system/system`. Without the repo, write the SVG by hand from the same values, with `<text font-family="Apfel Grotezk">` and the ready-made signature `system/img/signature.svg` from the site, and say the text isn't outlined.
- **Ask the person for:** the figure's claim (its title) and what it shows (the subtitle), the parts and how they connect, which one thing it is about (that goes red: a panel's heading, or a line or arrow and its label), where it will be used, and the signature's slot (a publication line such as "Wisdom · White paper No. 6" for a paper; the URL if nobody says). For a chart, the data and its source.
- **Check:** "Check before you publish" in `diagrams.md`. Look at the PNG at 400 px wide and in greyscale (`sips --resampleWidth 400 a.png --out small.png`; `sips --matchTo '/System/Library/ColorSync/Profiles/Generic Gray Profile.icc' a.png --out grey.png`): the smallest text still reads, and nothing relies on colour alone. Alt text says what the figure claims, then what it shows ("Cultural change feeds back into inner transformation: a loop of four stages, …").
- **Watch out:** one face (Apfel, no bold), no outlines on panels, no dashes, no legend, no red text except the key label.

## Paper

A paper is one A4 PDF, typeset from one Markdown file by the Typst pipeline in the `pdf-report-publishing` repo (its `sor` style). This folder decides the look; that repo renders it, and its `AGENTS.md` wins there. Usually checked out at `~/src/life-itself/pdf-report-publishing`; if not, `git clone https://github.com/life-itself/pdf-report-publishing` beside this repo.

- **Read:** in `print.md`, "The look in one paragraph", "Anatomy of a paper" and "Covers and credits". In `pdf-report-publishing`: `docs/styles/sor.md`, "How the paper's Markdown maps to the page" (every convention the build reads: the frontmatter fields, `## N. Title: after` for chapters, the summary box, quotations and epigraphs, figures as `*Fig N: Title. Caption*`), and `fonts/README.md`.
- **Copy:** in `pdf-report-publishing`, `typst/papers/wisdom.typ` to `typst/papers/<name>.typ`. It holds no text: everything comes from the frontmatter. It expects every field, `subseries` and `part` included: a paper that stands alone prints "· Part" on its title page, so ask, and say so if it stays. Don't change the `sor` style for one paper.
- **Make it:** a paper folder (in the paper's own repo, or a scratch folder) holding `essay.md` and `assets/`. In `essay.md`: the frontmatter with every field in the table; then the text in the conventions, with the draft's own title, subtitle and author lines removed (they are frontmatter now). The contents page is built only from a `## Annotated contents` section: a nested list of links to the chapter and section headings, each with `— a one-line summary` if the authors have them. Figures go in as PNG (the build crops their margins from the PNG: use the Diagram route's `<name>.share@2x.png`); with no PNG figure the build stops silently after "figure bounds". From `pdf-report-publishing`: `typst/build-paper.sh <name> <path/to/paper-folder>` writes `output/<name>.pdf`: copy it out to the person and delete it there. The build stops on anything it doesn't recognise: fix the Markdown, not the filter. Look at every page (`mkdir -p check && pdftoppm -r 40 -png <pdf> check/page`).
- **The cover:** the `sor` style draws none: without `cover_image` the PDF starts at the title page. So make one as an HTML page at A4 and export it at 2480 × 3508 (A4 at 300 dpi) with headless Chrome, named in `cover_image`. With art: the art at full size, the words around it. Without art, the plain typographic cover: ink on white, in the order of "Covers and credits" (series line, title, subtitle, a woodcut in place of the art, authors with the Life Itself credit), and the one-colour mark `system/logo/mark/seeds-mark-black.svg`, small at the foot if at all.
- **The editorial pass:** mark summary boxes, epigraphs and quotations only where the text already has them, or where the person asks; they are content decisions. Say which you added.
- **Ask the person for:** the final text, the authors, the series number, subseries and part, version and date, the URL, the licence (CC BY 4.0 by default), acknowledgements and credits, the cover art if any, and the figures. Without answers, take Wisdom's as the pattern (No. 6, Life Itself Sensemaking Studio) and list every guess.
- **Check:** "Check before you publish" in `print.md`. Polyamine only on the cover, title page, contents and chapter titles; red only for links and note marks; every page of the anatomy in order, none blank. A figure's title is drawn in the image and repeated by the caption's `Fig N: Title`: keep the caption's title short.
- **Watch out:** Polyamine and Restora are commercial faces, not yet licensed, and not in that repo: install them or put them in its `fonts/licensed/`. Without Restora the build sets Fraunces and says so; with only some of its weights installed it says nothing, so check the heads and quotations. Either way, say the type needs checking. The PDF is published with the paper, not committed in either repo.

## Email

- **Read:** `email.md`. No example yet: follow the guide.

## Assets

You need a file: the logo, a graphic, a font, a colour or size, a kit. Hand back the file's path (or its URL on the site), and copy it into the other repo only if asked. Never edit the file itself.

- **Look it up:** `reference.md` has one row per graphic set, logo version, font, colour, size, component, kit and example, with its path. Read only the section you need (`## Logo`, `## Graphics`, `## Fonts`, `## Colours`, …).
- **The logo:** the version from "Which mark where" and "Using it" in `logo.md` (the horizontal lockup by default; the stacked one in a footer or a narrow column), the colourway from "Colourways" (by the ground it sits on). Files: `system/logo/lockups/seeds-logo-<version>-<colourway>.svg`, or `-1200.png` and `-2400.png`; the mark alone at a fixed size, `system/logo/mark/sizes/seeds-mark-<colourway>-<px>.png`. Pass on the rules in "Using it": clear space, minimum size, no recolouring or effects.
- **A graphic:** choose the set by rights first: only the **woodcuts** and the **sprite** are ours; every other set is not cleared, for drafts and mockups only. Then search that set's `system/graphics/<set>/elements.json` (each element's `title`, `desc` and `kind`, and its `versions`, whose `file` names the file in `elements/`) rather than opening the gallery page. Pass on the set's colour and grounds from "Rules" in `graphics.md`. Woodcut files are SVG (`<file>.svg`); the swallows also come as `-black.png` and `-white.png`. Each SVG sets its ink on its root (`style="color:#1b1916"`), so as an `<img>` it stays ink: on night, inline it and set `color` to chalk `#ece7dc`, or hand over a copy with that one value changed, and say so. For a PDF or an email, prefer a PNG (the SVGs' rough edge is a filter some tools drop). `seeds.svg` and `seeds-red.svg` are a sheet on a paper rectangle: light grounds only. For a page built from `components.css`, a woodcut can come from the sprite instead (`graphics.md`, "The sprite").
- **A font:** `reference.md`, "Fonts". Apfel Grotezk is in `system/fonts/` (OFL), Bricolage Grotesque on Google Fonts. Polyamine and Restora are licensed: don't copy them into another repo or send them on.
- **A colour or size:** `system/tokens.css`, by token name, with its role in the comment beside it. On the site and in the components, use the token, not the value.
- **A photograph:** `photography.md`. Every current one is a placeholder, not cleared: say so.
- **Check:** the version and colourway suit the ground; the rights allow the use; the file comes from this folder, not an older export (those carry the old mark). Say what you chose and why.

## Check

The rules everywhere, then the checklist in the guide for what was made. Report what you checked and anything you guessed.

## Maintain

You're changing the design system itself, in this repo. Work from `projects/sor-design-system/`.

- **Read:** `MAINTAINING.md`, "Change the system": the common changes and what to keep in step. The rest of that file only as the change needs (how the site is built, specimen heights, publishing).
- **Add a graphic:** first check it isn't already in the set (compare it with the set's files; the woodcuts are generated by `system/graphics/woodcuts/wc.py`, and a hand-drawn file can sit beside them). Then the file in `system/graphics/<set>/elements/` in the set's formats (`elements.json`, `formats`: woodcuts are SVG only); an entry in that set's `elements.json`, edited by hand in the file's own indentation (fields: `system/graphics/README.md`, "elements.json"; the maker in `source`, and `rights` only where it differs from the set's); a row in the set's README. In a set with `"render": "inline"` (the woodcuts) every SVG is placed in one page, so give its `id`s new names that no other file in the set uses. Don't take a rights claim on trust for a set marked as ours: ask who made it. Then rebuild (below).
- **Change a token:** in `system/tokens.css` only, keeping its role comment true. Then find where the old value is written out (`grep -rn '<old value>' --include=*.md --include=*.html --include=*.py .`, leaving out `archive/`) and change or rebuild each place.
- **Record a decision:** the answer in the planning repo's issue tree, the rule as applied in the guide here, linked to it (`MAINTAINING.md`, "Recording decisions").
- **Never hand-edit** generated files: `graphics/<set>.md`, `logos.md`, the tables between `<!-- … -->` markers in `graphics.md` and `reference.md`, `specimens/`, `components.css`, `site/`.
- **Ask the person for:** who decided the change and when, if it's a rule; whether to commit (show the change first unless they said to ship).
- **Check:** the four build commands in `MAINTAINING.md`, "Publish", run clean; `git status` shows only what you meant to change; the guide, its route here, its prompt (in `prompts.md` and at the top of the guide) and `llms.txt` agree (adding a graphic or changing a value usually touches none of them; changing how a job is done touches all four); no published path moved without a redirect, and none that other repos read (`MAINTAINING.md`, "How the site is put together", "The roadmap and the prompts"). Generated pages can't be previewed locally (they are Flowershow pages): render a new graphic on its own to look at it, and after pushing read the changed page on https://design.seedsofrenaissance.org.
