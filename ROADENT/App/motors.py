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

    def clockwise(self, tf):
        pwm = GPIO.PWM(self.dir2_pin, 100)  # '100% power supplied'
        pwm.start(0)
        GPIO.output(self.dir_pin, True)
        time.sleep(tf)
        pwm.stop()

    def clockwise_slow(self, tf):
        pwm = GPIO.PWM(self.dir2_pin, 50)  # '100% power supplied'
        pwm.start(0)
        GPIO.output(self.dir_pin, True)
        time.sleep(tf)
        pwm.stop()

    def c_clockwise(self, tf):
        pwm = GPIO.PWM(self.dir2_pin, 100)  # '100% power supplied'
        pwm.start(0)
        GPIO.output(self.dir_pin, False)
        time.sleep(tf)
        pwm.stop()

    def stop(self):
        pwm = GPIO.PWM(self.dir2_pin, 0)
        pwm.stop()

