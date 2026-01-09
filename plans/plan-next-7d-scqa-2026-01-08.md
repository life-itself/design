# Next 7–10 Days Web Work Plan SCQA as of 2026-01-08

## Situation

- Life Itself now comprises multiple distinct but related web properties (main site, research sub-site, hubs, courses), with substantial prior work already completed on information architecture and visual/UX concepts.
- Technical capability has advanced to the point where fully functional sites can be shipped rapidly using a FlowerShow-style system, without requiring CMS-heavy infrastructure.
- The opportunity cost of extended deliberation is now higher than the cost of shipping imperfect but live sites.

## Complication

Work on the Life Itself web presence risks stalling due to:

* Over-scoping (attempting to resolve identity, governance, or long-term architecture prematurely).
* Fragmentation (switching between main site, sub-sites, and tech choices without a critical path).
* Re-litigation of settled questions (IA, visual language, WordPress vs non-WordPress).

At the same time, shipping only a landing page for “Life Itself” risks reopening unresolved identity questions, whereas focused sub-sites (e.g. research) already have clearer purpose and structure.

## Question

What is the minimal, execution-biased plan for the next 7–10 days that results in live, working websites, while deferring non-blocking strategic questions?

### Issue tree with provisional answers

* Integration vs separation
  * Why not integrate the research site directly into the main Life Itself website? **Answer: Research has a distinct audience, cadence, and epistemic function; separating it avoids reopening Life Itself identity questions and allows faster shipping.**
  * Is separation permanent or provisional? **Answer: Provisional; architectural separation now, with possible convergence later.**
* Role of the main Life Itself site
  * What is the function of the main Life Itself website in this phase? **Answer: Minimal hub-of-hubs: orientation, credibility, navigation, and signposting.**
  * What is it explicitly not trying to do? **Answer: Resolve identity, explain the full vision, or host all content.**
* Research sub-site purpose
  * What job does the research sub-site do? **Answer: Public-facing home for ongoing inquiry, outputs, and research identity.**
  * What does “done enough” mean for research in 7–10 days? **Answer: Clear framing, core pages, initial content, live and navigable.**
* Technical direction
  * What stack is assumed for this window? **Answer: FlowerShow-style static-first publishing.**
  * What technical questions are deferred? **Answer: CMS comparisons, WordPress, long-term platform consolidation.**
* Visual / UX outputs
  * Are mock-ups exploratory or implementation-ready? **Answer: Implementation-ready; visuals are in service of shipping.**
  * What level of polish is required? **Answer: Coherent and credible, not final or brand-perfect.**
* Briefing and reuse
  * Should each site have a short explicit brief? **Answer: Yes; lightweight briefs derived from this plan.**
  * What is the brief’s purpose? **Answer: To prevent scope creep and enable fast iteration or delegation.**
* Explicit exclusions
  * Are governance and identity questions addressed here? **Answer: No; explicitly deferred unless they block shipping.**
  * Are courses, hubs, or residencies in scope? **Answer: No, beyond links or placeholders.**

## Answer

### Core decision

For the next 7–10 days, priority is placed on **shipping two live sites** on a FlowerShow-style stack:

1. The **Life Itself main website** (minimal, hub-of-hubs).
2. The **Life Itself Research sub-site** (substantively complete).

All other questions are subordinated to this shipping goal.

### Scope (explicit)

In scope:

* Main Life Itself site: minimal framing, navigation, and credibility layer.
* Research sub-site: purpose, structure, core pages, and initial content.
* Visual/UX mock-ups sufficient to directly implement production pages.
* Technical implementation using the existing FlowerShow-style system.

Out of scope (for this window):

* WordPress evaluation or migration.
* Full Life Itself identity or governance resolution.
* Courses, hubs, or residency sub-sites beyond placeholders or links.
* Perfection-level copy or branding polish.

### Assumed technical position

* FlowerShow-style static-first publishing is the default.
* Decisions are made only if they unblock shipping.
* Reversibility is preferred over optimisation.

### Definition of “done”

By day 7–10:

* Both sites are live at stable URLs.
* Navigation works end-to-end.
* Core pages render correctly on desktop.
* Content can be edited and redeployed without friction.
* Visual design is coherent, even if not final.