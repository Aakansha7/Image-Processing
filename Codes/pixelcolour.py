import cv2
import numpy as np

# Global variable to store clicked points
clicked_points = []

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        bgr_color = img[y, x]  # OpenCV uses BGR ordering
        print(f"Clicked at: ({x}, {y}) - BGR Color: {bgr_color}")

# Load an image
img = cv2.imread('C:\VSCode\Images\Img.jpg')  
if img is None:
    print("Error: Could not open or find the image.")
    exit()

# Create a named window and bind mouse callback
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
