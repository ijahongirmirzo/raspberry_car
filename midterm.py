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
