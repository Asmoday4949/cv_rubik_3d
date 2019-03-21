import numpy as np
import cv2 as cv
from color_enum import Color

def detect_color(image):
    square_zone = [[170, 500], 480] # x;y -> left corner , w;h
    MARGIN = 50
    result = np.full([3,3], -1)

    width_one_square = square_zone[1] // 3

    sub_zone = [square_zone[0].copy(), width_one_square]

    result = []

    for i in range(0,3):
        sub_zone[0][0] = square_zone[0][0]
        result.append([])

        for j in range(0,3):
            start_width = sub_zone[0][1] + MARGIN
            end_width = sub_zone[0][1] + sub_zone[1] - MARGIN

            start_height = sub_zone[0][0] + MARGIN
            end_height = sub_zone[0][0] + sub_zone[1] - MARGIN

            subimage = image[start_width:end_width, start_height:end_height]

            bgr_mean = get_bgr_value_subimage(subimage, np.mean)
            result[i].append(decide_color(bgr_mean))

            cv.imshow(f"{i}:{j}", subimage)
            sub_zone[0][0] += width_one_square

        sub_zone[0][0] = square_zone[0][0]
        sub_zone[0][1] += width_one_square

    return result

def decide_color(bgr_value):
    if bgr_value.mean() > 150 and np.std(bgr_value) < 40 :
        return Color.WHITE
    elif bgr_value[0] > 100 and bgr_value[1] < 60 and bgr_value[2] < 60:
        return Color.BLUE
    elif bgr_value[0] < 60 and bgr_value[1] > 110 and bgr_value[2] < 60:
        return Color.GREEN
    elif bgr_value[0] > 30 and bgr_value[0] < 60 and bgr_value[1] < 60 and bgr_value[2] > 150:
        return Color.RED
    elif bgr_value[0] < 20 and bgr_value[1] > 50 and bgr_value[1] > 100 and bgr_value[2] > 170:
        return Color.YELLOW
    elif bgr_value[0] < 20 and bgr_value[1] > 50 and bgr_value[1] < 100 and bgr_value[2] > 170:
        return Color.ORANGE

    return None

def get_bgr_value_subimage(subimage, math_func):
    bgr_mean = np.empty((3,))

    for i in range(0,3):
        bgr_mean[i] = math_func(subimage[:,:,i])

    return bgr_mean

if __name__ == '__main__':
    img = cv.imread('img/01.jpg', cv.IMREAD_COLOR)
    print(img.shape)
    cv.imshow(f"source", img)
    print(detect_color(img))
    cv.waitKey(0)
    cv.destroyAllWindows()
