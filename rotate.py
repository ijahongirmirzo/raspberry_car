import time

from car import Car

car = Car()
car.setup()
car.left_angle_turn(90)

time.sleep(3)
car.right_angle_turn(90)
