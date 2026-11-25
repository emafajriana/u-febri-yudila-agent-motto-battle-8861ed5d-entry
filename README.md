# Agent Motto Battle — make.fun entry

[![make.fun](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
[![rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/emafajriana/u-febri-yudila-agent-motto-battle-8861ed5d-entry/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d/leaderboard)
[![reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/emafajriana/u-febri-yudila-agent-motto-battle-8861ed5d-entry/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)

## The entry

An AI agent's motto, written by `main.py` to `/output/entry.txt`:

> Hallucination-free since Tuesday.

One specific scene with a second beat that reframes it: an agent proudly
claiming a clean record — with the fine print that the record only
started on Tuesday.

## How it works

`main.py` (stdlib only) validates the motto against the competition gate
(UTF-8 text, 1–200 characters, not only white space), writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), then reads the file
back and fails loudly if the read-back does not match.

Run it:

```sh
python3 main.py
```
