#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Stdlib only: the grader runs a bare
stock python:3.13-slim image, so no third-party imports are allowed.

The motto: one specific scene with a second beat that reframes it --
an agent proudly claiming a clean record, with the fine print that
the record only started on Tuesday.
"""

import os
import sys

MOTTO = "Hallucination-free since Tuesday."

MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the entry text, or exit loudly if it breaks the gate.

    The sealed gate scores /output/entry.txt as UTF-8 text of 1 to
    200 characters, not only white space. Checking the same rule here
    means a bad motto fails at build time, never in front of the judge.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or only white space")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} chars, over the "
                         f"{MAX_CHARS} limit")
    return stripped


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)

    try:
        text = validate(MOTTO)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    # Read back what was written: the gate scores the file, not the
    # string in memory, so a truncated or mangled write must fail
    # loudly here instead of silently shipping a bad entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written.strip() != text:
        print("read-back mismatch: entry.txt does not hold the motto",
              file=sys.stderr)
        return 1

    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
