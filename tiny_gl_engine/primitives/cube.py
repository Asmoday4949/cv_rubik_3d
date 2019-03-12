from gl_tools import *
import struct
import glm

class Cube:
    def __init__(self, context):
        self.context = context
        self.init_arrays()
        self.init_buffers()


    def init_arrays(self):
        self.vertices = [-1.0, -1.0, -1.0,
                        1.0, -1.0, -1.0,
                        1.0, 1.0, -1.0,
                        -1.0, 1.0, -1.0,
                        # ---------------
                        -1.0, -1.0, 1.0,
                        1.0, -1.0, 1.0,
                        1.0, 1.0, 1.0,
                        -1.0, 1.0, 1.0,
                        ]


    def init_buffers(self):
        context = self.context
        self.prog = load_shaders(context, './primitives/shaders/vertex.glsl', './primitives/shaders/fragment.glsl')
        length = len(self.vertices)
        self.vbo = context.buffer(struct.pack(str(length) + 'f', *self.vertices))
        self.vao = context.simple_vertex_array(self.prog, self.vbo, 'vert')


    def get_prog():
        return self.prog


    def get_vao(self):
        return self.vao


    def get_vbo(self):
        return self.vbo
