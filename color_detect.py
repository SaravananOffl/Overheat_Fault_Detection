import cv2
import numpy as np

img = cv2.imread('bg.jpg')

img  = cv2.resize(img,(0,0),fx=0.2 , fy = 0.2)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

Lower_range = np.array([24,100,100], dtype=np.uint8)

Higher_range = np.array([44,255,255], dtype=np.uint8)


mask = cv2.inRange(hsv, Lower_range,Higher_range)

cv2.imshow('mask',mask)

cv2.imshow('image', img)

while(1):
    k=cv2.waitKey(0)
    if(k == 27):
        break

cv2.destroyAllWindows()
