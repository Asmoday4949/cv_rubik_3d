from gl_tools import *
import struct
import numpy

class Triangle:
    def __init__(self, context):
        self.context = context
        self.init_arrays()
        self.init_buffers()


    def init_arrays(self):
        self.vertices = numpy.array([
                        0.0, 1.0, -2.0,
                        -1.0, 0.0, -2.0,
                        1.0, 0.0, -2.0
                        ])
        self.indices = numpy.array([0,1,2])
        self.colors = numpy.array([1.0,0.0,0.0,
                                    0.0,1.0,0.0,
                                    0.0,0.0,1.0])


    def init_buffers(self):
        # https://github.com/moderngl/moderngl/blob/master/examples/06_index_buffer.py
        context = self.context
        self.prog = load_shaders(context, 'tiny_gl_engine/primitives/shaders/triangle_vertex.glsl', 'tiny_gl_engine/primitives/shaders/triangle_fragment.glsl')
        self.vbo = self.context.buffer(self.vertices.astype('f4').tobytes())
        self.cbo = self.context.buffer(self.colors.astype('f4').tobytes())
        self.ibo = self.context.buffer(self.indices.astype('i4').tobytes())
        vao_content = [
            (self.vbo, '3f', 'aVertex'),
            (self.cbo, '3f', 'aColor')
        ]
        self.vao = self.context.vertex_array(self.prog, vao_content, self.ibo)


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
