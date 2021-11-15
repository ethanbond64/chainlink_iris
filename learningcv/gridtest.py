import cv2
import numpy as np

# image  = cv2.imread("base.png")
# cv2.imshow("Image", image)

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray)

# blur = cv2.GaussianBlur(gray, (5,5), 0)
# cv2.imshow("blur", blur)

# thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
# cv2.imshow("thresh", thresh)

# _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# max_area = 0
# c = 0
# for i in contours:
#         area = cv2.contourArea(i)
#         if area > 1000:
#                 if area > max_area:
#                     max_area = area
#                     best_cnt = i
#                     image = cv2.drawContours(image, contours, c, (0, 255, 0), 3)
#         c+=1

# mask = np.zeros((gray.shape),np.uint8)
# cv2.drawContours(mask,[best_cnt],0,255,-1)
# cv2.drawContours(mask,[best_cnt],0,0,2)
# cv2.imshow("mask", mask)

# out = np.zeros_like(gray)
# out[mask == 255] = gray[mask == 255]
# cv2.imshow("New image", out)

# blur = cv2.GaussianBlur(out, (5,5), 0)
# cv2.imshow("blur1", blur)

# thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
# cv2.imshow("thresh1", thresh)

# _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# c = 0
# for i in contours:
#         area = cv2.contourArea(i)
#         if area > 1000/2:
#             cv2.drawContours(image, contours, c, (0, 255, 0), 3)
#         c+=1


# cv2.imshow("Final Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
img =  cv2.imread('base2.png')
gray = img#cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

# Blur the image
blur = cv2.GaussianBlur(thresh_inv,(1,1),0)

thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

# find contours
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

mask = np.ones(img.shape[:2], dtype="uint8") * 255
for c in contours:
    # get the bounding rect
    x, y, w, h = cv2.boundingRect(c)
    if w*h>1000:
        cv2.rectangle(mask, (x, y), (x+w, y+h), (0, 0, 255), -1)

res_final = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

cv2.imshow("boxes", mask)
cv2.imshow("final image", res_final)
cv2.waitKey(0)
cv2.destroyAllWindows()