#!/usr/bin/env python3
"""Entry program for make.fun u-ronigrv-the-one-line-laugh-7ccca46f.

Writes the one funny line to /output/entry.txt. Python 3, stdlib only.
"""
import os

LINE = "My phone died at 2 percent after warning me at 20, 10 and 5 percent, which is the most consistent relationship I have ever had."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1 to 200 characters")
    if LINE.count(".") != 1 or "\n" in LINE:
        raise SystemExit("line must be a single sentence")
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written: the entry must be exactly the line,
    # no trailing newline, nothing added.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()
