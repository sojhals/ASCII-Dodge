import msvcrt
import time
import os
import random

# Initialize Windows console to support ANSI escape sequences
os.system('')
score = 0
# Screen dimensions
width = 40
height = 20

# Initial center coordinates of the circle
cx = 0.0
cy = 0.0

# Movement speed modifier
speed = 2
delta_time = 0.3
print("Use WASD to move the circle. Press 'q' to quit.")
time.sleep(2)
start = 30
size = random.randint(1,3)
ran1 = random.randint(-9,9)
while True:
    # Check for non-blocking user input
    if msvcrt.kbhit():
        # Get the pressed key (lowercase)
        key = msvcrt.getch().decode('utf-8').lower()
        
        # Update center coordinates based on input
        if key == 'w':
            cy += speed    # Move Up
        elif key == 's':
            cy -= speed    # Move Down
        elif key == 'a':
            cx -= speed    # Move Left
        elif key == 'd':
            cx += speed    # Move Right
        elif key == 'q':
            break          # Quit program
    
    # Randomize and change speed
    if start <= -30:
        start = 30
        ran1 = random.randint(-9,9) 
        size = random.randint(1,3)
        if delta_time < 0.8:
            delta_time += 0.1

    # Clear the screen and reset cursor using ANSI escape codes
    # \033[H moves cursor to top-left; \033[J clears down from the cursor
    print("\033[H\033[J", end="")
    # Draw the frame using your mathematical grid logic
    output = []

    # Collision detection
    distance_sq = (cx - start)**2 + (cy-ran1)**2

    if distance_sq < size**2 or cx == 20 or cy == 10 or cx == -20 or cy == -10:
        print("GAME OVER")
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
    print("".join(output), end="", flush=True)

    # Program keeps running un-interrupted (simulation step)
    # Adjust this delay to control frame rate and movement responsiveness
    time.sleep(0.03) 
    start -= delta_time