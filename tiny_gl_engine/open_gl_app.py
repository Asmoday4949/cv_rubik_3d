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
    def __init__(self):
        self.init_screen()
        self.init_keys()
        self.context = create_context()
        self.load_shaders()
        self.build_camera()
        self.build_rubiks_cube()
        self.init_parser("F R U L B D")

    def init_screen(self):
        self.size = [256, 256]
        self.running = True
        pygame.init()
        pygame.display.set_caption('Rubik\'s Cube')
        self.screen = pygame.display.set_mode(self.size, pygame.OPENGL | pygame.DOUBLEBUF)

    def init_keys(self):
        self.SPEED = 10
        self.mouse_pressed = False
        self.mouse_pos_sum_x = 0
        self.mouse_pos_sum_y = 0
        self.start_time = 0

    def init_parser(self, rule):
        self.orders = rule.split(' ')
        self.start_time = time.time()

    def run(self):
        context = self.context
        context.enable(moderngl.DEPTH_TEST)
        cube = self.cube
        while self.running == True:
            for event in pygame.event.get():
                self.handle_keys_event(event)
            context.clear(0.0,0.0,0.0)
            cube.render()
            self.execute_orders()
            pygame.display.flip()
        pygame.quit()

    def handle_keys_event(self, event):
        camera = self.camera
        cube = self.cube
        if event.type == KEYDOWN:
            self.running = not (event.key == K_q)
            # cube.print()
            # if event.key == K_f:
            #     cube.rotate_x(2,False)
            # if event.key == K_g:
            #     cube.rotate_y(2,False)
            # if event.key == K_h:
            #     cube.rotate_z(2,False)
            # if event.key == K_c:
            #     cube.rotate_x(2,True)
            # if event.key == K_v:
            #     cube.rotate_y(2,True)
            # if event.key == K_b:
            #     cube.rotate_z(2,True)
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
            self.mouse_pos_sum_x += (delta_pos[0] * elapsed_time * self.SPEED)
            self.mouse_pos_sum_y += (delta_pos[1] * elapsed_time * self.SPEED)
            camera.move(self.mouse_pos_sum_x, self.mouse_pos_sum_y)
            camera.apply_view_perspective(self.prog)
        if event.type == MOUSEBUTTONUP:
            self.mouse_pressed = False

    def execute_orders(self):
        orders = self.orders
        elapsed_time = time.time() - self.start_time
        if len(orders) > 0 and elapsed_time > 1:
            order = orders.pop(0)
            print("Order executed : " + order)
            self.execute_order(order)
            time.sleep(1.0)
            start_time = time.time()

    def execute_order(self, order):
        cube = self.cube
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


    def load_shaders(self):
        context = self.context
        self.prog = load_shaders(context, 'tiny_gl_engine/primitives/shaders/cube_vertex.glsl', 'tiny_gl_engine/primitives/shaders/cube_fragment.glsl')

    def build_camera(self):
        size = self.size
        camera = Camera(70.0, size[0]/size[1], 0.1, 1000.0)
        camera.setup_shader(self.prog)
        self.camera = camera

    def build_rubiks_cube(self):
        cube = RubiksCube(self.context)
        cube.setup_shaders(self.prog)
        cube.create_geometry()
        self.cube = cube

    def build_cube(self):
        cube = Cube(self.context)
        cube.setup_shader(self.prog)
        cube.create_geometry()
        #cube.apply_model()
        self.cube = cube

if __name__ == '__main__':
    app = OpenGLApp()
    app.run()
