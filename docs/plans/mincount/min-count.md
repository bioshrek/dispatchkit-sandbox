A long document produces a very long tail: hundreds of words that appear once.
They push the interesting counts off the screen, and `--top N` is the wrong
tool for the job — it asks "how many rows" when the question is "how often is
often enough".

- Add a `min_count` parameter to `count_words` in `src/wordfreq/count.py`. It
  drops any word whose total is below the threshold, after counting. Default
  it to `1`, which keeps everything and so changes nothing for existing
  callers.
- Add `--min-count N` to the CLI, passing it through. A negative value is an
  error: exit 2 with a message on stderr, the way `--top` already handles one.
- `--min-count` and `--top` compose. Filter by count first, then take the top
  N of what survives — a limit applied before the filter would return fewer
  rows than asked for and look like a bug.

Add tests to `tests/test_count.py` whose names contain `mincount`: one that
the threshold drops words below it and keeps words at it, one that the default
changes nothing, and one that it composes with `--top` in that order.
