#!/bin/zsh
# Cut a painted or photographic animal (not a clean print) out of its paper.
# Writes NAME-original.png (source colours, transparent) and, in each ink,
# NAME-<ink>.svg/.png printed in three tones: solid, mid and a light tint.
# Usage: ./make-tonal.sh SOURCE NAME [crop WxH+X+Y] [edge%] [erase WxH+X+Y ...]
#   edge%: how dark a pixel must be to count as the animal's edge (default 82).
#   Pale areas enclosed by the edge are filled in, so pale wings stay solid.
#   erase boxes (in crop coordinates) lose thin dark marks such as lettering.
#   CLOSE=10 bridges gaps where a pale edge meets the paper with no outline.
set -e
SRC=$1; NAME=$2; CROP=$3; EDGE=${4:-82}; shift 4 2>/dev/null || shift $#
OUT=${0:a:h}/elements
T=$(mktemp -d)
typeset -A INKS
INKS=(black "#1b1916" blue "#03296f" green "#1f3d2b" mustard "#c9a227")

magick "$SRC" ${CROP:+-crop} ${CROP:+$CROP} +repage -filter Lanczos -resize 300% "$T/big.png"
for box in "$@"; do  # thin dark marks vanish under a grey closing; larger spots survive
  g=(${(s:x:)${box%%+*}}); o=(${(s:+:)${box#*+}})
  box3="$((g[1]*3))x$((g[2]*3))+$((o[1]*3))+$((o[2]*3))"
  magick "$T/big.png" \( +clone -crop $box3 +repage -morphology Close Disk:7 \) \
    -geometry +$((o[1]*3))+$((o[2]*3)) -composite "$T/big.png"
done
magick "$T/big.png" -colorspace Gray "$T/L.png"
# edge mask, then fill everything not connected to the paper
magick "$T/L.png" -blur 0x1 -threshold "$EDGE%" -negate -morphology Close Disk:${CLOSE:-3} "$T/m0.png"
magick "$T/m0.png" -negate -define connected-components:keep-top=1 -define connected-components:mean-color=true \
  -connected-components 8 -threshold 50% -negate -morphology Open Disk:2 "$T/fill.png"
# drop specks: keep pieces over 0.2% of the area (body, wings, antennae)
A=$(magick "$T/fill.png" -format "%[fx:int(w*h*0.002)]" info:)
magick "$T/fill.png" -define connected-components:area-threshold=$A -define connected-components:mean-color=true \
  -connected-components 8 -threshold 50% "$T/mask.png"
magick "$T/mask.png" -blur 0x1 "$T/alpha.png"

# original colours
magick "$T/big.png" "$T/alpha.png" -alpha off -compose CopyOpacity -composite -trim +repage -resize 1000x \
  -strip -define png:compression-level=9 PNG32:"$OUT/$NAME-original.png"

# three tones, each traced; pbm: black = ink
magick "$T/mask.png" -negate "$T/t1.pbm"
for lv th in 2 62 3 38; do
  magick "$T/L.png" -blur 0x1.5 -threshold "$th%" \( "$T/mask.png" -negate \) -compose Lighten -composite "$T/t$lv.pbm"
done
for lv in 1 2 3; do
  potrace "$T/t$lv.pbm" -s -t 8 -a 1.0 -O 0.4 --flat -o "$T/t$lv.svg"
done
python3 - "$T" "$OUT" "$NAME" ${(kv)INKS} <<'EOF'
import re, sys
T, out, name, *kv = sys.argv[1:]
svgs = [open(f"{T}/t{i}.svg").read() for i in (1, 2, 3)]
head = re.search(r"<svg[^>]*>", svgs[0]).group(0)
g = re.search(r'<g transform="([^"]*)"', svgs[0]).group(1)
paths = ["".join(re.findall(r"<path[^>]*/>", s, re.S)) for s in svgs]
for ink, hexv in zip(kv[::2], kv[1::2]):
    body = "".join(f'<g fill="{hexv}" fill-opacity="{op}">{p}</g>' for op, p in zip(("0.2", "0.5", "1"), paths))
    open(f"{out}/{name}-{ink}.svg", "w").write(f'{head}<g transform="{g}" stroke="none">{body}</g></svg>')
EOF
for c hex in ${(kv)INKS}; do
  magick -background none -density 72 "$OUT/$NAME-$c.svg" -trim +repage -resize 1000x PNG32:"$OUT/$NAME-$c.png"
  pngquant --quality 80-100 --speed 1 --strip --force --skip-if-larger --output "$OUT/$NAME-$c.png" "$OUT/$NAME-$c.png" || true
done
rm -rf "$T"
echo "wrote $OUT/$NAME-{original,black,blue,green,mustard}"
