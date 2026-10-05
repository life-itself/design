"""Regenerate graphics.js (inline sprite loader) from graphics.svg."""
import json, pathlib
here = pathlib.Path(__file__).parent
svg = (here / "graphics.svg").read_text().strip()
head = (here / "graphics.js").read_text().split("document.currentScript")[0]
(here / "graphics.js").write_text(head + "document.currentScript.insertAdjacentHTML('afterend'," + json.dumps(svg) + ");\n")
