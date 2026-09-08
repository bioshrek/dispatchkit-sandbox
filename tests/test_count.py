"""Tests for the counting core."""

from __future__ import annotations

from wordfreq.count import STOPWORDS, Count, count_words, tokenise


class TestTokenise:
    def test_it_lowercases(self) -> None:
        assert tokenise("The THE the") == ["the", "the", "the"]

    def test_it_keeps_apostrophes_inside_a_word(self) -> None:
        assert tokenise("don't") == ["don't"]

    def test_punctuation_separates_words(self) -> None:
        assert tokenise("a,b;c") == ["a", "b", "c"]


class TestCountWords:
    def test_the_most_frequent_word_comes_first(self) -> None:
        assert count_words("b a a")[0] == Count(word="a", total=2)

    def test_ties_are_broken_alphabetically_so_output_is_stable(self) -> None:
        assert [item.word for item in count_words("beta alpha")] == ["alpha", "beta"]

    def test_empty_text_counts_nothing(self) -> None:
        assert count_words("") == []

    def test_stopwords_default_off_keeps_the_word_the(self) -> None:
        assert count_words("the the cat")[0] == Count(word="the", total=2)

    def test_stopwords_filters_common_words_when_given(self) -> None:
        assert count_words("the the cat", stopwords=STOPWORDS) == [Count(word="cat", total=1)]

    def test_stopwords_does_not_change_output_when_none_match(self) -> None:
        assert count_words("cat dog", stopwords=STOPWORDS) == count_words("cat dog")
