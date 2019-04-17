
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
        #return deg - deg % 2

    for line in lines:
        # The below for loop runs till r and theta values  
        # are in the range of the 2d array 

        for r,theta in line:
            angles.append(approx_angle(theta))

    # print(angles)
    data = Counter(angles) 
    get_mode = dict(data) 
    mode_angle = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
    
    # print("Mode angle : "+str(mode_angle))

    def get_theta(line):
        for r, theta in line:
            return theta

    def filter_line(line):
        for r, theta in line:
            return approx_angle(theta) == mode_angle[0]

    lines_filter = list(filter(filter_line,lines))
    # print("length lines filter : "+str(len(lines_filter)))

    def filter_pack(line):
        rothetaline = rhotheta(line)
        for r, theta in rothetaline:
            return approx_angle_simple(theta) == mode_angle[0]

    line_pack_one = list(filter(lambda line:not filter_pack(line), lines_filter))
    line_pack_two = list(filter(filter_pack, lines_filter))
    print(str(len(lines_filter)) + " - " + str(len(line_pack_one)) + " - " + str(len(line_pack_two)))
    if not len(line_pack_one) + len(line_pack_two) == len(lines_filter):
        print("ERROR pack lines")
    # print("length lines filter : "+str(len(lines_filter)))
    
    return lines_filter



from hough import draw_lines, rhotheta

def filter_lines_two(lines):
    angles = []

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
        line_rotheta = rhotheta(line)

        for r,theta in line_rotheta:
            angles.append(approx_angle(theta))

    # print(angles)
    data = Counter(angles) 
    get_mode = dict(data) 
    mode_angle = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
    
    # print("Mode angle : "+str(mode_angle))

    def get_theta(line):
        for r, theta in line:
            return theta

    def filter_line(line):
        rothetaline = rhotheta(line)
        for r, theta in rothetaline:
            return approx_angle(theta) == mode_angle[0]



    lines_filter = list(filter(filter_line,lines))


def detect_lines_two(img):

    img2 = img.copy()

    # Read image 
    # Convert the image to gray-scale
    gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    # Find the edges in the image using canny detector

    edges = cv.Canny(gray, 50, 200)
    # Detect points that form a line
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=10, maxLineGap=250)
    
    lines = filter_lines_two(lines)
    # Draw lines on the image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img2, (x1, y1), (x2, y2), (255, 0, 0), 3)
    # Show result
    cv.imshow("Result Image", img2)



def find_intersects(lines):
    pass

def detect_lines(img):
    # Convert the img to grayscale 
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    # Apply edge detection method on the image 
    edges = cv.Canny(gray,50,200,apertureSize = 3) 
    
    # This returns an array of r and theta values 
    lines = cv.HoughLines(edges,1,np.pi/180, 50)
    
    lines = filter_lines(lines)

    find_intersects(lines)



    if not lines is None:

        # TODO Use this function and find why it doesnt work
        # draw_lines(img, lines)


        # print('Nb lines : '+str(len(lines)))
        for line in lines:
            # The below for loop runs till r and theta values  
            # are in the range of the 2d array 
            for r,theta in line: 
                
                # Stores the value of cos(theta) in a 
                a = np.cos(theta) 
            
                # Stores the value of sin(theta) in b 
                b = np.sin(theta) 
                
                # x0 stores the value rcos(theta) 
                x0 = a*r 
                
                # y0 stores the value rsin(theta) 
                y0 = b*r 
                
                # x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
                x1 = int(x0 + 1000*(-b)) 
                
                # y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
                y1 = int(y0 + 1000*(a)) 
            
                # x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
                x2 = int(x0 - 1000*(-b)) 
                
                # y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
                y2 = int(y0 - 1000*(a)) 
                
                # cv.line draws a line in img from the point(x1,y1) to (x2,y2). 
                # (0,0,255) denotes the colour of the line to be  
                #drawn. In this case, it is red.  
                cv.line(img,(x1,y1), (x2,y2), (0,0,255),2) 
        
        # All the changes made in the input image are finally 
        # written on a new image houghlines.jpg 
        # cv.imshow(f"Lines",img)

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

        # detect_lines_two(img)
        img_line = detect_lines(img)
        cv.imshow("source", img_line)

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