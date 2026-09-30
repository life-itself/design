#!/usr/bin/env python3
"""Build the round-two page: body faces, then eyebrow faces.

Only one thing changes per block. In the body section the eyebrow is held at
Apfel Grotezk; in the eyebrow section the body is held at the leading body
candidate. Otherwise you cannot tell which half you are reacting to.

The statement is set in Polyamine, which renders only where it is installed.
It stands in for Restora, which is commercial and cannot be embedded here.

    python3 build-round-02.py
"""
import base64, html, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).parent
CACHE = HERE / "fonts"
FS = "https://cdn.fontshare.com/wf/"
JD = "https://cdn.jsdelivr.net/fontsource/fonts/"

SOURCES = {
    "bespoke-serif.woff2": FS + "DGL7AR63QELJFTOEASXHFYM5NAKYODNK/GYJUWP667LEHZ5W2WM5CQDIWDFJX2DFY/DLLWXFUYSJGEWBBZLWVRWRKWK2K5HHIO.woff2",
    "bespoke-slab.woff2":  FS + "LT6CUPYRZ2JVDEFNZ2YVFQVDBYQ6HAJE/KHSOPSBQK7EFD27XA47KJCHMDUJ5CCEM/2IULMYS7GXHFHXL3JBAVQ3SQRKK2KG5A.woff2",
    "sentient.woff2":      FS + "RVTZPYAA57KV4AMXRX7ZIPJXSTYCRP7A/36OUS5CBIXRKI2QU7G7OUHOK7HHA53Y2/SIH66VPT4WS2HIF5PEJNDU4INNUF54LG.woff2",
    "hoover.woff2":        FS + "OQWQQBPOJ6JEQJV3IQRYIO6O37L3RDLS/64EBY5K6OPMMQUI6U3GHDF7ETCSNWW67/5PIX6GR4DQXNGX56EQFMKN7WIMTAIE26.woff2",
    "literata.woff2":      JD + "literata@latest/latin-400-normal.woff2",
    "bricolage.woff2":     JD + "bricolage-grotesque@latest/latin-400-normal.woff2",
    "apfel.woff2":         "https://raw.githubusercontent.com/collletttivo/apfel-grotezk/main/fonts/ApfelGrotezk-Mittel.woff2",
    "azeret.woff2":        JD + "azeret-mono@latest/latin-400-normal.woff2",
    "ysabeau.woff2":       JD + "ysabeau-office@latest/latin-400-normal.woff2",
}

PARA = ("Human history has always been a story of transformation – of old worlds dying and new "
        "ones being born. Every great crisis carries within it the seed of rebirth. We are a movement "
        "called to bring forth a civilizational renaissance grounded in Wisdom, Interbeing, Inner "
        "growth, Revoligion, Complexity and beyond capitalism.")
STATEMENT = "We are a vision and movement for civilizational renewal."
INVITE = "Read the full manifesto &middot; or continue &darr;"


def b64(name):
    CACHE.mkdir(exist_ok=True)
    p = CACHE / name
    if not p.exists():
        subprocess.run(["curl", "-sfL", "-o", str(p), SOURCES[name]], check=True)
    d = p.read_bytes()
    if d[:4] != b"wOF2":
        sys.exit("not a woff2: " + str(p))
    return base64.b64encode(d).decode("ascii")


