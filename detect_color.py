import numpy as np
import cv2 as cv
from color_enum import Color
import os


def detect_color(image, square_zone):
    MARGIN = 20
    result = np.full([3, 3], -1)
    width_one_square = square_zone[1] // 3
    sub_zone = [square_zone[0].copy(), width_one_square]
    result = []

    for i in range(0, 3):
        sub_zone[0][0] = square_zone[0][0]
        result.append([])

        for j in range(0, 3):
            start_width = sub_zone[0][1] + MARGIN
            end_width = sub_zone[0][1] + sub_zone[1] - MARGIN

            start_height = sub_zone[0][0] + MARGIN
            end_height = sub_zone[0][0] + sub_zone[1] - MARGIN

            subimage = image[start_width:end_width, start_height:end_height]

            bgr_mean, deviation = get_bgr_value_subimage(subimage, np.mean)
            #bgr_mean, deviation = get_bgr_value_subimage(subimage, np.median)

            # if deviation > 10:
            #    print("hello")
            #    return None

            color = decide_color(bgr_mean)

            result[i].append(decide_color(bgr_mean))

            cv.imshow(f"{i}:{j}", subimage)
            sub_zone[0][0] += width_one_square

        sub_zone[0][0] = square_zone[0][0]
        sub_zone[0][1] += width_one_square
    print(result)

    return result


def draw_square(image, zone):
    color = (0, 0, 0)
    pt1 = tuple(zone[0])
    pt2 = (zone[0][0] + zone[1], zone[0][1] + zone[1])

    cv.rectangle(image, pt2, pt1, color, 2)


def decide_color(bgr_value):
    hsv_value = np.squeeze(np.asarray(cv.cvtColor(
        np.uint8([[bgr_value]]), cv.COLOR_BGR2HSV)))

    if bgr_value.mean() > 150 and np.std(bgr_value) < 40:
        return Color.WHITE
    elif hsv_value[0] > 90 and hsv_value[0] < 120:
        return Color.BLUE
    elif hsv_value[0] < 90 and hsv_value[0] > 60:
        return Color.GREEN
    elif hsv_value[0] < 30 and hsv_value[0] > 10 and bgr_value[1] > 50:
        return Color.YELLOW
    # elif hsv_value[0] < 190 and hsv_value[0] > 160: # 160 change into
    elif hsv_value[0] < 190 and bgr_value[1] < 48:
        return Color.RED
    elif hsv_value[0] < 15 and bgr_value[1] > 48:
        return Color.ORANGE

    #print(hsv_value, bgr_value)
    return None


def get_bgr_value_subimage(subimage, math_func):
    bgr_mean = np.empty((3,))
    deviation = 0

    for i in range(0, 3):
        bgr_mean[i] = math_func(subimage[:, :, i])

    grayscale = cv.cvtColor(subimage, cv.COLOR_RGB2GRAY)
    deviation = np.std(grayscale)

    return bgr_mean, deviation

# if __name__ == '__main__':
#     square_zone = [[200, 150], 250]
#     detect_faces(square_zone)
