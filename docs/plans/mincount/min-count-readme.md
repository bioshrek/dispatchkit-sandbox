The README documents every flag `wordfreq` has. `--min-count` and `--total`
are now two of them and neither is there.

- Add both to the flag list in `README.md`, in the same style as the flags
  already documented: what each does, and what its default is.
- Say how `--min-count` composes with `--top`, because the order matters and a
  reader who guesses wrong will think one of the two is broken.
- Say that `--total` describes the table it follows, not the file, so a reader
  using it with `--stopwords` is not surprised by a smaller number.

`tests/test_readme.py` already asserts that the README documents the flags the
CLI accepts. Extend it so that assertion covers both new flags — the test name
must contain `readme`, which is what the acceptance command selects.
