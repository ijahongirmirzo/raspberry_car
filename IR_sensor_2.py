from car_details import *
import time

setup()
while True:
    if get_distance() > 50:
        forward()
    elif get_distance() < 50:
        backward()
    elif get_distance() == 50:
        stop()

    