# Building with the SoR design system

**Start here** if you are making anything for Seeds of Renaissance, whether you are a person or an AI agent: a web page, a social post, a thumbnail, a slide, a printed paper. Read this page, open the guide for what you're making, copy the closest example, then build.

## The brief in one paragraph

The feel is **grounded hope**: ink and paper, a little off-centre, with the hand visible (paper grain, torn edges, woodcut seeds and swallows). Pages are mostly white, paper and ink, and colour comes from photographs. Buttons are black. The logo red is only for an occasional link in running text. Pale yellow is a background, never text or highlight. One night section per page, plus the footer, meeting the light at a torn edge. Headlines and titles are Polyamine (under ~10 words; longer display text moves to Restora), reading is Bricolage Grotesque, labels are small uppercase Apfel Grotezk, and the poetic voice is Restora italic. Four faces, no more.

Who we're speaking to: see [feel.md](feel.md#who-we-design-for). How we sound: [voice.md](voice.md).

## Pick what you're making

| Making… | Guide | Copy from |
|---|---|---|
| A web page | [website.md](website.md) | [examples/web/](examples.md#website) |
| A post, announcement or poster for social media (Instagram, LinkedIn, Substack, X, link previews; 16:9, 4:5, 1:1, 9:16) | [social.md](social.md) | stub |
| A YouTube thumbnail or channel art | [youtube.md](youtube.md) | [examples/youtube/](examples.md#youtube) |
| Podcast show art or an episode cover | [podcast.md](podcast.md) | stub (episode cover in [examples/youtube/](examples/youtube/index.html)) |
| A slide deck | [slides.md](slides.md) | in progress |
| A printed or PDF paper, a poster | [print.md](print.md) | stub |
| A diagram, figure or chart | [diagrams.md](diagrams.md) | stub |
| The newsletter (The Greenhouse) | [email.md](email.md) | stub |
| Something in Canva | [social.md](social.md#canva) | stub |

What exists for each, and its status: [examples.md](examples.md#status).

## Rules that apply everywhere

1. **Four faces only.** Polyamine for headlines and titles under ~10 words; Restora for longer display text and the poetic italic; Bricolage Grotesque for reading; Apfel Grotezk for small uppercase labels.
2. **Ink and paper first.** White is the default ground, paper sometimes, pale yellow at times, one night per piece. Colour comes from photographs.
3. **Buttons and marks are ink.** Red is the logo's own red, an occasional link in running text, or the red woodcuts. Never a red button, heading or background.
4. **No bright yellow, no highlighting, no gradients** except a scrim to make text readable on a photo.
5. **The hand is our texture:** torn edges, paper grain, woodcuts. Not filters, not stock textures.
6. **Real copy in our voice** ([voice.md](voice.md)); images captioned like plates where there's room.
7. **Use the tokens** in `system/tokens.css`. If a format needs a fixed scale (thumbnails, slides, print), add it as tokens there, like `--thumb-*`.

## Check before you finish

- [ ] Four faces only, and the length rule (Polyamine under ~10 words, Restora beyond).
- [ ] No coloured buttons; red only as the logo, an in-text link or a red woodcut.
- [ ] No yellow text or highlight, no bright yellow, no gradients except a photo scrim.
- [ ] Copy is real and in our voice; photos marked as placeholders if not cleared.
- [ ] Plus the checklist in the guide for what you're making.

## Topic pages

- [feel.md](feel.md): grounded hope, what we are not, the three registers
- [voice.md](voice.md): key lines, tone, rewrites, calls to action
- [colour.md](colour.md): roles, proportion, do and don't
- [type.md](type.md): the faces, scale, and how to apply them
- [layout.md](layout.md): grounds, rhythm, torn edges, grid and spacing
- [graphics.md](graphics.md): woodcut swallow, seal, seeds and clusters; the full set in [woodcuts.html](woodcuts.html)
- [photography.md](photography.md): what to choose and avoid
- [logo.md](logo.md): versions and placement
- [components.md](components.md): every component with HTML
