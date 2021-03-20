from car_details import *
import time

setup()
while True:
    distance = get_distance()
    if distance > 49 and distance < 51:
        stop()
        time.sleep(0.5)
    elif distance > 50:
        forward()
    elif distance < 50:
        backward()


    