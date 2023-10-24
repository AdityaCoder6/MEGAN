import random 
import json 
import torch 
from AiModel import * 
from NeuralNetwork import *
from time import sleep 
from Listen  import  *
from Speak import *
from Clap import Tester
from Tasks import NonInputExecution
from Tasks import InputExecution
from Tasks import Music
# from LLaMa import Code
import cv2
import pyautogui
from speedtestGui import *

 
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') 
with open(r"C:\Users\AKANSHA\Downloads\MEGAN\Dataset\intents.json", "r") as json_data:
    

    if json_data is not None:
        intents = json.load(json_data) 
    else:
        pass

    
 
FILE = r"C:\Users\AKANSHA\OneDrive\Desktop\MEGAN\TrainData.pth" 
data = torch.load(FILE) 
 
input_size = data["input_size"] 
hidden_size = data["hidden_size"] 
output_size = data["output_size"] 
all_words = data["all_words"] 
tags = data["tags"] 
model_state = data["model_state"] 
 
model = NeuralNet(input_size,hidden_size,output_size).to(device) 
model.load_state_dict(model_state) 
model.eval()



Name = 'Megan'
def Main():

    sentence = MicExecution()
    result = str(sentence)
    if str(sentence).lower() == "bye":
        Bye = [
                "Goodbye! Have a wonderful day!",
                "See you later!",
                "Sleep well and take care!",
                "Take care and goodbye!",
                "Exiting. Have a fantastic day!" ]
        
        Speak(random.choice(Bye))
        exit()
    
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)



    output = model(X)

    _ , predicted = torch.max(output, dim = 1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]


    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent['tag']:
                
                reply=random.choice(intent['responses'])
                
                if "time" in reply:
                    NonInputExecution(reply)
                elif "date" in reply:
                    NonInputExecution(reply)
                elif "What_in_My_Hand" in reply:
                    NonInputExecution(reply)
                elif "day" in reply:
                    NonInputExecution(reply)
                elif "SpeedTest" in reply:
                    NonInputExecution(reply)
                elif "Doubt" in reply:
                    InputExecution(reply,result)
                elif "space news" in reply:
                    NonInputExecution(reply)
                elif "Message" in reply:
                    InputExecution(reply,result)
                elif "google" in reply:
                    InputExecution(reply,result)
                elif "wikipedia" in reply:
                    InputExecution(reply,result)
                elif "YoutubeSearch" in reply:
                    InputExecution(reply,result)
                elif "Music" in reply:
                    Music()
                # elif "" in reply:
                #     Code(result)
                # elif " " in reply:
                #     Code(result)
                else:
                    Speak(reply)

def MEGAN():
    pyautogui.press("esc")
    Speak("Face Verification Successful")
    sleep(2)
    Speak("Welcome Back Aditya Sir")
    Speak("Clap To Start Sir")
    Tester()
    Speak("Hello Sir I AM JARVIS, Your Personal AI Assistant")          
    while True:
        Main()




recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
recognizer.read('Brain\\Main\\Face-Recognition-main\\trainer\\trainer.yml')   #load trained model
cascadePath = "Brain\\Main\\Face-Recognition-main\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


id = 1 #number of persons you want to Recognize


names = ['','Aditya']  #names, leave first empty bcz counter starts from 0


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
cam.set(3, 640) # set video FrameWidht
cam.set(4, 480) # set video FrameHeight

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# flag = True

while True:

    ret, img =cam.read() #read the frames using the above created object

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

    faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match 
        if (accuracy < 100):
            id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            MEGAN()

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup

cam.release()
cv2.destroyAllWindows()









