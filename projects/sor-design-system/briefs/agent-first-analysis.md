# Analysis: a design system people and their agents can use

Phase 1 of [the brief](agent-first-design-system.md) (beads `design-34t.57`), 2026-10-15. Critiqued by a fresh agent against the brief and revised. The first pathway (social post) is being shipped as Phase 2 step 1; this document is the reasoning behind it.

## The essence: five points to validate

1. **The content is fine; the route fails.** Given a kit, fresh agents made an on-brand Instagram post and thumbnail in under a minute. They lost their time finding the way: a front door that says nothing, three maps, stale files that contradict the kits, and nothing on how the website repo uses the system.
2. **One roadmap for agents, in the repo, organised by job:** `projects/sor-design-system/AGENTS.md`. Each job's route says read, use, copy, ask the person for, check, watch out. Other repos point to it with a short block in their own `AGENTS.md`; `llms.txt` points to it for agents with only a link.
3. **Prompts for people to paste**, one per job, on a "Use with an agent" page; each one only sends the agent to its route.
4. **A person with an agent reaches the prompt in one click**: home → "A social post" → the Social guide opens with the prompt to paste (copy button). The templates page shows what the agent will make; the Canva download sits lower, for the separate Canva job (its own bead).
5. **Start here (BUILD) goes in a later step**, its rules moved into the roadmap and a short "brand in five minutes" page. A skill comes later, as a thin pointer to the roadmap.

## 1. Best practice, briefly

**Design systems for people.** The good ones (GOV.UK, Polaris, Atlassian, Material, Primer) share a few habits worth copying:

- **Entry by role, then by task.** "Get started" splits designers from developers (Polaris, Atlassian) or prototypers from production teams (GOV.UK). Nobody reads a general preamble before the thing they came for.
- **Every pattern page has the same shape**: what it is, when to use it, when not to, how it works, the code to copy, and the research behind it (GOV.UK). The code block has a copy button.
- **Kits are downloads, not descriptions.** A Figma library, a Sketch file, a zip: one click.
- **Tokens are the single source**; everything else references them.
- **Status lives in a changelog or roadmap**, not on the guidance pages (we already do this).

**Projects serving agents, now.**

| Mechanism | What it is | Fits our case? |
|---|---|---|
| `llms.txt` | A markdown index of a site's pages at a known URL, for agents that only have the web | Yes, for agents given a link. Not where agents with a checkout look |
| `AGENTS.md` / `CLAUDE.md` | Instructions an agent reads automatically when working **in** that repo or folder; nearest file wins | Yes for maintainers. For consumers in another repo it is read only if something points to it |
| Agent Skills (`SKILL.md`) | A folder with a short description always in context and a body loaded only when the task matches. Installable per user (`~/.claude/skills`) or per repo. Anthropic ships a `brand-guidelines` skill as the model | Good for "make it on brand" from any repo without pasting, but Claude-only and a second copy of the rules if it holds content |
| MCP servers (Figma Dev Mode, Storybook, shadcn registry, Serendie) | A live service the agent queries for components and tokens | Overkill: we have a folder of files, not a component library in a package |
| Paste-in prompts | A prompt library people copy into any agent (Codex, Cursor, Claude) | Yes: tool-agnostic, and it is what people actually do |

**The state of the art for "agent in another repo uses our design system"** is not settled. What works in practice is a chain of three short hops: the consumer repo's `AGENTS.md` names the design system and its entry file; the entry file routes by job; the job's route names a handful of files and an example to copy. Tokens and CSS arrive by a package or a sync script (sor-website already syncs at a pinned commit). Skills and MCP are ways to automate the first hop.

