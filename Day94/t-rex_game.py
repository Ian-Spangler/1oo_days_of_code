import pyautogui
from PIL import ImageGrab
import time

JUMP_KEY = "space"

# (left, top, right, bottom)
BOX = (300, 750, 500, 800)

def is_obstacle():   
    image = ImageGrab.grab(BOX)
    gray = image.convert("L")  
    pixels = gray.load()

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if pixels[x, y] < 85:
                return True   
    return False

print("🦖 Bot starting in 3 seconds...")
time.sleep(3)

while True:
    if is_obstacle():
        pyautogui.press(JUMP_KEY)
        time.sleep(0.1)
