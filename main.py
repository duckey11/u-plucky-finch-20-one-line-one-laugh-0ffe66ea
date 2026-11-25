#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os

ENTRY = (
    "I hired Marco the magician for my daughter's seventh birthday. "
    "He sawed the cake in half and invoiced me for two birthdays."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
