#!/usr/bin/env python3
"""Build the round-one heading archive.

Round one of the display-face search, with the verdicts given on 2026-09-30.
Kept as a record: the candidates as they were shown, each with the reaction it
got, so a later round does not re-propose something already rejected.

Faces that are not on Google Fonts are downloaded and embedded as base64. A
published artifact may only pull fonts from Google's CDN, but embedding the
file sidesteps that entirely, and it also makes this archive self-contained.

    python3 build-round-01.py      # writes round-01-headings.html
"""
import base64, html, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).parent
CACHE = HERE / "fonts"

# family -> url. Velvetyne publishes on GitLab, Collletttivo on GitHub;
# note the default branch differs between repos.
SOURCES = {
    "bluu-next.woff2":  "https://cdn.jsdelivr.net/npm/@fontsource/bluu-next@5.2.5/files/bluu-next-latin-700-normal.woff2",
    "bagnard.woff2":    "https://cdn.jsdelivr.net/npm/@fontsource/bagnard@5.2.5/files/bagnard-latin-400-normal.woff2",
    "coconat.woff2":    "https://raw.githubusercontent.com/collletttivo/Coconat/main/fonts/Coconat-Bold.woff2",
    "basteleur.woff2":  "https://gitlab.com/velvetyne/basteleur/-/raw/master/fonts/webfonts/Basteleur-Moonlight.woff2",
    "cantique.woff2":   "https://gitlab.com/velvetyne/cantique/-/raw/master/fonts/web/Cantique-Normal.woff2",
    "florderuina.woff2":"https://gitlab.com/velvetyne/flor-des-ruina/-/raw/main/fonts/woff2/FlorDeRuina-Ruina.woff2",
}

PARA = ("Human history has always been a story of transformation – of old worlds dying and new "
        "ones being born. Every great crisis carries within it the seed of rebirth. We are a movement "
        "called to bring forth a civilizational renaissance grounded in Wisdom, Interbeing, Inner "
        "growth, Revoligion, Complexity and beyond capitalism.")
STATEMENT = "We are a vision and movement for civilizational renewal."


def b64(name):
    CACHE.mkdir(exist_ok=True)
    p = CACHE / name
    if not p.exists():
        subprocess.run(["curl", "-sfL", "-o", str(p), SOURCES[name]], check=True)
    d = p.read_bytes()
    if d[:4] != b"wOF2":
        sys.exit("not a woff2: " + str(p))
    return base64.b64encode(d).decode("ascii")


