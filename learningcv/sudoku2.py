import cv2
import numpy as np


def find_cells(img):
    """
    Find the cells of a sudoku grid
    """
    img_area = img.shape[0] * img.shape[1]

    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Array containing the cropped cell image and its position in the grid
    cells = []
    for c in contours:
        area = cv2.contourArea(c)

        # Approximate the contour in order to determine whether the contour is a quadrilateral
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.017 * peri, True)

        # We are looking for a contour of a specific area in relation to the grid size
        # and that is roughly quadrilateral
        # We filter for areas that are too small or too large in relation to the whole image
        if area / img_area > 0.0001 and area / img_area < 0.02 and len(approx) == 4:
            # Using masking, we crop the cell into its own 28 by 28 pixel image
            mask = np.zeros_like(img)
            cv2.drawContours(mask, [c], -1, 255, -1)

            (y, x) = np.where(mask == 255)

            (top_y, top_x) = (np.min(y), np.min(x))
            (bottom_y, bottom_x) = (np.max(y), np.max(x))
            cell = img[top_y : bottom_y + 1, top_x : bottom_x + 1]

            cell = cell.copy()
            cell = cv2.resize(cell, (28, 28))

            # We also find the centroid of the cell in relation
            # to the grid
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cells.append(({"img": cell, "pos": (cX, cY)}))

    return cells

def find_grid(img):
    """
    Find a sudoku grid in an image. Returns a perspective adjusted image of the grid,
    cell information, and the homography matrix used for the perspective warp.
    """

    # Preprocess the image
    img_blur = cv2.blur(img, (3, 3))
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    thresh = cv2.adaptiveThreshold(
        img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 91, 3
    )

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        # Approximate the contour in order to determine whether the contour is a quadrilateral
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.01 * peri, True)

        # We are looking for a contour that is roughly a quadrilateral
        if len(approx) == 4:
            warped, M = four_point_transform(
                thresh,
                np.array([approx[0][0], approx[1][0], approx[2][0], approx[3][0]]),
            )

            cells = find_cells(warped)

            # We can be fairly certain we found a sudoku grid if the grid contains 81 cells
            print(len(cells))
            # if len(cells) == 25:
            return True, warped, M

    return False, None, None


def four_point_transform(img, pts):
    """
    Given an array of four points describing a quadrilateral in an
    image, returns a homography matrix that warps this quadrilateral
    into a top-down view
    """
    # Obtain a consistent order of the points and unpack them
    # individually
    rect = order_points_of_quadrilateral(pts)
    (top_left, top_right, bottom_right, bottom_left) = rect

    # Compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(
        ((bottom_right[0] - bottom_left[0]) ** 2)
        + ((bottom_right[1] - bottom_left[1]) ** 2)
    )
    widthB = np.sqrt(
        ((top_right[0] - top_left[0]) ** 2) + ((top_right[1] - top_left[1]) ** 2)
    )
    max_width = min(int(widthA), int(widthB))

    # Compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    height_a = np.sqrt(
        ((top_right[0] - bottom_right[0]) ** 2)
        + ((top_right[1] - bottom_right[1]) ** 2)
    )
    height_b = np.sqrt(
        ((top_left[0] - bottom_left[0]) ** 2) + ((top_left[1] - bottom_left[1]) ** 2)
    )
    max_height = min(int(height_a), int(height_b))

    # Now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array(
        [
            [10, 10],
            [max_width - 10, 10],
            [max_width - 10, max_height - 10],
            [10, max_height - 10],
        ],
        dtype="float32",
    )

    # Compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(img, M, (max_width + 10, max_height + 10))

    return warped, M

def order_points_of_quadrilateral(pts):
    """
    Given an array of four points describing a quadrilateral,
    sorts them in the following order:
    (top-left, top-right, bottom-right, bottom-left)
    """
    rect = np.zeros((4, 2), dtype="float32")
    # Summing the x and y coordinates of each point to one value,
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # Computing the difference between the x and y value of each point, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


# MAIN

img = cv2.imread('base4.png')
print(type(img))

# Ensure we keep the aspect ratio of the image
ratio = img.shape[0] / img.shape[1]
img = cv2.resize(img, (1100, int(1100 * ratio)))

valid, img_grid, M = find_grid(img)
print(valid)
    # Generate a 2D array representation of the grid present in the image
cells = find_cells(img_grid)
print(len(cells))