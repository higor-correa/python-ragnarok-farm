# https://docs.opencv.org/4.7.0/d4/dc6/tutorial_py_template_matching.html
import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def getMonsterPositions(
    needle_img_path, haystack_img_path, threshold=0.6, imReadMode = cv.IMREAD_GRAYSCALE, method = cv.TM_CCOEFF_NORMED ,debug_mode=None
):
    haystack_img = cv.imread(haystack_img_path, imReadMode)
    needle_img = cv.imread(needle_img_path, imReadMode)
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    result = cv.matchTemplate(haystack_img, needle_img, method)

    locations = np.where(result >= threshold)

    locations = list(zip(*locations[::-1]))

    rectangles = []
    points = []

    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

    if len(rectangles):
        print("Found needle.")

        # get dimensions of the image

        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        for x, y, w, h in rectangles:
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            center = (center_x, center_y)
            points.append(center)

            if debug_mode == "points":
                cv.drawMarker(haystack_img, center, marker_color, marker_type)
            elif debug_mode == "rectangles":
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                cv.rectangle(
                    haystack_img, top_left, bottom_right, line_color, line_type
                )

        if debug_mode:
            cv.imshow("Matches", haystack_img)
            cv.waitKey()
    else:
        print("Needle not found.")
    
    return points

points = getMonsterPositions("target-imgs/test02.png", 'screenshot.png', debug_mode='points')