# verdict: like | maybe | no
RENDERED = [
    dict(name="Polyamine", stack="'Polyamine','Didot','Bodoni 72',Georgia,serif", w=400,
         size="clamp(1.5rem,3.5vw,2.8rem)", track=".09em", verdict="like",
         src="Nasir-style commercial display serif · UICreative",
         gist="Organic and elegant. Luxurious and sleek, but with a living quality.",
         quote="Polyamine we like. It has something a little organic and elegant, but it is also "
               "a font that feels quite luxurious and sleek. Quite like luxury, high class, yet at "
               "the same time alive — it has this organic, living quality."),
    dict(name="Bagnard", stack="'Bagnard',Georgia,serif", w=400,
         size="clamp(1.5rem,3.5vw,2.8rem)", track=".09em", verdict="maybe",
         src="Velvetyne · free, SIL OFL",
         gist="Grounded, but very masculine — and still a backward-looking revival.",
         quote="Bagnard was better. Had a bit more to it, a bit more groundedness — but very "
               "masculine. Interesting and in the general direction, but probably a no against "
               "Polyamine or Restora."),
    dict(name="Bluu Next", stack="'Bluu Next',Georgia,serif", w=700,
         size="clamp(1.5rem,3.4vw,2.7rem)", track=".07em", verdict="no",
         src="Velvetyne · free, SIL OFL",
         gist="Interesting, but not interesting enough.",
         quote="Bluu Next was a bit boring. Was interesting, but not interesting enough."),
    dict(name="Cinzel", stack="'Cinzel',Georgia,serif", w=400,
         size="clamp(1.4rem,3.1vw,2.45rem)", track=".1em", verdict="no",
         src="Google Fonts · free",
         gist="A chiselled monument. Clean, classic Roman.",
         quote="This looks too much like a chiselled monument. Clean, classic Roman."),
    dict(name="Fraunces", stack="'Fraunces',Georgia,serif", w=500,
         size="clamp(1.45rem,3.2vw,2.55rem)", track=".045em", verdict="no",
         src="Google Fonts · free",
         gist="Endlessly adjustable, but no real personality. Nothing new.",
         quote="The thing about Fraunces is that you can adjust it a great deal, so I would not "
               "judge it on one setting. But it does not have real personality. It is nothing new. "
               "You do not feel alive."),
    dict(name="Instrument Serif", stack="'Instrument Serif',Georgia,serif", w=400,
         size="clamp(1.6rem,3.7vw,2.95rem)", track=".05em", verdict="no",
         src="Google Fonts · free",
         gist="Boring.",
         quote="Instrument Serif is just a bit boring."),
    dict(name="Italiana", stack="'Italiana',Georgia,serif", w=400,
         size="clamp(1.55rem,3.6vw,2.85rem)", track=".1em", verdict="no",
         src="Google Fonts · free · what the build renders today",
         gist="Classic and elegant, but no originality.",
         quote="Italiana has some of that as well — quite classic and elegant, but with no "
               "originality. There is no originality, so it is kind of boring."),
    dict(name="Coconat Bold", stack="'Coconat',Georgia,serif", w=400,
         size="clamp(1.45rem,3.3vw,2.6rem)", track=".055em", verdict="no",
         src="Collletttivo · free, open licence",
         gist="Fat and heavy. Not elegant.",
         quote="Coconat Bold: no. Just because it looks bad. It does not look elegant — it looks "
               "fat and heavy. Maybe it has to not be bold, or something like that."),
    dict(name="Basteleur Moonlight", stack="'Basteleur',Georgia,serif", w=400,
         size="clamp(1.4rem,3.2vw,2.5rem)", track=".075em", verdict="no",
         src="Velvetyne · free, SIL OFL",
         gist="Nordic, runic. Going backwards, not forwards.",
         quote="Basteleur Moonlight was too much of a reference to Nordic. It looks like runes. It "
               "looks like you are going backwards rather than forwards, because we are rebirthing, "
               "emerging forwards. We are not talking about the last Renaissance. We are talking "
               "about a new Renaissance, a new rebirth."),
    dict(name="Cantique", stack="'Cantique',Georgia,serif", w=400,
         size="clamp(1.3rem,2.9vw,2.25rem)", track=".05em", verdict="no",
         src="Velvetyne · free, SIL OFL",
         gist="Woo-woo, new-agey.",
         quote="This one is just a bit crazy and makes you think of magic. Cantique is woo-woo, "
               "new-agey."),
    dict(name="Flor de Ruina", stack="'Flor de Ruina',Georgia,serif", w=400,
         size="clamp(1.25rem,2.8vw,2.15rem)", track=".045em", verdict="no",
         src="Velvetyne · free, SIL OFL",
         gist="A video game or a disco ball.",
         quote="Flor de Ruina is just crazy, and it looks like I am in a video game, or a disco "
               "ball."),
]

# Shown as links, not rendered: commercial faces that cannot be embedded.
LISTED = [
    dict(name="Restora / Restora Neue", who="Nasir Udin", verdict="like",
         url="https://www.myfonts.com/collections/restora-font-nasir-udin",
         gist="Liked, for the same reasons as Polyamine.",
         quote="I end up liking Restora and Polyamine because they have something a little organic "
               "and elegant, but they are both fonts that do feel quite luxurious and sleek."),
    dict(name="Signifier", who="Klim Type Foundry", verdict="no",
         url="https://klim.co.nz/retail-fonts/signifier/",
         gist="Boring. Possibly a body face.",
         quote="Signifier is kind of boring, right? Just boring. It could be used for body text."),
    dict(name="GT Sectra", who="Grilli Type", verdict="no",
         url="https://www.grillitype.com/typeface/gt-sectra",
         gist="Too sharp. Feels like it will cut you.",
         quote="Sectra: too cutty, too sharp. Makes you feel you are going to be cut. Not good."),
    dict(name="Ogg", who="Sharp Type", verdict="no",
         url="https://sharptype.co/typefaces/ogg/",
         gist="Reads newspaper.",
         quote="Ogg has a bit more to it. But Ogg makes me think newspaper."),
    dict(name="Reckless", who="Displaay", verdict="no",
         url="https://displaay.net/typeface/reckless/",
         gist="No personality.",
         quote="Reckless is kind of boring. It does not really have any personality. Nothing much "
               "to it."),
    dict(name="Migra", who="Pangram Pangram", verdict="no",
         url="https://pangrampangram.com/products/migra",
         gist="A barber shop or a pub.",
         quote="Migra looks too much like a barber or a pub."),
    dict(name="Swear Display", who="OH no Type Co", verdict="none",
         url="https://ohnotype.co/fonts/swear", gist="Not reviewed.", quote=""),
    dict(name="Cardinal Fruit", who="Blaze Type", verdict="none",
         url="https://blazetype.eu/typefaces/cardinal-fruit", gist="Not reviewed.", quote=""),
]

