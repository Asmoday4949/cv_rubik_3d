


def primary_validation(rubik):
    color_counter = {}

    for face in rubik:
        for row in rubik:
            for cube in rubik:
                try:
                    color_counter[cube] += 1
                except KeyError:
                    color_counter[cube] = 1
    for i in range(1,7):
        if color_counter[i] != 9:
            raise Exception("Invalid cube detected - during primary validation")

    pass

def reconstruct(rubik):
    # structure int[6][3][3]




    pass
