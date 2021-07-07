import cv2
from time import sleep
import numpy as np

def fg():    
    vidCap=cv2.VideoCapture('C:/Users/yamal/Downloads/video.mp4')
    BS_MOG=cv2.createBackgroundSubtractorMOG2()
    delay= 60
    while vidCap.isOpened():
        ret,frame=vidCap.read()
        tempo = float(1/delay)
        sleep(tempo) 
        grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey,(3,3),5)
        MOG2_FGMask=BS_MOG.apply(blur)
        dilat = cv2.dilate( MOG2_FGMask,np.ones((5,5)))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
        dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
        cv2.imshow('MOG2',MOG2_FGMask)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cv2.destroyAllWindows()
    vidCap.release()

    
    