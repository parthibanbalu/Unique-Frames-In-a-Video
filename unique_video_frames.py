#Importing the Libraries
from skimage.measure import compare_ssim
import cv2
import os


try: 
    try:  
        if not os.path.exists('data'):  #create a new directory to save images
            os.makedirs('data') 
    except OSError: 
        print ('Error: Creating directory of data') 
    vidcap = cv2.VideoCapture("C://Users//pbalu//Videos//Timelapse_Welland_Canal_Bow_Forward_Far.mp4")
    success, image = vidcap.read()
    count = 0
    c = 0
    i1 = c
    i2 = c+1
    success = True
    while success:
        success,image = vidcap.read()
        if success == True:
            print('Read a new frame: ' + str(success) + ' : ' + str(count))
            cv2.imwrite("./data/frame "+str(count)+" .jpg", image)
            count+=1
        else:
            print('End of reading frames')
    while (True):
        imageA = cv2.imread("./data/frame " + str(i1) +" .jpg", cv2.IMREAD_COLOR)
        imageB = cv2.imread("./data/frame "+str(i2)+" .jpg", cv2.IMREAD_COLOR)
        resized_orig = cv2.resize(imageA, (300,200))    
        resized_mod = cv2.resize(imageB, (300,200))
        gray_orig = cv2.cvtColor(resized_orig, cv2.COLOR_BGR2GRAY)
        gray_mod = cv2.cvtColor(resized_mod, cv2.COLOR_BGR2GRAY)
        (score, diff) = compare_ssim(resized_orig, resized_mod, full = True, multichannel = True )
        if (score > 0.6): #score values can be selected based on video and it can be obtained by calculating the accuracy
            i3 = i2
            i2+=1
            os.remove("./data/frame "+str(i3) +" .jpg") # if they are similar enough, delete one of them
        else:
            i1 = i2
            i2+=1
        count-=1
except Exception as e: # displays an error message instead of closing the program
  print(e)
  input('Press ENTER to exit: ')

        
        
        
            
