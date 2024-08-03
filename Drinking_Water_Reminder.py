# Exercise 11

# Write a python program which reminds you of drinking water every hour or two.
# Your program can either beep or send desktop notifications for a specific operating system

import time
from plyer import notification
import win32com.client as win

i=int(input("How Many Times You Want To Run This Program: "))

while (i>0):

    # waiting time
    # Every hour this program nofied to you drink some water.

    time.sleep(3600)
    speaker=win.Dispatch("SAPI.SpVoice")
    notification.notify(
        title = "Drinking Water Remainder",
        message="Here you go and drink some water" ,
        # displaying time
        timeout=5)

    speaker.Speak("Here you go and drink some water")

    i-=1


