from tkinter import *
import pyautogui

def take_ss():
    add_data=entry.get()
    path=add_data+"\\test.png"
    # Path:- C:/Users/harsh/Desktop/Python_Projects/Screenshots
    print(path)
    ss=pyautogui.screenshot()
    ss.save(path)

win=Tk()
win.title("Take Screenshot")
win.geometry("700x400")
win.config(bg="white")
win.resizable(False, False)

entry=Entry(win, font=("Time New Roman", 30))
entry.place(x=20, height=70 , width= 660,y=50)

button=Button(win,text="Done", font=("Times New Roman", 50), command=take_ss)
button.place(x=250, height=100 , width= 200,y=140)

win.mainloop()

# Make a application
# So open cmd and write:- pyinstaller --onefile file_name.py