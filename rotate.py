import time

from car import Car

car = Car()
car.setup()
ultra_obstacle = car.get_distance()
print(ultra_obstacle)
