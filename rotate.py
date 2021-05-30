import time

from car import Car

car = Car()
car.setup()
# car.right_angle_turn(90)

while True:
    print(car.get_distance())