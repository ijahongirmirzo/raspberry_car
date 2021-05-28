import wiringpi
import time

# Pins for Motor Driver Inputs
from constants import *

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)


def setup():
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(MOTOR_1, 1)
    wiringpi.pinMode(MOTOR_2, 1)
    wiringpi.pinMode(MOTOR_3, 1)
    wiringpi.pinMode(MOTOR_4, 1)

    wiringpi.softPwmCreate(MOTOR_1, MIN_SPEED, MAX_SPEED)
    wiringpi.softPwmCreate(MOTOR_2, MIN_SPEED, MAX_SPEED)
    wiringpi.softPwmCreate(MOTOR_3, MIN_SPEED, MAX_SPEED)
    wiringpi.softPwmCreate(MOTOR_4, MIN_SPEED, MAX_SPEED)

    wiringpi.pinMode(trig_pin, io.OUTPUT)
    wiringpi.pinMode(echo_pin, io.INPUT)

    wiringpi.pinMode(LEFT_TRACER, io.INPUT)
    wiringpi.pinMode(RIGHT_TRACER, io.INPUT)


def forward(slowness_time=1):
    print('forward')
    wiringpi.softPwmWrite(MOTOR_1, int(MAX_SPEED / slowness_time))
    wiringpi.softPwmWrite(MOTOR_2, MIN_SPEED)
    wiringpi.softPwmWrite(MOTOR_3, int(MAX_SPEED / slowness_time))
    wiringpi.softPwmWrite(MOTOR_4, MIN_SPEED)


def stop():
    print('stop')
    wiringpi.softPwmWrite(MOTOR_1, MIN_SPEED)
    wiringpi.softPwmWrite(MOTOR_2, MIN_SPEED)
    wiringpi.softPwmWrite(MOTOR_3, MIN_SPEED)
    wiringpi.softPwmWrite(MOTOR_4, MIN_SPEED)


def right():
    print('right')
    wiringpi.softPwmWrite(MOTOR_1, MAX_SPEED)
    wiringpi.softPwmWrite(MOTOR_2, MIN_SPEED)
    wiringpi.softPwmWrite(MOTOR_3, MIN_SPEED)
    wiringpi.softPwmWrite(MOTOR_4, MAX_SPEED)


def left():
    print('left')
    wiringpi.softPwmWrite(MOTOR_1, MIN_SPEED)
    wiringpi.softPwmWrite(MOTOR_2, MAX_SPEED)
    wiringpi.softPwmWrite(MOTOR_3, MAX_SPEED)
    wiringpi.softPwmWrite(MOTOR_4, MIN_SPEED)


def backward(slowness_time=1):
    print('backward')
    wiringpi.softPwmWrite(MOTOR_1, MIN_SPEED)
    wiringpi.softPwmWrite(MOTOR_2, int(MAX_SPEED / slowness_time))
    wiringpi.softPwmWrite(MOTOR_3, MIN_SPEED)
    wiringpi.softPwmWrite(MOTOR_4, int(MAX_SPEED / slowness_time))


def smooth_left():
    print('smooth left')
    wiringpi.softPwmWrite(MOTOR_1, int(MAX_SPEED / 8))
    wiringpi.softPwmWrite(MOTOR_2, MIN_SPEED)
    wiringpi.softPwmWrite(MOTOR_3, MAX_SPEED)
    wiringpi.softPwmWrite(MOTOR_4, MIN_SPEED)


def smooth_right():
    print('smooth right')
    wiringpi.softPwmWrite(MOTOR_1, MAX_SPEED)
    wiringpi.softPwmWrite(MOTOR_2, MIN_SPEED)
    wiringpi.softPwmWrite(MOTOR_3, int(MAX_SPEED / 8))
    wiringpi.softPwmWrite(MOTOR_4, MIN_SPEED)


def get_distance():
    start_time, end_time = 0, 0
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
    left_tracer = int(wiringpi.digitalRead(LEFT_TRACER))
    right_tracer = int(wiringpi.digitalRead(RIGHT_TRACER))
    if left_tracer == NOT_BLACK and right_tracer == BLACK:
        return LEFT
    elif right_tracer == NOT_BLACK and left_tracer == BLACK:
        return RIGHT
    elif right_tracer == NOT_BLACK and left_tracer == NOT_BLACK:
        return STRAIGHT
    elif right_tracer == BLACK and left_tracer == BLACK:
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
