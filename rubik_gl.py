from OpenGL.GL import *
from OpenGL.GL import shaders
from vecutils import *
import pygame

class OpenGLApp:
    def __init__(self):
        self.init_screen()

    def init_screen(self):
        pygame.init()
        self.size = [500,500]
        pygame.display.set_mode(self.size, pygame.OPENGL | pygame.DOUBLEBUF)
        self.running = True

    def run(self):
        while self.running == True:
            for event in pygame.event.get():
                self.running = not (event.type == pygame.QUIT)
            self.clear()
            pygame.display.flip()
        pygame.quit()

    def build_triangle():
        vertices = farray([
        0.6,0.6,0.0,1.0,
        -0.6,0.6,0.0,1.0,
        0.0,-0.6,0.0,1.0,
        ])

        vertex_buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
        glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(vertices), vertices, GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def render():
        glUseProgram(shader_program)
        glBindVertexArray(vertex_array_object)
        glBindVertexArray(0)
        glUseProgram(0)

    def clear(self):
        glClearColor(1.0,1.0,1.0,1.0)
        glClear(GL_COLOR_BUFFER_BIT)

if __name__ == '__main__':
    app = OpenGLApp()
    app.run()
