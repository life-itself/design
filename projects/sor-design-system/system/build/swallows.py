"""The swallows-and-fingerprints ground, shared by the podcast thumbnail kit and the Instagram templates.

Sunlight (the system's pale yellow, --sunlight; chosen 13 October 2026 over plain white), the black swallow engraving rising from the bottom-left corner, the logo's fingerprints
faded to 20% around it, and a clear zone where the words go. Each function returns an SVG fragment;
`sys` is the relative path from the calling page to system/.

Used by examples/youtube/canva-kit/build.py and examples/social/instagram/build.py.
"""

GROUND = "#fbefc4"               # --sunlight. A paper-to-sunlight wash (GROUND_WASH) is the gentler alternative
GROUND_WASH = ("#fbfaf6", "#f6e2a4")
PRINTS_OPACITY = 0.2
SWALLOWS_ASPECT = 0.922          # height / width of swallows-flock-engraving-black.png
LOCKUP_ASPECT = 211 / 1200       # height / width of the horizontal lockup


def defs(W, H, clear=None):
    """Filters and masks. clear: (x, y, w, h), the area the prints fade out of, behind the words."""
    hole = ""
    if clear:
        x, y, w, h = clear
        hole = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="40" fill="#000" filter="url(#b40)"/>'
    return f"""<defs>
  <filter id="b40" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="40"/></filter>
  <mask id="mPrints" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="#fff"/>{hole}
  </mask>
  <linearGradient id="fadeDown" x1="0" y1="0" x2="0" y2="1"><stop offset=".68" stop-color="#fff"/><stop offset=".92" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <mask id="mFace" maskContentUnits="objectBoundingBox"><rect width="1" height="1" fill="url(#fadeDown)"/></mask>
</defs>"""


def white(W, H, wash=False):
    """The ground: sunlight, or the paper-to-sunlight wash (white behind the words, warm towards the bottom right)."""
    if not wash:
        return f'<rect width="{W}" height="{H}" fill="{GROUND}"/>'
    a, b = GROUND_WASH
    return (f'<linearGradient id="wash" x1="0" y1="0" x2="1" y2="1"><stop offset=".3" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>'
            f'<rect width="{W}" height="{H}" fill="url(#wash)"/>')


def prints(sys, rings, opacity=PRINTS_OPACITY):
    """The fingerprints of the logo's ring (system/img/fingerprints-red.png, no bird), faded.
    rings: list of (cx, cy, size, rotation). Several rings overlap to fill the corner."""
    out = ""
    for cx, cy, s, rot in rings:
        out += (f'<image href="{sys}/img/fingerprints-red.png" x="{cx - s / 2}" y="{cy - s / 2}" width="{s}" height="{s}" '
                f'transform="rotate({rot} {cx} {cy})"/>')
    return f'<g mask="url(#mPrints)" opacity="{opacity}">{out}</g>'


def swallows(sys, x, y, w, rot):
    h = round(w * SWALLOWS_ASPECT)
    return (f'<image href="{sys}/graphics/prints/elements/swallows-flock-engraving-black.png" x="{x}" y="{y}" width="{w}" height="{h}" '
            f'transform="rotate({rot} {x + w / 2} {y + h / 2})"/>')


def lockup(sys, x, y, w):
    """The horizontal logo (mark and name), colour, straight on white: no disc."""
    return f'<image href="{sys}/logo/lockups/seeds-logo-horizontal-colour-2400.png" x="{x}" y="{y}" width="{w}" height="{round(w * LOCKUP_ASPECT)}"/>'
