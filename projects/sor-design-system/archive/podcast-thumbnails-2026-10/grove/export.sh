#!/bin/sh
# Screenshot each png/*.html at 4x with a transparent background.
cd "$(dirname "$0")/png"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for f in *.html; do
  n="${f%.html}"; rm -f "$n.png"
  size=$(grep -o 'width="[0-9]*" height="[0-9]*"' "$f" | tail -1 | sed 's/width="\([0-9]*\)" height="\([0-9]*\)"/\1,\2/')
  ( "$CHROME" --headless=new --user-data-dir="${TMPDIR:-/tmp}/grove-chrome" --no-first-run --disable-gpu --hide-scrollbars --force-device-scale-factor=4 \
    --default-background-color=00000000 --window-size="$size" \
    --screenshot="$PWD/$n.png" "file://$PWD/$f" >/dev/null 2>&1 & pid=$!
    for i in $(seq 40); do [ -s "$n.png" ] && break; sleep 0.5; done; sleep 1; kill $pid 2>/dev/null )
done
ls -la *.png
