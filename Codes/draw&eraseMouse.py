import cv2
import numpy as np

# Global variables
drawing = False
mode = True
ix, iy = -1, -1

# Mouse callback function
def draw_and_erase(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        color = (0, 255, 0) if mode else (0, 0, 0)
        thickness = 2 if mode else 20
        cv2.line(img, (ix, iy), (x, y), color, thickness)
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        color = (0, 255, 0) if mode else (0, 0, 0)
        thickness = 2 if mode else 20
        cv2.line(img, (ix, iy), (x, y), color, thickness)

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Create a named window and bind mouse callback function
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_and_erase)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF

    # Toggle drawing/erasing mode on 'm' key press
    if k == ord('m'):
        mode = not mode

    # Clear the image on 'c' key press
    elif k == ord('c'):
        img = np.zeros((512, 512, 3), np.uint8)

    # Exit on 'q' key press
    elif k == ord('q'):
        break

cv2.destroyAllWindows()
