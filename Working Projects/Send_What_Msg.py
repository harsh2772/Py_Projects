import pywhatkit
import time
import pyautogui
import keyboard
def send_whatsapp_message(msg: str, phone_numbers: list):
    try:
        for phone_no in phone_numbers:
            pywhatkit.sendwhatmsg_instantly(phone_no=phone_no,message=msg,tab_close=True)

        time.sleep(10)
        pyautogui.click()

        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print(f"Message sent to {phone_no}!”)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    friend_numbers = ["+910315323435”, “+919911573511”, “+919540840568”]
    message="Hey bro, have you com"
    message="Hey bro, have you completed your Python task?"
    send_whatsapp_message(msg=message, phone_numbers=friend_numbers)
