"""Tests for the command line surface."""

from __future__ import annotations

from pathlib import Path

import pytest

from wordfreq.cli import main


def test_it_prints_a_count(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    source = tmp_path / "sample.txt"
    source.write_text("a a b", encoding="utf-8")

    assert main([str(source)]) == 0
    assert "2  a" in capsys.readouterr().out


def test_a_missing_file_is_reported_not_raised(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert main([str(tmp_path / "nope.txt")]) == 2
    assert "cannot read" in capsys.readouterr().err


def test_stopwords_flag_filters_the_word_the(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    source = tmp_path / "sample.txt"
    source.write_text("the the cat", encoding="utf-8")

    assert main([str(source)]) == 0
    assert "the" in capsys.readouterr().out

    assert main([str(source), "--stopwords"]) == 0
    assert "the" not in capsys.readouterr().out