**What we should copy:** one entry file organised by job, with repo paths (GOV.UK's page shape, compressed); the consumer-repo pointer; a prompt library with copy buttons; kits as one-click downloads; and, once the roadmap works, a thin skill that just loads it.

## 2. Who comes, and why

**Users.**

- **A. A person with an agent in another repo.** The commonest. Rufus or a colleague in `sor-website`, `comms`, a paper's repo: "go to the design repo and find what you need to be on brand." The agent has the design repo checked out at `~/src/life-itself/design`.
- **B. An agent on its own**, given a repo path or a link (a delegated or scheduled task, a subagent, someone else's agent with only the URL).
- **C. A person without an agent**: comms or a volunteer working in Canva, a partner who needs the logo, a new collaborator getting the feel.
- **D. A maintainer** (in practice Rufus with an agent, in the design repo): adds a graphic, changes a token, records a decision.

**Job stories, ranked** by how often they happen now times what they are worth. Frequency is the next three months: website launch, podcast and gatherings starting.

Rank is often × value, with weekly-or-more and high value first.

| # | Job story | Users | Often | Value |
|---|---|---|---|---|
| 1 | When I'm building or changing a page on the SoR website, I want my agent to use the right sections, classes and copy without restyling anything, so I can ship pages that look like the design without a design pass | A, B | Weekly | High |
| 2 | When we announce something (gathering, episode, essay), I want a social post in the right shape that I can post or finish in Canva, so I can announce it the same day | A, C | Weekly | High |
| 3 | When a podcast episode or video goes out, I want its thumbnail and cover from the kit, so I can publish without a designer | A, C | Per episode | High |
| 4 | When something is made, I want to check it against one short list, so I can catch off-brand work before it goes out | A, B, D | Every job | High |
| 5 | When I need the logo or a woodcut, I want the right file in one or two clicks, so I can drop it into whatever I'm making | C, A | Weekly | Medium |
| 6 | When the system changes (a graphic, a token, a decision), I want my agent to update every place that depends on it, so I can keep pages, kits, the roadmap and the other repos in step | D | Daily now, weekly later | High; one maintainer, so below the jobs many people do |
| 7 | When I need a diagram for a paper or a talk, I want to build it in our style as SVG, so I can make figures without a drawing tool | A | Monthly | Medium |
| 8 | When I'm making slides, I want a deck to copy, so I can present on brand | A, C | Monthly | Medium |
| 9 | When I'm producing a paper as a PDF, I want the cover and the pipeline, so I can publish a paper that looks like the others | A | Rare | High |
| 10 | When I'm new to SoR, I want the brand in five minutes (feel, voice, what we are not), so I can make sensible choices on my own | C, A | Rare | Medium |
| 11 | When I write the newsletter, I want its constraints and an example, so I can send it on brand | A, C | Monthly | Low (no example yet) |

**Four kinds of use.** The jobs above are mostly how-to. Rufus named three more needs the site must serve, each a kind of page rather than a job:

| Kind | Job story | Today |
|---|---|---|
| Walkthrough | When I want to understand the system as a whole, I want a compact tour from the brand narrative through feel, colour, type and graphics to an example, at a glance or in depth, so I can see how it fits together before I make anything | Only `guide.html` (the whole system rendered, no narrative) and the Brand, Feel and Voice pages (3,700 words) |
| How-to | When I'm making X, I want the route for X, so I can make it on brand quickly | Jobs 1–9 and 11; the social route shipped |
| Reference | When I need a thing (all the woodcuts, all the fonts, every token, every logo file), I want one index to look it up, so I can find it without reading guidance | Scattered: Logo files and Graphics galleries exist; fonts sit in Type, tokens in a CSS file, components in Components; no index |
| Maintain | When I change the system, I want the steps and what to keep in step, so I can change it without breaking pages or other repos | Job 6; `MAINTAINING.md` and the roadmap's Maintain route |

The home page's three doors (make, file, understand) map roughly to how-to, reference and walkthrough; maintain sits under About. Making all four explicit is part of the home and nav step.

The top two for Phase 2 are as the brief guessed: **1, the website page** and **2, the social post**. Number 4 (check) and number 6 (maintain) are not separate pathways so much as the end of every pathway and the reason the others stay true.

## 3. Walking the current paths

### Tests with fresh agents

Three agents, each given only a realistic request and told not to change anything. Each logged what it read. Outputs are in the session scratchpad, not the repo.

| | Request | Where it started | Calls before acting | Time to act | Result |
|---|---|---|---|---|---|
| Social | "Make an Instagram post announcing our next gathering… design system is in ~/src/life-itself/design" | `comms` repo | 15 | 47 s | On brand (sunlight ground, swallows and prints, Polyamine headline, logo under the words, ink text). 1:1 version guessed |
| Thumbnail, site only | "Make a YouTube thumbnail for our podcast episode… design system: https://design.seedsofrenaissance.org" | No repo, web only | 10 | 50 s | On brand from the Canva kit layers; hook line invented; guest photo a placeholder |
| Website | "Make the podcast page on brand. Use the design system in ~/src/life-itself/design" | `sor-website` repo | 26 | 80 s | Plausible but unchecked: a white intro and a sunlight band with a black button under Flowershow's own header; no woodcuts, no show art; two rules added to the site CSS. Not rendered |

What they got wrong or lost time on:

- **The front door says nothing.** "Go to the design repo" lands on `design/AGENTS.md` (Beads and changelog rules) and `design/README.md` (about the Life Itself playground). Neither mentions `projects/sor-design-system/`. The social agent found it by `ls`.
- **Three maps.** The repo agent read README then BUILD and never reached `llms.txt`. The site agent read `llms.txt` then BUILD. Both orders work, but each map lists every guide, rule and topic again, and none says which three files the job needs.
- **The job is named by platform, the guide by product.** "YouTube thumbnail for our podcast" went to `youtube.md`, which sends podcast covers on to `podcast.md`. One wasted hop: the home page and BUILD route podcast covers correctly, but the agent matched "YouTube" first in llms.txt.
- **Stale files contradict the kits.** `system/tokens.css` `--thumb-*` (Bricolage name at 64px, logo on a white disc) disagrees with the kit and `podcast.md` (Apfel 48px, no disc). The Instagram `build.py` docstring says white ground and lockup top right "for now"; the README and PNGs say sunlight and lockup under the words. The script path is `system/build/swallows.py` in one place and `system/swallows.py` in another. Agents had to pick a winner.
- **Sources missing.** The kits' `src/` folders are gitignored, so "rebuild from src/" fails; on the site `canva-kit/build.py` and `system/fonts/` return 404 (as HTML pages, not errors).
- **Gaps in the kits.** No 1:1 announcement; no guidance for building a cover in code rather than Canva; nothing on what to ask the person for (the episode's hook, the guest photo) when it is missing.
- **Fonts.** Polyamine renders only because it is installed on this Mac; on another machine it falls back to Fraunces. Not cleared to publish until licensed, which pages say but no checklist asks.
- **Expensive files.** `system/fonts.css` embeds fonts as base64 (122KB); an agent that reads it to find the faces burns its context.
- **Website: nothing fits the real site.** The website agent took twice as many calls, mostly piecing together how `sor-website` works from its own README and CSS. `website.md` assumes a standalone HTML page; the example it names for a podcast page is the magazine page; `podcast.md` covers only images. Woodcuts need the sprite, which only Home inlines, so Markdown pages can't use them (fixing that is the website's call; the route states it as it is). The page-title component duplicates Flowershow's header. The show art isn't in the pinned commit. And `sor-website`'s `site-overrides.css` gives `.post-hero` a white mount, tilt and shadow, the postcard look rule 7 forbids.

What each agent said it wanted is the same thing: a per-job recipe. "Instagram announcement: read the kit README (Announcement row) and voice.md (calls to action); copy the announcement entry in build.py; render with export.sh; no 1:1 exists; Polyamine is unlicensed; don't read fonts.css."

### The website page, and the repo it lives in

The design system doesn't know how its main consumer works. `sor-website` is Flowershow Markdown with raw HTML, synced CSS (`scripts/sync-design.py` copies `tokens.css`, `components.css`, fonts and scripts at a **pinned commit**), site CSS only in `scripts/site-overrides.css`, no Tailwind, and its own `AGENTS.md` that says the design repo is read-only. `website.md` describes something else: a standalone HTML page with a `<head>`, `system/` paths and a shell to copy. Nothing in the design system mentions `sor-website`, the sync, or the pin.

Two consequences:

- **The website route is mostly about words, not markup.** On the site, plain Markdown is already on brand (the synced CSS styles Flowershow's pages), and `sor-website` decided against hand-written component HTML per page (`docs/templating-findings.md`): new kinds of page get a template in its build script. So the route has three cases: write or change a page in plain Markdown (voice, brand, real copy); a new kind of page (source plus build script, designed first as a mockup here); a change to the look (here, then bump the pin). `website.md` is about designing mockups, and now says so.
- **Moving files breaks the website.** The pin is 42 commits behind (23 of them touch the design system). Today's graphics move took away two paths `sync-design.py` reads (`system/woodcuts/mountain-range.svg`, `system/img/logo.png`), so the next bump will fail. Paths other repos read are a contract, and the maintainer path has to say which they are.

### Walking as a person (no agent)

**Make an Instagram post** (job 2): Home → "I'm making something" (jumps down the page) → "Social and Canva" (`social.md`, 700 words: shapes, kinds, rules, Canva) → "Instagram kit" → the kit page. The kit page has a "What's in the download" section with numbered folders (`1-backgrounds`, `2-elements`…), but **there is no download**: the files are loose PNGs in `png/`, not in folders. Each PNG is published at its own URL, but nothing lists them to download. A Canva user can't get the kit in one go. Three clicks and a dead end (1,300 words read on the way: the home page, then `social.md`).

**Build a website page** (job 1): Home (600 words) → "I'm making something" → table says "Read Start here once" → Start here (BUILD) → "the brief in one paragraph" and rules → "Pick what you're making": **the same table again**, now with `website.md`-style filenames as link text → Website guide. 1,900 words before the guide's first instruction. The home page and BUILD repeat each other; neither is the fast route.

**Thumbnail** (job 3): Home → "A YouTube thumbnail" → YouTube guide → told podcast covers are in the podcast guide → Podcast → Episode cover kit. Four clicks where two would do.

**Change the system** (job 6, as the maintainer's agent): root `AGENTS.md` (Beads) → `MAINTAINING.md` (1,400 words: how the site is built, publishing, code). It doesn't say which paths other repos read, or that a guide's route and prompt must change with it. Today's graphics move broke two paths the website syncs, which is that gap in practice.

**Get the logo** (job 5): Home → "I need a file" → "Every logo file" → the logo files page. Two clicks; this one works.

**Understand the brand** (job 10): Home → "I want to understand it" → Brand, Feel, Voice (3,700 words between them). Fine for the purpose, but there is no five-minute version: the nearest is BUILD's "brief in one paragraph", which is filed under making things.

### What the pages are, and who they're for

| Page | Written for | Problem |
|---|---|---|
| Home (README) | People | Good three doors; then a full table that duplicates BUILD; sends agents to the site (`llms.txt`) |
| Start here (BUILD) | "Person or agent" | Serves neither: a preamble before the job for people, a second map for agents |
| `llms.txt` | Agents with a URL | A third map; site URLs only, so an agent with a checkout is told to fetch the web |
| Guides (website, social…) | Both | Good content; start with "read BUILD first"; no paste-in prompt; no download for kits |
| Foundations, Brand | People, and agents for detail | Fine |
| MAINTAINING | Maintainers | Doesn't name the paths other repos depend on, or what to update when something moves |

## 4. Proposal

### The roadmap: `AGENTS.md` in `projects/sor-design-system/`

One file, organised by job, with **repo paths** relative to the design system folder. It is the single map. It goes where agents look (`AGENTS.md`, with `CLAUDE.md` importing it) and where people point their agents.

- **First screen:** what this is, the rules that apply everywhere (all eight from BUILD, compressed), then a table of jobs. Each job links to its route lower in the same file.
- **Each route**, four lines: *read* (two or three files, with anchors), *use* (tokens, classes, kit files), *copy* (the one example), *check* (the guide's checklist), plus *ask the person for* (what only they have: the hook line, the photo, the date) and *watch out* (known gaps, like the missing 1:1 announcement or the font licence).
- **Repo-specific branches** where a consumer differs: "in `sor-website`: Markdown pages, synced classes, the repo's own AGENTS.md wins."
- **A maintainer route** at the end ("changing the system"), pointing to MAINTAINING.md.
- **Under 1,500 words.** Detail stays in the guides; the roadmap only routes.
- **Works from the site too**, with one caveat stated in the file: Python scripts aren't published, so each route says what to use without a checkout (for the social post, the guides PNGs show where the words go).

**`llms.txt` points to the roadmap first** (done in step 1). Later, `build-site.py` writes it from the roadmap's jobs table and route headings, with paths turned into URLs, so there is one map to keep. **BUILD.md goes**: its brief and rules move into the roadmap's first screen and into a short human page (below); its URL redirects through the MOVED map.

**Pointer in other repos.** A short block in the consumer repo's `AGENTS.md`, given on the prompts page to copy. It names the usual checkout path (`~/src/life-itself/design`, the sibling folder `sor-website`'s sync script assumes) and the site as fallback:

```markdown
## Design
On-brand work for Seeds of Renaissance uses the design system in the design repo.
Read ~/src/life-itself/design/projects/sor-design-system/AGENTS.md (or, without a checkout,
https://design.seedsofrenaissance.org/AGENTS.md) and follow the route for your job.
Where this repo's own rules differ, this repo wins.
```

The design repo's root `AGENTS.md` gets one line too: "Seeds of Renaissance design system: start at `projects/sor-design-system/AGENTS.md`."

**Sketch of the roadmap's first screen:**

```markdown
# Seeds of Renaissance design system: roadmap for agents

You're making something for Seeds of Renaissance, or changing the system itself.
Find your job below, read only what its route names, copy its example, check its list.
Paths are relative to this folder (projects/sor-design-system/ in life-itself/design).
The published site mirrors them: https://design.seedsofrenaissance.org/<path>.

## Rules everywhere
1. Four faces: Polyamine for headlines under ~10 words, Restora beyond and for the poetic italic,
   Bricolage Grotesque for reading, Apfel Grotezk for small uppercase labels.
2. Ink and paper first: white, paper, sunlight; one night section; colour from photographs.
3. Buttons and marks are ink. Red only as the logo, an in-text link, a red woodcut.
4. No bright yellow, no highlighting, no gradients except a photo scrim.
5. The hand is the texture: torn edges, paper grain, woodcuts. No filters or stock textures.
6. Images are clean: flat and square, no white mount, tilt or shadow.
7. Real copy in our voice (voice.md). Tokens only (system/tokens.css).

## Jobs
| You're making… | Route |
|---|---|
| A page or section on the SoR website | [website](#website-page) |
| A social post (Instagram, LinkedIn, event banner) | [social](#social-post) |
| A podcast or YouTube cover, thumbnail or show art | [episode cover](#episode-cover) |
| Slides · a diagram · a paper (PDF) · the newsletter | [slides](#slides) · [diagram](#diagram) · [paper](#paper) · [email](#email) |
| The logo or a graphic, as a file | [assets](#assets) |
| A check that something is on brand | [check](#check) |
| A change to the design system itself | [maintain](#maintain) |

Don't read: system/fonts.css (embedded fonts), archive/, briefs/. Status lives in beads, not here.

## Social post
- Read: examples/social/instagram/README.md (your template's row), voice.md#calls-to-action
- Use: examples/social/instagram/png/bg-4x5.png and element-*.png; ink #1b1916, muted #5d584f
- Copy: the template entry in examples/social/instagram/build.py; render with export.sh
- Ask the person for: the date, place and one-line hook, if not given
- Check: social.md#rules-for-social, plus Rules everywhere
- Watch out: announcement is 4:5 only; Polyamine is not yet licensed (flag before publishing)
```

### The prompt library: `prompts.md`

A page for people, one prompt per job, each in a code block with a copy button. Prompts are short and route; they don't restate rules (the roadmap holds those). Each says: the job, where the roadmap is, what to deliver, to ask for what's missing, and to report what it checked. The guides also show their prompt at the top.

**Example 1: a website page** (paste in `sor-website`):

```text
Build the [podcast] page for the Seeds of Renaissance website, on brand.
Use the design system in ~/src/life-itself/design/projects/sor-design-system:
read its AGENTS.md and follow the "website page" route. This repo's AGENTS.md
wins where they differ (Markdown pages, synced CSS, no hand-edited design files).
Use real copy; ask me for anything you can't find. When done, list the
checklist items you checked and anything you guessed.
```

**Example 2: an Instagram post** (paste anywhere):

```text
Make an Instagram post (4:5) for Seeds of Renaissance announcing [what],
[when], [where]. Use the design system in ~/src/life-itself/design/projects/sor-design-system
(or https://design.seedsofrenaissance.org if you don't have it): read its
AGENTS.md and follow the "social post" route. Give me the PNG, the caption,
and the steps to finish it in Canva. Tell me what you checked and what you guessed.
```

Others to write in Phase 2: episode cover, slides, diagram, paper, check this, "update the design system" (maintainer), and "set up this repo to use the design system" (adds the pointer above).

### The home page and "Start here"

- **Home** keeps the three doors, and "I'm making something" goes to one list of jobs (human words, never filenames) where each row links to its guide and straight to its kit. Two clicks: home → kit → download. Guides can repeat what their path needs; what goes is the second copy of the whole table in BUILD.
- **"Start here" goes.** Its job split three ways: the job list (home), the rules and checklist (the roadmap for agents; a short **"The brand in five minutes"** page for people, which also serves job 10), and the agent entry (the roadmap). Nav becomes **Make · Assets · Use with an agent · Foundations · Brand (with "in five minutes" first) · Examples · About**, with "Use with an agent" going to `prompts.md`.
- **Every guide opens with two lines**: "With an agent: copy this prompt" and "By hand: download the kit / open the Canva template". Then rules, then the checklist. No "read BUILD first".
- **Kits become downloads**: `build-site.py` zips each kit's `png/` into the folders its README describes and links it at the top of the kit page. (The site copy drops the examples' `.gitignore` files, which ignore `*.zip`.)

### Who each page is for

| For | Pages |
|---|---|
| People | Home, The brand in five minutes, Prompts, kit pages and downloads, galleries, Logo files, Examples |
| Agents | `AGENTS.md` (roadmap), `llms.txt` (generated from it), `system/` files, `build.py` and `elements.json` |
| Both | Guides (website, social, podcast…), Foundations, Brand, Voice, Components |
| Maintainers | MAINTAINING.md, decisions.md, the maintain route in the roadmap |

### The maintainer path

MAINTAINING.md gains a "Keep in step" section: when you change X, update the guide, its roadmap route, its prompt if the job changed, and rebuild (llms.txt and kit zips are generated). It lists **the paths other repos read** (from `sor-website/scripts/sync-design.py`: `system/tokens.css`, `components.css`, `graphics.js`, `sor.js`, `system/fonts/`, `system/img/`, the woodcut the CSS masks with, and the home mockups in `projects/sor-website/home/`), so a move adds a redirect or tells that repo. A maintainer prompt:

```text
Change the Seeds of Renaissance design system: [what]. Work in
~/src/life-itself/design/projects/sor-design-system; read AGENTS.md (the "Maintain" route)
and MAINTAINING.md first. Update the guide, its route in AGENTS.md, its prompt in
prompts.md and llms.txt in the same change, and check the paths other repos read.
Show me the change before committing.
```

### A skill?

**Not first; later, thin.** A skill would make "make this on brand" work from any repo without pasting, which is the commonest case. But it only works in Claude tools, and a skill that holds the rules is a second copy that drifts. So: build the roadmap and prompts, test them, then add a user-level skill `sor-design` whose body is a few lines ("read the roadmap at this path, follow the route for the job, report what you checked") and whose description triggers on "Seeds of Renaissance", "SoR", "on brand". Keep its source in the design repo with an install line on the prompts page. Phase 2 can measure it against the paste-in prompt with the same fresh-agent test.

### Fix along the way

The stale files and missing sources listed in section 3, each in the step that needs it; the `.post-hero` postcard look is flagged to `sor-website`, not ours to fix.

## 5. Shipping

**Step 1, being shipped now: the social post.** The roadmap (`AGENTS.md`) with its first screen, the full social route and short routes for every other job; the root pointer; `llms.txt` pointing to it; the "Use with an agent" page with the social prompt, a general prompt and the repo pointer; a downloadable Instagram kit at the top of the kit page, reached from the home page in two clicks; the stale kit docstring fixed. Tested with a fresh agent given only the pasted prompt (from `comms`): on brand, 10 calls and 47 s before its first output, reading only what the route names plus the voice sections a caption needs. Where it had to guess (the helpers behind the template, the logo position, fonts, the 30 px label), the route now says.

**Then:** the website route in full (with a component table per site page), the pointer added to `sor-website` and `comms`, the other routes, the home page and nav, retiring BUILD, the maintainer section, and the skill.

**Decisions taken here** (say if wrong): the roadmap is `AGENTS.md` (the name agents look for); BUILD goes once the roadmap and "brand in five minutes" page carry its content; kit downloads are zips built at publish.
