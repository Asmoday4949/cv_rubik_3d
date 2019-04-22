
# Python 2/3 compatibility
from __future__ import print_function
import sys
PY3 = sys.version_info[0] == 3


import numpy as np
import cv2 as cv
from color_enum import Color

if PY3:
    xrange = range

def detect_face(img):
    # Pretraitement
    # Suppression du bruit
    img = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)

    # Transformation en niveau de gris
    imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,thresh = cv.threshold(imgray,127,255,0)

    #im2, contours, hierarchy = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv.findContours(imgray, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    img_clone = img.copy()
    cv.drawContours(img_clone, contours, -1, (0,255,0), 2)
    cv.imshow(f"Contours",img_clone)

    cv.waitKey(0)
    # cv.boundingRect(conts)

    # Clean noise
    
    # Improve contrast
    
    # Find square

    # Take biggest one

    # Check if it's a valid image

    # Extract square



#!/usr/bin/env python

'''
Simple "Square Detector" program.
Loads several images sequentially and tries to find squares in each image.
'''

def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_squares(img):
    img = cv.GaussianBlur(img, (5, 5), 0)
    squares = []
    for gray in cv.split(img):
        for thrs in xrange(0, 255, 26):
            if thrs == 0:
                bin = cv.Canny(gray, 0, 50, apertureSize=5)
                bin = cv.dilate(bin, None)
            else:
                _retval, bin = cv.threshold(gray, thrs, 255, cv.THRESH_BINARY)
            contours, _hierarchy = cv.findContours(bin, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                cnt_len = cv.arcLength(cnt, True)
                cnt = cv.approxPolyDP(cnt, 0.02*cnt_len, True)
                if len(cnt) == 4 and cv.contourArea(cnt) > 1000 and cv.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                    if max_cos < 0.1:
                        squares.append(cnt)
    return squares

def main():
    from glob import glob
    for fn in glob('img/0*.jpg'):
        img = cv.imread(fn)
        squares = find_squares(img)
        cv.drawContours( img, squares, -1, (0, 255, 0), 3 )
        cv.imshow('squares', img)
        ch = cv.waitKey()
        if ch == 27:
            break

    print('Done')

import math
from collections import Counter 
from hough import segment_angle_linspace

def filter_lines(lines):

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
        for r,theta in line:
            angles.append(approx_angle(theta))

    data = Counter(angles) 
    get_mode = dict(data)
    mode_angle = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
    
    print("Mode angle : "+str(mode_angle))

    def get_theta(line):
        for r, theta in line:
            return theta

    def filter_line(line):
        for r, theta in line:
            return approx_angle(theta) == mode_angle[0]

    lines_filter = list(filter(filter_line,lines))

    def filter_pack(line):
        rothetaline = rhotheta(line)
        for r, theta in rothetaline:
            return approx_angle_simple(theta) == mode_angle[0]

    line_pack_one = list(filter(lambda line:not filter_pack(line), lines_filter))
    line_pack_two = list(filter(filter_pack, lines_filter))
    
    return line_pack_one, line_pack_two


from hough import draw_lines, rhotheta

def draw_lines_perso(img, lines, color, thickness):
    for line in lines:
        for r,theta in line: 
            a = np.cos(theta) 
            b = np.sin(theta) 
            x0 = a*r 
            y0 = b*r 
            x1 = int(x0 + 1000*(-b)) 
            y1 = int(y0 + 1000*(a)) 
            x2 = int(x0 - 1000*(-b)) 
            y2 = int(y0 - 1000*(a)) 
            cv.line(img,(x1,y1), (x2,y2), color, thickness) 

def find_intersects(pack_one, pack_two, img):
    def filter_pack(lines):
        lines_filtered = []
        for i in range(0, len(lines)-1):
            append = True
            for j in range(i+1, len(lines)):
                line_one = lines[i]    
                line_two = lines[j]
                dist = line_one[0][0] - line_two[0][0]
                append = append and abs(dist) > 2
            if append:
                lines_filtered.append(lines[i])
        return lines_filtered

    distances_one = []
    distances_two = []
    distances = []

    pack_one = filter_pack(pack_one)
    pack_two = filter_pack(pack_two)

    draw_lines_perso(img, pack_one, color=(0,0,255), thickness=1)
    draw_lines_perso(img, pack_two, color=(0,255,0), thickness=1)
    cv.imshow("FILTER 2", img)

    for i in range(0, len(pack_one)-1):
        for j in range(i+1, len(pack_one)):
            line_one = pack_one[i]    
            line_two = pack_one[j]
            dist = line_one[0][0] - line_two[0][0]
            distances.append(abs(dist))
            distances_one.append(abs(dist))
    
    for i in range(0, len(pack_two)-1):
        for j in range(i+1, len(pack_two)):
            line_one = pack_two[i]    
            line_two = pack_two[j]
            dist = line_one[0][0] - line_two[0][0]
            distances.append(abs(dist))
            distances_two.append(abs(dist))
    
    data = Counter(distances)
    print(data)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    print(mode)
    
    data = Counter(distances_one)
    print(data)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    print(mode)

    data = Counter(distances_two)
    print(data)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    print(mode)


from hough import intersection
def detect_lines(img):
    # Convert the img to grayscale 
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    # Apply edge detection method on the image 
    edges = cv.Canny(gray,50,200,apertureSize = 3) 
    

    # canny to find the edges
    #canny = cv2.Canny(nonoise, 0, 10)
    canny = cv.Canny(gray.copy(), 3, 150)
    
    # dwalton
    # dilate the image to make the edge lines thicker
    kernel = np.ones((5, 5), np.uint8)
    cv.imshow("Canny other", canny)
    dilated = cv.dilate(canny, kernel, iterations=2)
    
    cv.imshow("Canny delated", dilated)

    try:
        (_, contours, hierarchy) = cv.findContours(dilated.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    except ValueError:
        (contours, hierarchy) = cv.findContours(dilated.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    con_img = img.copy()
    cv.drawContours(con_img, contours, -1, (0,255,0), 3)
    
    cv.imshow("Contours", con_img)

    poly_img = img.copy()
    for con in contours:
        epsilon = 0.1*cv.arcLength(con,True)
        approx = cv.approxPolyDP(con,epsilon,True, 4)
        cv.drawContours(poly_img, [approx], -1, (0, 0, 255), 3)
    cv.imshow("poly dp", poly_img)

    
    # This returns an array of r and theta values 
    lines = cv.HoughLines(edges,1,np.pi/180, 50)
    
    seg_one, seg_two = filter_lines(lines)


    l1 = min(seg_one, key=lambda l:l[0][0])
    l2 = max(seg_one, key=lambda l:l[0][0])
    
    l3 = min(seg_two, key=lambda l:l[0][0])
    l4 = max(seg_two, key=lambda l:l[0][0])


    find_intersects(seg_one, seg_two, img.copy())

    draw_lines_perso(img, seg_one, color=(0,0,255), thickness=1)
    draw_lines_perso(img, seg_two, color=(0,255,0), thickness=1)

    draw_lines_perso(img, [l1], color=(0,255,255), thickness=2)
    draw_lines_perso(img, [l2], color=(0,255,255), thickness=2)
    draw_lines_perso(img, [l3], color=(0,255,255), thickness=2)
    draw_lines_perso(img, [l4], color=(0,255,255), thickness=2)

    i1 = intersection(l1,l3)
    i2 = intersection(l1,l4)
    i3 = intersection(l2,l3)
    i4 = intersection(l2,l4)
    
    pts1 = np.float32([i1,i2,i3,i4])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

    M = cv.getPerspectiveTransform(pts1,pts2)
    dst = cv.warpPerspective(img,M,(300,300))
    cv.imshow("cubix", dst)

    return img

if __name__ == '__main__':
    # detect_face(cv.imread('img/01.jpg'))
    #lines(cv.imread('img/01.jpg'))

    try:
        cap = cv.VideoCapture(0)
    except Exception as e:
        print("error while opening camera")
        raise e

    while True:
        ret, img = cap.read()
        sq = img.copy()

        # detect_lines_two(img)
        img_line = detect_lines(img)
        cv.imshow("source", img_line)

        squares = find_squares(sq)
        cv.drawContours(sq, squares, -1, (0, 255, 0), 3 )
        cv.imshow('squares', sq)

        if img_line.size == 0:
            raise Exception(-1)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cv.waitKey(0)

# if __name__ == '__main__':
#     img = cv.imread('img/01.jpg', cv.IMREAD_COLOR)
    
#     #print(img.shape)
#     cv.imshow(f"source", img)
    
#     print(detect_face(img))
    
#     cv.waitKey(0)
#     cv.destroyAllWindows()