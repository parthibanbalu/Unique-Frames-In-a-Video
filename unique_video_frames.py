#importing the libraries

import cv2 
import os 
import shutil
import numpy as np
  
# Read the video from specified path 
cam = cv2.VideoCapture("C:\\Users\\pbalu\\Downloads\\task\\Timelapse_Welland_Canal_Bow_Forward_Far.mp4") 

try: 
      
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 


def getFrame(sec):
    cam.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = cam.read()
    if hasFrames:
        cv2.imwrite("./data/frame "+str(sec)+" sec.jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 3.0
success = getFrame(sec)
while success:
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
  

  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
cv2.destroyAllWindows() 