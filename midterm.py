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
        pass

    obstacle = car.get_obstacle()
    if obstacle == STOP:
        car.right_angle_turn(90)
        car.smooth_left()
        time.sleep(0.5)
        while True:
            car.forward(50)
            trace = car.get_trace()
            obstacle = car.get_obstacle()
            if obstacle == RIGHT or trace == LEFT:
                car.right()
            elif trace == LEFT:
                car.left()
            elif trace == FORWARD:
                car.forward(speed)
            elif trace == STOP:
                break
        car.stop()
        car.left_angle_turn(90)
        temp_trace_counter = 0
        while True:
            car.forward(50)
            trace = car.get_trace()
            if trace in [LEFT, RIGHT]:
                temp_trace_counter = + 1
            if trace in [LEFT, RIGHT, STOP] and temp_trace_counter >= 2:
                break
        car.stop()
        car.right_angle_turn(90)
        while True:
            trace = car.get_trace()
            if trace == RIGHT:
                car.right()
            elif trace == LEFT:
                car.left()
            elif trace == FORWARD:
                car.forward(speed)
            elif trace == STOP:
                break
        car.stop()

    # if not passed_ultra_obstacle:
    #     ultra_obstacle = car.get_distance()
    #     if ultra_obstacle <= 20:
    #         car.stop()
    #         while True:
    #             ultra_obstacle = car.get_distance()
    #             if ultra_obstacle > 20:
    #                 passed_ultra_obstacle = True
    #                 break

    # time.sleep(0.3)
