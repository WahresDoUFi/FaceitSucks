import pyautogui
import numpy as np
import time
import keyboard

color_to_find = (255, 85, 0)
search_area = (1480, 455, 1, 400) 
color_area = (1483, 464, 1, 1)
scroll_amount = 400 
scroll_pause_time = 0.1 

def find_and_click_color(color, area):
    screenshot = pyautogui.screenshot(region=area)
    screenshot_np = np.array(screenshot)

    found = False
    active = False
    for y in range(screenshot_np.shape[0]):
        for x in range(screenshot_np.shape[1]):
            r, g, b = screenshot_np[y, x]
            if((r, g, b) == color_to_find):
                if(not active):
                    active = True
                    found = True
                    x = search_area[0]
                    y = search_area[1] + y
                    pyautogui.click(x, y)
                    time.sleep(0.05)
            else:
                active = False
    
    return found

def main():
    screenshot = pyautogui.screenshot(region=color_area)
    print(screenshot.getcolors())
    while True:
        found = find_and_click_color(color_to_find, search_area)
        if not found:
            print("No more pixels found. Exiting...")
            break

        pyautogui.scroll(-scroll_amount)
        time.sleep(scroll_pause_time) 

if __name__ == "__main__":
    print("Press Shift + G to start...")
    keyboard.wait('shift + g') 
    print("Starting execution...")
    main()
