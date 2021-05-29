import time

from car import Car

car = Car()
car.setup()
car.backward(50)
time.sleep(3)
car.stop()