LABEL = {"like": "Liked", "maybe": "Maybe", "no": "No", "none": "Not reviewed"}


def rendered_block(i, f):
    q = f'<p class="quote">{html.escape(f["quote"])}</p>' if f["quote"] else ""
    return f'''
  <section class="cand">
    <div class="col label">
      <div class="lhead">
        <span class="rank">{i:02d}</span>
        <div class="lname">
          <h2>{html.escape(f["name"])}</h2>
          <p class="src">{f["src"]}</p>
        </div>
        <span class="flag v-{f["verdict"]}">{LABEL[f["verdict"]]}</span>
      </div>
      <p class="gist">{html.escape(f["gist"])}</p>
      {q}
    </div>
    <div class="frame">
      <span class="tag">{i:02d} &middot; {html.escape(f["name"])}</span>
      <div class="finner">
        <p class="ftext">{PARA}</p>
        <h3 class="fstatement" style="font-family:{f['stack']};font-weight:{f['w']};font-size:{f['size']};letter-spacing:{f['track']}">{STATEMENT}</h3>
        <p class="finvite">Read the full manifesto <span aria-hidden="true">&middot;</span> or continue &darr;</p>
      </div>
    </div>
  </section>'''


def listed_row(f):
    q = f'<p class="quote">{html.escape(f["quote"])}</p>' if f["quote"] else ""
    return (f'<li><span class="lf"><a href="{f["url"]}" target="_blank" rel="noopener">'
            f'{html.escape(f["name"])}</a><small>{html.escape(f["who"])}</small></span>'
            f'<span class="ld"><span class="flag v-{f["verdict"]}">{LABEL[f["verdict"]]}</span>'
            f'<b>{html.escape(f["gist"])}</b>{q}</span></li>')


PAGE = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Heading faces &middot; round one</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400..700&family=Fraunces:opsz,wght,SOFT,WONK@9..144,100..900,0..100,0..1&family=Instrument+Serif&family=Italiana&family=Newsreader:opsz,wght@6..72,200..800&display=swap">
<style>
/* Reading column for the commentary, full-bleed black bands for the samples.
   Chrome is the reader's own interface font so that the only serifs on the
   page are the candidates themselves. */
:root{{
  --page:#fbfaf7; --fg:#1a1817; --muted:#6f675f; --line:#e4ded6; --accent:#b81414;
  --ok:#1d7a4c; --night:#080707; --daylight:#efebe4;
  --ui:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  color-scheme:light;
}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{
  --page:#15130f; --fg:#ece7df; --muted:#8e867c; --line:#312d27; --accent:#f0736f;
  --ok:#5bc48c; color-scheme:dark;
}}}}
:root[data-theme="dark"]{{
  --page:#15130f; --fg:#ece7df; --muted:#8e867c; --line:#312d27; --accent:#f0736f;
  --ok:#5bc48c; color-scheme:dark;
}}
*,*::before,*::after{{box-sizing:border-box}}
body{{margin:0;background:var(--page);color:var(--fg);font-family:var(--ui);
  font-size:15.5px;line-height:1.65;-webkit-font-smoothing:antialiased}}

@font-face{{font-family:"Bluu Next";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("bluu-next.woff2")}) format("woff2")}}
@font-face{{font-family:"Bagnard";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("bagnard.woff2")}) format("woff2")}}
@font-face{{font-family:"Coconat";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("coconat.woff2")}) format("woff2")}}
@font-face{{font-family:"Basteleur";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("basteleur.woff2")}) format("woff2")}}
@font-face{{font-family:"Cantique";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("cantique.woff2")}) format("woff2")}}
@font-face{{font-family:"Flor de Ruina";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("florderuina.woff2")}) format("woff2")}}
/* Commercial, no web file: renders only where it is installed. */
@font-face{{font-family:"Polyamine";src:local("Polyamine"),local("Polyamine-Regular");font-display:swap}}

