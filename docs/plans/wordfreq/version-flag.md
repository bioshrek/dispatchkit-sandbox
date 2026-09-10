`wordfreq` has no way to say which version it is. `pyproject.toml` declares
`version = "0.1.0"`, but nothing surfaces it, so a bug report cannot name the
build it came from.

- Add `--version` to the CLI. It prints the version and exits 0, and it does
  so without requiring the `path` argument — a user asking which version they
  have does not have a file in mind.
- Take the number from the installed package metadata
  (`importlib.metadata.version`), not a second literal in the source. Two
  places holding one version number is how they come to disagree.
- Expose it as `wordfreq.__version__` as well, so a caller importing the
  library can read it without shelling out.

Add tests to `tests/test_cli.py` whose names contain `version`: one that the
flag prints the number from the metadata, and one that it works with no path
argument given.
