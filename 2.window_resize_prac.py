import numpy as np
import cv2 as cv

image = np.zeros((200, 300), np.uint8) #200,300 으로 처음에 그림
image.fill(255) #나머지 변한건 흰색으로 채울걱

title1, title2 = 'AUTOSIZE', 'NORMAL'

cv.namedWindow(title1, cv.WINDOW_AUTOSIZE) #Auto -> 만들때꺼 그대로 이미지 픽셀
cv.namedWindow(title2, cv.WINDOW_NORMAL) #Normal -> 픽셀 개수도 같이 확장

cv.imshow(title1, image)
cv.imshow(title2, image)

cv.resizeWindow(title1, 400, 300)
cv.resizeWindow(title2, 400, 300)

cv.waitKey(0)
cv.destroyAllWindows()
