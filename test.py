import time

from car_details import forward, stop, setup, smooth_left

setup()
forward()
time.sleep(5)
smooth_left()
time.sleep(2)
stop()
