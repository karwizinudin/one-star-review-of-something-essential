#!/usr/bin/env python3
"""One-star review of something essential: oxygen.

Writes a single deadpan one-star review, at most 160 characters,
of an everyday essential everyone relies on, to /output/entry.txt.
"""

import os

REVIEW = (
    "Oxygen is invisible, flavourless, and somehow the one thing "
    "I cannot live without. Worst monopoly I have ever been forced "
    "to support."
)

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 160
# characters, not only white space, on a single line. Refuse to write
# anything that would fail it.
MAX_CHARS = 160


def validate(text):
    if not text or not text.strip():
        raise ValueError("review must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "review is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    validate(REVIEW)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
