import cv2

img = cv2.imread('lena.jpg',1)

img = cv2.line(img, (0,0),(255,255),(255,0,0),5)    #color is in [[BGR]] format

cv2.imshow('image',img)

cv2.waitKey(0)      #keep the image window for a certain time, in ms, 0 means keep shouwing until manually close it.
cv2.destroyAllWindows()