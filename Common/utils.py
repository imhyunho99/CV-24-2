import cv2 as cv
import numpy as np

def print_matInfo(name, image):
    if image.dtype == 'unit8':
        mat_type = 'CV_8U'
    elif image.dtype == 'int8':
        mat_type = 'CV_8S'
    elif image.dtype == 'unit16':
        mat_type = 'CV_16U'
    elif image.dtype == 'int16':
        mat_type = 'CV_16S'
    elif image.dtype == 'float32':
        mat_type = 'CV_32F'
    elif image.dtype == 'float':
        mat_type = 'CV_64F'
    nchannel = 3 if image.ndim == 3 else 1

    print("%12s: depth(%s), Channels(%s)->mat_type(%sC%d)"%(name, image.dtype, nchannel,mat_type,nchannel))
