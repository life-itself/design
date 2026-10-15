"""Build the diagram signature (diagrams.md#the-signature) into system/img/:

  signature.svg, signature.png, signature@2x.png                 light grounds
  signature-dark.svg, signature-dark.png, signature-dark@2x.png  dark grounds
  signature-name.svg, … signature-name-dark.svg, …              name only, no URL

Transparent backgrounds. 1x is for a 1600px-wide export (mark 64px); @2x for 3200px.
PNGs are rendered with headless Chrome. Rerun after changing system/outline.py or the URL.
Needs: fonttools, uharfbuzz (see outline.py); Google Chrome."""
import pathlib, subprocess, sys, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from outline import SYSTEM, DISC, signature

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PAD = 4  # keeps antialiased edges inside the canvas
img = SYSTEM / "img"


def png(svg_path, out, w, h, scale):
    html = pathlib.Path(tempfile.mkdtemp()) / "s.html"
    html.write_text(f'<html><body style="margin:0;background:transparent"><img src="{svg_path.as_uri()}" width="{w}" height="{h}"></body></html>')
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--default-background-color=00000000",
                    f"--force-device-scale-factor={scale}", f"--window-size={w},{h}", f"--screenshot={out}", html.as_uri()],
                   check=True, capture_output=True)


VERSIONS = [(t, u) for u in (True, False) for t in ("light", "dark")]
for i, (theme, with_url) in enumerate(VERSIONS):
    frag, w = signature(theme) if with_url else signature(theme, url=None)
    W, H = round(w) + 2 * PAD, DISC + 2 * PAD
    name = "signature" + ("" if with_url else "-name") + ("" if theme == "light" else "-dark")
    svg = img / f"{name}.svg"
    svg.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="{-PAD} {-PAD} {W} {H}">'
                   f'<title>Seeds of Renaissance</title>{frag}</svg>\n')
    png(svg, img / f"{name}.png", W, H, 1)
    png(svg, img / f"{name}@2x.png", W, H, 2)
    print(name, W, H)
