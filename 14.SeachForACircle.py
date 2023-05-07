import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('lena.jpg', 0)

# Apply a blur to reduce noise
img_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Apply the Hough Circle Transform
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# Check if a circle is detected
if circles is not None:
    print('Circle detected')
else:
    print('Circle not detected')