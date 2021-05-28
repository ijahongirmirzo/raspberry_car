import time

from car_details import get_obstacle

while True:
    get_obstacle()
    time.sleep(0.5)
    print('---------')