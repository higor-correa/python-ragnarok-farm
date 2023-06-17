# https://docs.opencv.org/4.7.0/d4/dc6/tutorial_py_template_matching.html
import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

haystack_img = cv.imread("screenshot.png", cv.IMREAD_GRAYSCALE)
# needle_img = cv.imread("target-imgs/1702.jpg", cv.IMREAD_GRAYSCALE)
needle_img = cv.imread("target-imgs/test01.png", cv.IMREAD_GRAYSCALE)
needle_w = needle_img.shape[1]
needle_h = needle_img.shape[0]

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
# print(result)

# 0.60 eh o necessario para encontrar o outro abaixo
threshold = 0.6
locations = np.where(result >= threshold)
# print(locations)

# basicamente coloca a lista em formato [(x,y), (x,y)]
locations = list(zip(*locations[::-1]))
# print(locations)

rectangles = []
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
        """
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)
        """

        center_x = x + int(w / 2)
        center_y = y + int(h / 2)
        cv.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)


    cv.imshow("Matches", haystack_img)
    cv.waitKey()
else:
    print("Needle not found.")
