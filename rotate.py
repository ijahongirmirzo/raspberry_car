import time

from car import Car

car = Car()
car.setup()
ultra_obstacle = car.get_distance()
if ultra_obstacle <= 30:
    car.stop()
    while True:
        ultra_obstacle = car.get_distance()
        if ultra_obstacle > 30:
            passed_ultra_obstacle = True
            car.forward(50)
            print('done')
            break
        else:
            print('still obstacle')
