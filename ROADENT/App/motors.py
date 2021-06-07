import time
import RPi.GPIO as GPIO


class Motor:
    def __init__(self, dir_pin, speed_pin):
        self.dir_pin= dir_pin
        self.speed_pin= speed_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.speed_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)

    def clockwise(self, tf):
        PWM = GPIO.PWM(self.speed_pin, 100)  # '100% power supplied'
        PWM.start(0)
        GPIO.output(self.dir_pin, True)
        time.sleep(tf)
        PWM.stop()

    def clockwise_slow(self, tf):
        PWM = GPIO.PWM(self.speed_pin, 50)  # '100% power supplied'
        PWM.start(0)
        GPIO.output(self.dir_pin, True)
        time.sleep(tf)
        PWM.stop()

    def c_clockwise(self, tf):
        PWM = GPIO.PWM(self.speed_pin, 100)  # '100% power supplied'
        PWM.start(0)
        GPIO.output(self.dir_pin, False)
        time.sleep(tf)
        PWM.stop()

    def stop():
        PWM = GPIO.PWM(self.speed_pin, 100)