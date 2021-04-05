import RPi.GPIO as GPIO
import time

def forward(tf):
    init()
    PWM = GPIO.PWM(Power, 100)  '100% power supplied'
    PWM.start(0)
    GPIO.output(Motor_1, True)
    GPIO.output(Motor_2, True)
    GPIO.output(Motor_3, True)
    GPIO.output(Motor_4, True)
    time.sleep(tf)

def forward_slow(tf):
    init()
    PWM = GPIO.PWM(Power, 20) '20% power supplied'
    PWM.start(0)
    GPIO.output(Motor_1, True)
    GPIO.output(Motor_2, True)
    GPIO.output(Motor_3, True)
    GPIO.output(Motor_4, True)
    time.sleep(tf)