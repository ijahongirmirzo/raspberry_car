import time

from car_details import *

setup()
not_found_times = 0
while True:
    trace = get_trace()
    if trace == RIGHT:
        not_found_times = 0
        right()
        time.sleep(0.5)
    elif trace == LEFT:
        not_found_times = 0
        left()
        time.sleep(0.5)
    elif trace == STRAIGHT:
        not_found_times = 0
        forward(2)
    elif trace == STOP:
        if not_found_times <= 5:
            backward(2)
            not_found_times += 1
        else:
            stop()
