import cv2

# Load images
img = cv2.imread('C:\VSCode\Images\img0.jpg')
template = cv2.imread('C:\VSCode\Images\img0.jpg')

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# Define threshold and find locations
threshold = 0.8
loc = cv2.threshold(result, threshold, 1, cv2.THRESH_BINARY)[1]

# Draw rectangles around matched areas
matched_points = cv2.findNonZero(loc)
for pt in matched_points:
    cv2.rectangle(img, (pt[0][0], pt[0][1]), (pt[0][0] + template.shape[1], pt[0][1] + template.shape[0]), (0, 255, 0), 2)

# Display result
cv2.imshow('Image', img)
cv2.imshow('Template', template)
cv2.waitKey(0)
cv2.destroyAllWindows()
