#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes the GPS's excuse for the scenic detour past the goats to /output/entry.txt,
one line, at most 199 characters, no trailing newline.
"""

import os

ENTRY = "I didn't get you lost. I gave you a scenic detour past a wedding, a lake, and three very confused goats. You're welcome."


def main():
    line = ENTRY.strip()
    if not 1 <= len(line) <= 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
