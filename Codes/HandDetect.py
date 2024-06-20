import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img_path = "C:\VSCode\Images\Hand.png"
img = cv2.imread(img_path)

# Check if the image was loaded successfully
if img is None:
    print(f"Error: Unable to load image at {img_path}")
    exit()

# Resize the image for consistency
img = cv2.resize(img, (600, 700))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to get a binary image
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Dilate the image to fill in gaps
dilated = cv2.dilate(thresh, None, iterations=6)

# Find contours
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Process each contour
for contour in contours:
    # Approximate the contour
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # Get the convex hull of the contour
    hull = cv2.convexHull(approx)
    
    # Draw contours and convex hull
    cv2.drawContours(img, [contour], -1, (50, 50, 150), 2)
    cv2.drawContours(img, [hull], -1, (0, 255, 0), 2)

    # Find the convexity defects
    hull_indices = cv2.convexHull(contour, returnPoints=False)
    defects = cv2.convexityDefects(contour, hull_indices)

    # Draw convexity defects if any
    if defects is not None:
        for i in range(defects.shape[0]):
            s, e, f, _ = defects[i, 0]
            far = tuple(contour[f][0])
            cv2.circle(img, far, 5, [0, 0, 255], -1)

    # Get extreme points of the contour
    extLeft = tuple(contour[contour[:, :, 0].argmin()][0])
    extRight = tuple(contour[contour[:, :, 0].argmax()][0])
    extTop = tuple(contour[contour[:, :, 1].argmin()][0])
    extBot = tuple(contour[contour[:, :, 1].argmax()][0])

    # Draw extreme points
    cv2.circle(img, extLeft, 8, (255, 0, 255), -1)  # Pink
    cv2.circle(img, extRight, 8, (0, 125, 255), -1) # Brown
    cv2.circle(img, extTop, 8, (255, 10, 0), -1)    # Blue
    cv2.circle(img, extBot, 8, (19, 152, 152), -1)  # Green

# Display the results using matplotlib
titles = ["Processed Image", "Grayscale", "Threshold"]
images = [img, gray, thresh]
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

cv2.destroyAllWindows()
