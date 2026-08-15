// Life Itself / Second Renaissance report template — prototype
// Palette sampled from the existing "Second Renaissance" whitepaper cover
// (2rbook/assets/whitepaper-1-cover.webp) and the Life Itself logotype.

#let cream = rgb("#FFFFE3")
#let ink   = rgb("#191512")
#let gold  = rgb("#B99A54")
#let sage  = rgb("#5B6B3A")

#let report(
  title: "",
  subtitle: "",
  authors: "",
  date: "",
  logo: none,
  body,
) = {
  set document(title: title, author: authors)

  // ---- Cover page --------------------------------------------------
  set page(paper: "a4", fill: cream, margin: (x: 3.2cm, top: 4.2cm, bottom: 3.2cm))
  set text(font: "Liberation Sans", fill: ink)

  if logo != none {
    align(top + left)[#image(logo, width: 3.4cm)]
    v(2.6cm)
  }

  align(left)[
    #text(size: 40pt, weight: 800, fill: ink)[#title]
    #v(0.5cm)
    #text(size: 17pt, weight: 400, fill: ink.lighten(10%))[#subtitle]
    #v(1.2cm)
    #line(length: 3.2cm, stroke: 2pt + gold)
    #v(0.6cm)
    #text(size: 12pt, weight: 600)[#authors]
    #v(0.15cm)
    #text(size: 10pt, fill: ink.lighten(35%))[#date]
  ]

  pagebreak()

  // ---- Table of contents --------------------------------------------
  set page(paper: "a4", fill: white, margin: (x: 3cm, y: 3cm))
  set text(font: "Liberation Serif", size: 11pt, fill: ink)
  heading(numbering: none, outlined: false)[Contents]
  v(0.3cm)
  outline(title: none, indent: auto)

  pagebreak()

  // ---- Body pages -----------------------------------------------------
  set page(
    paper: "a4",
    fill: white,
    margin: (x: 2.8cm, top: 2.6cm, bottom: 2.8cm),
    header: context {
      if here().page() > 3 {
        set text(size: 8.5pt, fill: ink.lighten(45%), font: "Liberation Sans")
        align(right)[#upper(title)]
        v(-0.2cm)
        line(length: 100%, stroke: 0.4pt + gold.lighten(20%))
      }
    },
    footer: context {
      set text(size: 9pt, fill: ink.lighten(40%), font: "Liberation Sans")
      align(center)[#counter(page).display()]
    },
  )
  set text(font: "Liberation Serif", size: 11.3pt, fill: ink, lang: "en")
  set par(justify: true, leading: 0.72em, first-line-indent: 0em)

  show emph: it => text(fill: sage.darken(10%), it)

  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    v(0.4cm)
    set text(font: "Liberation Sans", size: 22pt, weight: 800, fill: ink)
    block(it.body)
    line(length: 2.4cm, stroke: 2pt + gold)
    v(0.5cm)
  }

  show heading.where(level: 2): it => {
    v(0.6cm)
    set text(font: "Liberation Sans", size: 14pt, weight: 700, fill: sage.darken(15%))
    block(it.body)
    v(0.15cm)
  }

  show heading.where(level: 3): it => {
    set text(font: "Liberation Sans", size: 12pt, weight: 700, fill: ink)
    block(it.body)
  }

  show image: it => {
    align(center)[#box(width: 78%, it)]
  }

  show link: it => text(fill: sage.darken(10%), it)

  body
}
