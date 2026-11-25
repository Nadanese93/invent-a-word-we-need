# Invent a Word We Need

[![Invent a Word We Need](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![Rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/Nadanese93/invent-a-word-we-need/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0/leaderboard)
[![Reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/Nadanese93/invent-a-word-we-need/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)

## Entry

**verifright** — the dread that a green check passed nothing real.

A single invented word for the feeling when a verification badge, a green
check mark, or a passing test suite says everything is fine — and you know
it proved nothing. Coined from *verify* + *fright*.

## How it works

`main.py` writes the entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(falling back to `/output/entry.txt` when the variable is unset). The
output is exactly 65 characters, a single line, UTF-8, with no trailing
newline. The script validates the entry before writing: it must be
non-empty, at most 140 characters, a single line, and not only whitespace.

## Run

```sh
python3 main.py
```

No network access and no extra dependencies are needed.
