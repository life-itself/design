"""Re-render the page images in examples/print/img/ from the built Wisdom paper PDF.

index.html shows nine pages of the paper as images. When the paper is rebuilt
(typst/build-paper.sh wisdom in pdf-report-publishing), page numbers can shift: before
re-rendering, check each page below is still the part its caption names, and change PAGES
(and the file names in index.html) if not.

Run:  python3 build.py [PDF]     PDF defaults to ../pdf-report-publishing/output/wisdom.pdf
                                 beside the design repo
Needs: pdftoppm (poppler)."""
import pathlib, subprocess, sys
here = pathlib.Path(__file__).resolve().parent
PDF = here.parents[4] / "pdf-report-publishing" / "output" / "wisdom.pdf"
DPI = 110

# (page, name): the cover as JPEG, the rest as PNG
PAGES = [
    (1, "cover"), (2, "title"), (3, "imprint"), (5, "contents"), (8, "body-figure"),
    (12, "chapter-opening"), (13, "body-quotes"), (15, "summary-box"), (40, "back-cover"),
]

def render(pdf, page, name):
    out = here / "img" / f"wisdom-{page:02d}-{name}"
    fmt = ["-jpeg", "-jpegopt", "quality=88"] if name == "cover" else ["-png"]
    subprocess.run(["pdftoppm", "-r", str(DPI), *fmt, "-f", str(page), "-l", str(page), "-singlefile", str(pdf), str(out)], check=True)
    print(out.relative_to(here), f"from page {page}")

if __name__ == "__main__":
    pdf = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else PDF
    if not pdf.exists():
        sys.exit(f"No PDF at {pdf}: build it with typst/build-paper.sh wisdom in pdf-report-publishing, or pass its path")
    for page, name in PAGES:
        render(pdf, page, name)
