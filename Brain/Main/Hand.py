

from Detector import *
import os

def main():
    videoPath = 0

    configPath = os.path.join(r'Brain\Main\Object_Detection_model_data\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
    modelPath = os.path.join(r"C:\Users\AKANSHA\OneDrive\Desktop\MEGAN\Brain\Main\Object_Detection_model_data\frozen_inference_graph.pb")
    classesPath = os.path.join(r"C:\Users\AKANSHA\OneDrive\Desktop\MEGAN\Brain\Main\Object_Detection_model_data\coco.names")

    detector = Detector(videoPath , configPath , modelPath , classesPath)
    detector.onVideo()
if __name__ == "__main__":
    main()
    