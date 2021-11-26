import cv2
import numpy as np
import math
import pytesseract

def get_angle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    ang = ang + 360 if ang < 0 else ang
    return (ang - 180) if 180 <= ang else ang

def filter_by_text(polygons, img):
    for polygon in polygons:
        mask = np.zeros(img.shape[:2], np.uint8)
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        og_plate_img = img[topx:bottomx + 1, topy:bottomy + 1]
        text = pytesseract.image_to_string(og_plate_img, config='--psm 13')

        if len(text.strip()) > 1 :
            print('plate found')
            return polygon, text

    return None, ''

def validate_angles(polygon):
    angle1 = get_angle(polygon[0][0],polygon[1][0],polygon[2][0])
    angle2 = get_angle(polygon[1][0],polygon[2][0],polygon[3][0])
    angle3 = get_angle(polygon[2][0],polygon[3][0],polygon[0][0])
    angle4 = get_angle(polygon[3][0],polygon[0][0],polygon[1][0])
    angles = [angle1,angle2,angle3,angle4]

    # validate that each individual angle is reasonable
    for angle in angles:
        if angle < 55 or angle > 125:
            return False

    # Validate total adds to near 360
    angle_sum = sum(angles)
    if angle_sum > 355 and angle_sum < 365:
        return True    
    
    return False

def filter_polygons(contours):
    polygons = []
    for c in contours:

        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.03 * peri, True)

        # Check number of sides
        if len(approx) == 4:
            if validate_angles(approx):
                polygons.append(approx)

    return polygons

def read_text(img):
    img = cv2.resize(img, (600, 400))
    filename = 'tempimg.png'
    cv2.imwrite(filename, img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 12, 20, 20)
    edges = cv2.Canny(gray, 30, 170)

    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    n_top_contours = 30
    print(cv2.contourArea)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:n_top_contours]

    polygons = filter_polygons(contours)

    if polygons is None or len(polygons) == 0 :
        return ""

    corners, text = filter_by_text(polygons,img)
    
    if corners is None or len(corners) == 0:
        return ""

    return text