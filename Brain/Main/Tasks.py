import datetime
from Speak import Speak
from Hand import *
from speedtestGui import *
from Study import *
from Whatsapp import *
import pywhatkit
from LLaMa import *
import webbrowser as web


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Speak(f"The time is {time}")
    
def Date():
    date = datetime.date.today()
    Speak(f"The Date is {date}")

def Day():
    day = datetime.datetime.now().strftime("%A")
    Speak(f"Today is {day}" )

def What_in_My_Hand():
    Speak("Displaying on Screen Sir")
    main()

def SpeedTest():
    CS()

def NonInputExecution(query):

    if "time" in query :
        Time()
    
    elif "date" in query:
        Date()
    
    elif "day" in query:
        Day()
    
    elif "What_in_My_Hand" in query:

        What_in_My_Hand()

    elif "SpeedTest" in query:
        SpeedTest()

    elif "space news" in query :
        Speak("input the date Whom news you want ")
        date = input("Enter The Date")

        from NASA import NasaNews
        NasaNews(date)
    
    


def InputExecution(tag,query):
    if "Doubt" in tag:
        Study(query)

    elif "Message" in tag:
        query = str(query).replace("send ","")
        query = str(query).replace("whatsapp ","")
        query = str(query).replace("message ","")
        query = str(query).replace("to ","")
        query = str(query).replace("Send ","")
        query = str(query).replace("Whatsapp ","")
        query = str(query).replace("Message ","")
        query = str(query).replace("To ","")

        message(query)

    elif "google" in tag:
        query = str(query).replace("google ","")
        query = str(query).replace("search ","")
        pywhatkit.search(query)
    
    elif "wikipedia" in tag:
        name = str(query).replace("who is ","").replace("about ","").replace("wikipedia ","").replace("what is ","")
        import wikipedia
        result = wikipedia.summary(name)
        Speak(result)
    
    
    elif "YoutubeSearch" in tag:
        result = "https://www.youtube.com/results?search_query=" + query
        web.open(result)
        Speak("This is what i found Sir")

        pywhatkit.playonyt(query)
        Speak("Starting the video sir ")
    
    elif "Music" in tag:
        # result = "https://www.youtube.com/results?search_query=" + query
        # web.open(result)
        # Speak("This is what i found Sir")
        Speak("What type of music would you like to listen to?")


        pywhatkit.playonyt(query)
        Speak("Playing Music sir ")
    
def Music():
    Speak("What type of music would you like to listen to?")
    query = MicExecution()
    
    result= str(query)
        

    pywhatkit.playonyt(result)
    Speak("Playing Music sir ")
    
# InputExecution("Doubt","What Is gravity")










