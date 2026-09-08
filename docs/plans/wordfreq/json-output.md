The current output is aligned columns, which nothing downstream can consume.
Add `--json`.

- Emit a JSON array of objects, one per word, in the same order the text output
  uses: `[{"word": "a", "total": 2}]`. An array, not an object keyed by word,
  because order is meaningful here and JSON objects do not promise it.
- It must honour `--top N`, which is why this task waits on that one. Apply the
  same limit to the same list; do not re-implement the slice.
- Print nothing else on stdout in this mode — no header, no summary. Anything
  extra makes the output unparseable, which defeats the flag.
- An empty input is `[]`, not an empty string.

Add tests to `tests/test_cli.py` whose names contain `json`, and assert by
`json.loads`-ing the captured stdout rather than by string matching.
