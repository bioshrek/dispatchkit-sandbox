# dispatchkit-sandbox

A **disposable** repository. It exists to give
[`dispatchkit`](https://github.com/bioshrek/dispatchkit) a live target: real issues, a real
Project board, a real coding agent and real CI, in a place where a misbehaving first run costs
nothing. Delete it whenever.

The payload is `wordfreq`, a deliberately small word-frequency CLI. It is real code with real
tests and real CI, because dispatchkit's design rules out no-op tasks: a task that cannot fail
proves nothing about the pipeline that dispatched it.

```sh
uv run wordfreq README.md
```

## `wordfreq` at a glance

Use `--top` to keep output short when you only need the most frequent words:

```sh
uv run wordfreq README.md --top 5
```

Use `--min-count` to hide words that do not occur often enough (default: `1`). It is
applied before `--top`, so `--top` selects the most frequent words from the remaining
words:

```sh
uv run wordfreq README.md --min-count 3 --top 5
```

Use `--stopwords` to drop common words like `the` so domain words surface first:

```sh
uv run wordfreq README.md --stopwords
```

Use `--total` to print the total and distinct counts after the table (default: off).
The total describes that table after its filters, not the whole file, so
`--stopwords --total` can report fewer words than the file contains:

```sh
uv run wordfreq README.md --stopwords --total
```

Use `--json` for machine-readable output that can be piped to other tools:

```sh
uv run wordfreq README.md --json --top 3
```

If a file is not valid UTF-8, `wordfreq` falls back to UTF-8 with replacement, warns on stderr,
and still returns counts:

```sh
uv run wordfreq docs/latin1-sample.txt
```
