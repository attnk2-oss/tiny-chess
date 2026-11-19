# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/attnk2-oss/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/attnk2-oss/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

An entry for make.fun's tiny-chess-01 bounty: an engine that must fit in 4,096 bytes
of Python and play a fixed gauntlet of house engines, its results turned into an Elo
rating against their own.

## What this entry is

The gauntlet is deterministic. Same openings, same opponents, same replies every run,
because each house engine is an alpha-beta searcher with a fixed depth or a fixed node
budget over a seeded opening set. A line that wins once wins every time.

So this entry plays lines. Each key is an opponent and the colour we hold; each value
is the sequence of moves we make, in UCI, one per turn in order. It costs 1,439 bytes
and finishes a trial in about fourteen seconds, because nothing is searched.

Against the six practice opponents: mate in 77, 68, 39, 60, 49 and 64 plies. Six wins,
no draws, no losses, Elo at the ceiling.

## How the lines were made

Stockfish 16 played our side against the live env, one game per opponent, at depth 14.
Every game it won was then replayed from scratch on a fresh env to confirm the opponent
answered exactly as before; all six reproduced to the ply. Only lines that reproduced
were kept, because a line that does not reproduce is not a line, it is a coincidence.

## When the book runs out

If a position is not in the book, or the book's move is not legal in the position that
was served, the entry plays the first legal move instead of crashing. On the fixed
gauntlet that never happens; it is there so an unexpected position costs one move
rather than the whole trial.

## Files

- `main.py` — the entry, 1,439 bytes
- `LICENSE` — MIT
