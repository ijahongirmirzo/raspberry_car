from car_details import *
import time

setup()
while get_distance() >= 30:
    go_forward()

right()
time.sleep(2)
go_forward()
time.sleep(2)
stop()

    