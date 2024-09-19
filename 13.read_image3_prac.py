import cv2 as cv
from Common.utils import print_matInfo

title1, title2 = '16bit unchange', '32bit unchange'

color2unchanged1 = cv.imread("read_16.tif", cv.IMREAD_UNCHANGED)
color2unchanged2 = cv.imread("read_32.tif", cv.IMREAD_UNCHANGED)

print("16/32 bit 10,10 화소값")

print(title1, '자료형', type(color2unchanged1[10][10][0]))
print(title1, '화솟값', color2unchanged1[10][10]) #32bit => unit16
print(title2, '자료형', type(color2unchanged2[10][10][0]))
print(title2, '화솟값', color2unchanged2[10][10]) #32bit => float32

cv.imshow(title1, color2unchanged1)
cv.imshow(title2, color2unchanged2)
cv.waitKey(0)
cv.destroyAllWindows()