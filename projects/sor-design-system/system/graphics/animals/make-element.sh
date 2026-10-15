#!/bin/zsh
# Cut an animal woodcut out of its paper and write SVG + PNG in each ink colour.
# Usage: ./make-element.sh SOURCE NAME [threshold%] [crop WxH+X+Y]
#   NAME is subject-style, e.g. fox-sitting-linocut; colour is appended.
# Paper is flattened (divided by a blurred local maximum) so uneven light
# does not turn grey, then thresholded and traced with potrace.
# Set NOFLAT=1 for clean white backgrounds with very large solid areas.
set -e
SRC=$1; NAME=$2; TH=${3:-55}; CROP=$4
OUT=${0:a:h}/elements
TMP=$(mktemp -d)
typeset -A INKS
INKS=(black "#1b1916" blue "#03296f" green "#1f3d2b" mustard "#c9a227")

magick "$SRC" ${CROP:+-crop} ${CROP:+$CROP} +repage -colorspace Gray -resize 300% "$TMP/g.png"
if [[ -n $NOFLAT ]]; then cp "$TMP/g.png" "$TMP/flat.png"; else
magick "$TMP/g.png" \( +clone -resize 5% -morphology Dilate Disk:6 -resize "$(magick identify -format %wx%h! "$TMP/g.png")" -blur 0x20 \) \
  +swap -compose Divide_Dst -composite -level 0,100% "$TMP/flat.png"; fi
magick "$TMP/flat.png" -blur 0x2 -threshold "$TH%" -morphology Open Disk:1 "$TMP/bw.pbm"
potrace "$TMP/bw.pbm" -s -t 6 -a 1.0 -O 0.4 --flat -o "$TMP/raw.svg"
perl -0pi -e 's/<\?xml[^>]*>\s*//; s/<!DOCTYPE[^>]*>\s*//s' "$TMP/raw.svg"  # no DTD: artifact publishing rejects it

for c hex in ${(kv)INKS}; do
  sed -e "s/fill=\"#000000\"/fill=\"$hex\"/" "$TMP/raw.svg" > "$TMP/c.svg"
  # trim viewBox to the ink
  magick -background none -density 72 "$TMP/c.svg" -trim +repage -resize 1000x \
    PNG32:"$OUT/$NAME-$c.png"
  cp "$TMP/c.svg" "$OUT/$NAME-$c.svg"
  pngquant --quality 80-100 --speed 1 --strip --force --skip-if-larger --output "$OUT/$NAME-$c.png" "$OUT/$NAME-$c.png" || true
done
rm -rf "$TMP"
echo "wrote $OUT/$NAME-{black,blue,green}.{svg,png}"
