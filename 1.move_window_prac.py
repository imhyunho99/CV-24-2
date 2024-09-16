import numpy as np
import cv2 as cv

image = np.zeros((200, 400), np.uint8)
image[:] = 0
image[10:20] = 255
image[30:40] = 124

title1, title2 = 'Position1', 'Position2'

cv.namedWindow(title1, cv.WINDOW_AUTOSIZE)#창 생성
cv.namedWindow(title2)

cv.moveWindow(title1, 150, 150) #창 이동
cv.moveWindow(title2, 400, 50)

cv.imshow(title1, image)
cv.imshow(title2, image)

cv.waitKeyEx(0)
cv.destroyAllWindows()





