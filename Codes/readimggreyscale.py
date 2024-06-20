import cv2
 
img = cv2.imread('C:\VSCode\Images\IMAGE.jpeg', cv2.IMREAD_GRAYSCALE)
 
print('Image Dimensions :', img.shape)