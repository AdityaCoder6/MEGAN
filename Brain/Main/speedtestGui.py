from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
from speedtestUi import Ui_MainWindow
import sys
from Speak import *
from time import sleep 

def CS():

    Speak("Checking The Speed Sir Wait For a While")

    def run_uit():
        import speedtest

        speed = speedtest.Speedtest()

        upload = speed.upload()

        correct_Up = int(int(upload)/800000)

        download = speed.download()

        correct_down = int(int(download)/800000)

        Speak(f"Downloading Speed is {correct_down} M B Per Second")
        sleep(1)
        Speak(f"Uploading Speed is {correct_down} M B Per Second")

        exit()


    class MainThread(QThread):

        def __init__(self):

            super(MainThread,self).__init__()

        def run(self):
            run_uit()

    StartExe = MainThread()

    class StartExecution(QMainWindow):
        def __init__(self):

            super().__init__()
            self.ui = Ui_MainWindow()

            self.ui.setupUi(self)
            self.ui.label = QMovie(r"C:\Users\AKANSHA\OneDrive\Desktop\MEGAN\Brain\Main\GUI Material\giphy.gif")
            self.ui.gif.setMovie(self.ui.label)

            self.ui.label.start()
            StartExe.start()

    App = QApplication(sys.argv)
    speedtest = StartExecution()
    speedtest.show()
    exit(App.exec_())

# CS()

    

