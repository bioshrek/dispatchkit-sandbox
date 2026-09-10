"""A small word-frequency CLI."""

from importlib.metadata import version

from wordfreq.count import Count, count_words, tokenise

__version__ = version("wordfreq")

__all__ = ["Count", "__version__", "count_words", "tokenise"]
