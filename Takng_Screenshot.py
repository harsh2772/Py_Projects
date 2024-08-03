from mss import mss
from time import sleep
import os

name=input("Enter The Name of Screenshot: ")
name+=".png"

os.chdir("C:/Users/harsh/Desktop/Python_Projects/Screenshots")

with mss() as sct:
    sleep(3)
    sct.shot()


os.rename("monitor-1.png", name)

# Another Way

import pyautogui

ss=pyautogui.screenshot()
ss.save("SS.png")