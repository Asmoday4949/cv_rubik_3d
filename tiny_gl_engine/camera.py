import numpy
import math
import pyrr

class Camera:
    def __init__(self, fov, aspect, near, far):
        self.create_perspective_matrix(fov, aspect, near, far)
        self.create_view_matrix()


    def cotan(self, value):
        return math.cos(value) / math.sin(value)


    def create_perspective_matrix(self, fov, aspect, near, far):
        perspective = pyrr.matrix44.create_perspective_projection_matrix(fov, aspect, near, far)
        self.perspective = tuple(perspective.flatten())


    def create_view_matrix(self):
        eye = numpy.array([5.0,5.0,10.0])
        target = numpy.array([0.0,0.0,0.0])
        up = numpy.array([0.0,1.0,0.0])
        view = pyrr.matrix44.create_look_at(eye, target, up)
        self.view = tuple(view.flatten())


    def apply_view_perspective(self, prog):
        prog['uVMatrix'].value = self.view
        prog['uPMatrix'].value = self.perspective


    def setup_shader(self, prog):
        self.prog = prog
        self.apply_view_perspective(prog)
