import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    # print(voices)
    engine.setProperty("voices",voices[0].id)
    engine.setProperty("rate",170)
    print("")
    print(f"JARVIS : {Text}")
    print("")
    engine.say(Text)
    engine.runAndWait()

# Speak("Hello Sir")