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
        self.build_cube_object()

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
            #self.cube.set_prog_parameters(None, self.camera)
            self.vao.render(moderngl.TRIANGLES)
            pygame.display.flip()
        pygame.quit()

    def build_camera(self):
        self.camera = Camera(70.0, 1.0, 0.1, 1000.0)

    def build_cube_object(self):
        camera = self.camera
        cube = Cube(self.context)
        cube.set_prog_parameters()
        camera.set_prog_parameters(cube.get_prog())
        self.vao = cube.get_vao()
        self.cube = cube

if __name__ == '__main__':
    app = OpenGLApp()
    app.run()