BODIES = [
    dict(rank="B1", name="Bespoke Slab", css="'Bespoke Slab',Georgia,serif", size="1.32rem", lh="1.6",
         who="Indian Type Foundry, via Fontshare · free for commercial use",
         flag="My pick",
         gist="The most genuinely weighty of them, without being fat.",
         note="Even, low-contrast strokes and warm slab details. It holds its colour on black "
              "where a finer serif goes grey, and it gives the page the ballast the brief asks "
              "for while staying contemporary rather than Victorian. Against a sleek display "
              "face this is a real contrast rather than a quieter version of the same thing."),
    dict(rank="B2", name="Bespoke Serif", css="'Bespoke Serif',Georgia,serif", size="1.34rem", lh="1.6",
         who="Indian Type Foundry, via Fontshare · free for commercial use",
         flag="Close second",
         gist="Sturdy and wide, with flared, slightly odd details.",
         note="The same family as the slab, without the slabs. A little more elegant and a "
              "little less grounded, so it depends which way you want to lean. Low contrast "
              "means no hairlines to flicker out on the dark frames."),
    dict(rank="B3", name="Bricolage Grotesque", css="'Bricolage Grotesque',system-ui,sans-serif",
         size="1.26rem", lh="1.62",
         who="Mathieu Triay · free, SIL OFL",
         flag="The sans option",
         gist="The strongest contrast, and unmistakably forward-looking.",
         note="A grotesque with ink traps and deliberately awkward details — the ink traps are "
              "the giveaway that it is drawn now rather than revived. Chunky enough to act as a "
              "foil to a delicate display serif. The biggest departure on the page, so it is "
              "either obviously right or obviously wrong."),
    dict(rank="B4", name="Hoover", css="'Hoover',Georgia,serif", size="1.34rem", lh="1.6",
         who="Gaëtan Baehr, via Fontshare · free for commercial use",
         flag="Most personality",
         gist="Compact and mannered. Real presence, possibly too much of it.",
         note="Narrow, slab-ish and full of character — look at the W and the g. It has more "
              "personality than anything else here, which is what you have been asking for. The "
              "risk is the opposite of boring: it may tire over a long manifesto."),
    dict(rank="B5", name="Sentient", css="'Sentient',Georgia,serif", size="1.3rem", lh="1.6",
         who="Noopur Choksi, Indian Type Foundry · free for commercial use",
         flag="Competes with the heading",
         gist="Elegant and warm — but it is in the display register.",
         note="Well drawn and it reads beautifully, but the contrast is high and the mood is "
              "close to Polyamine and Restora. That makes it a smaller cousin of the heading "
              "rather than a counterweight to it, which is exactly what the brief says not to "
              "do. Included so you can see the failure mode."),
    dict(rank="B6", name="Literata", css="'Literata',Georgia,serif", size="1.3rem", lh="1.6",
         who="TypeTogether · free, SIL OFL",
         flag="The safe one",
         gist="Solid, screen-first, and probably boring.",
         note="Drawn for Google Books, so extended screen reading is the whole brief. Sturdy "
              "stems, no hairlines, dependable on both grounds. Here as the baseline: if "
              "everything above feels like too much, this is what restraint looks like, and "
              "it is very likely the one you call boring."),
]

EYEBROWS = [
    dict(name="Apfel Grotezk", css="'Apfel Grotezk',system-ui,sans-serif", flag="My pick",
         who="Collletttivo · free, SIL OFL",
         note="Flat terminals and slightly odd proportions — the quality you liked in Karla. "
              "Warm rather than cold-Swiss, sturdy at 12px reversed out, and it carries the "
              "down arrow and middot, which several candidates do not."),
    dict(name="Azeret Mono", css="'Azeret Mono',ui-monospace,monospace", flag="If you want texture",
         who="Displaay · free, SIL OFL",
         note="Mono gives the most tension against an elegant serif. It reads forward-looking "
              "rather than retro-terminal, which most monos fail at. The reservation: mono adds "
              "a fourth texture to the system and reads technical, which pulls against "
              "groundedness and wholeness."),
    dict(name="Ysabeau Office", css="'Ysabeau Office',system-ui,sans-serif", flag="The warm one",
         who="Christian Thalmann · free, SIL OFL",
         note="A humanist sans with Garamond bones — the most grounded and whole of the three, "
              "and the least edgy. Use 500 or above; the light weights disappear on black."),
]


def body_block(f):
    return f'''
  <section class="cand">
    <div class="col label">
      <div class="lhead">
        <span class="rank">{f["rank"]}</span>
        <div class="lname"><h2>{html.escape(f["name"])}</h2><p class="src">{f["who"]}</p></div>
        <span class="flag{' pick' if f["rank"] == "B1" else ''}">{html.escape(f["flag"])}</span>
      </div>
      <p class="gist">{html.escape(f["gist"])}</p>
      <p class="note">{f["note"]}</p>
    </div>
    <div class="frame">
      <span class="tag">{f["rank"]} &middot; {html.escape(f["name"])}</span>
      <div class="finner">
        <p class="ftext" style="font-family:{f['css']};font-size:{f['size']};line-height:{f['lh']}">{PARA}</p>
        <h3 class="fstatement">{STATEMENT}</h3>
        <p class="finvite">{INVITE}</p>
      </div>
    </div>
  </section>'''


