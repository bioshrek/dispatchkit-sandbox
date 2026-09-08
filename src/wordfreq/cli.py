"""The command line surface."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from wordfreq.count import STOPWORDS, count_words


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="wordfreq", description="Count words in a file.")
    parser.add_argument("path", type=Path, help="the file to read")
    parser.add_argument(
        "--stopwords",
        action="store_true",
        help="filter out common English stopwords (e.g. 'the', 'a', 'is')",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=None,
        help="print only the N most frequent words (default: print all)",
    )
    args = parser.parse_args(argv)

    if args.top is not None and args.top < 0:
        print(f"wordfreq: --top must not be negative, got {args.top}", file=sys.stderr)
        return 2

    try:
        text = args.path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"wordfreq: cannot read {args.path}: {exc}", file=sys.stderr)
        return 2

    stopwords = STOPWORDS if args.stopwords else None
    counts = count_words(text, stopwords=stopwords)
    if args.top is not None:
        counts = counts[: args.top]

    for count in counts:
        print(f"{count.total:>7}  {count.word}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
