import cv2

# Load the image
img = cv2.imread('C:\VSCode\Images\img8.jpg')

# Flip the image horizontally
flipped_img = cv2.flip(img, 1)

# Save the flipped image
cv2.imwrite('flipped_image.jpg', flipped_img)