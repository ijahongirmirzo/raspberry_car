from car_details import *
from constants import STOP

forward()
while True:
  trace = get_trace()
  if trace == STOP:
    detected_line_count = detected_line_count + 1
  if detected_line_count >= 2:
    stop()
    break
