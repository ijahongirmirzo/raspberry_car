import time

from car import Car

car = Car()
car.setup()
while True:
    obstacle = car.get_obstacle()
    print(obstacle)
    time.sleep(1)
