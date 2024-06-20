import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Define triangle vertices
center = (256, 256)
side_length = 200
height = side_length * np.sqrt(3) / 2
half_side = side_length / 2
triangle_pts = np.array([
    (int(center[0]), int(center[1] - height / 3)),
    (int(center[0] - half_side), int(center[1] + 2 * height / 3)),
    (int(center[0] + half_side), int(center[1] + 2 * height / 3))
], np.int32)

# Draw triangle on image
cv2.polylines(img, [triangle_pts], isClosed=True, color=(0, 255, 0), thickness=2)

# Calculate and display centroid coordinates
centroid = np.mean(triangle_pts, axis=0, dtype=np.int32)
cv2.putText(img, f"Centroid: ({centroid[0]}, {centroid[1]})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Display the image with the triangle and centroid
cv2.imshow('Equilateral Triangle with Centroid', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
