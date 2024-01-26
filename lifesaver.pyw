import time
import os
os.system("pip install keyboard")
time.sleep(1)
import keyboard

alt_press_count = 0 # track the alt press counts

def on_alt_pressed(e):
    global alt_press_count
    if e.name == 'alt':
        alt_press_count += 1

        # Check if Alt key is pressed we can modify the below integer to make it work on multiple presses
        if alt_press_count == 2:
            print("Alt key pressed. Killing the program.")
            # Replace 'msedge.exe' with the name of the program you want to kill
            os.system("taskkill /f /im msedge.exe")

            # Reset the Alt press count for future presses
            alt_press_count = 0


# Register the Alt key press event you can change the key here.
keyboard.on_press_key('alt', on_alt_pressed)

# Keep the script running
keyboard.wait('esc')  # You can change 'esc' to any other key to exit the script

# Unregister the key press event when done
keyboard.unhook_all()
