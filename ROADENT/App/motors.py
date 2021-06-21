import sys
import time
import RPi.GPIO as GPIO

mode = GPIO.getmode()

GPIO.cleanup

Motor1_Forward = 26
Motor1_Backward = 24

Motor2_Forward = 37
Motor2_Backward = 34

sleeptime = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1_Forward, GPIO.OUT)
GPIO.setup(Motor1_Backward, GPIO.OUT)

GPIO.setup(Motor2_Forward, GPIO.OUT)
GPIO.setup(Motor2_Backward, GPIO.OUT)


def forward(x):
    GPIO.output(Motor1_Forward, GPIO.HIGH)
    GPIO.output(Motor2_Forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Motor1_Forward, GPIO.LOW)
    GPIO.output(Motor2_Forward, GPIO.LOW)


def reverse(x):
    GPIO.output(Motor1_Backward, GPIO.HIGH)
    GPIO.output(Motor2_Backward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Motor1_Backward, GPIO.LOW)
    GPIO.output(Motor2_Backward, GPIO.LOW)


while True:
    forward(5)
    reverse(5)
    GPIO.cleanup()

'''
# Method 2:

import RPi.GPIO as GPIO
from gpiozero import 
import time

motor_1 = Motor(forward = 4, backward = 14)
motor_2 = Motor(forward = 14, backward = 27)

motor_1.forward()
motor_2.backward()

motor_1.stop()
motor_2.stop()


'''

import time
import RPi.GPIO as GPIO


class Motor:
    def __init__(self, dir_pin, speed_pin):
        self.dir_pin = dir_pin
        self.speed_pin = speed_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.speed_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)

    def clockwise(self, tf):
        pwm = GPIO.PWM(self.speed_pin, 100)  # '100% power supplied'
        pwm.start(0)
        GPIO.output(self.dir_pin, True)
        time.sleep(tf)
        pwm.stop()

    def clockwise_slow(self, tf):
        pwm = GPIO.PWM(self.speed_pin, 50)  # '100% power supplied'
        pwm.start(0)
        GPIO.output(self.dir_pin, True)
        time.sleep(tf)
        pwm.stop()

    def c_clockwise(self, tf):
        pwm = GPIO.PWM(self.speed_pin, 100)  # '100% power supplied'
        pwm.start(0)
        GPIO.output(self.dir_pin, False)
        time.sleep(tf)
        pwm.stop()

    def stop(self):
        pwm = GPIO.PWM(self.speed_pin, 0)
        pwm.stop()
'''
