# Life Itself HTML Presentations

HTML slide templates for Life Itself presentations. Single-file, zero-dependency, runs in any browser.

## Templates

### `life-itself-warm-earth-reference.html`

The canonical Life Itself brand slide template. Warm earth palette (sand, clay, charcoal), Cormorant Garamond + DM Sans typography, scroll-snapping full-viewport slides.

**Use as a starting point** — copy the file, rename it, replace content.

## How to use

```bash
# Preview in browser
open presentations/life-itself-warm-earth-reference.html

# Start a new deck
cp presentations/life-itself-warm-earth-reference.html presentations/my-new-deck.html
```

Navigate slides: arrow keys, space, scroll, or swipe. Nav dots on the right.

## Assets

- `life-itself-logotype.webp` — logotype alongside this HTML for standalone rendering
- Canonical logotype source: `~/src/lifeitself/assets/lifeitself/life-itself-logotype.webp`

## Logo pattern

- **Title slide**: inline `<a>/<img>` centered below subtitle
- **All other slides**: CSS `::after` pseudo-element, bottom-right, via `.slide::after`
- `.slide-title::after { display: none }` suppresses the CSS logo on the title slide
- `.slide-subsection::after, .slide-clay-dark::after { opacity: 0.35 }` dims on dark backgrounds

## Updating / rebuilding

1. Edit the HTML directly — CSS variables in `:root` control all colors and sizes
2. After significant changes, sync to the Claude skill working copy:
   ```bash
   cp presentations/life-itself-warm-earth-reference.html \
      ~/.claude/skills/frontend-slides/assets/life-itself-warm-earth-reference.html
   ```
3. The Claude `frontend-slides` skill (preset 13 in `STYLE_PRESETS.md`) uses this file as its reference implementation
