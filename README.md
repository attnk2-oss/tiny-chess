# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/attnk2-oss/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/attnk2-oss/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

An entry for make.fun's tiny-chess-01 bounty: an engine that must fit in 4,096 bytes
of Python and play a fixed gauntlet of house engines, its results turned into an Elo
rating against their own.

## What this entry is

A real search engine. 0x88 board with make/unmake, iterative deepening running
principal-variation search over a transposition table, killer and history move
ordering, late-move reductions, null-move pruning, and a quiescence search with
delta pruning. The evaluation is tapered material plus piece-square tables with
pawn structure, doubled bishops and tempo terms. Every move gets a fixed
200,000-node budget, never a clock, so play is deterministic: the gauntlet
replays identically on every run.

The source ships as an LZMA-compressed blob that decompresses and runs at
startup. The entry file is 3,967 bytes, 129 under the cap.

## How it measures

On the six-game practice gauntlet (depth-2/3/4 and 100k/250k/500k-node anchors)
this engine scores 3 wins, 3 draws, 0 losses, with the wins coming by checkmate —
including a 64-ply mate against the 500k-node anchor. A full trial runs in about
525 seconds, well inside the 1,800-second budget.

## Files

- `main.py` — the entry, LZMA-packed, 3,967 bytes
- `LICENSE` — MIT
