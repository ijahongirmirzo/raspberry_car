import time

from car_details import *

setup()
not_found_times = 0
slowness = 1.8
detection_count = 0
while True:
    trace = get_trace()
    if trace == RIGHT:
        detection_count += 1
        right()
    elif trace == LEFT:
        detection_count += 1
        left()
    elif trace == STRAIGHT:
        if detection_count != 0:
            detection_count -= 1
        else:
            slowness = 1.5
        forward(slowness)
    elif trace == STOP:
        stop()
    if detection_count >= 2:
        slowness = 2
    time.sleep(0.3)
