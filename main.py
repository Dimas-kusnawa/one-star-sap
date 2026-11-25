#!/usr/bin/env python3
"""One Star, Written in Sap — a one-line 1-star review by a houseplant.

Writes the review to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Stdlib only, deterministic, no network.
"""

import os

# The review, in the plant's own voice:
# - the grievance: three years in one pot, no drainage, roots drowned;
# - the owner's blame: the roots get called "needy" for drowning;
# - the sting: the pothos got a name, this plant got a sticky note.
# One line, one star, 178 characters (limit 1-279).
LINE = (
    "One star. Three years in the same pot with no drainage, "
    "and when my roots drowned he called them 'needy'. "
    "The pothos next door got a name; "
    "I got a sticky note that says 'plant?'."
)


def main() -> None:
    # Deterministic: same line, same bytes, every run.
    # No trailing newline: the gate counts characters, so write exactly LINE.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
