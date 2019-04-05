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
        perspective = pyrr.matrix44.create_perspective_projection_matrix(fov, aspect, near, far).flatten()
        self.perspective = tuple(perspective)


    def prepare_view_matrix(self):
        self.create_view_matrice([0,0,2], 0)
        # view = pyrr.matrix44.create_identity()
        # self.view = tuple(view)


    def get_perspective_matrix(self):
        return self.perspective


    def get_view_matrix(self):
        return self.view


    def create_view_matrice(self, translation, degree):
        radian = degree * math.pi / 180.0
        translation_matrix = pyrr.matrix44.create_from_translation(numpy.array(translation))
        translation_matrix = numpy.transpose(translation_matrix)
        y_rotation_matrix = pyrr.matrix44.create_from_axis_rotation(numpy.array([0.0,1.0,0.0]), radian, dtype=float)
        y_rotation_matrix = numpy.transpose(y_rotation_matrix)
        view = pyrr.matrix44.multiply(y_rotation_matrix, translation_matrix).flatten()
        self.view = tuple(view.flatten())
