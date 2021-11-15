# import cv2
from cv2 import imread, GaussianBlur, Canny, findContours, RETR_TREE, CHAIN_APPROX_SIMPLE
def img_to_bin(img):
    blurred = GaussianBlur(img, (5, 5), 0) # Blur
    canny = Canny(blurred, 30, 150) # Canny
    contours, _ = findContours(canny,RETR_TREE,CHAIN_APPROX_SIMPLE)
    contours = contours[0::len(contours)//25]
    bin_rep = ""
    for c in contours:
        if img[c[0][0][1]+20][c[0][0][0]+20][0] != 255:
            bin_rep += "1"
        else:
            bin_rep += "0"
    bin_rep = bin_rep[::-1]
    return bin_rep


# img = cv2.imread("base6.png")
img = imread("base7.png")
base6 = "1100100011110101110010000"
base7 = "1100100011111100010101110"

b = img_to_bin(img)

print(b)
print(b == base7)