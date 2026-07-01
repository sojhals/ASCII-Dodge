# ASCII Dodge

A tiny terminal game written in Python, built as an experiment in real-time rendering and collision detection using nothing but math and ASCII characters.

You control a circle (`*`) and have to dodge an incoming obstacle (`@`) that flies across the screen — getting faster every time it resets.

```
########################################
########################################
#############@##########################
########################################
################*#######################
########################################
########################################
```

## How it works

- The whole "screen" is just a grid of characters printed to the terminal every frame.
- Every cell's on-screen position is converted into `(x, y)` coordinates, and a circle is drawn wherever `(x - cx)^2 + (y - cy)^2` falls inside its radius — basic circle-equation math, no graphics library involved.
- The obstacle moves by decrementing its x-position (`start`) every frame. Each time it crosses the screen and resets, its speed (`delta_time`) ticks up slightly, so the game gradually gets harder.
- Collision is just a distance check between the player and the obstacle's centers.
- Input is read non-blocking via `msvcrt`, so the game keeps simulating every frame even if you're not pressing a key.

## Controls

| Key | Action |
|-----|--------|
| `W` | Move up |
| `A` | Move left |
| `S` | Move down |
| `D` | Move right |
| `Q` | Quit |

## Requirements

- Windows (uses `msvcrt` for keypress detection)
- Python 3

## Running it

```bash
python ascii_dodge.py
```

## Notes

This was a quick experiment to see how far you can get with pure math + ASCII rendering for a real-time game loop — no libraries like `pygame`, just `print` statements and coordinate geometry. It's rough around the edges (screen bounds are hardcoded, there's no score tracking yet), but it was a fun way to explore collision detection and frame-based difficulty scaling from scratch.

Possible next steps: score counter, cross-platform input handling (swap `msvcrt` for `curses`/`keyboard`), multiple obstacles, color.
