#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""camera.py: Represent a camera """

__author__ = "Lucas Bulloni, Malik Fleury, Bastien Wermeille"
__version__ = "1.0.0"


import numpy
import math
import pyrr


class Camera:
    def __init__(self, fov, aspect, near, far):
        """ Init camera """
        self.create_perspective_matrix(fov, aspect, near, far)
        self.create_view_matrix()

    def cotan(self, value):
        """ Math cotan """
        return math.cos(value) / math.sin(value)

    def create_perspective_matrix(self, fov, aspect, near, far):
        """ Create the perspective matrix """
        perspective = pyrr.matrix44.create_perspective_projection_matrix(fov, aspect, near, far)
        self.perspective = perspective

    def create_view_matrix(self):
        """ Create the view matrix """
        eye = numpy.array([0.0,0.0,10.0])
        target = numpy.array([0.0,0.0,0.0])
        up = numpy.array([0.0,1.0,0.0])
        view = pyrr.matrix44.create_look_at(eye, target, up)
        self.initial_view = self.view = view

    def apply_view_perspective(self, prog):
        """ Apply the current matrices to the shader """
        prog['uVMatrix'].value = tuple(self.view.flatten())
        prog['uPMatrix'].value = tuple(self.perspective.flatten())

    def move(self, dx, dy):
        """ Move the camera on y and x axis """
        oneDegRad = 1.0 * math.pi / 180.0
        v_rotation = pyrr.matrix44.create_from_x_rotation(dy * oneDegRad)
        h_rotation = pyrr.matrix44.create_from_y_rotation(dx * oneDegRad)
        rotation = pyrr.matrix44.multiply(h_rotation, v_rotation)
        final_view = pyrr.matrix44.multiply(rotation, self.initial_view)
        self.view = final_view

    def setup_shader(self, prog):
        """ Set a new shader and apply the matrices """
        self.prog = prog
        self.apply_view_perspective(prog)
