import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy
import time

# Setting Dimension of a video
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim=(width,height)


# Set Path And Video Name
path="C:/Users\harsh\Desktop\Python_Projects/Screen Recording/"
path=path.replace("\\","/")
vid=input("Enter Video Name: ")
vid_name=path+vid+".mp4"


# Give the format of a video
f=cv2.VideoWriter_fourcc(*"XVID")

# Set Video Name , format , fps, dimension
output = cv2.VideoWriter(vid_name,f,30,dim)

# Duration of a recording
start_time=time.time()
dur=10+7                    # +7 is a Buffer Time Which is the Running Code.
end_time=start_time+dur

while True:

    image=pyautogui.screenshot()    # Taking Continuously Screenshots
    frame_1=numpy.array(image)      # Merge Frames by using numpy module
    frame_2=cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)     # In this shows the original colour of frame

    output.write(frame_2)       # Write The Freames in your output which will be created in out of the loop.

    current_time=time.time()

    if current_time>end_time:   # For Ending the loop
        break

output.release()                # End The Screen Recording
