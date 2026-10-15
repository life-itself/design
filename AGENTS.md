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
| A paper (PDF) or poster | [Paper](#paper) |
| The newsletter | [Email](#email) |
| The logo or a graphic, as a file | [Assets](#assets) |
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

A podcast episode is published as a YouTube video, so its thumbnail is the episode cover: use `podcast.md`, not `youtube.md`.

- **Read:** `podcast.md`, `examples/youtube/canva-kit/README.md`.
- **Use:** `examples/youtube/canva-kit/png/02-background-with-logo.png`; the sizes in the kit README.
- **Ask the person for:** the episode's sharpest line (the hook, not the title), the guest's name and photo.
- **Check:** "Before you publish" in `podcast.md`. Channel art and other YouTube images: `youtube.md`.

## Slides

- **Read:** `slides.md`. **Copy:** a deck in `examples/slides/`. **Check:** `slides.md`.

## Diagram

- **Read:** `diagrams.md`. **Copy:** a figure in `examples/diagrams/`; build it as SVG with the helpers in `examples/diagrams/build.py`. **Check:** `diagrams.md`.

## Paper

- **Read:** `print.md` (covers, anatomy of a paper, the Typst pipeline). **Copy:** `examples/print/`. **Check:** `print.md`.

## Email

- **Read:** `email.md`. No example yet: follow the guide.

## Assets

- **Logo:** `logo.md` says which version goes where; the files are in `system/logo/`, all shown on `logos.md`.
- **Graphics:** `graphics.md` lists the sets and their rules; files and `elements.json` in `system/graphics/<set>/`.
- **Photographs:** `photography.md`. Every current photograph is a placeholder, not cleared for use.

## Check

The rules everywhere, then the checklist in the guide for what was made. Report what you checked and anything you guessed.

## Maintain

Read `MAINTAINING.md`. When you change something, update in the same change: the guide, its route here, its prompt in `prompts.md`, and `llms.txt`. Other repos read some paths directly (the website syncs from `system/`): don't move a file without checking.
