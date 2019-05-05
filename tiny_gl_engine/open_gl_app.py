#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""open_gl_app.py: 3D application of the rubik's cube"""

__author__ = "Lucas Bulloni, Malik Fleury, Bastien Wermeille"
__version__ = "1.0.0"

import struct
import moderngl
import pygame
import numpy as np
import time
from pygame.locals import *
from tiny_gl_engine.gl_tools import *
from tiny_gl_engine.primitives.cube import *
from tiny_gl_engine.rubiks_cube import *
from tiny_gl_engine.camera import *

class OpenGLApp:
    def __init__(self, rules):
        """ Init all the stuff """
        self.init_screen()
        self.init_keys()
        self.context = create_context()
        self.load_shaders()
        self.build_camera()
        self.build_rubiks_cube()
        self.init_parser(rules)
        self.randomize()

    def init_screen(self):
        """ Init the screen """
        self.size = [1024, 720]
        self.running = True
        pygame.init()
        pygame.display.set_caption('Rubik\'s Cube')
        self.screen = pygame.display.set_mode(self.size, pygame.OPENGL | pygame.DOUBLEBUF)

    def init_keys(self):
        """ Init data for camera mouvements """
        self.SPEED = 40
        self.mouse_pressed = False
        self.mouse_pos_sum_x = 0
        self.mouse_pos_sum_y = 0
        self.start_time = 0

    def init_parser(self, rule):
        """ Parse the solution and create the reversed solution """
        self.orders = rule.split(' ')
        self.reversed_orders = self.inverse_orders(self.orders)
        self.current_index = len(self.orders)
        self.start_time = time.time()

    def randomize(self):
        """ Execute rotation (inverse order) to get the mixed rubik's cube """
        for i in range(0, len(self.reversed_orders)):
            self.previous()

    def run(self):
        """ Main of the program """
        context = self.context
        context.enable(moderngl.DEPTH_TEST)
        cube = self.cube
        while self.running == True:
            for event in pygame.event.get():
                self.handle_keys_event(event)
            context.clear(0.0,0.0,0.0)
            cube.render()
            pygame.display.flip()
        pygame.quit()

    def handle_keys_event(self, event):
        """ Handle the keys pressed (Camera, next and previous rotations) """
        camera = self.camera
        cube = self.cube
        if event.type == KEYDOWN:
            self.running = not (event.key == K_q)
            # cube.print()
            if event.key == K_LEFT:
                self.previous()
            if event.key == K_RIGHT:
                self.next()
        if event.type == MOUSEBUTTONDOWN:
            self.mouse_pressed = True
            self.start_pos = event.pos
            self.start_time = time.time()
        if event.type == MOUSEMOTION and self.mouse_pressed:
            delta_pos = (event.pos[0] - self.start_pos[0], event.pos[1] - self.start_pos[1])
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            self.start_pos = event.pos
            self.start_time = current_time
            self.mouse_pos_sum_x -= (delta_pos[0] * elapsed_time * self.SPEED)
            self.mouse_pos_sum_y -= (delta_pos[1] * elapsed_time * self.SPEED)
            camera.move(self.mouse_pos_sum_x, self.mouse_pos_sum_y)
            camera.apply_view_perspective(self.prog)
        if event.type == MOUSEBUTTONUP:
            self.mouse_pressed = False

    def inverse_orders(self, orders):
        """ Create the array of inversed orders """
        inversed_orders = []
        for order in orders:
            if '2' in order:
                inversed_orders.append(order)
            elif '\'' in order:
                inversed_orders.append(order[0])
            else:
                inversed_orders.append(order[0] + '\'')
        return inversed_orders

    def previous(self):
        """ Execute the previous rotation """
        orders = self.reversed_orders;
        if self.current_index > 0:
            self.current_index -= 1
            order = orders[self.current_index]
            self.execute_order(order)

    def next(self):
        """ Execute the next rotation """
        orders = self.orders
        if self.current_index < len(orders):
            order = orders[self.current_index]
            self.execute_order(order)
            self.current_index += 1

    def execute_order(self, order):
        """ Transform string order into rotation """
        cube = self.cube

        if order == 'F2':
            for i in range(0,2):
                cube.rotate_z(2, True)
        if order == 'R2':
            for i in range(0,2):
                cube.rotate_x(2, True)
        if order == 'U2':
            for i in range(0,2):
                cube.rotate_y(2, True)
        if order == 'L2':
            for i in range(0,2):
                cube.rotate_x(0, False)
        if order == 'B2':
            for i in range(0,2):
                cube.rotate_z(0, False)
        if order == 'D2':
            for i in range(0,2):
                cube.rotate_y(0, False)

        if order == 'F':
            cube.rotate_z(2, True)
        if order == 'R':
            cube.rotate_x(2, True)
        if order == 'U':
            cube.rotate_y(2, True)
        if order == 'L':
            cube.rotate_x(0, False)
        if order == 'B':
            cube.rotate_z(0, False)
        if order == 'D':
            cube.rotate_y(0, False)

        if order == 'F\'':
            cube.rotate_z(2, False)
        if order == 'R\'':
            cube.rotate_x(2, False)
        if order == 'U\'':
            cube.rotate_y(2, False)
        if order == 'L\'':
            cube.rotate_x(0, True)
        if order == 'B\'':
            cube.rotate_z(0, True)
        if order == 'D\'':
            cube.rotate_y(0, True)


    def load_shaders(self):
        """ Loads shaders (vertex and fragment) """
        context = self.context
        self.prog = load_shaders(context, 'tiny_gl_engine/primitives/shaders/cube_vertex.glsl', 'tiny_gl_engine/primitives/shaders/cube_fragment.glsl')

    def build_camera(self):
        """ Create the camera """
        size = self.size
        camera = Camera(70.0, size[0]/size[1], 0.1, 1000.0)
        camera.setup_shader(self.prog)
        self.camera = camera

    def build_rubiks_cube(self):
        """ Create the rubik's cube """
        cube = RubiksCube(self.context)
        cube.setup_shaders(self.prog)
        cube.create_geometry()
        self.cube = cube

    def build_cube(self):
        """ Build a cube (test purpose) """
        cube = Cube(self.context)
        cube.setup_shader(self.prog)
        cube.create_geometry()
        #cube.apply_model()
        self.cube = cube

if __name__ == '__main__':
    app = OpenGLApp()
    app.run()
