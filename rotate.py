import time

from car import Car

car = Car()
car.setup()
while True:
    car.backward(50)

