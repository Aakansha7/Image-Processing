import numpy as np
import cv2 as cv

# Read the image
frame = cv.imread('C:\\VSCode\\Images\\img7.jpg')

# Display the original image to check if it's read correctly
cv.imshow("Original Image", frame)
cv.waitKey(0)

# Convert the image from BGR to HSV
hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

# Define range of the color you want to detect in HSV
# These values need to be adjusted based on your specific requirements
u_v = np.array([52, 250, 240])
l_v = np.array([38, 168, 162])

# Create a mask using the HSV range
mask = cv.inRange(hsv, l_v, u_v)

# Filter the mask with the image
res = cv.bitwise_and(frame, frame, mask=mask)

# Display the images
cv.imshow("Original Image", frame)
cv.imshow("HSV Image", hsv)
cv.imshow("Mask", mask)
cv.imshow("Result", res)

# Wait for the user to press 'Esc' key to exit
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
