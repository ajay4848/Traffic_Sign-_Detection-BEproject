from tkinter import messagebox as ms
import time    
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image 


        
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
cap = cv2.VideoCapture(0)
    
#    id = input('enter user id')
    #id=entry2.get()
    
sampleN=0;
    
while 1:
    
        ret, img = cap.read()
    
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
        for (x,y,w,h) in faces:
    
            sampleN=sampleN+1;
    
            cv2.imwrite("facesData/User."+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
    
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
            cv2.waitKey(100)
    
        cv2.imshow('img',img)
        
        cv2.waitKey(1)
        
        if sampleN > 30:
            break
       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
    #entry2.delete(0,'end')
cv2.destroyAllWindows()
ms.showinfo('Success!', 'Capture Successfully !')