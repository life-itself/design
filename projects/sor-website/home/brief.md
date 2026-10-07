# Home page: brief

The landing page of the full Seeds of Renaissance site, not a standalone one-page site. It goes live as soon as it is good enough and then keeps changing.

## TL;DR

A calm page that scrolls normally and follows the Experiences sequence, with a few quiet moments of magic and little interaction. It opens with a line that speaks to the reader's longing and an invitation to the Greenhouse newsletter. It says plainly what we are, invites people to join the calls, and offers two ways to go deeper: courses and the podcast.

| # | Section | What it does |
|---|---|---|
| 1 | **Opening** | "For all those whose hearts burn for a new world to emerge." Video or photo behind it. Main call to action: the Greenhouse newsletter. |
| 2 | **What this is** | The Dawn manifesto paragraph and the statement "a vision and movement for civilizational renewal", perhaps with one line on what we do. Links to the manifesto and the vision. |
| 3a | **Join us** | Split screen: the Leap collage next to the regular calls, with the next date and a button. The only place the call is offered. |
| 3b | **Courses** | Our courses: what you learn, and the next one. |
| 3c | **Podcast** | The latest episodes. |
| 4 | **Close** | Newsletter again, support and footer. Optionally a still swallows image from Experiences. |

**Intentions**

- **Orient fast:** within about five seconds a newcomer knows who we are, that it is for them, and what to do next.
- **Main action:** sign up to the Greenhouse newsletter (once a month).
- **Second action:** join a call (in 3a).
- **Ways deeper:** courses and the podcast. The vision is one link away from section 2.

**Feel**

- **Grounded hope, leaning towards dawn:** hope earned by facing the dark, not by skipping past it.
- **A little off-centre, earthy and crafted:** paper, torn edges, woodcuts.
- **Calm and spacious**, with moments of beauty and awe borrowed from Experiences.
- **Not** glossy, corporate, wellness or woo, and not a hard sell.

**Why a normal page, not an interactive one.** Heavy scroll-driven animation makes visitors sit through a show before they learn what we are or what to do. It is weaker on mobile, for accessibility and for search, and it tires people who come back. SpaceX is the model: full-bleed media, one line, one button, normal scrolling. In practice:

- Standard sections built from the design system.
- Slow, quiet motion at most (a background loop, a fade), turned off under `prefers-reduced-motion`.
- Texture does the character work, not animation.
- The full Experiences live on their own page, linked from the home page.

Sources: Rufus and Sylvie's notes (October 2026); the Experiences home sequence ([../../sor-experiences-2026/experiences/00-home/brief.md](../../sor-experiences-2026/experiences/00-home/brief.md)); the existing design-system mockup ([../../sor-design-system/examples/web/home.html](../../sor-design-system/examples/web/home.html)).

## Step 0: review what we have

Before building anything new, Rufus and Sylvie review the existing design-system home page together. It is close already: photo hero (currently featuring the Global Connection Call), "What we believe", "Take part", a night section of selected work, Mythos, "Coming up", an interlude and "Engage". Note what to keep, cut and reorder against the sequence below. Its hero currently leads with the call; under this brief it leads with the newsletter.

## Sections

### 1. Opening

- **Line:** *For all those whose hearts burn for a new world to emerge.* (Experiences frame 1 has a variant: "For all the living beings whose heart burns to see a new world emerge". Settle on one.)
- **Background:** video if we can find a good one, otherwise a photo or a quiet loop of the floating seeds. Component: `.hero-photo`.
- **Main call to action:** sign up to the Greenhouse newsletter. The call is *not* offered here; it lives in 3a.

### 2. What this is

- The main manifesto statement (Experiences frame 2): the "Human history has always been a story of transformation…" paragraph, then *We are a vision and movement for civilizational renewal.*
- **Open question: is the paragraph enough?** It says what we believe but not what we do. Suggestion: add one short line after it naming what we are, drawn from [brand.md](../../sor-design-system/brand.md) (for example "a media house and spaces of belonging: calls, courses, a podcast"). Keep it to one line, not a list of everything we do.
- **Links:** read the manifesto, and go further into the vision on a separate page (see `design-ky7`, Sylvie's narrative deck).
- Static, or a single slow brighten at most.

### 3a. Join us

A split screen: the "Leap" collage ([walking.jpg](../../sor-design-system/system/img/walking.jpg), people walking toward the torn yellow field) next to the regular calls, with the next date and a button. This is becoming our "join us" image; the manifesto page hero already uses it. No animation. Naming (call vs gathering) is still to settle (`design-3mb`).

### 3b. Courses and 3c. Podcast

Two ways to go deeper, each its own beat. Leave the magazine and papers off the home page, because otherwise it is too much; they are reachable through the navigation.

- **Open question: two sections or one mixed section?**
  - Two separate beats: courses (white or paper ground), then the podcast (night ground).
  - One mixed section like the "Selected work" night section in the current mockup, with courses and podcast side by side.
- Avoid the label "Media" here; say "Podcast" (and "Videos" if needed).

### 4. Close

Newsletter again, support, and the footer. Components: `.engage`, `.site-footer`. Optionally a still ending moment from Experiences frame 5 (the swallows).

**Cut for now:** a "more of the vision" section. The vision is linked from section 2 instead.

## Open questions

- Section 2: add a line about what we do, or keep only the manifesto paragraph?
- Sections 3b and 3c: two beats or one mixed section?
- What goes behind the opening: video or image.
- Naming and site structure: calls vs gatherings; Media vs Learn vs Community (`design-3mb`).

## Build

1. Sylvie settles content and order in this brief (taste, copy, sequence).
2. An AI build copies [examples/web/home.html](../../sor-design-system/examples/web/home.html) into this folder, following [BUILD.md](../../sor-design-system/BUILD.md) and [website.md](../../sor-design-system/website.md). It uses only system components and real copy from [voice.md](../../sor-design-system/voice.md), [brand.md](../../sor-design-system/brand.md) and [content/](../../sor-design-system/content/).
3. Rufus and Sylvie tweak the copy and the details.
4. If the build needs a new component, add it to the design system rather than styling it here.
