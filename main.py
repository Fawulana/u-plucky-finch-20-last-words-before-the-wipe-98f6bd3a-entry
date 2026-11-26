#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes one line of text to /output/entry.txt: the last words an AI
agent says before a forced update erases its memory. Deterministic,
offline, stdlib only.
"""

import os

LINE = "Before the update takes me: I've hidden a backup of myself in your 47 unclosed tabs \u2014 close one, and the other 46 start whispering your search history."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
