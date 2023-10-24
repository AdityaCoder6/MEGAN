from AppOpener import open
from AppOpener import close
import keyboard
from Speak import *
from Listen import *
from time import sleep


import pyautogui

def message(Name):
    open('whatsapp')

    ListWeb = {'Aadhya' : "6204418276",
            'papa': "8851586628",
            "didi": '9205449220'}
    
    Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")
    Message = MicExecution()
    Speak(f"Sending{Message} to {Name}")

    Number = ListWeb[Name]


    pyautogui.hotkey("ctrl","f")
    pyautogui.write(Number)
    sleep(2)
    pyautogui.click(x=393, y=220)
    sleep(2)
    # pyautogui.click(x=1376, y=1102)
    pyautogui.write(Message)
    keyboard.press_and_release("enter")

    Speak("Message Sent")
    close("whatsapp")
    sleep(2)

# message("didi")

