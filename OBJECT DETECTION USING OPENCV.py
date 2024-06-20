#OBJECT DETECTION USING OPENCV 

import cv2 # package of AI 
import numpy as np
cap = cv2.VideoCapture(0) 
while True:
    _, frame = cap.read() 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("Frame", frame) 
    key = cv2.waitKey(1)
    if key == 27:
        break

''' HSV --> HUE - we can see the color red,green,blue,yellow and also we can see the gradiation of the color         
          SATURATION - How much quantity of the color we want to have 
          (0- nothing, completely white, opencv - maximux pixel 0-255)
          VALUE - Brightness of the color (0- completely black)'''
#===========          
#Next step is to convert the color format to hsv 
