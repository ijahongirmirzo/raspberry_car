from car_details import *
detected_line_count = 0
while True:
  trace = get_trace()
  if trace == STRAIGHT:
    detected_line_count = detected_line_count + 1
  if detected_line_count >= 2:
    stop()
    break
  forward()
