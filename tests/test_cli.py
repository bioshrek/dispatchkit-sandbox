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


def test_top_limits_the_number_of_printed_words(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    source = tmp_path / "sample.txt"
    source.write_text("a a b", encoding="utf-8")

    assert main([str(source), "--top", "1"]) == 0
    out = capsys.readouterr().out
    assert "2  a" in out
    assert "1  b" not in out


def test_top_zero_prints_nothing(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    source = tmp_path / "sample.txt"
    source.write_text("a a b", encoding="utf-8")

    assert main([str(source), "--top", "0"]) == 0
    assert capsys.readouterr().out == ""


def test_top_without_flag_prints_everything(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    source = tmp_path / "sample.txt"
    source.write_text("a a b", encoding="utf-8")

    assert main([str(source)]) == 0
    out = capsys.readouterr().out
    assert "2  a" in out
    assert "1  b" in out


def test_top_negative_is_rejected(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    source = tmp_path / "sample.txt"
    source.write_text("a a b", encoding="utf-8")

    assert main([str(source), "--top", "-1"]) == 2
    assert "--top" in capsys.readouterr().err
