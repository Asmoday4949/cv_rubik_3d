
from color_enum import Color

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

def reconstruct(rubik):
    # structure int[6][3][3]

    pass


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
            [Color.WHITE, Color.BLUE, Color.BLUE],
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

    primary_color_validation(rubik1)
    #primary_color_validation(rubik2)
    #primary_color_validation(rubik3)