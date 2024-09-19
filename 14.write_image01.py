import cv2 as cv
image = cv.imread("read_color.jpg", cv.IMREAD_COLOR)


params_jpg = (cv.IMWRITE_JPEG_QUALITY, 10)        # JPEG 화질 설정
params_png = [cv.IMWRITE_PNG_COMPRESSION, 9]       # PNG 압축 레벨 설정
## 행렬을 영상 파일로 저장


cv.imwrite("write_test1.jpg", image)       # 디폴트는 95
cv.imwrite("write_test2.jpg", image, params_jpg) # 지정 화질로 저장 (저화질)
cv.imwrite("write_test3.png", image, params_png)
cv.imwrite("write_test4.bmp", image)         # BMP 파일로 저장
print("저장 완료")


