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
passed_ultra_obstacle = False
# zebra_pass_count = 0
while True:
    trace = car.get_trace()
    if trace == RIGHT:
        detection_count += 1
        car.right()
    elif trace == LEFT:
        detection_count += 1
        car.left()
    elif trace == FORWARD:
        if detection_count != 0:
            detection_count -= 1
        else:
            speed = 75
        car.forward(speed)
    elif trace == STOP:
        if passed_first_obstacle and passed_second_obstacle:
            # car.forward(30)
            # new_trace = car.get_trace()
            # if trace == STOP:
            car.stop()
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
        time.sleep(1)
        obstacle = car.get_obstacle()
        if obstacle == STOP:
            if not passed_first_obstacle or not passed_second_obstacle:
                car.right_angle_turn(90)
                while True:
                    car.forward(50)
                    trace = car.get_trace()
                    if trace == STOP:
                        car.metered_backward(2)
                        car.left_angle_turn(90)
                        obstacle = car.get_obstacle()
                        if obstacle == FORWARD:
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
                            if not passed_first_obstacle:
                                passed_first_obstacle = True
                            if not passed_second_obstacle:
                                passed_second_obstacle = True
                            break
                        else:
                            car.right_angle_turn(90)
                            continue

        else:
            continue

    if not passed_ultra_obstacle:
        ultra_obstacle = car.get_distance()
        if ultra_obstacle <= 30:
            car.stop()
            while True:
                ultra_obstacle = car.get_distance()
                if ultra_obstacle > 30:
                    passed_ultra_obstacle = True
                    car.forward(50)
                    break

    # time.sleep(0.3)
