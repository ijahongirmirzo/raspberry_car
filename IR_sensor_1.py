from car_details import *
import time
forward()
while True:
  trace = get_trace()
  if trace == STOP:
    break
    
backward()
time.sleep(3)
right()
time.sleep(3.5)
stop()  
