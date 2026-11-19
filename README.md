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
ordering, late-move reductions, null-move pruning, reverse futility pruning and
late-move pruning at shallow depth, with a quiescence search using delta pruning.
The evaluation is a full PeSTO tapered eval: midgame and endgame piece-square
tables for all six piece types with Rofchade material values, phase-interpolated,
plus doubled bishops and a tempo term. Draw scores found by repetition or the
fifty-move rule are never stored in the transposition table, so a path that saw
the position as a draw cannot poison a different route to the same position.
Every move gets a fixed 200,000-node budget, never a clock, so play is
deterministic: the gauntlet replays identically on every run. The env HTTP calls
carry a 60-second timeout and the driver idles between the house engine's moves
instead of hot-polling.

The source ships as an LZMA-compressed blob that decompresses and runs at
startup, packed by the kit's own compress command. The entry file is 4,076 bytes,
20 under the cap.

## How it measures

On the six-game practice gauntlet (depth-2/3/4 and 100k/250k/500k-node anchors)
this engine scores 5 wins, 0 draws, 1 loss. All five wins come by checkmate,
against depth-2, depth-3, depth-4 and the 100k and 250k-node anchors; the one
loss is against the 500k-node anchor, by checkmate at ply 137. A full trial runs
in about 740 seconds, well inside the 1,800-second budget, with the slowest
single move at 7.4 seconds against the 10-second per-move limit.

## Files

- `main.py` — the entry, LZMA-packed, 4,076 bytes
- `LICENSE` — MIT
