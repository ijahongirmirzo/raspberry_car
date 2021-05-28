import time

from car_details import *

setup()
not_found_times = 0
while True:
    trace = get_trace()
    if trace == RIGHT:
        right()
    elif trace == LEFT:
        left()
    elif trace == STRAIGHT:
        forward(1.8)
    elif trace == STOP:
        stop()
    time.sleep(0.3)
