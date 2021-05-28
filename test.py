import time

from car_details import *

setup()
not_found_times = 0
slowness = 1.2
stop_skip_counter = 0
last_detected_at = None
while True:
    trace = get_trace()
    if trace == RIGHT:
        last_detected_at = time.time()
        slowness = 1.5
        right()
    elif trace == LEFT:
        last_detected_at = time.time()
        slowness = 1.5
        left()
    elif trace == STRAIGHT:
        if last_detected_at and time.time() - last_detected_at >= 1.5:
            slowness = 1.2
        forward(slowness)
    elif trace == STOP:
        forward()
        time.sleep(3)
    # time.sleep(0.3)
