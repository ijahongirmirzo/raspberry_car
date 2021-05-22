import wiringpi
import time

# Pins for Motor Driver Inputs
motor_1 = 1
motor_2 = 4
motor_3 = 5
motor_4 = 6
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
trig_pin = 28
echo_pin = 29

left_tracer_pin = 10
right_tracer_pin = 11

STOP = 0
STREIGHT = 1
RIGHT = 2
LEFT = 3


def setup():
    wiringpi.wiringPiSetup() 
    wiringpi.pinMode(motor_1, io.OUTPUT)
    wiringpi.pinMode(motor_2, io.OUTPUT)
    wiringpi.pinMode(motor_3, io.OUTPUT)
    wiringpi.pinMode(motor_4, io.OUTPUT)

    wiringpi.pinMode(trig_pin, io.OUTPUT)
    wiringpi.pinMode(echo_pin, io.INPUT)

    wiringpi.pinMode(left_tracer_pin, io.INPUT)
    wiringpi.pinMode(right_tracer_pin, io.INPUT)



def forward():
    # Going forwards
    print('forward')
    wiringpi.digitalWrite(motor_1, io.HIGH)
    wiringpi.digitalWrite(motor_2, io.LOW)
    wiringpi.digitalWrite(motor_3, io.HIGH)
    wiringpi.digitalWrite(motor_4, io.LOW)

def stop():
    print('stop')
    wiringpi.digitalWrite(motor_1, io.LOW)
    wiringpi.digitalWrite(motor_2, io.LOW)
    wiringpi.digitalWrite(motor_3, io.LOW)
    wiringpi.digitalWrite(motor_4, io.LOW)

def right():
    print('right')
    wiringpi.digitalWrite(motor_1, io.HIGH)
    wiringpi.digitalWrite(motor_2, io.LOW)
    wiringpi.digitalWrite(motor_3, io.LOW)
    wiringpi.digitalWrite(motor_4, io.HIGH)

def left():
    print('left')
    wiringpi.digitalWrite(motor_1, io.LOW)
    wiringpi.digitalWrite(motor_2, io.HIGH)
    wiringpi.digitalWrite(motor_3, io.HIGH)
    wiringpi.digitalWrite(motor_4, io.LOW)

def backward():
    print('backward')
    wiringpi.digitalWrite(motor_1, io.LOW)
    wiringpi.digitalWrite(motor_2, io.HIGH)
    wiringpi.digitalWrite(motor_3, io.LOW)
    wiringpi.digitalWrite(motor_4, io.HIGH)

def get_distance():
    start_time, end_time = 0, 0
    distance = 0.0
    wiringpi.digitalWrite(trig_pin, io.HIGH)
    time.sleep(0.00001)
    wiringpi.digitalWrite(trig_pin, io.LOW)

    while wiringpi.digitalRead(echo_pin) == 0:
        start_time = time.time()

    while wiringpi.digitalRead(echo_pin) == 1:
        end_time = time.time()

    distance = (end_time - start_time) * 34300 / 2

    return abs(distance)

def get_trace():
    left_tracer = int(wiringpi.digitalRead(left_tracer_pin))
    right_tracer = int(wiringpi.digitalRead(right_tracer_pin))
    white = 0
    not_white = 1
    print(left_tracer)
    print(right_tracer)
    if left_tracer == white and right_tracer == not_white:
        return RIGHT
    elif right_tracer == white and left_tracer == not_white:
        return LEFT
    elif right_tracer == white and left_tracer == white:
        return STREIGHT
    elif right_tracer == not_white and left_tracer == not_white:
        return STOP
    

# if __name__ == '__main__':
#     setup()
#     forward()
#     time.sleep(2)
#     backward()
#     time.sleep(2)
#     right()
#     time.sleep(3)
#     left()
#     time.sleep(3)
#     stop()
