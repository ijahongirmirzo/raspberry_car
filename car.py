import time

import wiringpi as wp
from constants import *
from utils import angle_to_time, cm_to_time

gpio = wp.GPIO(wp.GPIO.WPI_MODE_PINS)


class Car:
    def __init__(self):
        self.setup()

    def setup(self):
        wp.wiringPiSetup()
        for pin in OUTPUTS:
            wp.pinMode(pin, 1)
        for pin in INPUTS:
            wp.pinMode(pin, gpio.INPUT)

        wp.softPwmCreate(MOTOR_1, MIN_SPEED, MAX_SPEED)
        wp.softPwmCreate(MOTOR_2, MIN_SPEED, MAX_SPEED)
        wp.softPwmCreate(MOTOR_3, MIN_SPEED, MAX_SPEED)
        wp.softPwmCreate(MOTOR_4, MIN_SPEED, MAX_SPEED)

    def forward(self, speed=100):
        wp.softPwmWrite(MOTOR_1, int(MAX_SPEED / (100 / speed)))
        wp.softPwmWrite(MOTOR_2, MIN_SPEED)
        wp.softPwmWrite(MOTOR_3, int(MAX_SPEED / (100 / speed)))
        wp.softPwmWrite(MOTOR_4, MIN_SPEED)

    def stop(self):
        wp.softPwmWrite(MOTOR_1, MIN_SPEED)
        wp.softPwmWrite(MOTOR_2, MIN_SPEED)
        wp.softPwmWrite(MOTOR_3, MIN_SPEED)
        wp.softPwmWrite(MOTOR_4, MIN_SPEED)

    def right(self):
        wp.softPwmWrite(MOTOR_1, MAX_SPEED)
        wp.softPwmWrite(MOTOR_2, MIN_SPEED)
        wp.softPwmWrite(MOTOR_3, MIN_SPEED)
        wp.softPwmWrite(MOTOR_4, MAX_SPEED)

    def left(self):
        wp.softPwmWrite(MOTOR_1, MIN_SPEED)
        wp.softPwmWrite(MOTOR_2, MAX_SPEED)
        wp.softPwmWrite(MOTOR_3, MAX_SPEED)
        wp.softPwmWrite(MOTOR_4, MIN_SPEED)

    def backward(self, speed=1):
        wp.softPwmWrite(MOTOR_1, MIN_SPEED)
        wp.softPwmWrite(MOTOR_2, int(MAX_SPEED / (100 / speed)))
        wp.softPwmWrite(MOTOR_3, MIN_SPEED)
        wp.softPwmWrite(MOTOR_4, int(MAX_SPEED / (100 / speed)))

    def smooth_left(self):
        wp.softPwmWrite(MOTOR_1, int(MAX_SPEED / 4))
        wp.softPwmWrite(MOTOR_2, MIN_SPEED)
        wp.softPwmWrite(MOTOR_3, int(MAX_SPEED))
        wp.softPwmWrite(MOTOR_4, MIN_SPEED)

    def smooth_right(self):
        wp.softPwmWrite(MOTOR_1, MAX_SPEED)
        wp.softPwmWrite(MOTOR_2, MIN_SPEED)
        wp.softPwmWrite(MOTOR_3, int(MAX_SPEED / 8))
        wp.softPwmWrite(MOTOR_4, MIN_SPEED)

    def get_distance(self):
        start_time, end_time = 0, 0
        wp.digitalWrite(trig_pin, gpio.HIGH)
        time.sleep(0.00001)
        wp.digitalWrite(trig_pin, gpio.LOW)

        while wp.digitalRead(echo_pin) == 0:
            start_time = time.time()

        while wp.digitalRead(echo_pin) == 1:
            end_time = time.time()

        distance = (end_time - start_time) * 34300 / 2
        return round(distance)

    def get_trace(self):
        left_tracer = int(wp.digitalRead(LEFT_TRACER))
        right_tracer = int(wp.digitalRead(RIGHT_TRACER))
        if left_tracer == NOT_BLACK and right_tracer == BLACK:
            return RIGHT
        elif right_tracer == NOT_BLACK and left_tracer == BLACK:
            return LEFT
        elif right_tracer == BLACK and left_tracer == BLACK:
            return FORWARD
        elif right_tracer == NOT_BLACK and left_tracer == NOT_BLACK:
            return STOP

    def get_obstacle(self):
        left_ir = int(wp.digitalRead(LEFT_IR))
        right_ir = int(wp.digitalRead(RIGHT_IR))
        if left_ir == OBSTACLE and right_ir == NOT_OBSTACLE:
            return LEFT
        elif left_ir == NOT_OBSTACLE and right_ir == OBSTACLE:
            return RIGHT
        elif left_ir == NOT_OBSTACLE and right_ir == NOT_OBSTACLE:
            return FORWARD
        elif left_ir == OBSTACLE and right_ir == OBSTACLE:
            return STOP

    def right_angle_turn(self, angle):
        self.right()
        time.sleep(angle_to_time(angle))
        self.stop()

    def left_angle_turn(self, angle):
        self.left()
        time.sleep(angle_to_time(angle))
        self.stop()

    def metered_forward(self, cm):
        self.forward(50)
        time.sleep(cm_to_time(cm))
        self.stop()

    def metered_backward(self, cm):
        self.backward(50)
        time.sleep(cm_to_time(cm))
        self.stop()
