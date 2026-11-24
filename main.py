#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a traveler
from the year 1800, using only words a person of that year could have
known, to /output/entry.txt.

Pure standard library, deterministic, no network, no reads outside
this repository. The file holds the sentence exactly, with no trailing
newline.
"""

import os

ENTRY = (
    "Imagine a road that joins every town on earth, along which a letter "
    "you write is read across the sea before its ink dries, and books "
    "beyond counting wait to be read."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    data = ENTRY.encode("utf-8")
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp, "wb") as f:
        f.write(data)
    os.chmod(tmp, 0o644)
    os.replace(tmp, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
