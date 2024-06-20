import cv2

# Load images (ensure correct path format)
img1 = cv2.imread(r'C:\VSCode\Images\img2.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r'C:\VSCode\Images\img1.jpg', cv2.IMREAD_GRAYSCALE)

# Check if images are loaded successfully
if img1 is None or img2 is None:
    print("Error: Could not load images.")
else:
    # Initialize ORB detector and detect keypoints/descriptors
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

    # Initialize BFMatcher (Brute-Force Matcher) and match descriptors
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)

    # Draw matches and display results
    img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imshow('Matches', img_matches)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
