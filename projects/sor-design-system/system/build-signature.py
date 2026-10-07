"""Build the diagram signature (diagrams.md#the-signature) into system/img/:

  signature.svg, signature.png, signature@2x.png                 light grounds
  signature-dark.svg, signature-dark.png, signature-dark@2x.png  dark grounds
  signature-name.svg, … signature-name-dark.svg, …              name only, no URL
  signature.excalidraw                                           all four, as images at fixed size

Transparent backgrounds. 1x is for a 1600px-wide export (mark 64px); @2x for 3200px.
PNGs are rendered with headless Chrome. Rerun after changing system/outline.py or the URL.
Needs: fonttools, uharfbuzz (see outline.py); Google Chrome."""
import base64, json, pathlib, subprocess, sys, tempfile, time
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


files, elements = {}, []
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
    # Excalidraw: one image element per version, at 1x size (drawn on a ground so the dark one shows)
    fid = f"sor-{name}"
    files[fid] = {"mimeType": "image/png", "id": fid, "created": int(time.time() * 1000),
                  "dataURL": "data:image/png;base64," + base64.b64encode((img / f"{name}@2x.png").read_bytes()).decode()}
    y = i * (H + 60)
    if theme == "dark":
        elements.append(dict(type="rectangle", id=f"sor-night-{i}", x=-24, y=y - 24, width=W + 48, height=H + 48, angle=0,
                             strokeColor="transparent", backgroundColor="#171613", fillStyle="solid", strokeWidth=1,
                             strokeStyle="solid", roughness=0, opacity=100, groupIds=[], frameId=None, roundness=None,
                             seed=1, version=1, versionNonce=1, isDeleted=False, boundElements=None, updated=1,
                             link=None, locked=True))
    elements.append(dict(type="image", id=fid, x=0, y=y, width=W, height=H, angle=0, strokeColor="transparent",
                         backgroundColor="transparent", fillStyle="solid", strokeWidth=1, strokeStyle="solid",
                         roughness=0, opacity=100, groupIds=[], frameId=None, roundness=None, seed=2 + i, version=1,
                         versionNonce=2 + i, isDeleted=False, boundElements=None, updated=1, link=None, locked=False,
                         status="saved", fileId=fid, scale=[1, 1]))

(img / "signature.excalidraw").write_text(json.dumps(
    {"type": "excalidraw", "version": 2, "source": "sor-design-system/system/build-signature.py",
     "elements": elements, "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None}, "files": files}, indent=1))
