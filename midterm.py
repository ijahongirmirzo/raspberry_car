import time

from car import Car
from constants import *

not_found_times = 0
speed = 75
detection_count = 0
stop_skip_counter = 0
car = Car()
passed_first_obstacle = False
passed_second_obstacle = False
zebra_pass_count = 0
while True:
    trace = car.get_trace()
    if trace == RIGHT:
        detection_count += 1
        car.right()
    elif trace == LEFT:
        detection_count += 1
        car.left()
    elif trace == STRAIGHT:
        if detection_count != 0:
            detection_count -= 1
        else:
            speed = 75
        car.forward(speed)
    elif trace == STOP:
        if zebra_pass_count >= 2:
            car.forward(30)
            new_trace = car.get_trace()
            if trace == STOP:
                car.stop()
        elif not passed_first_obstacle or \
                (passed_first_obstacle, passed_second_obstacle):
            car.forward(30)
            time.sleep(3)
            zebra_pass_count += 1
        elif passed_first_obstacle and not passed_second_obstacle:
            car.stop()
            time.sleep(1)
            car.backward(50)
            time.sleep(3)
            car.left_angle_turn(90)
            car.forward(50)
    if detection_count >= 2:
        speed = 50

    obstacle = car.get_obstacle()
    if obstacle == STOP:
        car.stop()
        time.sleep(3)
        obstacle = car.get_obstacle()
        if obstacle == STOP:
            if not passed_first_obstacle:
                car.right_angle_turn(90)
                while True:
                    car.forward(50)
                    trace = car.get_trace()
                    if trace == STOP:
                        car.metered_backward(2)
                        car.left_angle_turn(90)
                        obstacle = car.get_obstacle()
                        if obstacle == STRAIGHT:
                            car.forward(50)
                            while True:
                                trace = car.get_trace()
                                if trace == STOP:
                                    car.metered_backward(2)
                                    car.left_angle_turn(90)
                                    car.forward(30)
                                    trace_count = 0
                                    while True:
                                        trace = car.get_trace()
                                        if trace in [STOP, LEFT, RIGHT]:
                                            if trace_count == 0:
                                                trace_count += 1
                                                continue
                                            car.right_angle_turn(90)
                                            car.forward(50)
                                            break
                                    break
                            passed_first_obstacle = True
                            break
                        else:
                            car.right_angle_turn(90)
                            continue

            elif not passed_second_obstacle:
                pass

        else:
            continue

    # time.sleep(0.3)
