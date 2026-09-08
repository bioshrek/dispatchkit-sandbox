`the` wins every count, which makes the output nearly useless. Add opt-in
stopword filtering.

- Add a `--stopwords` flag to `cli.py` and the filtering itself to `count.py`,
  next to the counting it modifies. Keep the two separable: `count_words`
  should take the stopword set as an argument rather than reaching for a
  global, so it stays testable without the CLI.
- Ship a small built-in English list (roughly the usual 25–50: articles,
  pronouns, prepositions, auxiliaries). Put it in `count.py` as a frozenset.
- Filtering happens after tokenising and before counting.
- Off by default. Existing output must not change when the flag is absent.

Add tests to `tests/test_count.py` whose names contain `stopword`, since the
acceptance command selects on that.
