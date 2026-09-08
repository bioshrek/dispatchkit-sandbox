"""Counting words, kept separate from how they are printed."""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

_WORD = re.compile(r"[a-z0-9']+")


@dataclass(frozen=True, slots=True)
class Count:
    word: str
    total: int


def tokenise(text: str) -> list[str]:
    """Lowercase words. Apostrophes are kept, so `don't` is one word."""
    return _WORD.findall(text.lower())


def count_words(text: str) -> list[Count]:
    """Counts, most frequent first, ties broken alphabetically so it is stable."""
    counter = Counter(tokenise(text))
    ordered = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    return [Count(word=word, total=total) for word, total in ordered]
