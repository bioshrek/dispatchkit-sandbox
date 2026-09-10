`wordfreq` prints a table of counts and nothing else, so answering "how many
words are in this file at all" means piping the output through `awk`.

- Add `--total` to the CLI. With it, print one extra line after the table
  giving the total number of words counted and the number of distinct words,
  in that order.
- It counts what was actually counted: if `--stopwords` dropped words, they
  are not in the total. The line describes the table above it, not the file.
- Without the flag, nothing changes. Print the line to stdout, after the
  table, so a reader sees it last.

Add tests to `tests/test_cli.py` whose names contain `total`: one that the
line appears with the flag and not without it, and one that it reflects the
filtering `--stopwords` did.
