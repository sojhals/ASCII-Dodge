# ASCII Dodge

A tiny terminal game written in Python, built as an experiment in real-time rendering and collision detection using nothing but math and ASCII characters.

You control a circle (`*`) that can move vertically and resize itself, and you have to dodge an incoming obstacle (`@`) that crosses the screen, getting faster and randomly sized every time it resets.

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
- Every cell's on-screen position is converted into `(x, y)` coordinates, and a circle is drawn wherever `(x - cx)^2 + (y - cy)^2` falls inside its radius, basic circle-equation math, no graphics library involved.
- The obstacle moves by decrementing its x-position (`start`) every frame. Each time it crosses the screen and resets, its speed (`delta_time`) ticks up slightly and its size is re-randomized, so the game gradually gets harder and less predictable.
- Your circle can also grow or shrink in real time. Shrinking gives you a smaller hitbox to slip past obstacles, growing gives you a bigger one, at your own risk.
- Collision is calculated by treating both circles' true radii (derived from their drawn sizes) and checking whether the distance between their centers is smaller than the sum of both radii, i.e. whether the two circles visually overlap.
- Input is read using real-time key state polling (`GetAsyncKeyState`) rather than buffered keypress events, so movement and resizing respond continuously while a key is held down, instead of one step per tap.

## Controls

| Key | Action |
|-----|--------|
| `W` | Move up |
| `S` | Move down |
| `A` | Shrink |
| `D` | Grow |
| `Q` | Quit |

## Requirements

- Windows (uses the Windows API via `ctypes` for key state polling and console input handling)
- Python 3

## Running it

```bash
python ascii_dodge.py
```

## Notes

This was a quick experiment to see how far you can get with pure math and ASCII rendering for a real-time game loop, no libraries like `pygame`, just character grids, coordinate geometry, and circle collision math. It went through a few iterations along the way: fixing floating-point comparisons that broke the obstacle reset and boundary detection, eliminating screen flicker by combining terminal writes into a single call, switching from tap-based to hold-based movement, and tuning the collision formula so the hitbox actually matches what's drawn on screen.

Possible next steps: score persistence, cross-platform input handling (swap the Windows-only key polling for a library like `keyboard` or `pynput`), multiple obstacles, color.