def eyebrow_block(f):
    return f'''
  <section class="cand">
    <div class="col label">
      <div class="lhead">
        <div class="lname"><h2>{html.escape(f["name"])}</h2><p class="src">{f["who"]}</p></div>
        <span class="flag{' pick' if f["flag"] == "My pick" else ''}">{html.escape(f["flag"])}</span>
      </div>
      <p class="note">{f["note"]}</p>
    </div>
    <div class="frame frame-short">
      <span class="tag">{html.escape(f["name"])}</span>
      <div class="finner">
        <p class="ftext" style="font-family:'Bespoke Slab',Georgia,serif;font-size:1.32rem">{PARA}</p>
        <p class="finvite" style="font-family:{f['css']}">{INVITE}</p>
      </div>
    </div>
  </section>'''


PAGE = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Body and eyebrow faces</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Italiana&display=swap">
<style>
:root{{
  --page:#fbfaf7; --fg:#1a1817; --muted:#6f675f; --line:#e4ded6; --accent:#b81414;
  --night:#080707; --daylight:#efebe4;
  --ui:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  color-scheme:light;
}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{
  --page:#15130f; --fg:#ece7df; --muted:#8e867c; --line:#312d27; --accent:#f0736f;
  color-scheme:dark;
}}}}
:root[data-theme="dark"]{{
  --page:#15130f; --fg:#ece7df; --muted:#8e867c; --line:#312d27; --accent:#f0736f;
  color-scheme:dark;
}}
*,*::before,*::after{{box-sizing:border-box}}
body{{margin:0;background:var(--page);color:var(--fg);font-family:var(--ui);
  font-size:15.5px;line-height:1.65;-webkit-font-smoothing:antialiased}}

@font-face{{font-family:"Bespoke Serif";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("bespoke-serif.woff2")}) format("woff2")}}
@font-face{{font-family:"Bespoke Slab";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("bespoke-slab.woff2")}) format("woff2")}}
@font-face{{font-family:"Sentient";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("sentient.woff2")}) format("woff2")}}
@font-face{{font-family:"Hoover";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("hoover.woff2")}) format("woff2")}}
@font-face{{font-family:"Literata";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("literata.woff2")}) format("woff2")}}
@font-face{{font-family:"Bricolage Grotesque";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("bricolage.woff2")}) format("woff2")}}
@font-face{{font-family:"Apfel Grotezk";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("apfel.woff2")}) format("woff2")}}
@font-face{{font-family:"Azeret Mono";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("azeret.woff2")}) format("woff2")}}
@font-face{{font-family:"Ysabeau Office";font-weight:100 900;font-display:swap;
  src:url(data:font/woff2;base64,{b64("ysabeau.woff2")}) format("woff2")}}
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
.rec .said{{color:var(--fg);border-left:2px solid var(--line);padding-left:12px;margin:12px 0}}

.cand{{margin-top:56px}}
.label{{margin-bottom:18px}}
.lhead{{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:8px}}
.rank{{font-size:12px;font-weight:600;color:var(--muted);letter-spacing:.08em}}
.lname h2{{margin:0;font-size:1.02rem;font-weight:600;letter-spacing:-.008em}}
.src{{margin:1px 0 0;font-size:11.5px;color:var(--muted)}}
.flag{{margin-left:auto;font-size:10.5px;font-weight:700;letter-spacing:.1em;
  text-transform:uppercase;border:1px solid var(--line);border-radius:999px;
  padding:3px 9px;white-space:nowrap;color:var(--muted)}}
.flag.pick{{color:var(--accent);border-color:var(--accent)}}
.gist{{margin:0;font-size:15.5px;font-weight:600;max-width:70ch}}
.note{{margin:7px 0 0;color:var(--muted);font-size:14.5px;max-width:76ch}}

.frame{{position:relative;background:var(--night);min-height:clamp(480px,86vh,940px);
  display:grid;place-items:center;padding:clamp(3rem,10vh,7rem) clamp(20px,6vw,64px)}}
