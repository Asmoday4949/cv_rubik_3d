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
        self.perspective = perspective

    def create_view_matrix(self):
        eye = numpy.array([0.0,0.0,10.0])
        target = numpy.array([0.0,0.0,0.0])
        up = numpy.array([0.0,1.0,0.0])
        view = pyrr.matrix44.create_look_at(eye, target, up)
        self.initial_view = self.view = view


    def apply_view_perspective(self, prog):
        prog['uVMatrix'].value = tuple(self.view.flatten())
        prog['uPMatrix'].value = tuple(self.perspective.flatten())


    def move(self, dx, dy):
        oneDegRad = 1.0 * math.pi / 180.0
        v_rotation = pyrr.matrix44.create_from_x_rotation(dy * oneDegRad)
        h_rotation = pyrr.matrix44.create_from_y_rotation(dx * oneDegRad)
        rotation = pyrr.matrix44.multiply(h_rotation, v_rotation)
        final_view = pyrr.matrix44.multiply(rotation, self.initial_view)
        self.view = final_view


    def setup_shader(self, prog):
        self.prog = prog
        self.apply_view_perspective(prog)