.col{{max-width:1100px;margin:0 auto;padding-inline:16px}}
header.top{{padding-block:52px 4px}}
header.top .inner{{max-width:66ch}}
header.top h1{{font-weight:600;font-size:clamp(1.35rem,2.6vw,1.75rem);line-height:1.25;
  letter-spacing:-.011em;margin:0 0 10px;text-wrap:balance}}
header.top .kicker{{font-size:11px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);margin:0 0 10px;font-weight:600}}
header.top p{{margin:0 0 12px;color:var(--muted)}}
header.top b{{font-weight:600;color:var(--fg)}}

.rec{{border-left:1.5px solid var(--accent);padding:2px 0 2px 16px;margin:26px 0 0;max-width:66ch}}
.rec h2{{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);
  font-weight:700;margin:0 0 8px}}
.rec p{{margin:0 0 10px;color:var(--muted)}}
.rec p:last-child{{margin-bottom:0}}
.rec b{{color:var(--fg);font-weight:600}}
.rec .said{{font-style:normal;color:var(--fg);border-left:2px solid var(--line);
  padding-left:12px;margin:12px 0}}

.cand{{margin-top:56px}}
.label{{margin-bottom:18px}}
.lhead{{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:8px}}
.rank{{font-size:12px;font-weight:600;color:var(--muted);letter-spacing:.08em;
  font-variant-numeric:tabular-nums}}
.lname h2{{margin:0;font-size:1.02rem;font-weight:600;letter-spacing:-.008em}}
.src{{margin:1px 0 0;font-size:11.5px;color:var(--muted)}}
.flag{{font-size:10.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  border:1px solid var(--line);border-radius:999px;padding:3px 9px;white-space:nowrap;
  color:var(--muted)}}
.lhead .flag{{margin-left:auto}}
.flag.v-like{{color:var(--ok);border-color:var(--ok)}}
.flag.v-no{{color:var(--accent);border-color:var(--accent)}}
.gist{{margin:0;font-size:15.5px;font-weight:600;max-width:70ch}}
.quote{{margin:7px 0 0;color:var(--muted);font-size:14.5px;max-width:74ch;
  border-left:2px solid var(--line);padding-left:12px}}

.frame{{position:relative;background:var(--night);min-height:clamp(480px,86vh,940px);
  display:grid;place-items:center;padding:clamp(3rem,10vh,7rem) clamp(20px,6vw,64px)}}
.frame .tag{{position:absolute;top:14px;left:16px;font-size:10.5px;letter-spacing:.14em;
  text-transform:uppercase;color:#6a635b;font-weight:600;font-variant-numeric:tabular-nums}}
.finner{{display:grid;justify-items:center;gap:clamp(2.4rem,6vw,4.2rem);width:100%;max-width:60rem}}
.ftext{{font-family:"Newsreader",Georgia,serif;color:var(--daylight);
  font-size:clamp(1.1rem,1.9vw,1.45rem);line-height:1.62;text-align:center;
  max-width:52ch;margin:0;text-wrap:pretty}}
.fstatement{{color:var(--daylight);text-transform:uppercase;line-height:1.28;
  text-align:center;margin:0;max-width:22em;text-wrap:balance}}
.finvite{{font-family:"Newsreader",Georgia,serif;color:var(--daylight);margin:0;text-align:center;
  font-size:clamp(.85rem,1.3vw,1rem);letter-spacing:.07em;text-transform:uppercase;opacity:.75}}

.sect{{padding-block:64px 0}}
.sect .inner{{max-width:66ch}}
.sect h2{{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);
  font-weight:700;margin:0 0 8px}}
.sect h3{{font-size:1.15rem;font-weight:600;margin:0 0 10px;letter-spacing:-.008em}}
.sect p{{margin:0 0 10px;color:var(--muted)}}

.lookup{{list-style:none;padding:0;margin:14px 0 0;border-top:1px solid var(--line)}}
.lookup li{{padding:14px 0;border-bottom:1px solid var(--line);display:grid;
  grid-template-columns:minmax(150px,auto) 1fr;gap:6px 20px;align-items:start}}
.lookup .lf{{font-weight:600;font-size:14.5px;min-width:0}}
.lookup .lf a{{color:var(--fg);text-decoration:none;border-bottom:1px solid var(--line)}}
.lookup .lf a:hover{{border-bottom-color:var(--accent);color:var(--accent)}}
.lookup .lf small{{display:block;font-weight:400;color:var(--muted);font-size:11.5px}}
.lookup .ld{{min-width:0}}
.lookup .ld .flag{{float:right;margin-left:12px}}
.lookup .ld b{{font-weight:600;font-size:14.5px}}
@media (max-width:600px){{.lookup li{{grid-template-columns:1fr}}}}

footer.fin{{padding-block:34px 72px;margin-top:56px;border-top:1px solid var(--line)}}
footer.fin .inner{{max-width:66ch;color:var(--muted);font-size:14.5px}}
footer.fin h2{{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--fg);
  font-weight:600;margin:0 0 10px}}