.frame-short{{min-height:clamp(360px,58vh,620px)}}
.frame .tag{{position:absolute;top:14px;left:16px;font-size:10.5px;letter-spacing:.14em;
  text-transform:uppercase;color:#6a635b;font-weight:600}}
.finner{{display:grid;justify-items:center;gap:clamp(2.4rem,6vw,4.2rem);width:100%;max-width:60rem}}
.ftext{{color:var(--daylight);text-align:center;max-width:52ch;margin:0;text-wrap:pretty}}
.fstatement{{font-family:'Polyamine','Didot','Bodoni 72',Georgia,serif;font-weight:400;
  color:var(--daylight);text-transform:uppercase;font-size:clamp(1.5rem,3.5vw,2.8rem);
  letter-spacing:.09em;line-height:1.28;text-align:center;margin:0;max-width:22em;text-wrap:balance}}
.finvite{{font-family:'Apfel Grotezk',system-ui,sans-serif;color:var(--daylight);margin:0;
  text-align:center;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;opacity:.8}}

.sect{{padding-block:64px 0}}
.sect .inner{{max-width:66ch}}
.sect h2{{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);
  font-weight:700;margin:0 0 8px}}
.sect h3{{font-size:1.15rem;font-weight:600;margin:0 0 10px;letter-spacing:-.008em}}
.sect p{{margin:0 0 10px;color:var(--muted)}}
.sect b{{color:var(--fg);font-weight:600}}

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
    <p class="kicker">Seeds of Renaissance &middot; type &middot; round two</p>
    <h1>Body faces, and the small voice underneath</h1>
    <p>Six body faces in the real frame, then three for the eyebrow line. <b>Only one thing changes per block.</b> Through the body section the eyebrow is held at Apfel Grotezk; through the eyebrow section the body is held at Bespoke Slab.</p>
    <p>The statement is set in <b>Polyamine</b>, standing in for Restora, which is commercial and cannot be embedded. It renders only on a machine with Polyamine installed — elsewhere that line falls back and should be ignored.</p>

    <div class="rec">
      <h2>What I think</h2>
      <p class="said">&ldquo;If you take that, then you have to compensate with something more weighty and grounded in the body.&rdquo;</p>
      <p>That is the whole test. The body is not a neutral container here, it is the ballast — so the usual advice of pairing a display serif with a quiet workhorse is exactly wrong, and a face that is merely well-behaved will fail the same way the classical headings did.</p>
      <p>My pick is <b>Bespoke Slab</b>: the most genuinely weighty of them without tipping into fat, contemporary rather than revived, and a real counterweight rather than a smaller echo of the heading. <b>Bespoke Serif</b> is the same idea with a little more elegance and a little less heft.</p>
      <p>Two are here as arguments rather than candidates. <b>Sentient</b> shows the failure mode of picking a body face from the display register. <b>Literata</b> shows what pure restraint looks like, and is the one I expect you to call boring.</p>
    </div>
  </div>
</header>

<section class="sect col"><div class="inner">
  <h2>Part one</h2><h3>The body</h3>
  <p>Six candidates, ranked. All are free for commercial use. Commercial options exist — Arizona Mix from Dinamo and Right Serif from Pangram Pangram are the strongest — but they cannot be embedded, so they are not shown rather than not considered.</p>
</div></section>
{"".join(body_block(f) for f in BODIES)}

<section class="sect col"><div class="inner">
  <h2>Part two</h2><h3>The eyebrow</h3>
  <p>The smallest voice on the page: labels, captions, and the invitation line. It has never been chosen — the build falls back to the system font by accident.</p>
  <p>One practical constraint that decided more than taste did: the line ends in a down arrow, and <b>several otherwise good faces have no arrow glyph at all</b>. Everything shown here carries both the arrow and the middot.</p>
</div></section>
{"".join(eyebrow_block(f) for f in EYEBROWS)}

<footer class="fin">
  <div class="inner">
    <h2>Notes</h2>
    <p>Round one, with the verdicts on it: <a href="round-01-headings.html">round-01-headings.html</a>. The brief: <a href="../type.md">type.md</a>.</p>
    <p>Sizes are tuned per face, since they have different x-heights and setting them all at one size would flatter the large-eyed ones. Measure is 52 characters throughout, as in the build.</p>
  </div>
</footer>
</body>
</html>'''

ascii_page = PAGE.encode("ascii", "xmlcharrefreplace").decode("ascii")
out = HERE / "round-02-body.html"
out.write_text(ascii_page)

bare = ascii_page[ascii_page.index("<title>"):ascii_page.rindex("</body>")]
bare = bare.replace("</head>\n<body>\n", "")
for tag in ("<!doctype", "<html", "<body>", "</body>", "</head>"):
    assert tag not in bare, "skeleton tag leaked: " + tag
alt = HERE / "round-02-body.artifact.html"
alt.write_text(bare)

for f in (out, alt):
    print(f"{f.stat().st_size/1024:.0f} KB  {f.name}")
