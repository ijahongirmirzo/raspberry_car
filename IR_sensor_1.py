from car_details import *
import time

setup()
while get_distance() >= 30:
    forward()

right()
time.sleep(2)
forward()
time.sleep(2)
stop()

    