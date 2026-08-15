#!/usr/bin/env python3
"""Clean a Google-Docs-exported Markdown file for typesetting.

- Strips the manual hyperlinked TOC block at the top
- Removes empty `#` page-break headers Google Docs export leaves behind
- Un-escapes backslash-escaped punctuation (\\. \\- \\[ \\] etc.)
- Converts `\\=>` sequences to a real arrow
- Strips heading anchor ids `{#foo}` (not needed once we control the template)
"""
import re
import sys

def clean(text: str) -> str:
    lines = text.split("\n")

    # Drop the manual TOC: everything from the first "[**Introduction" style
    # link line up to (not including) the first real heading.
    out = []
    skipping_toc = False
    for line in lines:
        if re.match(r"^\[\*\*", line):
            skipping_toc = True
            continue
        if skipping_toc and line.strip() == "":
            continue
        if line.startswith("# "):
            skipping_toc = False
        out.append(line)
    text = "\n".join(out)

    # Remove empty page-break headers: a line that is just "#" possibly with trailing space.
    text = re.sub(r"(?m)^#\s*$\n?", "", text)

    # Strip heading anchor ids: "## Title {#some-anchor}" -> "## Title"
    text = re.sub(r"\s*\{#[^}]*\}", "", text)

    # Un-escape common Google Docs backslash-escapes.
    text = re.sub(r"\\?=\\>", "→", text)  # => or \=\> -> right arrow
    for ch in ['.', '-', '[', ']', '(', ')', '*', '_']:
        text = text.replace("\\" + ch, ch)

    # Collapse 3+ blank lines to 2.
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip() + "\n"


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        content = f.read()
    with open(dst, "w", encoding="utf-8") as f:
        f.write(clean(content))
    print(f"Cleaned {src} -> {dst}")
