#!/bin/sh
# Build the layer pages, then screenshot each one at 2x (2560 × 1440) into png/.
# Transparent layers keep their transparency; in Canva, drop each PNG in and stretch it to fill the 1280 × 720 page.
cd "$(dirname "$0")"
python3 build.py >/dev/null
mkdir -p png && rm -f png/*.png
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for f in src/*.html; do
  n=$(basename "$f" .html); rm -f "png/$n.png"
  ( "$CHROME" --headless=new --user-data-dir="${TMPDIR:-/tmp}/sor-canva-kit-chrome" --no-first-run --disable-gpu --hide-scrollbars \
      --force-device-scale-factor=2 --default-background-color=00000000 --window-size=1280,720 \
      --allow-file-access-from-files --virtual-time-budget=8000 \
      --screenshot="$PWD/png/$n.png" "file://$PWD/$f" >/dev/null 2>&1 & pid=$!
    for i in $(seq 60); do [ -s "png/$n.png" ] && break; sleep 0.5; done; sleep 1; kill $pid 2>/dev/null )
done
ls -la png
# Web-sized copies of the finished examples, for the examples page and the docs
mkdir -p web
for n in example-one-guest example-two-guests example-with-guides; do
  sips -s format jpeg -s formatOptions 84 -Z 1280 "png/$n.png" --out "web/$n.jpg" >/dev/null
done
