import numpy as np
import cv2 as cv

def detect_color(image):
    square_zone = ((170, 500), (480, 480)) # x;y -> left corner , w;h
    MARGIN = 15
    result = numpy.full([3,3], -1)

    width_one_square = square_zone[1][0] // 3

    for i in range(0,3):
        for j in range(0,3):
            pass
