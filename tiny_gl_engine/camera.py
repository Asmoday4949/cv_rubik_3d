import numpy
import math
import pyrr

class Camera:
    def __init__(self, fov, aspect, near, far):
        self.prepare_perspective_matrix(fov, aspect, near, far)
        self.prepare_view_matrix()


    def cotan(self, value):
        return math.cos(value) / math.sin(value)


    def prepare_perspective_matrix(self, fov, aspect, near, far):
        perspective = pyrr.matrix44.create_perspective_projection_matrix(fov, aspect, near, far)
        self.perspective = tuple(perspective.flatten())


    def prepare_view_matrix(self):
        eye = numpy.array([0.0,3.0,3.0])
        target = numpy.array([0.0,0.0,0.0])
        up = numpy.array([0.0,1.0,0.0])
        view = pyrr.matrix44.create_look_at(eye, target, up)
        self.view = tuple(view.flatten())


    def set_prog_parameters(self, prog):
        prog['uVMatrix'].value = self.get_view_matrix()
        prog['uPMatrix'].value = self.get_perspective_matrix()

    def get_perspective_matrix(self):
        return self.perspective


    def get_view_matrix(self):
        return self.view
