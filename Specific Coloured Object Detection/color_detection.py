import cv2
import numpy as np
from PIL import Image
import os



""" Setting Limits for input value """

def get_limits(color):
     bgr_value = np.uint8([[color]]) #insert the bgr value to convert it in to the hsv value
     hsv_color = cv2.cvtColor(bgr_value,cv2.COLOR_BGR2HSV)

     lower_limit = hsv_color[0][0][0] - 10,100,100
     upper_limit = hsv_color[0][0][0] + 10,255,255

     lower_limit = np.array(lower_limit, dtype=np.uint8)
     upper_limit = np.array(upper_limit, dtype=np.uint8)

     return  lower_limit, upper_limit


""" Change the yellow color to required color
 and the input shoud be in RGB colorspace """

yellow = [0,255,255] # Yellow in RGB colorspace
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit , upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsv_image,lowerLimit , upperLimit )
    mask_ = Image.fromarray(mask) # Converting to numpy array
    bbox = mask_.getbbox()
    masked_image = cv2.bitwise_and(frame, hsv_image, mask=mask)


    if bbox is not None:
        x1,y1,x2,y2 =bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2), (0,255,0), 5)


    # Display the color mask
    cv2.imshow("HSV Mask", masked_image)
    #cv2.imshow('Mask', mask)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()