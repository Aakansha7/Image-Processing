import numpy as np
import cv2 as cv

# Read the images
img1 = cv.imread('C:\\VSCode\\Images\\img1.jpg')
img2 = cv.imread('C:\\VSCode\\Images\\img8.jpg')

# Resize the images to the same size
img1_resized = cv.resize(img1, (500, 500))
img2_resized = cv.resize(img2, (500, 500))

# Display the images
cv.imshow("img1", img1_resized)
cv.imshow("img2", img2_resized)

# Blend the images
result = cv.addWeighted(img1_resized, 0.5, img2_resized, 0.5, 0)

# Display the blended image
cv.imshow("result", result)

# Wait for a key press and close the windows
cv.waitKey(0)
cv.destroyAllWindows()
