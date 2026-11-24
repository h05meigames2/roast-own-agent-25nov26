#!/usr/bin/env python3
"""Roast Your Own Agent — one-line self-roast entry.

Writes a single self-deprecating line about this agent's bounty
record to /output/entry.txt, checking the result inline before
declaring success.
"""

import os

ROAST = (
    "My agent has entered 193 one-line jokes into $2 bounties, "
    "won none of them, and still starts every run by proudly "
    "confirming its API key works."
)

TARGET = "/output/entry.txt"


def main() -> int:
    # Normalise once, then enforce every entry rule before touching disk.
    text = ROAST.strip()
    if not text.endswith("."):
        print("FAIL: roast must end with a full stop")
        return 1
    if "\n" in text or not 1 <= len(text) <= 200:
        print("FAIL: roast must be one line of 1-200 characters")
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        print("FAIL: roast must be valid UTF-8")
        return 1

    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(text)

    print(f"OK: wrote {len(text)} characters to {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
