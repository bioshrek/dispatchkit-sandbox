"""The command line surface."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from wordfreq.count import count_words


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="wordfreq", description="Count words in a file.")
    parser.add_argument("path", type=Path, help="the file to read")
    args = parser.parse_args(argv)

    try:
        text = args.path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"wordfreq: cannot read {args.path}: {exc}", file=sys.stderr)
        return 2

    for count in count_words(text):
        print(f"{count.total:>7}  {count.word}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
