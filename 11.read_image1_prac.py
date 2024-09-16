import cv2 as cv
path1 = 'matplot.jpg'
path2 = 'read_color.jpg'
path3 = 'read_gray.jpg'
path4 = 'read_16.tif'
path5 = 'read_32.tif'

def print_MatInfo(name, image):
    if image.dtype == 'unit8':
        mat_type = 'CV_8U'
    elif image.dtype == 'int8':
        mat_type = 'CV_8I'
    elif image.dtype == 'unit':
        mat_type = 'CV_8I'
    elif image.dtype == 'int8':
        mat_type = 'CV_8I'
    elif image.dtype == 'int8':
        mat_type = 'CV_8I'
    elif image.dtype == 'int8':
        mat_type = 'CV_8I'
cv.imshow(title1, gray2gray)
cv.imshow(title2, gray2color)
cv.waitKey(0)
cv.destroyAllWindows()