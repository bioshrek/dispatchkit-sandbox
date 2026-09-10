"""Tests for the command line surface."""

from __future__ import annotations

import json
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


def test_encoding_fallback_counts_file_with_invalid_utf8(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    source = tmp_path / "latin1.txt"
    source.write_bytes(b"caf\xe9 cafe cafe")

    assert main([str(source)]) == 0
    captured = capsys.readouterr()
    assert "2  cafe" in captured.out
    assert "1  caf" in captured.out
    assert "not valid UTF-8" in captured.err


def test_encoding_missing_file_still_reports_oserror(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert main([str(tmp_path / "nope.txt")]) == 2
    assert "cannot read" in capsys.readouterr().err


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


def test_json_prints_machine_readable_counts(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    source = tmp_path / "sample.txt"
    source.write_text("b a a", encoding="utf-8")

    assert main([str(source), "--json"]) == 0
    assert json.loads(capsys.readouterr().out) == [
        {"word": "a", "total": 2},
        {"word": "b", "total": 1},
    ]


def test_json_honours_top_limit(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    source = tmp_path / "sample.txt"
    source.write_text("c b a a", encoding="utf-8")

    assert main([str(source), "--json", "--top", "2"]) == 0
    assert json.loads(capsys.readouterr().out) == [
        {"word": "a", "total": 2},
        {"word": "b", "total": 1},
    ]


def test_json_empty_input_is_empty_array(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    source = tmp_path / "empty.txt"
    source.write_text("", encoding="utf-8")

    assert main([str(source), "--json"]) == 0
    assert json.loads(capsys.readouterr().out) == []
