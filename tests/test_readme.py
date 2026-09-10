"""Tests for README feature coverage."""

from __future__ import annotations

from pathlib import Path


def test_readme_mentions_new_cli_flags_and_encoding_fallback() -> None:
    readme = Path("README.md").read_text(encoding="utf-8").lower()

    assert "uv run wordfreq readme.md --top 5" in readme
    assert "--min-count" in readme
    assert "default: `1`" in readme
    assert "uv run wordfreq readme.md --stopwords" in readme
    assert "--total" in readme
    assert "default: off" in readme
    assert "uv run wordfreq readme.md --json --top 3" in readme
    assert "falls back to utf-8 with replacement" in readme
    assert "warns on stderr" in readme
