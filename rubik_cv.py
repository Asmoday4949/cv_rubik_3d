import numpy as np
import cv2 as cv

from detect_color import detect_color
from reconstruct import reconstruct
from face_detection import detect_lines
# from tiny_gl_engine.open_gl_app import OpenGLApp

def detect_faces(square_zone = None):

    faces = []
    faces_in = set()

    try:
        cap = cv.VideoCapture(0)
    except Exception as e:
        print("error while opening camera")
        raise e

    while len(faces_in) < 6:
        ret, img = cap.read()


        img = detect_lines(img)

        if square_zone == None and not img is None:
            square_zone = [[0,0], img.shape[0]]
        
        print(faces)

        can_detect_color = False

        if not img is None and can_detect_color:
            face = detect_color(img, square_zone)

            if face != None:
                middle = face[1][1]

                if middle not in faces_in and middle != None:
                    faces_in.add(middle)
                    faces.append(face)
                    print("New face detected", middle)

            cv.imshow("source", img)

            if img.size == 0:
                raise Exception(-1)
        if cv.waitKey(1):
            print(0xFF)
            if 0xFF == ord('q'):
                break
            elif 0xFF == ord('d'):
                print('hello2')
                can_detect_color = True

    return faces


def rubik_cv():
    faces = detect_faces()
    cube = reconstruct(faces)

    print(faces)
    print(cube)

    # gl_app = OpenGLApp()
    # gl_app.run()

if __name__ == '__main__':
    rubik_cv()
