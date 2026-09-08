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

## Why the payload is unfinished on purpose

The gaps below are the backlog the scheduler dispatches. Each one is a genuine chore that
produces a genuine diff and takes genuine CI time.

- No `--top N` limit; it prints every word.
- No stopword filtering, so `the` wins every time.
- No `--json` output, so nothing downstream can consume it.
- `read_text` has no encoding fallback, so it raises on a non-UTF-8 file.
