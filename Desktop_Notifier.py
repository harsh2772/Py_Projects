import time
from plyer import notification
import win32com.client as win

if __name__ == "__main__":

    time.sleep(5)
    speaker=win.Dispatch("SAPI.SpVoice")
    notification.notify(
        title="Hello World",
        message="Time To Code",
        app_icon="C:/Users/harsh/Desktop/Python_Projects/Source Files/Msg.ico",
        # displaying time
        timeout=10
    )
    speaker.Speak("Hello")

# Run Python File in background
# So open cmd and write-> pythonw file_name.py