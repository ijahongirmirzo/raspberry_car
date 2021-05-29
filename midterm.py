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
            speed = 70
        car.forward(speed)
    elif trace == STOP:
        if passed_first_obstacle and passed_second_obstacle:
            # car.forward(30)
            # new_trace = car.get_trace()
            # if trace == STOP:
            car.stop()
        elif passed_first_obstacle and not passed_second_obstacle:
            car.stop()
            car.metered_backward(2)
            car.left_angle_turn(90)
            temp_speed = 40
            started_at = time.time()
            while True:
                trace = car.get_trace()
                print(f'It is final trace: {trace}')
                if trace == RIGHT:
                    car.right()
                elif trace == LEFT:
                    car.left()
                elif trace == FORWARD:
                    car.forward(temp_speed)
                elif trace == STOP:
                    car.stop()
                    break
            overall_time = int(time.time() - started_at)
            print(f'Time elapsed: {overall_time}')
            # exit()
            car.backward(temp_speed)
            time.sleep(overall_time)
            car.left_angle_turn(90)
            is_returning = True
            continue
    if detection_count >= 2:
        speed = 50
        detection_count = 4

    if not passed_first_obstacle or (not passed_second_obstacle and is_returning):
        obstacle = car.get_obstacle()
        if obstacle == STOP:
            car.stop()
            time.sleep(1)
            obstacle = car.get_obstacle()
            if obstacle in [STOP, RIGHT, LEFT]:
                if not passed_first_obstacle or not passed_second_obstacle:
                    car.right_angle_turn(90)
                    while True:
                        car.forward(40)
                        trace = car.get_trace()
                        if trace == STOP:
                            print('wrong 1')
                            car.metered_backward(4)
                            car.left_angle_turn(45)
                            obstacle = car.get_obstacle()
                            if obstacle in [FORWARD, LEFT, RIGHT]:
                                while True:
                                    trace = car.get_trace()
                                    print(f'current trace: {trace}')
                                    if trace == STOP:
                                        print('wrong 2')
                                        car.metered_backward(2)
                                        car.left_angle_turn(90)
                                        trace_count = 0
                                        while True:
                                            car.forward(40)
                                            trace = car.get_trace()
                                            if trace in [STOP, LEFT, RIGHT]:
                                                print('wrong 3')
                                                if trace_count == 0:
                                                    trace_count += 1
                                                    continue
                                                car.metered_backward(2)
                                                car.right_angle_turn(90)
                                                speed = 50
                                                break
                                        break
                                    elif trace == RIGHT:
                                        car.left()
                                    elif trace == LEFT:
                                        car.right()
                                    elif trace == FORWARD:
                                        car.forward(50)

                                if not passed_first_obstacle:
                                    passed_first_obstacle = True
                                if passed_first_obstacle and not passed_second_obstacle and is_returning:
                                    passed_second_obstacle = True
                                break
                            else:
                                car.right_angle_turn(90)
                                continue

            else:
                continue

    if not passed_ultra_obstacle:
        ultra_obstacle = car.get_distance()
        if ultra_obstacle <= 20:
            car.stop()
            while True:
                ultra_obstacle = car.get_distance()
                if ultra_obstacle > 20:
                    passed_ultra_obstacle = True
                    break

    # time.sleep(0.3)