footer.fin p{{margin:0 0 10px}}
</style>
</head>
<body>
<header class="top col">
  <div class="inner">
    <p class="kicker">Seeds of Renaissance &middot; type &middot; round one &middot; reviewed 30 September 2026</p>
    <h1>Heading faces, and what was said about them</h1>
    <p>Nineteen candidates for the Dawn statement, shown in the real frame. This is the record of the round, kept so a later one does not re-propose what has already been turned down. <b>Two were liked: Polyamine and Restora.</b></p>

    <div class="rec">
      <h2>What came out of it</h2>
      <p class="said">&ldquo;Weightiness is important, this grounded weightiness. We are saying something relatively significant, but at the same time it wants to have a bit of an edge, a bit of novelty. It wants life &mdash; life and groundedness and wholeness &mdash; without becoming just organic kitsch.&rdquo;</p>
      <p class="said">&ldquo;I end up liking Restora and Polyamine because they have something a little organic and elegant, but they are both fonts that do feel quite luxurious and sleek. The thing is, if you take that, then you have to compensate with something more weighty and grounded in the body.&rdquo;</p>
      <p>The rejections divide cleanly. Most of the classical faces failed as <b>boring</b> &mdash; well drawn, no personality, nothing new. The stranger ones failed as <b>backward-looking</b>, which is the sharper objection: this is a new rebirth emerging forwards, not a return to the last Renaissance, so runes and revivals are out.</p>
      <p>The full brief, and where it goes next: <a href="../type.md">type.md</a>.</p>
    </div>
  </div>
</header>
{"".join(rendered_block(i, f) for i, f in enumerate(RENDERED, 1))}

<section class="sect col"><div class="inner">
  <h2>Also reviewed</h2>
  <h3>Commercial faces, shown as links</h3>
  <p>These could not be embedded, so they were reviewed on the foundries&rsquo; own specimen pages rather than in the frame.</p>
  <ul class="lookup">
    {"".join(listed_row(f) for f in LISTED)}
  </ul>
</div></section>

<footer class="fin">
  <div class="inner">
    <h2>Notes</h2>
    <p>Polyamine renders here only where it is installed; it has no web font file and is loaded through <code>local()</code>. Everywhere else its block shows a fallback.</p>
    <p>The body face is the same in every frame, so the heading is the only variable. It is Newsreader, a placeholder, not a decision.</p>
  </div>
</footer>
</body>
</html>'''

ascii_page = PAGE.encode("ascii", "xmlcharrefreplace").decode("ascii")

# Standalone copy: opens straight from disk, needs its own document skeleton.
out = HERE / "round-01-headings.html"
out.write_text(ascii_page)

# Artifact copy: the platform supplies the skeleton, so ship the parts bare.
# Generated on demand and kept out of the repo, since it duplicates the above.
bare = ascii_page[ascii_page.index("<title>"):ascii_page.rindex("</body>")]
bare = bare.replace("</head>\n<body>\n", "")   # the slice spans the head/body boundary
for tag in ("<!doctype", "<html", "<body>", "</body>", "</head>"):
    assert tag not in bare, "skeleton tag leaked into the artifact copy: " + tag
alt = HERE / "round-01-headings.artifact.html"
alt.write_text(bare)

for f in (out, alt):
    print(f"{f.stat().st_size/1024:.0f} KB  {f.name}")
