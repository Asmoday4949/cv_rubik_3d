#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""face_detection.py: Identify a face of a rubik's cube in an image"""

__author__ = "Lucas Bulloni, Malik Fleury, Bastien Wermeille"
__version__ = "1.0.0"


import math
import cv2 as cv
import numpy as np

from hough import intersection, rhotheta
from color_enum import Color
from collections import Counter


def filter_lines(lines):
    """Keep th greater set of parralel and perpendicular lines

    Return a tuple of list of lines, the parralel and the perpendicular
    """
    angles = []

    def approx_angle_simple(theta):
        deg = theta * 180 / math.pi - 2
        # TODO Improve
        deg = int(deg)
        deg = deg - deg % 2

        return deg

    def approx_angle(theta):
        deg = theta * 180 / math.pi - 2
        # TODO Improve
        deg = int(deg)
        deg = deg - deg % 2

        while deg > 90:
            deg = deg - 90
        while deg < 0:
            deg = deg + 90

        return deg

    for line in lines:
        for _, theta in line:
            angles.append(approx_angle(theta))

    data = Counter(angles)
    get_mode = dict(data)
    mode_angle = [k for k, v in get_mode.items() if v ==
                  max(list(data.values()))]

    def filter_line(line):
        for _, theta in line:
            return approx_angle(theta) == mode_angle[0]

    lines_filter = list(filter(filter_line, lines))

    def filter_pack(line):
        rothetaline = rhotheta(line)
        for _, theta in rothetaline:
            return approx_angle_simple(theta) == mode_angle[0]

    line_pack_one = list(
        filter(lambda line: not filter_pack(line), lines_filter))
    line_pack_two = list(filter(filter_pack, lines_filter))

    return line_pack_one, line_pack_two


def draw_lines_perso(img, lines, color, thickness):
    """ Draw a line in an image
    """
    for line in lines:
        for r, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*r
            y0 = b*r
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            cv.line(img, (x1, y1), (x2, y2), color, thickness)


def resize_img(img, la1, la2, lb1, lb2):
    """ Resize an image given 4 lines
    """
    i1 = intersection(la1, lb1)
    i2 = intersection(la1, lb2)
    i3 = intersection(la2, lb1)
    i4 = intersection(la2, lb2)

    pts1 = np.float32([i1, i2, i3, i4])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

    M = cv.getPerspectiveTransform(pts1, pts2)
    image_resized = cv.warpPerspective(img, M, (300, 300))
    return image_resized


def detect_rubik(img):
    """ Detect lines making 
    """
    # Convert the img to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Apply edge detection method on the image
    edges = cv.Canny(gray, 50, 200, apertureSize=3)

    # This returns an array of r and theta values
    lines = cv.HoughLines(edges, 1, np.pi/180, 50)

    # Return None if no lnes are detected
    if lines is None:
        return None

    seg_one, seg_two = filter_lines(lines)
    if len(seg_one) <= 0 or len(seg_two) <= 0:
        return None

    l1 = min(seg_one, key=lambda l: l[0][0])
    l2 = max(seg_one, key=lambda l: l[0][0])

    l3 = min(seg_two, key=lambda l: l[0][0])
    l4 = max(seg_two, key=lambda l: l[0][0])

    img_resized = resize_img(img.copy(), l1, l2, l3, l4)

    draw_lines_perso(img, seg_one, color=(0, 0, 255), thickness=1)
    draw_lines_perso(img, seg_two, color=(0, 255, 0), thickness=1)

    draw_lines_perso(img, [l1], color=(0, 255, 255), thickness=2)
    draw_lines_perso(img, [l2], color=(0, 255, 255), thickness=2)
    draw_lines_perso(img, [l3], color=(0, 255, 255), thickness=2)
    draw_lines_perso(img, [l4], color=(0, 255, 255), thickness=2)

    cv.imshow("cubix", img_resized)

    return img_resized


def face_detection():
    """Main code for launching a processing detecting a face
    """
    try:
        cap = cv.VideoCapture(0)
    except Exception as e:
        print("error while opening camera")
        raise e

    while True:
        ret, img = cap.read()
        sq = img.copy()

        img_line = detect_rubik(img.copy())
        if not img_line is None:
            cv.imshow("Result", img_line)

        if not img_line is None and img_line.size == 0:
            raise Exception(-1)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cv.waitKey(0)


if __name__ == '__main__':
    face_detection()
