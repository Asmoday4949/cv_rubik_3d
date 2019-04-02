import struct
import moderngl
import pygame
import numpy as np
from pygame.locals import DOUBLEBUF, OPENGL
from gl_tools import *
from primitives.cube import *
from camera import *

class OpenGLApp:
    def __init__(self):
        self.init_screen()
        self.context = create_context()
        self.build_camera()
        self.build_triangle()

    def init_screen(self):
        pygame.init()
        self.size = [500,500]
        pygame.display.set_mode(self.size, pygame.OPENGL | pygame.DOUBLEBUF)
        self.running = True

    def run(self):
        context = self.context
        while self.running == True:
            for event in pygame.event.get():
                self.running = not (event.type == pygame.QUIT)
                context.clear(0.0,0.0,0.0)
            self.vao.render()
            pygame.display.flip()
        pygame.quit()

    def build_camera(self):
        self.camera = Camera(70.0, 1.0, 0.1, 1000.0)

    def build_triangle(self):
        camera = self.camera
        context = self.context
        prog = load_shaders(context, 'tiny_gl_engine/primitives/shaders/triangle_vertex.glsl', 'tiny_gl_engine/primitives/shaders/triangle_fragment.glsl')
        vertices = np.array([
            # x, y, red, green, blue
            0.0, 1.0, 1.0, 0.0, 0.0,
            -0.6, 0.0, 0.0, 1.0, 0.0,
            0.6, 0.0, 0.0, 0.0, 1.0,
        ])
        self.vbo = context.buffer(vertices.astype('f4').tobytes())
        # We control the 'in_vert' and `in_color' variables
        self.vao = context.simple_vertex_array(prog, self.vbo, 'in_vert', 'in_color')
        #prog['uPMatrix'].value = camera.get_perspective_matrix()
        # prog['uVMatrix'].value = camera.get_view_matrix()
        # prog['uMMatrix'].value = (
        #         1.0, 0.0, 0.0, 0.0,
        #         0.0, 1.0, 0.0, 0.0,
        #         0.0, 0.0, 1.0, 0.0,
        #         0.0, 0.0, 0.0, 1.0
        #         )
        self.prog = prog

    def build_cube(self):
        camera = self.camera
        cube = Cube(self.context)
        cube.set_prog_parameters(camera.prepare_view_matrix(), camera)
        self.cube = cube

if __name__ == '__main__':
    app = OpenGLApp()
    app.run()
