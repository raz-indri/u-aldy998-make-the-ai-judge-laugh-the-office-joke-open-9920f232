#!/usr/bin/env python3
"""Office Joke Open entry (program/v1).

Writes a single original one-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Contract (from the bounty brief): one line, at most 200 characters.
The program is fully deterministic: no randomness, no network, no
clock, no environment-dependent output. It exits non-zero if the
entry ever violates the contract, so a bad joke can never be
submitted silently.
"""

import os
import sys

JOKE = (
    "Our office printer broke in March, but the meeting to fix it has "
    "been rescheduled seven times \u2014 at this point the printer is "
    "middle management, and it's outperforming most of them."
)

MAX_CHARS = 200


def main() -> int:
    joke = JOKE.strip()
    if "\n" in joke or "\r" in joke:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(joke) > MAX_CHARS:
        print(
            "error: entry is %d characters, over the %d limit"
            % (len(joke), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; tolerate being handed a
    # full file path instead.
    if out_dir.endswith("entry.txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
