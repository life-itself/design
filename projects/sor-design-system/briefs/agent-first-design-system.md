# Brief: a design system people and their agents can use

What to work out and build so the Seeds of Renaissance design system is quick to use for its real users: mostly people working with an AI agent, sometimes agents on their own, sometimes people on their own, and the few who maintain it. This is a brief for the analysis first, then for the design and build that follow from it. Progress is tracked in beads (`design-34t.57`), not here.

Source: `projects/sor-design-system/` in `life-itself/design`, published at https://design.seedsofrenaissance.org (Flowershow, CI on merge to `main`; see MAINTAINING.md).

## Why: Rufus's critique (2026-10-15)

After a round of restructuring (three ways in on the home page, regrouped nav, guides stripped of status), the site still doesn't work for the job people come for:

1. **The paths weren't walked.** "I'm making something" on the home page leads to a "Make something" table that says to read "Start here" first. "Start here" (BUILD.md) makes you read a brief, then feel and voice, then shows "Pick what you're making": the same table again, with `website.md`-style filenames as link text. Why read "Start here" at all if I'm making something? The home page and BUILD.md repeat each other without either being the fastest route.
2. **It's unclear who a page is for.** Is BUILD.md for a person or an agent? It reads as both and serves neither well.
3. **No copy-and-paste.** The commonest use is a person with an agent: "paste this into your agent to build X on brand", "paste this to maintain the design system". There is nothing to paste.
4. **The repo is the better source for agents.** Work happens in other repos (the website, social, papers). A person says to their agent "go to the design repo and find what you need to be on brand". An agent with a checkout should read the files in Git, not parse the published pages; the site is more for humans. Today the routes are site-first.
5. **The use cases weren't thought through.** The work should start from who comes, what they are doing and the quickest way to get it done. Some repetition is fine if it serves a path. Maintainers need their own path too.

## Goal

A design system that is best practice for people and for agents, and above all for people working with agents:

- **One concise roadmap for agents**: "You're doing X: read these files, use these tokens and classes, copy this example, check against this list." Short, efficient, and pointing into the repo by path. It works whether the agent reads the repo or the site.
- **Copy-and-paste prompts for people**: one per common job, ready to paste into an agent working in another repo ("Build a page for the SoR website on brand", "Make an Instagram post", "Make a diagram for a paper", "Update the design system").
- **A short, obvious human path** on the site for each job, with no detour through pages you don't need.
- **A maintainer path**: how to change the system and keep pages, prompts and the roadmap in step.
- Possibly **a skill** (e.g. a Claude Code skill "use the SoR design system", or instructions to install in the website repo), if analysis shows it beats a roadmap file.

## Phase 1: analysis (deliver before building)

1. **Best practice.** Briefly survey how good design systems serve people (e.g. GOV.UK Design System, Shopify Polaris, Atlassian, Material) and how projects serve agents now (llms.txt, AGENTS.md/CLAUDE.md, Claude skills, "for AI" pages, MCP). What is the state of the art for a design system used by agents working in other repos? Keep it short and say what we should copy.
2. **Who and what: job stories.** List the users (person with agent in another repo; agent alone, given a link or a repo path; designer or comms person without an agent, e.g. in Canva; maintainer) and write job stories in the form "When…, I want to…, so I can…". Cover at least: build a website page or section; make a social post or Canva graphic; make a YouTube thumbnail or podcast cover; make slides; make a paper or diagram; find and download a logo or graphic; check something is on brand; understand the brand quickly; change the system (add a graphic, change a token, record a decision). Rank them by frequency and value.
3. **Critique the current system** against the top job stories. Walk each path as that user would: clicks, files read, words read before acting, dead ends, repetition, `.md` link text, site vs repo. Use a fresh subagent given only a realistic prompt (e.g. working in `~/src/life-itself/sor-website`, "make the podcast page on brand using the design system at ~/src/life-itself/design") and record where it goes and what it gets wrong.
4. **Proposal.** Information architecture for repo and site: what the agent roadmap file is and where it lives (e.g. `AGENTS.md` or `llms.txt` at the design system root, plus a pointer the website repo can include); the prompt library; what the home page and "Start here" become (merge, cut or split by audience); which pages are for people, which for agents, and which serve both; whether to make a skill. Include a sketch of the roadmap's first screen and two example prompts.

**Before showing Rufus anything**, have a new subagent critique the Phase 1 analysis against this brief (does it cover every section, does it answer the critique above, is the proposal concrete), and fix what it finds.

**Then show shipped work, not a plan.** Build and ship one pathway end to end (Phase 2, step 1, one area only) and show Rufus that: issues are easier to spot in something shipped than in a plan. If the plan is shown at all, give only its essence: the few key points to validate, not the full document.

## Phase 2: design and build

1. **Two pathways end to end first**: the top two job stories (likely "build a website page from the website repo with an agent" and "make a social post / Canva graphic"). Build the roadmap entry, the paste-in prompt, the human path on the site, and anything the pages lack. Then test each with a fresh agent and a person's click-through, and fix until it is quick.
2. **Then the rest** of the job stories, the maintainer path, and the home page and nav to match.
3. **Keep it in step**: one place that says how the roadmap, prompts and pages are kept current when the system changes (in MAINTAINING.md).

## Constraints

- Pages state the rules as they are now; status and progress go in beads (MAINTAINING.md, "Pages state rules, not progress").
- British spelling, plain short sentences; match the existing voice of the docs.
- Don't break published URLs without a redirect (build-site.py has a MOVED map).
- Commit when Rufus agrees the work; publishing is CI on merge to `main`.

## Done when

- The analysis (best practice, job stories, critique, proposal) is written up and has passed a subagent critique against this brief.
- For the top two jobs, a person can paste one prompt into an agent in another repo, and a fresh agent produces on-brand work having read only what the roadmap points to. A person without an agent reaches what they need in two clicks from the home page.
- The roadmap, prompts and maintainer path exist, with the rest of the job stories covered.
