import numpy as np
import cv2 as cv

from detect_color import detect_faces
from reconstruct import reconstruct
from tiny_gl_engine.open_gl_app import OpenGLApp

def rubik_cv():
    square_zone = [[200, 150], 250]
    #faces = detect_faces(square_zone)
    #cube = reconstruct(faces)

    gl_app = OpenGLApp()
    gl_app.run()

if __name__ == '__main__':
    rubik_cv()
