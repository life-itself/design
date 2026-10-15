# Use with an agent

Prompts to paste into an AI agent (Claude, Codex, Cursor) so it makes things on brand. Fill in the parts in square brackets. Each prompt sends the agent to [the roadmap for agents](AGENTS.md), which tells it which files to read for the job, what to copy and what to check.

The agent works best with the design repo on the same computer (`git clone https://github.com/life-itself/design ~/src/life-itself/design`). Without it, the agent reads the same files from this site.

## Make a social post

For an Instagram post (4:5) announcing an event, an episode or an essay. You get the image, the caption, and the steps to finish it in Canva if you want to.

```text
Make an Instagram post (4:5) for Seeds of Renaissance announcing [what], [when], [where].
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system (or, if that folder isn't there,
https://design.seedsofrenaissance.org/AGENTS.md). Follow its "Social post" route and
read only what it names. Don't change anything in the design repo.
Give me the PNG, a caption in our voice, and the steps to finish it in Canva.
Ask me for anything you need that you can't find. Then tell me what you checked
and what you guessed.
```

The [Instagram templates](examples/social/instagram/README.md) show what it will make.

## Make or change a website page

Paste this into your agent in the sor-website repo. It writes the page in Markdown; the site's styles, synced from the design system, make it look right.

```text
[Make / change] the [which] page on the Seeds of Renaissance website, on brand.
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system. Follow its "Website page" route
and read only what it names. This repo's own AGENTS.md wins where they differ.
Don't change anything in the design repo.
Write real copy in our voice and mark anything you're unsure of with a TODO.
Ask me for facts you can't find. Then tell me what you checked and what you guessed.
```

## Make a podcast episode cover

The YouTube thumbnail for an episode (1280 × 720), which is also its cover. You get the image, a video title, the description's opening lines, and the steps to finish it in Canva. A photo of the guest already cut out (a transparent PNG) gives the best result; without one, the agent leaves the guest for you to add in Canva.

```text
Make the YouTube cover (1280 × 720) for the Seeds of Renaissance podcast episode
with [guest], about [what the episode is about, in a line].
The hook: "[a phrase they say in the episode, three to five words]".
The guest's photo: [path to the photo, ideally cut out].
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system (or, if that folder isn't there,
https://design.seedsofrenaissance.org/AGENTS.md). Follow its "Episode cover" route and
read only what it names. Don't change anything in the design repo.
Give me the PNG, a video title, the description's opening lines, and the steps to
finish it in Canva. Ask me for anything you need that you can't find. Then tell me
what you checked and what you guessed.
```

The [podcast kit](examples/youtube/canva-kit/README.md) shows what it will make.

## Make slides

For a talk, a call or a workshop. You get a deck you present from the browser and a PDF, built from the system's slide types: Study for a paper or research talk, Gathering for a call or community evening.

```text
Make a slide deck for Seeds of Renaissance: [the talk, the event and date, the speakers].
Here is the outline: [the outline or text, or a path to it].
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system (or, if that folder isn't there,
https://design.seedsofrenaissance.org/AGENTS.md). Follow its "Slides" route and
read only what it names. Don't change anything in the design repo.
Give me the deck as an HTML page I can present from, and a PDF.
Ask me for anything you need that you can't find. Then tell me what you checked
and what you guessed.
```

The [example decks](examples/slides/index.html) show what it will make.

## Make a diagram

For a figure in a paper, on slides or shared on its own: a framework, a process, a chart. You get an SVG for the page, a PNG for sharing, alt text and the script that builds them, so it can be changed later. A sketch (a photo of paper or a whiteboard) helps.

```text
Make a diagram for Seeds of Renaissance: [what it shows, its parts and how they connect].
It's for [a paper / a post / slides]. [Path to a sketch or notes, if any.]
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system (or, if that folder isn't there,
https://design.seedsofrenaissance.org/AGENTS.md). Follow its "Diagram" route and
read only what it names. Don't change anything in the design repo.
Give me the SVG for the page, the PNG for sharing, alt text, and the script that
builds them. Ask me for anything you need that you can't find. Then tell me what
you checked and what you guessed.
```

The [diagram examples](examples/diagrams/index.html) show what it will make.

## Make a paper (PDF)

For a white paper or a long essay, typeset as one A4 PDF in the house style. You get the PDF and the paper's Markdown, marked up so the PDF can be rebuilt when the text changes. Have the final text ready: the agent typesets it, it doesn't edit it.

```text
Make the PDF of [the paper] for Seeds of Renaissance. The text is in [path to the
Markdown or document]; the figures are in [path], the cover art is [path, or none].
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system (or, if that folder isn't there,
https://design.seedsofrenaissance.org/AGENTS.md). Follow its "Paper" route and
read only what it names. Don't change anything in the design repo.
Give me the PDF and the paper's Markdown as you marked it up. Ask me for anything
you need that you can't find. Then tell me what you checked and what you guessed.
```

The [Wisdom paper, page by page](examples/print/index.html), shows what it will make.

## Find the logo, a graphic or a font

When you need a file: the right version of the logo for a ground, a woodcut for a page, the fonts. You get the files, the rules that go with them and whether they're cleared to publish. To browse them yourself: [Reference](reference.md), [Logo files](logos.md), [Graphics](graphics.md).

```text
Find [the Seeds of Renaissance logo / a graphic of what / the fonts / the colours]
for [what it's for, and the ground it sits on: white, paper, night, a photograph].
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system (or, if that folder isn't there,
https://design.seedsofrenaissance.org/AGENTS.md). Follow its "Assets" route and
read only what it names. Don't change anything in the design repo.
Give me the files (copy them to [where], or give me their paths), the rules that
go with them, and whether they're cleared for public use. Then tell me what you
checked and what you guessed.
```

## Make anything else

For any other job (the newsletter, a check that something is on brand, a thumbnail for a talk), the agent finds its route in the roadmap.

```text
Make [what you need] for Seeds of Renaissance, on brand.
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system (or, if that folder isn't there,
https://design.seedsofrenaissance.org/AGENTS.md). Find the route for this job and read
only what it names. Where this repo's own rules differ, this repo wins.
Ask me for anything you need that you can't find. Then tell me what you checked
and what you guessed.
```

## Change the design system

For maintainers: add a graphic, change a colour or size, record a decision, change a guide. The agent works in the design repo and keeps the guide, the roadmap, the prompts and the site in step. More in [Maintaining](MAINTAINING.md).

```text
Change the Seeds of Renaissance design system: [what, and why; who decided it, if it's a rule].
Work in ~/src/life-itself/design/projects/sor-design-system. Follow the "Maintain"
route in its AGENTS.md and read only what it names.
Keep the guide, its route in AGENTS.md, its prompt in prompts.md and llms.txt
in step where the change touches them, and check the paths other repos read.
Show me the change before committing. Then tell me what you checked and what you guessed.
```

## Set up a repo once

So that agents in a repo you work in always know where the design system is, add this to that repo's `AGENTS.md` (or `CLAUDE.md`):

```markdown
## Design
On-brand work for Seeds of Renaissance uses the design system in the design repo.
Read ~/src/life-itself/design/projects/sor-design-system/AGENTS.md (or, without
that folder, https://design.seedsofrenaissance.org/AGENTS.md) and follow the route
for your job. Where this repo's own rules differ, this repo wins.
```
