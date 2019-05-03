
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

    for white in range(0,4):
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
        faces[Color.WHITE] = np.rot90(faces[Color.WHITE])

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
    
    # test = [[[Color.YELLOW, Color.YELLOW, Color.YELLOW], [Color.BLUE, Color.GREEN, Color.ORANGE], [Color.WHITE, Color.BLUE, Color.GREEN]], [[Color.ORANGE, Color.YELLOW, Color.ORANGE], [Color.GREEN, Color.RED, Color.ORANGE], [Color.ORANGE, Color.BLUE, Color.BLUE]], [[Color.GREEN, Color.RED, Color.YELLOW], [Color.WHITE, Color.BLUE, Color.RED], [Color.GREEN, Color.GREEN, Color.BLUE]], [[Color.RED, Color.BLUE, Color.YELLOW], [Color.GREEN, Color.ORANGE, Color.ORANGE], [Color.RED, Color.WHITE, Color.ORANGE]], [[Color.BLUE, Color.ORANGE, Color.GREEN], [Color.GREEN, Color.WHITE, Color.YELLOW], [Color.BLUE, Color.YELLOW, Color.RED]], [[Color.WHITE, Color.RED, Color.RED], [Color.WHITE, Color.YELLOW, Color.WHITE], [Color.WHITE, Color.RED, Color.WHITE]]]
    # test = [[[Color.GREEN, Color.GREEN, Color.GREEN], [Color.GREEN, Color.GREEN, Color.GREEN], [Color.GREEN, Color.GREEN, Color.GREEN]], [[Color.RED, Color.RED, Color.RED], [Color.RED, Color.RED, Color.RED], [Color.RED, Color.RED, Color.RED]], [[Color.BLUE, Color.BLUE, Color.BLUE], [Color.BLUE, Color.BLUE, Color.BLUE], [Color.BLUE, Color.BLUE, Color.BLUE]], [[Color.ORANGE, Color.ORANGE, Color.ORANGE], [Color.ORANGE, Color.ORANGE, Color.ORANGE], [Color.ORANGE, Color.ORANGE, Color.ORANGE]], [[Color.WHITE, Color.WHITE, Color.WHITE], [Color.WHITE, Color.WHITE, Color.WHITE], [Color.WHITE, Color.WHITE, Color.WHITE]], [[Color.YELLOW, Color.YELLOW, Color.YELLOW], [Color.YELLOW, Color.YELLOW, Color.YELLOW], [Color.YELLOW, Color.YELLOW, Color.YELLOW]]]
    test = [[[Color.WHITE, Color.WHITE, Color.WHITE], [Color.GREEN, Color.GREEN, Color.GREEN], [Color.GREEN, Color.GREEN, Color.GREEN]],
     [[Color.RED, Color.RED, Color.RED], [Color.RED, Color.RED, Color.RED], [Color.RED, Color.RED, Color.RED]], 
     [[Color.YELLOW, Color.YELLOW, Color.YELLOW], [Color.BLUE, Color.BLUE, Color.BLUE], [Color.BLUE, Color.BLUE, Color.BLUE]],
      [[Color.ORANGE, Color.ORANGE, Color.ORANGE], [Color.ORANGE, Color.ORANGE, Color.ORANGE], [Color.ORANGE, Color.ORANGE, Color.ORANGE]], 
      [[Color.BLUE, Color.BLUE, Color.BLUE], [Color.WHITE, Color.WHITE, Color.WHITE], [Color.WHITE, Color.WHITE, Color.WHITE]], 
      [[Color.GREEN, Color.GREEN, Color.GREEN], [Color.YELLOW, Color.YELLOW, Color.YELLOW], [Color.YELLOW, Color.YELLOW, Color.YELLOW]]]
    print(reconstruct(test))
