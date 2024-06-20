import cv2
import numpy as np

# Create a black image
image = np.zeros((512, 512, 3), np.uint8)

# Define the start and end points of the line
start_point = (50, 50)
end_point = (450, 450)

# Define the color (BGR format, Blue, Green, Red)
color = (0, 255, 0)

# Define the thickness of the line (2 px)
thickness = 2

# Draw the line
cv2.line(image, start_point, end_point, color, thickness)

# Display the image
cv2.imshow('Line', image)

# Wait until a key is pressed and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
