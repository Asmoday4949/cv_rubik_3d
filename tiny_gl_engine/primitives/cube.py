from gl_tools import *
import struct
import glm

class Cube:
    def __init__(self, context):
        self.context = context
        self.init_arrays()
        self.init_buffers()


    def init_arrays(self):
        self.full_data = (0.0, 1.0, -3.0,      # Vertex
                        1.0, 0.0, 0.0, 1.0,     # Color

                        1.0, 0.0, -3.0,
                        0.0, 1.0, 0.0, 1.0,

                        -1.0, 0.0, -3.0,
                        0.0, 0.0, 1.0, 1.0,

                        # -1.0, 1.0, -1.0,
                        # 1.0, 0.0, 0.0, 1.0,

                        # ---------------
                        # -1.0, -1.0, 1.0,
                        # 1.0, 0.0, 0.0, 1.0,
                        #
                        # 1.0, -1.0, 1.0,
                        # 1.0, 0.0, 0.0, 1.0,
                        #
                        # 1.0, 1.0, 1.0,
                        # 1.0, 0.0, 0.0, 1.0,
                        #
                        # -1.0, 1.0, 1.0,
                        # 1.0, 0.0, 0.0, 1.0,
                        )

    def init_buffers(self):
        context = self.context
        self.prog = load_shaders(context, 'tiny_gl_engine/primitives/shaders/cube_vertex.glsl', 'tiny_gl_engine/primitives/shaders/cube_fragment.glsl')
        length = len(self.full_data)
        self.vbo = context.buffer(struct.pack(str(length) + 'f', *self.full_data))
        self.vao = context.simple_vertex_array(self.prog, self.vbo, 'aVertex', 'aColor')


    def set_prog_parameters(self, model, camera):
        prog = self.prog
        print(prog)
        # https://github.com/moderngl/moderngl/blob/master/examples/02_uniforms_and_attributes.py
        prog['uPMatrix'].value = camera.get_perspective_matrix()
        prog['uVMatrix'].value = camera.get_view_matrix()
        prog['uMMatrix'].value = (
                1.0, 0.0, 0.0, 0.0,
                0.0, 1.0, 0.0, 0.0,
                0.0, 0.0, 1.0, 0.0,
                0.0, 0.0, 0.0, 1.0
                )


    def get_prog():
        return self.prog


    def get_vao(self):
        return self.vao


    def get_vbo(self):
        return self.vbo
