import time

from car import Car
from constants import *

not_found_times = 0
speed = 70
detection_count = 0
stop_skip_counter = 0
car = Car()
passed_first_obstacle = False
passed_second_obstacle = False
passed_ultra_obstacle = False
is_returning = False
waiting_for_last_border = False
process_last_border = False
trace_stops = 0
# zebra_pass_count = 0
while True:
    trace = car.get_trace()
    if trace == RIGHT:
        car.right()
    elif trace == LEFT:
        car.left()
    elif trace == FORWARD:
        car.forward(speed)
    elif trace == STOP:
        if trace_stops <= 2:
            trace_stops += 1
            continue
        car.stop()
    obstacle = car.get_obstacle()
    if obstacle == STOP and passed_ultra_obstacle:
        car.left_angle_turn(180)

    if not passed_ultra_obstacle and CHECK_ULTRA_SONIC:
        # is_worked = False
        while car.get_distance() <= 5:
            car.stop()
            time.sleep(3)
            passed_ultra_obstacle = True
