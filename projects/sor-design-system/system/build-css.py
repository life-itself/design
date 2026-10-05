"""Build components.css from components.src.css by inlining the textures in textures.txt
(the torn-edge mask and the paper grain, both SVG data URIs)."""
import pathlib
here = pathlib.Path(__file__).parent
tex = dict(l.split("=", 1) for l in (here / "textures.txt").read_text().splitlines() if l)
css = (here / "components.src.css").read_text()
for k, v in tex.items():
    css = css.replace('url("%s")' % k, 'url("%s")' % v)
css = css.replace("Generated: components.css = this file", "GENERATED from components.src.css; edit that, then run build-css.py. Source:", 1)
(here / "components.css").write_text(css)
