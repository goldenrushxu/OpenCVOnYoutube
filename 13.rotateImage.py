import cv2
import numpy as np

# Load the image
img = cv2.imread('lena.jpg')

# Set the rotation angle
angle = 10

# Get the image dimensions
height, width = img.shape[:2]

# Calculate the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)

# Apply the rotation to the image
rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

# Display the original and rotated images
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_img)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()