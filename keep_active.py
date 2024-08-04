import pyautogui
import time

def move_mouse():
    while True:
        # Get the current position of the mouse
        x, y = pyautogui.position()
        
        # Move the mouse to the right by 1 pixel and back to original position
        pyautogui.moveTo(x + 10, y)
        pyautogui.moveTo(x, y)
        
        # Wait for 5 minutes (300 seconds)
        time.sleep(1)

if __name__ == "__main__":
    move_mouse()