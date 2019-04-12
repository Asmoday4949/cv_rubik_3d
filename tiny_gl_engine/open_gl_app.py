import struct
import moderngl
import pygame
import numpy as np
from pygame.locals import DOUBLEBUF, OPENGL
from tiny_gl_engine.gl_tools import *
from tiny_gl_engine.primitives.cube import *
from tiny_gl_engine.rubiks_cube import *
from tiny_gl_engine.camera import *

class OpenGLApp:
    def __init__(self):
        self.init_screen()
        self.context = create_context()
        self.load_shaders()
        self.build_camera()
        self.build_rubiks_cube()

    def init_screen(self):
        pygame.init()
        self.size = [500,500]
        pygame.display.set_mode(self.size, pygame.OPENGL | pygame.DOUBLEBUF)
        self.running = True

    def run(self):
        context = self.context
        context.enable(moderngl.DEPTH_TEST)
        #context.wireframe = True
        while self.running == True:
            for event in pygame.event.get():
                self.running = not (event.type == pygame.QUIT)
            context.clear(0.0,0.0,0.0)
            self.cube.render()
            pygame.display.flip()
        pygame.quit()

    def load_shaders(self):
        context = self.context
        self.prog = load_shaders(context, 'tiny_gl_engine/primitives/shaders/cube_vertex.glsl', 'tiny_gl_engine/primitives/shaders/cube_fragment.glsl')

    def build_camera(self):
        camera = Camera(70.0, 1.0, 0.1, 1000.0)
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
