#not completed yet, learnt until the link below
#
#https://www.youtube.com/watch?v=a7_dBO3EAng

import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)


def click_event(event, x, y, flags, param):
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     print(x, ", ", y)
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     strXY = str(x) + ", " + str(y)
    #     cv2.putText(img, strXY, (x, y), font, 0.5, (255,0,0), 1)
    #     cv2.imshow('image',img)
    # if event == cv2.EVENT_RBUTTONDOWN:
    #     blue = img[y, x, 0]     #getting the blue value of (x,y)
    #     green = img[y, x, 1]    #get the green value of (x,y) 
    #     red = img[y, x, 2]      #get the red value of (x,y)
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     strXY = str(blue) + ", " + str(green) + ", " + str(red)
    #     cv2.putText(img, strXY, (x, y), font, 0.5, (255,255,0), 1)
    #     cv2.imshow('image',img)

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
        point.append([x, y])

        if len(point) >= 2:
            cv2.line(img, point[-1], point[-2], (0, 0, 255), 1)

        cv2.imshow('image',img)

img = np.zeros((512, 512, 3),np.uint8)        #create a black back ground
# img = cv2.imread('lena.jpg',1)                  #read a image as back ground

cv2.imshow('image',img)

point = []
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)

cv2.destroyAllWindows()