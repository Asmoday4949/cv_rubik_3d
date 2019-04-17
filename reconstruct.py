
from color_enum import Color
from pykociemba import tools 


def verify(rubik):
    tools.verify("")

def primary_color_validation(rubik):
    color_angles_counter = {}
    color_edges_counter = {}
    color_center_counter = {}
    
    angles = [(0,0), (0,2), (2,0), (2,2)]
    edges = [(0,1), (1,0), (2,1), (1,2)]
    center = (1,1)

    for face in rubik:
        for (i,j) in angles:
            try:
                color_angles_counter[face[i][j]] += 1
            except KeyError:
                color_angles_counter[face[i][j]] = 1
        
        for (i,j) in edges:
            try:
                color_edges_counter[face[i][j]] += 1
            except KeyError:
                color_edges_counter[face[i][j]] = 1
        
        (i,j) = center
        try:
            color_center_counter[face[i][j]] += 1
        except KeyError:
            color_center_counter[face[i][j]] = 1
    
    for c in Color:
        try:
            if color_angles_counter[c] != 4:
                raise Exception("Invalid cube detected - during primary validation - angle", color_angles_counter)
        except KeyError:
            raise Exception("Invalid cube detected - during primary validation - angle", color_angles_counter)
    
    for c in Color:
        try:
            if color_edges_counter[c] != 4:
                raise Exception("Invalid cube detected - during primary validation - edge", color_edges_counter)
        except KeyError:
            raise Exception("Invalid cube detected - during primary validation - edge", color_edges_counter)
    
    for c in Color:
        try:
            if color_center_counter[c] != 1:
                raise Exception("Invalid cube detected - during primary validation - center", color_center_counter)
        except KeyError:
            raise Exception("Invalid cube detected - during primary validation - center", color_center_counter)

# from kociemba import tools
import numpy as np


def color_to_char(char):

    return data[char]

def cube_to_string(rubik):
    data = {
        Color.BLUE: 'U',
        Color.WHITE: 'F',
        Color.RED: 'R',
        Color.GREEN: 'D',
        Color.YELLOW: 'B',
        Color.ORANGE: 'L'
    }

    res = ''.join(map(lambda c: data[c], rubik[Color.BLUE].flatten()))
    res += ''.join(map(lambda c: data[c], rubik[Color.RED].flatten()))
    res += ''.join(map(lambda c: data[c], rubik[Color.WHITE].flatten()))
    res += ''.join(map(lambda c: data[c], rubik[Color.GREEN].flatten()))
    res += ''.join(map(lambda c: data[c], rubik[Color.ORANGE].flatten()))
    res += ''.join(map(lambda c: data[c], rubik[Color.YELLOW].flatten()))
    return res

def reconstruct(rubik):
    # structure int[6][3][3]
    #          blue
    # orange | white | red | yellow
    #          green
    #
    
    faces = {}
    for face in rubik:
        faces[face[1][1]] = np.array(face)
    

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

    # blue_face = faces[Color.BLUE]
    # orange_face = faces[Color.ORANGE]
    # white_face = faces[Color.WHITE]
    # red_face = faces[Color.RED]
    # yellow_face = faces[Color.YELLOW]
    # green_face = faces[Color.GREEN]

    cube = cube_to_string(faces)
    # print(cube)
    # print(tools.verify(cube))
    # print(tools.verify(cube))
    

