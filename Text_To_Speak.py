import win32com.client

speaker=win32com.client.Dispatch("SAPI.SpVoice")

while True:

    s=input("Enter Which You Want to speak by the PC: ")

    if(s=="q"):
        speaker.Speak("Quiting The Program")
        break

    speaker.Speak(s)