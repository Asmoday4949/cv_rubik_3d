from primitives.cube import *
import numpy

class RubiksCube:
    def __init__(self, context):
        self.n = 3
        self.array = [[[Cube(context) for k in range(self.n)] for j in range(self.n)] for i in range(self.n)]

    def setup_shaders(self, prog):
        for i in range(0, self.n):
            for j in range(0, self.n):
                for k in range(0, self.n):
                    cube = self.array[i][j][k]
                    cube.setup_shader(prog)

    def create_geometry(self):
        offset = numpy.array([-2.0,-2.0,-2.0])
        for i in range(0, self.n):
            for j in range(0, self.n):
                for k in range(0, self.n):
                    cube = self.array[i][j][k]
                    cube.create_geometry()
                    cube.create_model(numpy.copy(offset))
                    offset[2] += 2
                offset[1] += 2
                offset[2] = -2
            offset[0] += 2
            offset[1] = offset[2] = -2

    def render(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                for k in range(0, self.n):
                    cube = self.array[i][j][k]
                    cube.apply_model()
                    cube.render()
