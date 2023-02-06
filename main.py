import random
import time
import pyautogui
import keyboard

while True:
    
    x = random.randint(0, pyautogui.size().width)
    y = random.randint(0, pyautogui.size().height)
    pyautogui.moveTo(x, y, duration=0.25)
    last_mouse_position = pyautogui.position()
    time.sleep(1)
    # print(last_mouse_position)
    # print(pyautogui.position())
    if keyboard.is_pressed("space") or pyautogui.position() != last_mouse_position:
        break
    else:
        continue
