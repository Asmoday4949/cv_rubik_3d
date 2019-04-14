from tiny_gl_engine.primitives.cube import *
import numpy

class RubiksCube:
    def __init__(self, context):
        self.n = 3
        self.X_AXIS = numpy.array([1.0,0.0,0.0])
        self.Y_AXIS = numpy.array([0.0,1.0,0.0]) # ??
        self.Z_AXIS = numpy.array([0.0,0.0,1.0])
        self.ROTATION_CCW = [[(2,0),(1,0),(0,0)],[(2,1),(1,1),(0,1)],[(2,2),(1,2),(0,2)]]
        id = 0
        self.array = numpy.array([[[Cube(context, str(i*9 + j*3 + k)) for k in range(self.n)] for j in range(self.n)] for i in range(self.n)])

    def print(self):
        print("START-----------")
        for x in range(0, self.n):
            for y in range(self.n-1, -1, -1):
                for z in range(0, self.n):
                    cube = self.array[x][y][z]
                    print(str(cube) + ",", end='')
                print()
            print("-----------END")

    def setup_shaders(self, prog):
        for x in range(0, self.n):
            for y in range(0, self.n):
                for z in range(0, self.n):
                    cube = self.array[x][y][z]
                    cube.setup_shader(prog)

    def create_geometry(self):
        offset = numpy.array([-2.0,-2.0,-2.0])
        for x in range(0, self.n):
            for y in range(0, self.n):
                for z in range(0, self.n):
                    cube = self.array[x][y][z]
                    cube.create_geometry()
                    cube.create_model(numpy.copy(offset))
                    offset[2] += 2
                offset[1] += 2
                offset[2] = -2
            offset[0] += 2
            offset[1] = offset[2] = -2

    def render(self):
        for x in range(0, self.n):
            for y in range(0, self.n):
                for z in range(0, self.n):
                    cube = self.array[x][y][z]
                    cube.apply_model()
                    cube.render()

    def rotate_x(self, layer, clockwise):
        array = self.array
        for y in range(0, self.n):
            for z in range(0, self.n):
                cube = array[layer][y][z]
                cube.rotate(self.X_AXIS, clockwise)
        self.rot_memory_x(layer,clockwise)

    def rotate_y(self, layer, clockwise):
        array = self.array
        self.print()
        for x in range(0, self.n):
            for z in range(0, self.n):
                cube = array[x][layer][z]
                cube.rotate(self.Y_AXIS, clockwise)
        self.rot_memory_y(layer, clockwise)

    def rotate_z(self, layer, clockwise):
        array = self.array
        for x in range(0, self.n):
            for y in range(0, self.n):
                cube = array[x][y][layer]
                cube.rotate(self.Z_AXIS, clockwise)
        self.rot_memory_z(layer, clockwise)

    def rot_memory_x(self, layer, clockwise):
        array = self.array
        arrayCopy = numpy.copy(array)
        for i in range(0, self.n):
            for j in range(0, self.n):
                indices = self.ROTATION_CCW[i][j]
                if not clockwise:
                    array[layer][indices[0]][indices[1]] = arrayCopy[layer][i][j]
                else:
                    array[layer][i][j] = arrayCopy[layer][indices[0]][indices[1]]

    def rot_memory_y(self, layer, clockwise):
        array = self.array
        arrayCopy = numpy.copy(array)
        for i in range(0, self.n):
            for j in range(0, self.n):
                indices = self.ROTATION_CCW[i][j]
                if not clockwise:
                    array[i][layer][j] = arrayCopy[indices[0]][layer][indices[1]]
                else:
                    array[indices[0]][layer][indices[1]] = arrayCopy[i][layer][j]

    def rot_memory_z(self, layer, clockwise):
        array = self.array
        arrayCopy = numpy.copy(array)
        for i in range(0, self.n):
            for j in range(0, self.n):
                indices = self.ROTATION_CCW[i][j]
                if not clockwise:
                    array[indices[0]][indices[1]][layer] = arrayCopy[i][j][layer]
                else:
                    array[i][j][layer] = arrayCopy[indices[0]][indices[1]][layer]
