from car_details import *
import time
while True:
  trace = get_trace()
  print(trace)
  if trace == STRAIGHT:
      return forward()
  elif trace == RIGHT:
      return right()
  elif trace == LEFT:
      return left()
  elif trace == STOP:
      return stop()