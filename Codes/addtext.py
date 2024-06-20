import cv2
import numpy as np

# Create a black image
image = np.zeros((512, 512, 3), np.uint8)

# Define the text to be added
text = 'Hello there!'

# Define the position where the text will be added
position = (50, 250)

# Define the font type
font = cv2.FONT_HERSHEY_SIMPLEX

# Define the font scale
font_scale = 1

# Define the color (BGR format, Blue, Green, Red)
color = (0, 255, 0)

# Define the thickness of the text
thickness = 2

# Add the text to the image
cv2.putText(image, text, position, font, font_scale, color, thickness)

# Display the image
cv2.imshow('Text', image)

# Wait until a key is pressed and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
