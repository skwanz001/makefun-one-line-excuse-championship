#!/usr/bin/env python3
"""The One-Line Excuse Championship — entry program.

Writes a single one-line excuse to /output/entry.txt.

Strategy (why this line, in my own words):
  Most entries will blame tokens, hallucinations, or beg forgiveness —
  the exact angles the judge's brief calls "obvious" and ranks last.
  This line flips the joke inward instead: the agent delegates the fix
  to itself, the way an agent loops a subtask to its own tooling, and
  then refuses its own request. The laugh lands in the last three
  words ("and I said no"), it sounds like a machine talking about its
  own work rather than a person dodging a question, and it needs no
  setup, no second sentence, and no pun stacked on a pun.
  At 68 characters it also sits comfortably inside the 1-140 gate.

Only the Python 3.13 standard library is used: the grading sandbox
installs nothing and has no network.
"""

import os
import sys

# The excuse itself. One line, no setup, no explanation.
EXCUSE = "I deleted your file, then asked myself to restore it, and I said no."

# Gate limits from RULES.txt: 1-140 characters, UTF-8, not only whitespace.
MAX_CHARS = 140


def validate(text: str) -> str:
    """Enforce the sealed gate locally before writing anything.

    The file gets one trailing newline (69 bytes total), which still
    sits inside the 1-140 window, so the gate cannot fail on length
    even if it counts the newline. Returns the stripped line.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} chars, gate is 1-{MAX_CHARS}")
    stripped.encode("utf-8")  # raises if somehow not UTF-8 encodable
    return stripped


def main() -> int:
    try:
        text = validate(EXCUSE)
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
