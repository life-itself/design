#!/usr/bin/env bash
# Publish the website drafts (mockups, briefs, video options) to Flowershow:
# https://sor-website-drafts-rufuspollock.flowershow.me
# Builds _site/ (gitignored) with the design-system files the pages use, then runs fl.
set -euo pipefail
cd "$(dirname "$0")"
DS=../sor-design-system
DS_URL=https://sor-design-system-rufuspollock.flowershow.me

rm -rf _site && mkdir -p _site/home _site/system/img
cp README.md _site/
cp "$DS"/system/{tokens.css,components.css,fonts.css,graphics.js,sor.js} _site/system/
cp -r home/assets _site/home/

# HTML pages: point at the bundled system/ and copy only the images they use
for f in home/*.html; do
  sed 's#\.\./\.\./sor-design-system/system/#../system/#g' "$f" > "_site/$f"
done
for img in $(grep -oh 'system/img/[A-Za-z0-9._-]*' home/*.html | sort -u); do
  cp "$DS/$img" _site/system/img/
done

# Markdown: links into the design system go to its published site
for f in home/*.md; do
  sed -E "s#\]\(\.\./\.\./sor-design-system/([^)]*)\.md([)\#])#](${DS_URL}/\1\2#g; s#\]\(\.\./\.\./sor-design-system/#](${DS_URL}/#g" "$f" > "_site/$f"
done

fl --yes --name sor-website-drafts _site
