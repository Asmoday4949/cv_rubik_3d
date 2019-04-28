
from color_enum import Color
from pykociemba import tools 

import numpy as np

def cube_to_string(rubik):
    data = {
        Color.BLUE: 'U',
        Color.WHITE: 'F',
        Color.RED: 'R',
        Color.GREEN: 'D',
        Color.YELLOW: 'B',
        Color.ORANGE: 'L'
    }

    res = ''.join(map(lambda c: data[c],
rubik[Color.BLUE].flatten()))
    res += ''.join(map(lambda c: data[c],
rubik[Color.RED].flatten()))
    res += ''.join(map(lambda c: data[c],
rubik[Color.WHITE].flatten()))
    res += ''.join(map(lambda c: data[c],
rubik[Color.GREEN].flatten()))
    res += ''.join(map(lambda c: data[c],
rubik[Color.ORANGE].flatten()))
    res += ''.join(map(lambda c: data[c],
rubik[Color.YELLOW].flatten()))
    return res

def reconstruct(rubik):
    faces = {}
    for face in rubik:
        faces[face[1][1]] = np.transpose(np.array(face))
    print(faces)

    for blue in range(0,4):
        for red in range(0,4):
            for orange in range(0,4):
                for green in range(0,4):
                    for yellow in range(0,4):
                        cube = cube_to_string(faces)
                        valid = tools.verify(cube)
                        if valid == 0:
                            print("Found it")
                            print(valid)
                            print(cube)
                            return cube
                        faces[Color.YELLOW] = np.rot90(faces[Color.YELLOW])
                    faces[Color.GREEN] = np.rot90(faces[Color.GREEN])
                faces[Color.ORANGE] = np.rot90(faces[Color.ORANGE])
            faces[Color.RED] = np.rot90(faces[Color.RED])
        faces[Color.BLUE] = np.rot90(faces[Color.BLUE])

    cube = cube_to_string(faces)

    raise Exception("Invalid cube")
    return cube
    # print(cube)
    # print(tools.verify(cube))
    # print(tools.verify(cube))
    
import kociemba

if __name__ == '__main__':
    # print(tools.verify("BBRUUUUDFBRUURRBBDLFFFFFRFBDLFDDDFDDLBDLLLRLRLBUUBRURL"))
    # print(kociemba.solve("BBRUUUUDFBRUURRBBDLFFFFFRFBDLFDDDFDDLBDLLLRLRLBUUBRURL"))
    
    test = [
        [
            [Color.ORANGE,Color.WHITE,Color.WHITE],
            [Color.WHITE,Color.WHITE,Color.WHITE],
            [Color.RED,Color.WHITE,Color.YELLOW]
        ],
        [
            [Color.YELLOW,Color.RED,Color.BLUE],
            [Color.BLUE,Color.RED,Color.RED],
            [Color.YELLOW,Color.YELLOW,Color.GREEN]
        ],
        [
            [Color.ORANGE,Color.YELLOW,Color.BLUE],
            [Color.BLUE,Color.YELLOW,Color.RED],
            [Color.BLUE,Color.RED,Color.ORANGE]
        ],
        [
            [Color.ORANGE,Color.YELLOW,Color.GREEN],
            [Color.ORANGE,Color.ORANGE,Color.ORANGE],
            [Color.RED,Color.ORANGE,Color.RED]
        ],
        [
            [Color.YELLOW,Color.YELLOW,Color.RED],
            [Color.BLUE,Color.BLUE,Color.BLUE],
            [Color.BLUE,Color.GREEN,Color.WHITE]
        ],
        [
            [Color.GREEN,Color.ORANGE,Color.WHITE],
            [Color.GREEN,Color.GREEN,Color.GREEN],
            [Color.WHITE,Color.GREEN,Color.GREEN]
        ]
    ]
    print(reconstruct(test))
