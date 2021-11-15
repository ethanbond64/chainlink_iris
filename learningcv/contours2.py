import cv2
import numpy as np
from imutils import contours as cnts

img = cv2.imread("base6.png")

cv2.imshow('Original Image',img)
cv2.waitKey()

blurred = cv2.GaussianBlur(img, (5, 5), 0) # Blur

canny = cv2.Canny(blurred, 30, 150) # Canny
cv2.imshow('new image', canny)
cv2.waitKey()

contours, _ = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0::4]
print('Cs')
print(img.shape)
bin_rep = ""

# max_height = np.max(c[::, 3])
# nearest = max_height * 1.4

# contours.sort(key=lambda r: [int(nearest * round(float(r[1]) / nearest)), r[0]])

# contours = cnts.sort_contours(contours, method="top-to-bottom")[0]
print(len(contours))
for c in contours:
    # print(c)
    print(img[c[0][0][0]+20][c[0][0][1]+20],img[c[0][0][0]+20][c[0][0][1]+20][0] != 255)
    img = cv2.circle(img, (c[0][0][0]+20,c[0][0][1]+20), 5, (0, 0, 255), 2)
    if img[c[0][0][0]+20][c[0][0][1]+20][0] != 255:
        bin_rep += "1"
    else:
        bin_rep += "0"
    cv2.imshow('Original Im',img)
    cv2.waitKey()  

bin_rep = bin_rep[::-1]
print(bin_rep)
print(bin_rep == "1100100011110101110010000")
    # print(img[c[0]])
cv2.imshow('Original Im',img)
cv2.waitKey()  
# print(len(contours))
# print(len(contours[0]))
# print(len(contours[0][0]))
# print(contours[0])
# print(contours[1])

# Draw contours on canny (this connects the contours
cv2.drawContours(canny, contours, -1, 255, 2)
thresh = 255 - canny

h, w = thresh.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
# Floodfill from point (0, 0)
cv2.floodFill(thresh, mask, (0,0), 123);

cv2.imshow('new image', thresh)
cv2.waitKey()
