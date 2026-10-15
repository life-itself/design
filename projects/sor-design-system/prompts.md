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

Paste this into your agent in the `sor-website` repo. It writes the page in Markdown; the site's styles, synced from the design system, make it look right.

```text
[Make / change] the [which] page on the Seeds of Renaissance website, on brand.
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system. Follow its "Website page" route
and read only what it names. This repo's own AGENTS.md wins where they differ.
Don't change anything in the design repo.
Write real copy in our voice and mark anything you're unsure of with a TODO.
Ask me for facts you can't find. Then tell me what you checked and what you guessed.
```

## Make anything else

For any other job (a thumbnail, slides, a diagram, a paper), the agent finds its route in the roadmap.

```text
Make [what you need] for Seeds of Renaissance, on brand.
Use the Seeds of Renaissance design system: the roadmap is AGENTS.md in
~/src/life-itself/design/projects/sor-design-system (or, if that folder isn't there,
https://design.seedsofrenaissance.org/AGENTS.md). Find the route for this job and read
only what it names. Where this repo's own rules differ, this repo wins.
Ask me for anything you need that you can't find. Then tell me what you checked
and what you guessed.
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
