import RPi.GPIO as GPIO
from time import sleep
from constants import *


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTOR_1, GPIO.OUT)
    GPIO.setup(MOTOR_2, GPIO.OUT)
    GPIO.setup(MOTOR_3, GPIO.OUT)
    GPIO.setup(MOTOR_4, GPIO.OUT)


def forward():
    GPIO.output(MOTOR_1, GPIO.HIGH)
    GPIO.output(MOTOR_2, GPIO.LOW)
    GPIO.output(MOTOR_3, GPIO.HIGH)
    GPIO.output(MOTOR_4, GPIO.LOW)


def backward():
    GPIO.output(MOTOR_1, GPIO.LOW)
    GPIO.output(MOTOR_2, GPIO.HIGH)
    GPIO.output(MOTOR_3, GPIO.LOW)
    GPIO.output(MOTOR_4, GPIO.HIGH)


def right():
    GPIO.output(MOTOR_1, GPIO.HIGH)
    GPIO.output(MOTOR_2, GPIO.LOW)
    GPIO.output(MOTOR_3, GPIO.LOW)
    GPIO.output(MOTOR_4, GPIO.HIGH)


def left():
    GPIO.output(MOTOR_1, GPIO.LOW)
    GPIO.output(MOTOR_2, GPIO.HIGH)
    GPIO.output(MOTOR_3, GPIO.HIGH)
    GPIO.output(MOTOR_4, GPIO.LOW)


def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    forward()
    backward()
    destroy()