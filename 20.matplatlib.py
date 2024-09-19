import cv2 as cv
import matplotlib.pyplot as plt

image  = cv.imread("matplot.jpg", cv.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")

rows, cols = image.shape[:2]
rgb_img = cv.cvtColor(image,cv.COLOR_BGR2RGB)
gray_img = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

fig = plt.figure(num=1, figsize=(3,4))
plt.imshow(image ), plt.title('figure1- original(bgr)')
plt.axis('off'), plt.tight_layout()

fig = plt.figure(num=2, figsize=(6,4))
plt.suptitle( 'figure2- pyplot image display')
plt.subplot(1,2,1), plt.imshow(rgb_img)
plt.axis([0,cols, rows,0]), plt.title('rgb color')
plt.subplot(1,2,2), plt.imshow(gray_img, cmap='gray')
plt.title('gray_img2')
plt.show()