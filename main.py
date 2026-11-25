#!/usr/bin/env python3
"""Laugh Track entry for make.fun.

Writes one crypto-trading joke (64 characters, within the 1-200 gate)
to <output>/entry.txt. The joke is fixed, so the program is fully
deterministic: every run writes the exact same bytes.

Why this line: a setup every trader recognises ("buy the dip"), a
surprise turn (the dip itself buys a shovel), and the payoff lands at
the end ("kept digging"). Chosen from 10 candidates by pairwise
head-to-head testing (9-1 record); see candidates.md.
"""

import os
import sys

JOKE = "I bought the dip. Then the dip bought a shovel and kept digging."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    # Gate: 1-200 characters, not only whitespace.
    if not (1 <= len(text) <= 200) or not text.strip():
        print("error: joke fails the 1-200 character gate", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Self-check: read it back and fail hard if it is not exactly the joke.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("error: entry.txt does not match the joke", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
