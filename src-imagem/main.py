import cv2 as cv
import numpy as np

# https://docs.opencv.org/4.7.0/d4/dc6/tutorial_py_template_matching.html

haystack_img = cv.imread("screenshot.png", cv.IMREAD_GRAYSCALE)
needle_img = cv.imread("target-imgs/1702.jpg", cv.IMREAD_GRAYSCALE)
# needle_img = cv.imread("target-imgs/test01.png", cv.IMREAD_GRAYSCALE)


result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

# cv.imshow("Result", result)
# cv.waitKey()

# get the best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print(f"Best match top left position: {max_loc}")
print(f"Best match confidence: {max_val}")

threshold = 0.5
if max_val >= threshold:
    print("Found needle.")

    # get dimensions of the image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(
        haystack_img,
        top_left,
        bottom_right,
        color=(0, 255, 0),
        thickness=2,
        lineType=cv.LINE_4,
    )
    cv.imshow("Result", haystack_img)
    cv.waitKey()
else:
    print("Needle not found.")
