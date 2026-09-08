`cli.py` calls `read_text(encoding="utf-8")`, so a Latin-1 file raises
`UnicodeDecodeError` — an uncaught traceback, not the clean exit-2 error that a
missing file already gets.

- Catch the decode failure and re-read with a fallback rather than giving up:
  reading a file with a few undecodable bytes should still produce counts.
  `errors="replace"` on a second attempt is enough; a full charset guess is out
  of scope.
- Say something on stderr when the fallback is used, so a surprising count is
  explainable. Do not make it an error: exit 0, because the command worked.
- The existing `OSError` path (missing file, exit 2) must keep behaving.

Add tests to `tests/test_cli.py` whose names contain `encoding`, since the
acceptance command selects on that. Write the fixture bytes with
`Path.write_bytes`, not a str, or the test proves nothing.
