
import cv2
img = cv2.imread('lena.jpg', 0)   #flag 1:color image, 0: grayscale mode, -1: load unchanged including alpha channel

cv2.imshow('image', img)           #show a image
k = cv2.waitKey(0) & 0xFF          #keep the image window for a certain time, in ms, 0 means keep shouwing until manually close it.

if k == 27:
    cv2.destroyAllWindows()         #kill all the displayed windows
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()         #kill all the displayed windows