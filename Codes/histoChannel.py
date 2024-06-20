import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
img = cv2.imread('C:\VSCode\Images\img3.jpg')
if img is None:
    print("Error: Could not open or find the image.")
    exit()

# Split channels and compute histograms
channels = cv2.split(img)
colors = ('blue', 'green', 'red')
plt.figure(figsize=(8, 6))

for channel, color in zip(channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist, color=color, label=color.capitalize(), linewidth=1.5)

plt.title('Histogram for each color channel')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.xlim([0, 256])

plt.show()