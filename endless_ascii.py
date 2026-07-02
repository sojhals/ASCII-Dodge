import ctypes
import time
import sys
import os
import random

# Initialize Windows console to support ANSI escape sequences
os.system('')
score = 0
# Screen dimensions
width = 40
height = 20
score = 0

# Initial center coordinates of the circle
cx = 0.0
cy = 0.0

# Movement speed modifier
speed = 2
delta_time = 0.3
def key_down(key):
    # Returns True if the key is currently being held
    return ctypes.windll.user32.GetAsyncKeyState(ord(key)) & 0x8000 != 0
def flush_input():
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-10)  # STD_INPUT_HANDLE
    kernel32.FlushConsoleInputBuffer(handle)
print("Use WASD to move the circle. Press 'q' to quit.")
time.sleep(2)
start = 30
size = 1
ran1 = random.randint(-9,9)
while True:
    # Check held keys every frame instead of waiting for a keypress event
    if key_down('W'):
        cy += speed * delta_time    
    if key_down('S'):
        cy -= speed * delta_time 
    if key_down('A'):
        cx -= speed * delta_time
    if key_down('D'):
        cx += speed * delta_time 
    if key_down('Q'):
        break
    
    # Randomize and change speed
    if start <= -30:
        start = 30
        ran1 = random.randint(-9,9) 
        score += 1
        if delta_time < 1:
            delta_time += 0.1
        if size < 6:
            size += 1
    # Clear the screen and reset cursor using ANSI escape codes
    # \033[H moves cursor to top-left; \033[J clears down from the cursor
    sys.stdout.write("\033[H")
    # Draw the frame using your mathematical grid logic
    output = []

    # Collision detection
    distance_sq = (cx - start)**2 + (cy-ran1)**2

    if distance_sq < size**2 or cx >= 20 or cy >= 12 or cx <= -20 or cy <= -12:
        sys.stdout.write("\033[H\033[0J")
        sys.stdout.write("GAME OVER\n")
        sys.stdout.flush()
        sys.stdout.write("Score:")
        sys.stdout.write(str(score))
        flush_input()
        check = True
        break

    for row in range(height):
        y = ((height - 1) / 2 - row)

        for col in range(width):
            x = (col - (width - 1) / 2) / 2
            # Player
            if (x - cx)**2 + (y - cy)**2 < size+1:
                output.append("*")
            # Obstacle
            elif (x - start)**2 + (y-ran1)**2 < size:
                output.append("@")
            # Background
            else:
                output.append("#")

        output.append("\n")   
        
    # Print the entire frame at once to reduce screen flicker
    sys.stdout.write("\033[H\033[0J" + "".join(output))
    sys.stdout.flush()

    # Program keeps running un-interrupted (simulation step)
    # Adjust this delay to control frame rate and movement responsiveness
    time.sleep(0.016) 
    start -= delta_time
