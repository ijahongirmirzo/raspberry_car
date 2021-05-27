import wiringpi
import time

# Pins for Motor Driver Inputs
from constants import *

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)


def setup():
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(MOTOR_1, io.OUTPUT)
    wiringpi.pinMode(MOTOR_2, io.OUTPUT)
    wiringpi.pinMode(MOTOR_3, io.OUTPUT)
    wiringpi.pinMode(MOTOR_4, io.OUTPUT)

    wiringpi.softPwmCreate(MOTOR_1, MIN_SPEED, MAX_SPEED)
    wiringpi.softPwmCreate(MOTOR_2, MIN_SPEED, MAX_SPEED)
    wiringpi.softPwmCreate(MOTOR_3, MIN_SPEED, MAX_SPEED)
    wiringpi.softPwmCreate(MOTOR_4, MIN_SPEED, MAX_SPEED)

    wiringpi.pinMode(trig_pin, io.OUTPUT)
    wiringpi.pinMode(echo_pin, io.INPUT)

    wiringpi.pinMode(LEFT_TRACER, io.INPUT)
    wiringpi.pinMode(RIGHT_TRACER, io.INPUT)


def forward():
    print('forward')
    wiringpi.digitalWrite(MOTOR_1, io.HIGH)
    wiringpi.digitalWrite(MOTOR_2, io.LOW)
    wiringpi.digitalWrite(MOTOR_3, io.HIGH)
    wiringpi.digitalWrite(MOTOR_4, io.LOW)


def stop():
    print('stop')
    wiringpi.digitalWrite(MOTOR_1, io.LOW)
    wiringpi.digitalWrite(MOTOR_2, io.LOW)
    wiringpi.digitalWrite(MOTOR_3, io.LOW)
    wiringpi.digitalWrite(MOTOR_4, io.LOW)


def right():
    print('right')
    wiringpi.digitalWrite(MOTOR_1, io.HIGH)
    wiringpi.digitalWrite(MOTOR_2, io.LOW)
    wiringpi.digitalWrite(MOTOR_3, io.LOW)
    wiringpi.digitalWrite(MOTOR_4, io.HIGH)


def left():
    print('left')
    wiringpi.digitalWrite(MOTOR_1, io.LOW)
    wiringpi.digitalWrite(MOTOR_2, io.HIGH)
    wiringpi.digitalWrite(MOTOR_3, io.HIGH)
    wiringpi.digitalWrite(MOTOR_4, io.LOW)


def backward():
    print('backward')
    wiringpi.digitalWrite(MOTOR_1, io.LOW)
    wiringpi.digitalWrite(MOTOR_2, io.HIGH)
    wiringpi.digitalWrite(MOTOR_3, io.LOW)
    wiringpi.digitalWrite(MOTOR_4, io.HIGH)


def smooth_left():
    wiringpi.softPwmWrite(MOTOR_1, int(MAX_SPEED / 8))
    wiringpi.softPwmWrite(MOTOR_2, MAX_SPEED)
    wiringpi.softPwmWrite(MOTOR_3, MAX_SPEED)
    wiringpi.softPwmWrite(MOTOR_4, MIN_SPEED)


def slow_forward():
    wiringpi.pwmWrite(MOTOR_1, 200)
    wiringpi.digitalWrite(MOTOR_1, io.HIGH)
    wiringpi.digitalWrite(MOTOR_2, io.LOW)
    wiringpi.digitalWrite(MOTOR_3, io.HIGH)
    wiringpi.digitalWrite(MOTOR_4, io.LOW)


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
    left_tracer = int(wiringpi.digitalRead(LEFT_TRACER))
    right_tracer = int(wiringpi.digitalRead(RIGHT_TRACER))
    if left_tracer == WHITE and right_tracer == NOT_WHITE:
        return RIGHT
    elif right_tracer == WHITE and left_tracer == NOT_WHITE:
        return LEFT
    elif right_tracer == WHITE and left_tracer == WHITE:
        return STRAIGHT
    elif right_tracer == NOT_WHITE and left_tracer == NOT_WHITE:
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
