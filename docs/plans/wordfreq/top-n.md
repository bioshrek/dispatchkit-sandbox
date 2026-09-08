Printing every word is unusable on anything longer than a paragraph. Add a
`--top N` option to `wordfreq` that prints only the N most frequent words.

- The limit belongs in `cli.py`. `count_words` already returns the full list in
  a stable order, and it should keep doing so — slicing is a presentation
  concern, and the JSON task will need the same unsliced list.
- Default to printing everything, so today's behaviour is unchanged when the
  flag is absent.
- `--top 0` should print nothing rather than everything; reject a negative N
  with a non-zero exit and a message on stderr, matching how a missing file is
  already handled.

Add tests to `tests/test_cli.py` whose names contain `top`, since the
acceptance command selects on that.
