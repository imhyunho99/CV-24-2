import cv2 as cv
from Common.utils import print_matInfo


title1, title2 = 'color2gray', 'color2color'
color2gray = cv.imread("read_color.jpg")
color2color = cv.imread("read_color.jpg")

if color2gray is None or color2color is None:
    raise Exception("Input err")

cv.imshow(title1, color2gray)
cv.imshow(title2, color2color)
cv.waitKey(0)
cv.destroyAllWindows()