import time
import RPi.GPIO as GPIO


class Motor:
    def __init__(self, dir_pin, dir2_pin):
        self.dir_pin = dir_pin
        #self.speed_pin = speed_pin
        self.dir2_pin= dir2_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.dir2_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)

    def clockwise(self):
        GPIO.output(self.dir_pin, True)
        GPIO.output(self.dir2_pin, False)       

    def c_clockwise(self):
        GPIO.output(self.dir_pin, False)
        GPIO.output(self.dir2_pin, True)

    def stop(self):
        GPIO.output(self.dir_pin, False)
        GPIO.output(self.dir2_pin, False)

