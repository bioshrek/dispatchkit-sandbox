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

Use `--stopwords` to drop common words like `the` so domain words surface first:

```sh
uv run wordfreq README.md --stopwords
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
