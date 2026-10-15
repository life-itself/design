#!/bin/sh
# Show art at 3000 × 3000 (the 1000 × 1000 artboard at 3×), and square episode art from the
# Instagram 1:1 podcast template at 3000 × 3000. Small JPG previews go in web/.
cd "$(dirname "$0")"
python3 build.py >/dev/null
(cd ../social/instagram && python3 build.py >/dev/null)
mkdir -p png web && rm -f png/*.png
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
shot() { # page, output, width, height, scale
  ( "$CHROME" --headless=new --user-data-dir="${TMPDIR:-/tmp}/sor-podcast-chrome" --no-first-run --disable-gpu --hide-scrollbars \
      --force-device-scale-factor="$5" --default-background-color=00000000 --window-size="$3,$4" \
      --allow-file-access-from-files --virtual-time-budget=8000 --screenshot="$PWD/$2" "file://$1" >/dev/null 2>&1 & pid=$!
    for i in $(seq 60); do [ -s "$2" ] && break; sleep 0.5; done; sleep 1; kill $pid 2>/dev/null )
}
for n in show-art show-art-wash; do shot "$PWD/src/$n.html" "png/$n.png" 1000 1000 3; done
IG="$(cd ../social/instagram && pwd)/src"
shot "$IG/example-podcast-1x1.html" png/episode-art-example.png 1080 1080 2.7778
shot "$IG/bg-1x1.html" png/episode-art-background.png 1080 1080 2.7778
shot "$IG/guides-podcast-1x1.html" png/episode-art-guides.png 1080 1080 2.7778
for f in png/*.png; do n=$(basename "$f" .png); sips -s format jpeg -s formatOptions 84 -Z 1000 "$f" --out "web/$n.jpg" >/dev/null; done
sips -g pixelWidth png/show-art.png png/episode-art-example.png | grep pixel
