# precalculated by measuring
from constants import *


def angle_to_time(angle):
    if angle == 90:
        return 0.40
    elif angle == 45:
        return 0.20


def cm_to_time(cm):
    return cm * CM_PER_SECOND

# def traced_movement(trace, car, speed=50):
#     if trace == RIGHT:
#         car.right()
#     elif trace == LEFT:
#         car.left()
#     elif trace == FORWARD:
#         car.forward(speed)
#     elif trace == STOP:
#         pass