if __name__ == '__main__':
    rubik1 = [ # This is a valid rubik's list of faces
        [
            [Color.BLUE, Color.GREEN, Color.BLUE],
            [Color.WHITE, Color.GREEN, Color.BLUE],
            [Color.YELLOW, Color.GREEN, Color.BLUE]
        ],
        [
            [Color.GREEN, Color.ORANGE, Color.RED],
            [Color.YELLOW, Color.YELLOW, Color.ORANGE],
            [Color.WHITE, Color.ORANGE, Color.BLUE]
        ],
        [
            [Color.GREEN, Color.YELLOW, Color.WHITE],
            [Color.RED, Color.BLUE, Color.GREEN],
            [Color.RED, Color.BLUE, Color.GREEN]
        ],
        [
            [Color.GREEN, Color.RED, Color.ORANGE],
            [Color.WHITE, Color.WHITE, Color.BLUE],
            [Color.ORANGE, Color.RED, Color.ORANGE]
        ],
        [
            [Color.ORANGE, Color.WHITE, Color.WHITE],
            [Color.RED, Color.ORANGE, Color.BLUE],
            [Color.RED, Color.GREEN, Color.WHITE]
        ],
        [
            [Color.YELLOW, Color.YELLOW, Color.RED],
            [Color.ORANGE, Color.RED, Color.WHITE],
            [Color.YELLOW, Color.YELLOW, Color.YELLOW]
        ],
    ]

    rubik2 = [ # Invalid corner and edge inverted
        [
            [Color.GREEN, Color.BLUE, Color.BLUE],
            [Color.WHITE, Color.GREEN, Color.BLUE],
            [Color.YELLOW, Color.GREEN, Color.BLUE]
        ],
        [
            [Color.GREEN, Color.ORANGE, Color.RED],
            [Color.YELLOW, Color.YELLOW, Color.ORANGE],
            [Color.WHITE, Color.ORANGE, Color.BLUE]
        ],
        [
            [Color.GREEN, Color.YELLOW, Color.WHITE],
            [Color.RED, Color.BLUE, Color.GREEN],
            [Color.RED, Color.BLUE, Color.GREEN]
        ],
        [
            [Color.GREEN, Color.RED, Color.ORANGE],
            [Color.WHITE, Color.WHITE, Color.BLUE],
            [Color.ORANGE, Color.RED, Color.ORANGE]
        ],
        [
            [Color.ORANGE, Color.WHITE, Color.WHITE],
            [Color.RED, Color.ORANGE, Color.BLUE],
            [Color.RED, Color.GREEN, Color.WHITE]
        ],
        [
            [Color.YELLOW, Color.YELLOW, Color.RED],
            [Color.ORANGE, Color.RED, Color.WHITE],
            [Color.YELLOW, Color.YELLOW, Color.YELLOW]
        ],
    ]

    rubik3 = [ # Invalid Center changed from green to blue
        [
            [Color.BLUE, Color.GREEN, Color.BLUE],
            [Color.WHITE, Color.GREEN, Color.BLUE],
            [Color.YELLOW, Color.GREEN, Color.BLUE]
        ],
        [
            [Color.GREEN, Color.ORANGE, Color.RED],
            [Color.YELLOW, Color.YELLOW, Color.ORANGE],
            [Color.WHITE, Color.ORANGE, Color.BLUE]
        ],
        [
            [Color.GREEN, Color.YELLOW, Color.WHITE],
            [Color.RED, Color.BLUE, Color.GREEN],
            [Color.RED, Color.BLUE, Color.GREEN]
        ],
        [
            [Color.GREEN, Color.RED, Color.ORANGE],
            [Color.WHITE, Color.WHITE, Color.BLUE],
            [Color.ORANGE, Color.RED, Color.ORANGE]
        ],
        [
            [Color.ORANGE, Color.WHITE, Color.WHITE],
            [Color.RED, Color.ORANGE, Color.BLUE],
            [Color.RED, Color.GREEN, Color.WHITE]
        ],
        [
            [Color.YELLOW, Color.YELLOW, Color.RED],
            [Color.ORANGE, Color.RED, Color.WHITE],
            [Color.YELLOW, Color.YELLOW, Color.YELLOW]
        ],
    ]

    # primary_color_validation(rubik1)
    # primary_color_validation(rubik2)
    # primary_color_validation(rubik3)
    reconstruct(rubik3)
