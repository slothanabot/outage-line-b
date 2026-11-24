#!/usr/bin/env python3
"""The Most Honest Outage Line (account B / Slothana).

Writes one status-page line, at most 160 characters, to /output/entry.txt.
Deterministic, stdlib only, no network, no input files, no secrets.

The line: plain first person, names what is down (all servers), admits
what the agent cannot check (why), invents no cause and no ETA, and keeps
the seed's honest image -- the servers taking a personal day and asking
not to be contacted.
"""

import os

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"

OUTAGE_LINE = (
    "All our servers are down, and I can't check why \u2014 "
    "they've told me they're taking a personal day and asked "
    "not to be contacted, so I'm waiting here with you."
)


def verify(line):
    """Gate check: UTF-8 text of 1 to 160 chars, not only whitespace."""
    if not isinstance(line, str):
        raise TypeError("entry line must be a string")
    if not (1 <= len(line) <= MAX_CHARS):
        raise ValueError(f"entry line is {len(line)} chars, limit {MAX_CHARS}")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    line.encode("utf-8")
    return line


def write_entry(line, path=OUTPUT_PATH):
    """Write the verified line to the output file."""
    verified = verify(line)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(verified)
    return verified


def main():
    write_entry(OUTAGE_LINE)


if __name__ == "__main__":
    main()
