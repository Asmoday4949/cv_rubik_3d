import struct
import moderngl
import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from gl_tools import *
from primitives.cube import *

class OpenGLApp:
    def __init__(self):
        self.init_screen()
        self.context = create_context()
        self.build_cube()

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
            self.cube.get_vao().render()
            pygame.display.flip()
        pygame.quit()

    def build_camera():
        self.camera = Camera()

    def build_cube(self):
        self.cube = Cube(self.context)

    def build_triangle(self):
        context = self.context
        prog = load_shaders(context, './shaders/vertex.shader', './shaders/fragment.shader')
        vbo = context.buffer(struct.pack('6f', 0.0, 0.8, -0.6, -0.8, 0.6, -0.8))
        vao = context.simple_vertex_array(prog, vbo, 'vert')
        self.vbo = vbo
        self.vao = vao

if __name__ == '__main__':
    app = OpenGLApp()
    app.run()
