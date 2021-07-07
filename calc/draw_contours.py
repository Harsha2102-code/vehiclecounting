import cv2
from time import sleep
import numpy as np

def rectangle():
    vehicle=0
    validvehicles=[]
    def centroid(x, y, w, h):
        x1 = int(w / 2)
        y1 = int(h / 2)
        cx = x + x1
        cy = y + y1
        return cx,cy
    vidCap=cv2.VideoCapture('C:/Users/yamal/Downloads/video.mp4')
    BS_MOG=cv2.bgsegm.createBackgroundSubtractorMOG()
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
        conts,h=cv2.findContours(dilatada,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        cv2.line(frame,(25,550),(1200,550),(0,0,255),2)
        cv2.line(frame,(25,544),(1200,544),(0,255,0),1)#green line below
        cv2.line(frame,(25,556),(1200,556),(0,255,0),1)#green line above
     
        
    #extract contours
        
        for (i,c) in enumerate(conts):
            (x,y,w,h) = cv2.boundingRect(c)
            visiblevehicle=(w>=80) and (h>=80)
            if not visiblevehicle:
                 continue
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)        
            center=centroid(x,y,w,h)
            validvehicles.append(center)
            cv2.circle(frame, center, 4, (0, 0,255),-1)
                
            for (X,Y) in validvehicles:
                if Y<556 and  Y>544:
                        vehicle+=1
                        cv2.line(frame, (25, 550), (1200, 550), (0,0,255), 3)  
                        validvehicles.remove((X,Y))
                            
        
        cv2.putText(frame,'total vehicles:{}'.format(vehicle),(50,50),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),5)
        cv2.imshow("counter" , frame)
        cv2.imshow("dilatada",dilatada)
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()

    vidCap.release()
    