import cv2
import numpy
import pyautogui
import tkinter as tk

def start_scanning():
    target_image = cv2.imread("target.png")
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2GRAY)
    screenshot = cv2.resize(screenshot, (target_image.shape[1], target_image.shape[0]))
    result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    pyautogui.click(max_loc[0] + target_image.shape[1] // 2, max_loc[1] + target_image.shape[0] // 2)
    window.after(1000, start_scanning)


