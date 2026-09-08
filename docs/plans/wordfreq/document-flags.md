Four flags landed and the README still documents none of them. Bring it up to
date; this task waits on all four so the surface it describes is final.

- Document `--top`, `--stopwords`, `--json` and the non-UTF-8 fallback, each
  with a short worked example in the existing style.
- Replace the "Why the payload is unfinished on purpose" list: those gaps are
  now closed, and leaving them there would be a lie about the code.
- Keep it a README, not a manual. A few lines per flag.

Add `tests/test_readme.py` asserting the README mentions `--top`, `--stopwords`,
`--json` and the encoding fallback, and make it pass. The acceptance is
`uv run pytest -q -k readme`.

It is a test rather than a shell grep for a reason worth knowing: this task is
`verify = "auto"`, which means the merge is gated on CI being green, so an
acceptance CI does not run gates nothing at all. Writing it as a test puts the
check in the same pipeline that decides the merge.
