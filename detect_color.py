#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""detect_color.py: Detect the 9 colors of a rubik's cube from a picture"""

__author__ = "Lucas Bulloni, Malik Fleury, Bastien Wermeille"
__version__ = "1.0.0"

import numpy as np
import cv2 as cv

from color_enum import Color


def detect_color(image, square_zone):
    """
    main function, detect color at the zone defined

    zone : [top left corner, width]
    """
    MARGIN = 20
    result = np.full([3, 3], -1)
    width_one_square = square_zone[1] // 3  # width of one subsquare
    sub_zone = [square_zone[0].copy(), width_one_square]
    result = []

    for i in range(0, 3):
        sub_zone[0][0] = square_zone[0][0]
        result.append([])

        for j in range(0, 3):
            start_width = sub_zone[0][1] + MARGIN
            end_width = sub_zone[0][1] + sub_zone[1] - MARGIN

            start_height = sub_zone[0][0] + MARGIN
            end_height = sub_zone[0][0] + sub_zone[1] - MARGIN

            # image of a single color
            subimage = image[start_width:end_width, start_height:end_height]

            bgr_mean, deviation = get_bgr_value_subimage(subimage, np.mean)
            #bgr_mean, deviation = get_bgr_value_subimage(subimage, np.median)

            color = decide_color(bgr_mean)

            result[i].append(decide_color(bgr_mean))

            # For debug, display every sub images
            # cv.imshow(f"{i}:{j}", subimage)
            sub_zone[0][0] += width_one_square

        sub_zone[0][0] = square_zone[0][0]
        sub_zone[0][1] += width_one_square
    print(result)

    return result


def draw_square(image, zone):
    """
    draw a square at the zone scanned
    """
    color = (0, 0, 0)
    pt1 = tuple(zone[0])
    pt2 = (zone[0][0] + zone[1], zone[0][1] + zone[1])

    cv.rectangle(image, pt2, pt1, color, 2)


def decide_color(bgr_value):
    """
    decide which color corresponding to a bgr_value
    """
    hsv_value = np.squeeze(np.asarray(cv.cvtColor(
        np.uint8([[bgr_value]]), cv.COLOR_BGR2HSV)))

    if bgr_value.mean() > 150 and np.std(bgr_value) < 40:
        return Color.WHITE
    elif hsv_value[0] > 90 and hsv_value[0] < 120:
        return Color.BLUE
    elif hsv_value[0] < 90 and hsv_value[0] > 60:
        return Color.GREEN
    elif hsv_value[0] < 30 and hsv_value[0] > 10 and bgr_value[1] > 50:
        return Color.YELLOW
    # elif hsv_value[0] < 190 and hsv_value[0] > 160: # test 2
    elif hsv_value[0] < 190 and bgr_value[1] < 48:
        return Color.RED
    elif hsv_value[0] < 15 and bgr_value[1] > 48:
        return Color.ORANGE

    return None


def get_bgr_value_subimage(subimage, math_func):
    """
    get the color of the subimage
    subimage : image
    math_fund : mathematical function to compute this color in bgr
    """
    bgr_mean = np.empty((3,))
    deviation = 0

    for i in range(0, 3):
        bgr_mean[i] = math_func(subimage[:, :, i])

    grayscale = cv.cvtColor(subimage, cv.COLOR_RGB2GRAY)
    deviation = np.std(grayscale)

    return bgr_mean, deviation
