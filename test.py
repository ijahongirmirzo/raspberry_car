import time

from car_details import *

setup()
not_found_times = 0
while True:
    trace = get_trace()
    if trace == RIGHT:
        not_found_times = 0
        right()
    elif trace == LEFT:
        not_found_times = 0
        left()
    elif trace == STRAIGHT:
        not_found_times = 0
        forward(2)
    elif trace == STOP:
        if not_found_times <= 5:
            forward(3)
            not_found_times += 1
        else:
            stop()
