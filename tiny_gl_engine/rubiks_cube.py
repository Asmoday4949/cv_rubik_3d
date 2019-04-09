from primitives.cube import *
import numpy

class RubiksCube:
    def __init__(self, context):
        self.n = 3
        self.array = [[[Cube(context) for k in range(self.n)] for j in range(self.n)] for i in range(self.n)]
        self.create()

    def create(self):
        offset = numpy.array([-2.0,-2.0,-2.0])
        for i in range(0, self.n):
            for j in range(0, self.n):
                for k in range(0, self.n):
                    cube = self.array[i][j][k]
                    cube.prepare_model(numpy.copy(offset))
                    offset[2] += 2
                offset[1] += 2
                offset[2] = -2
            offset[0] += 2
            offset[1] = offset[2] = -2

    def render(self, camera):
        for i in range(0, self.n):
            for j in range(0, self.n):
                for k in range(0, self.n):
                    cube = self.array[i][j][k]
                    camera.set_prog_parameters(cube.get_prog())
                    cube.render()

    def set_prog_parameters(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                for k in range(0, self.n):
                    cube = self.array[i][j][k]
                    cube.set_prog_parameters()

    def get_prog(self):
        return self.array[1][1][1].get_prog()

    def get_vao(self):
        return self.array[1][1][1].get_vao()
