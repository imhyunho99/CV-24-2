import numpy as np
import cv2 as cv

def onMouse(event, x, y , flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 버튼 누르기")
    elif event == cv.EVENT_LBUTTONUP:
        print("마우스 왼쪽 버튼 뗴기")
    elif event == cv.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")

image = np.full((200,200), 255, np.uint8)

title1, title2 = "Mouse Event1", "Mouse Event2"
cv.imshow(title1, image)
cv.imshow(title2, image)

cv.setMouseCallback(title1, onMouse)
cv.waitKey(0)
cv.destroyAllWindows()