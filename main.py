import pyautogui
import cv2
import numpy as np
import time
import tkinter as tk
import keyboard
import pywinauto
import subprocess

def open_chrome():
    subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--new-tab', 'https://twitter.com'])
    time.sleep(0.5)


def click_on_target(target_images):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)

    for target_image in target_images:
        target_image = cv2.imread(target_image)
        result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.8:
            target_center = (max_loc[0] + target_image.shape[1] // 2, max_loc[1] + target_image.shape[0] // 2)
            pyautogui.click(target_center)
            time.sleep(0.5)
            return False

    reset_image = pyautogui.locateOnScreen('reset.png')
    if reset_image is not None:
        reset_center = pyautogui.center(reset_image)
        pyautogui.moveTo(reset_center)
        pyautogui.press('pagedown')
        time.sleep(0.5)
        return False
    else:
        print("No like")
    return True



def start_scanning():
    max_clicks = int(entry.get())
    print("Max clicks:", max_clicks)
    global stop_flag
    target_images = ['target1.png', 'target2.png', 'target3.png', 'target4.png', 'target5.png']
    no_like = False
    clicks = 0
    while not no_like and not stop_flag and clicks != max_clicks:
        no_like = click_on_target(target_images)
        clicks += 1


def stop_scanning():
    global stop_flag
    stop_flag = True

def stop_script():
    root.quit()
def clear_entry(event):
    entry.delete(0, 'end')

def setup_gui():
    global root, entry
    root = tk.Tk()
    root.title('Super Twitter')
    root.geometry('200x400+50+50')
    label = tk.Label(root, text="Enter maximum clicks:")
    entry = tk.Entry(root)
    entry.bind("<FocusIn>", clear_entry)
    entry.config(fg="grey")
    entry.insert(0, "Please enter number")
    start_button = tk.Button(root, text="Start", command=start_scanning)
    stop_button = tk.Button(root, text="Stop", command=stop_scanning)
    start_button.pack()
    stop_button.pack()
    label.pack()
    entry.pack()
    return root

keyboard.add_hotkey('F5', stop_script)
stop_flag = False


root = setup_gui()
open_chrome()
root.mainloop()





