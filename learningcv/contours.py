import cv2
import numpy as np
from imutils import contours as cnts
# Define square size
min_square_size = 987
# Read Image
img = cv2.imread('base6.png')
# Threshold and find edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Threshold the image - segment white background from post it notes
_, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV);
# Find the contours
contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


# Create a list for post-it images
images = []
# Iterate through the contours in the image
print(len(contours))


(contours, _) = cnts.sort_contours(contours, method="top-to-bottom")

bins = ""
for contour in contours:
    area = cv2.contourArea(contour)
    # If the contour is not really small, or really big
    h,w = img.shape[0], img.shape[1]
    if area > min_square_size and area < h*w-(2*(h+w)):
        # Get the four corners of the contour
        epsilon = .1 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        # Draw the point
        # print(approx.shape)
        for point in approx: cv2.circle(img, tuple(point[0]), 2, (255,0,0), 2)
        # Warp it to a square
        pts1 = np.float32(approx)
        pts2 = np.float32([[0,0],[300,0],[300,300],[0,300]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(img,M,(300,300))
        print(dst[10][10][0])
        bins += str(int(dst[10][10][0] == 255))
        # Add the square to the list of images
        images.append(dst.copy())
# print(len(images))
print(bins)
print("1100100011101010001010111")
# Show the complete image with dots on the corners
cv2.imshow('img', img)
# cv2.imwrite('/home/stephen/Desktop/corners.png', img)
cv2.waitKey()

# # Write the images to the desktop
# idx = 0
# for image in images:
#     # cv2.imwrite('/home/stephen/Desktop/'+str(idx)+'.png', image)
#     # print(img[20][20])
#     cv2.imshow('img', image)
#     cv2.waitKey()
    # idx += 1
# cv2.destroyAllWindows()