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
    if obstacle == STOP and \
            (passed_ultra_obstacle or
             (not passed_first_obstacle or
              not passed_second_obstacle)):
        car.backward(2)
        car.right_angle_turn(90)
        car.forward(50)
        time.sleep(0.8)
        car.left_angle_turn(90)
        # car.stop()
        while True:
            car.forward(10)
            trace = car.get_trace()
            obstacle = car.get_obstacle()
            if obstacle == RIGHT or trace == RIGHT:
                car.right()
            elif trace == LEFT:
                car.left()
            elif trace == FORWARD:
                car.forward(10)
            elif trace == STOP:
                break
        car.stop()
        car.metered_backward(1)
        car.left_angle_turn(90)
        car.forward(50)
        time.sleep(0.8)
        while True:
            trace = car.get_trace()
            if trace in [LEFT, RIGHT, STOP]:
                break
        car.stop()
        car.metered_backward(1)
        car.right_angle_turn(90)
        if not passed_first_obstacle:
            while True:
                trace = car.get_trace()
                if trace == RIGHT:
                    car.right()
                elif trace == LEFT:
                    car.left()
                elif trace == FORWARD:
                    car.forward(50)
                elif trace == STOP:
                    break
            car.stop()
            car.metered_backward(1)
            car.left_angle_turn(90)
            started_at = time.time()  #
            while True:
                trace = car.get_trace()
                if trace == RIGHT:
                    car.right()
                elif trace == LEFT:
                    car.left()
                elif trace == FORWARD:
                    car.forward(50)
                elif trace == STOP:
                    break
            car.stop()
            elapsed_time = int(time.time() - started_at)
            time.sleep(1)
            car.backward(50)
            time.sleep(elapsed_time)
            car.left_angle_turn(90)
            passed_first_obstacle = True

    if not passed_ultra_obstacle and CHECK_ULTRA_SONIC:
        ultra_obstacle = car.get_distance()
        if ultra_obstacle <= 20:
            car.stop()
            while True:
                ultra_obstacle = car.get_distance()
                if ultra_obstacle > 20:
                    passed_ultra_obstacle = True
                    break
