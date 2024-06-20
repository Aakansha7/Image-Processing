import cv2
import numpy as np

# Create a black image
image = np.zeros((512, 512, 3), np.uint8)

# Defining the center and radius of the circle
center_coordinates = (256, 256)
radius = 100

# BGR
color = (0, 255, 0)

thickness = 2

# Draw the circle
cv2.circle(image, center_coordinates, radius, color, thickness)

# Display the image
cv2.imshow('Circle', image)

# Wait until a key is pressed and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
