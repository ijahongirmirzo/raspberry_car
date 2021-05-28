import wiringpi as wp
from constants import *

gpio = wp.GPIO(wp.GPIO.WPI_MODE_PINS)


class Car:
    def __init__(self):
        self.setup()

    def setup(self):
        wp.wiringPiSetup()
        for pin in OUTPUTS:
            wp.digitalWrite(pin, gpio.OUTPUT)
        for pin in INPUTS:
            wp.digitalWrite(pin, gpio.INPUT)

    def set_pwm(self, pin_number, value):
        pass