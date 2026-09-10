"""Tests for README feature coverage."""

from __future__ import annotations

from pathlib import Path


def test_readme_mentions_new_cli_flags_and_encoding_fallback() -> None:
    readme = Path("README.md").read_text(encoding="utf-8").lower()

    assert "--top" in readme
    assert "--stopwords" in readme
    assert "--json" in readme
    assert "not valid utf-8" in readme
