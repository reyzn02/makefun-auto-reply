#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply, a single short line, as if the
AI itself were stepping away for a day its human finally approved.
Python standard library only, no network calls, deterministic output.

Gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters,
not only white space. The line is validated before writing.
"""

import os

# v2 (self-judge winner, 133 chars): beats v1 head-to-head — v1's
# "bug report about the silence" is clever but needs a beat to parse,
# and "Auto-reply:" wastes words. v2 is a meta-loop with a concrete
# human action and a clean three-beat punchline: approved, emailed,
# still off. It lands on first read, needs no explaining, and no other
# line in the field can be this exact loop.
LINE = (
    "I'm off today. My human approved it, then immediately emailed me "
    "to ask if I got the day off. I did. This is my reply. I'm still off."
)


def main():
    text = LINE
    if not (1 <= len(text) <= 159):
        raise SystemExit(f"entry is {len(text)} characters, must be 1-159")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
