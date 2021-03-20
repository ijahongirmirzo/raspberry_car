from car_details import *
import time

setup()
while get_distance() != 50:
    if get_distance() > 50:
        forward()
    elif get_distance() < 50:
        backward()


stop()

    