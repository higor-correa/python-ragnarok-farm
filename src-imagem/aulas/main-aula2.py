# https://docs.opencv.org/4.7.0/d4/dc6/tutorial_py_template_matching.html
import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

haystack_img = cv.imread("screenshot.png", cv.IMREAD_GRAYSCALE)
# needle_img = cv.imread("target-imgs/1702.jpg", cv.IMREAD_GRAYSCALE)
needle_img = cv.imread("target-imgs/test01.png", cv.IMREAD_GRAYSCALE)


result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
# print(result)

# 0.60 eh o necessario para encontrar o outro abaixo
threshold = 0.60
locations = np.where(result >= threshold)
# print(locations)

# basicamente coloca a lista em formato [(x,y), (x,y)]
locations = list(zip(*locations[::-1]))
# print(locations)

if locations:
    print("Found needle.")

    # get dimensions of the image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        cv.rectangle(
            haystack_img,
            top_left,
            bottom_right,
            line_color,
            line_type,
        )

    cv.imshow("Matches", haystack_img)
    cv.waitKey()
else:
    print("Needle not found.")
