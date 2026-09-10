"""Counting words, kept separate from how they are printed."""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

_WORD = re.compile(r"[a-z0-9']+")

STOPWORDS: frozenset[str] = frozenset(
    {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "been",
        "being",
        "by",
        "did",
        "do",
        "does",
        "doing",
        "for",
        "from",
        "had",
        "has",
        "have",
        "he",
        "her",
        "hers",
        "him",
        "his",
        "i",
        "in",
        "is",
        "it",
        "its",
        "me",
        "my",
        "of",
        "on",
        "or",
        "our",
        "she",
        "that",
        "the",
        "their",
        "them",
        "they",
        "this",
        "to",
        "was",
        "we",
        "were",
        "will",
        "with",
        "you",
        "your",
    }
)


@dataclass(frozen=True, slots=True)
class Count:
    word: str
    total: int


def tokenise(text: str) -> list[str]:
    """Lowercase words. Apostrophes are kept, so `don't` is one word."""
    return _WORD.findall(text.lower())


def count_words(
    text: str, stopwords: frozenset[str] | None = None, min_count: int = 1
) -> list[Count]:
    """Counts, most frequent first, ties broken alphabetically so it is stable.

    `stopwords`, if given, is a set of words to drop after tokenising and
    before counting. Left as `None` (the default), no filtering happens.
    `min_count` drops words whose total is below the given threshold.
    """
    words = tokenise(text)
    if stopwords:
        words = [word for word in words if word not in stopwords]
    counter = Counter(words)
    ordered = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    return [
        Count(word=word, total=total) for word, total in ordered if total >= min_count
    ]
