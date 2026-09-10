"""The command line surface."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from wordfreq import __version__
from wordfreq.count import STOPWORDS, count_words


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="wordfreq", description="Count words in a file.")
    parser.add_argument("path", nargs="?", type=Path, help="the file to read")
    parser.add_argument(
        "--version",
        action="store_true",
        help="print the installed package version and exit",
    )
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
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit counts as a JSON array",
    )
    args = parser.parse_args(argv)

    if args.version:
        print(__version__)
        return 0

    if args.path is None:
        parser.error("the following arguments are required: path")

    if args.top is not None and args.top < 0:
        print(f"wordfreq: --top must not be negative, got {args.top}", file=sys.stderr)
        return 2

    try:
        text = args.path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(
            f"wordfreq: {args.path} is not valid UTF-8; replacing undecodable bytes",
            file=sys.stderr,
        )
        try:
            text = args.path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            print(f"wordfreq: cannot read {args.path}: {exc}", file=sys.stderr)
            return 2
    except OSError as exc:
        print(f"wordfreq: cannot read {args.path}: {exc}", file=sys.stderr)
        return 2

    stopwords = STOPWORDS if args.stopwords else None
    counts = count_words(text, stopwords=stopwords)
    if args.top is not None:
        counts = counts[: args.top]

    if args.json:
        print(json.dumps([{"word": count.word, "total": count.total} for count in counts]))
        return 0

    for count in counts:
        print(f"{count.total:>7}  {count.word}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
