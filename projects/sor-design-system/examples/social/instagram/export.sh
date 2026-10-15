#!/bin/sh
# Build the pages, then screenshot each one at its real size (1080 wide) into png/.
# Transparent layers keep their transparency; in Canva, drop each PNG in and stretch it to fill the page.
cd "$(dirname "$0")"
python3 build.py >/dev/null
mkdir -p png && rm -f png/*.png
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for f in src/*.html; do
  n=$(basename "$f" .html)
  size=$(grep -o '<svg width="[0-9]*" height="[0-9]*"' "$f" | sed 's/.*width="\([0-9]*\)" height="\([0-9]*\)"/\1,\2/')
  ( "$CHROME" --headless=new --user-data-dir="${TMPDIR:-/tmp}/sor-instagram-chrome" --no-first-run --disable-gpu --hide-scrollbars \
      --force-device-scale-factor=1 --default-background-color=00000000 --window-size="$size" \
      --allow-file-access-from-files --virtual-time-budget=8000 \
      --screenshot="$PWD/png/$n.png" "file://$PWD/$f" >/dev/null 2>&1 & pid=$!
    for i in $(seq 60); do [ -s "png/$n.png" ] && break; sleep 0.5; done; sleep 1; kill $pid 2>/dev/null )
done
# Elements that are plain copies of system files
cp ../../../system/img/fingerprints-red.png png/element-fingerprint-ring.png
cp ../../../system/prints/elements/swallows-flock-engraving-black.png png/element-swallows-flock-black.png
cp ../../../system/logo/lockups/seeds-logo-horizontal-colour-2400.png png/element-logo-lockup.png
cp ../../../system/logo/mark/seeds-mark-colour.png png/element-logo-mark.png
ls png | wc -l
