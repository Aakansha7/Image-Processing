import cv2

# Reading the image in grayscale mode by setting the flag as 0
img = cv2.imread(r'C:\VSCode\Images\img2.jpg', 0)
(thresh, binary_image) = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY)

# Displaying original grayscale image and binary image
cv2.imshow('Original Image', img)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()