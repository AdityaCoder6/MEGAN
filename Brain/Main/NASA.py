import requests
import os 
from PIL import Image
from Speak import *
import random

Api_Key = "xbMraZQ6n3GScZ94yVW0ACaSanYb3qPsZC3MqgBS"

def NasaNews(Date):

    Speak("extracting the information sir")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params = {"date":str(Date)}

    r = requests.get(Url,params= Params)

    Data = r.json()
    Info = Data["explanation"]

    Title = Data["title"]

    Image_url = Data['url']

    Image_r = requests.get(Image_url)

    FileName = str(Date) + ".jpg"

    with open(FileName,"wb") as f:
        f.write(Image_r.content)

    Path_1 = "C:\\Users\\AKANSHA\\OneDrive\\Desktop\\MEGAN\\" + str(FileName)
    Path_2 = "C:\\Users\\AKANSHA\\OneDrive\\Desktop\\MEGAN\\Brain\\Main\\Space Data\\" + str(FileName)

    os.rename(Path_1,Path_2)
    
    img = Image.open(Path_2)

    img.show()

    Speak(f"Title : {Title} ")
    Speak(f"According to Nasa :{Info} ")



# NasaNews("2020-09-09")