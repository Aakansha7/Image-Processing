import cv2
import numpy as np

# Read the image from file
image = cv2.imread('C:\VSCode\Images\image10.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error loading image")
else:
    # Draw a green line from (50, 50) to (450, 50) with thickness 2
    cv2.line(image, (50, 50), (450, 50), (0, 255, 0), 2)

    # Draw a red rectangle from (100, 100) to (400, 300) with thickness 2
    cv2.rectangle(image, (100, 100), (400, 300), (0, 0, 255), 2)

    # Draw a blue circle with center at (256, 400) and radius 50 with thickness 2
    cv2.circle(image, (256, 400), 50, (255, 0, 0), 2)

    # Add white text "Hello, OpenCV" at position (50, 450) with font scale 1 and thickness 2
    cv2.putText(image, 'Hello there!', (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the image
    cv2.imshow('Drawing Shapes', image)
    cv2.waitKey(0)  # Wait until a key is pressed
    cv2.destroyAllWindows()  # Close the window
