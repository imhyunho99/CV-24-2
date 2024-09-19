import numpy as np
import cv2 as cv

image8 = cv.imread("read_color.jpg", cv.IMREAD_COLOR)

image16 = np.uint16(image8 * (65535/255))       # 형변환 및 화소 스케일 조정
image32 = np.float32(image8 * (1/255))

print("image8 행렬의 일부\n %s\n"  % image8[10:12, 10:13])
print("image16 행렬의 일부\n %s\n" % image16[10:12, 10:13])
print("image32 행렬의 일부\n %s\n" % image32[10:12, 10:13])

cv.imwrite("write_test_16.tif", image16)
cv.imwrite("write_test_32.tif", image32)

cv.imshow("image16", image16)
cv.imshow("image32", (image32*255).astype("uint8"))
cv.waitKey(0)


