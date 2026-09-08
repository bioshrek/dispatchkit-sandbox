Four flags landed and the README still documents none of them. Bring it up to
date; this task waits on all four so the surface it describes is final.

- Document `--top`, `--stopwords`, `--json` and the non-UTF-8 fallback, each
  with a short worked example in the existing style.
- Replace the "Why the payload is unfinished on purpose" list: those gaps are
  now closed, and leaving them there would be a lie about the code.
- Keep it a README, not a manual. A few lines per flag.

The acceptance greps for `--top`, `--stopwords`, `--json` and `encoding`, and
runs the test suite to make sure the documentation edit did not break anything.
