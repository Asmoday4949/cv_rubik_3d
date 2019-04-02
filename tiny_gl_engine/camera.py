from gl_tools import *
import numpy
import pyrr
import math

class Camera:
    def __init__(self, fov, aspect, near, far):
        self.prepare_perspective_matrix(fov, aspect, near, far)
        self.prepare_view_matrix()


    # def prepare_perspective_matrix(self, right, left, top, bottom, near, far):
    #     # http://vispy.org/modern-gl.html
    #     self.perspective = [
    #                         [2*near/(right-left), 0.0, (right+left)/(right-left), 0.0],
    #                         [0.0, 2*near/(top-bottom)], 0.0, -(top+bottom)/(top-bottom), 0.0],
    #                         [0.0, 0.0, -(far+near)/(far-near), -(2*near*far)/(far-near)],
    #                         [0.0, 0.0, -1.0, 0.0]
    #                         ]


    def cotan(self, value):
        return math.cos(value) / math.sin(value)


    def prepare_perspective_matrix(self, fov, aspect, near, far):
        f = self.cotan(fov/2.0);
        self.perspective = (
                            f/aspect, 0.0, 0.0, 0.0,
                            0.0, f, 0.0, 0.0,
                            0.0, 0.0, (far+near)/(near-far), -1.0,
                            0.0, 0.0, 2*near*far/(near-far), 0.0,
                            )


    def prepare_view_matrix(self):
        self.view = get_unit_matrix()


    def get_perspective_matrix(self):
        return self.perspective


    def get_view_matrix(self):
        return self.view
