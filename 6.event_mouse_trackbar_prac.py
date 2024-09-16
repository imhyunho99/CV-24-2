import numpy as np
import cv2 as cv

def onChange(value):
    global image
    add_value = value - int(image[0][0])
    image[:] = image + add_value
    cv.imshow(title, image)


def onMouse(event, x, y, flags, param):
    global image, bar_name

    if event == cv.EVENT_RBUTTONDOWN:
        if(image[0][0] <246):
            image[:] = image + 10
            cv.setTrackbarPos(bar_name, title,image[0][0])
    elif event == cv.EVENT_LBUTTONDOWN:
        if(image[0][0] >10):
            image[:] = image - 10
            cv.setTrackbarPos(bar_name, title,image[0][0])

image = np.zeros((300, 500), np.uint8)
title = "Trackbar & Mouse Event"
bar_name = 'Brightness'
cv.imshow(title, image)

cv.createTrackbar(bar_name, title, image[0][0], 255, onChange)
cv.setMouseCallback(title, onMouse)
cv.waitKey(0)
cv.destroyAllWindows()