import cv2
import numpy as np

# Create a black image
image = np.zeros((512, 512, 3), np.uint8)

# Define the top-left and bottom-right corners of the rectangle
top_left_corner = (100, 100)
bottom_right_corner = (400, 400)

# Define the color (BGR format, Blue, Green, Red)
color = (0, 0, 255)

# Define the thickness of the rectangle border (2 px)
thickness = 2

# Draw the rectangle
cv2.rectangle(image, top_left_corner, bottom_right_corner, color, thickness)

# Display the image
cv2.imshow('Rectangle', image)

# Wait until a key is pressed and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
