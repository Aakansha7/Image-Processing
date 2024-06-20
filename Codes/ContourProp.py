import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv2.imread("C:\\VSCode\\Images\\img4.jpg")
img = cv2.resize(img, (600, 700))

# Convert to grayscale
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold
ret, thresh = cv2.threshold(img1, 220, 255, cv2.THRESH_BINARY_INV)

# Find contours
cnts, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

area1 = []
for c in cnts:
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        area = cv2.contourArea(c)
        area1.append(area)

        if area < 10000:
            epsilon = 0.01 * cv2.arcLength(c, True)  # Arc length (perimeter) of the contour
            data = cv2.approxPolyDP(c, epsilon, True)

            hull = cv2.convexHull(data)

            x, y, w, h = cv2.boundingRect(hull)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (125, 10, 20), 5)

        # Draw the contour and center of the shape on the image
        cv2.drawContours(img, [c], -1, (50, 100, 50), 2)
        cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(img, "center", (cX - 20, cY - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Plot the images
titles = ["Original Image", "Grayscale Image", "Threshold Image"]
images = [img, img1, thresh]
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
