import RPi.GPIO as GPIO
import time

def forward(tf):
    init()
    PWM = GPIO.PWM(Power, 100)  '100% power supplied'
    PWM.start(0)
    GPIO.output(Motor_A+, True)
    GPIO.output(Motor_A-, False)
    GPIO.output(Motor_B+, True)
    GPIO.output(Motor_B-, False)
    time.sleep(tf)

def forward_slow(tf):
    init()
    PWM = GPIO.PWM(Power, 20) '20% power supplied'
    PWM.start(0)
    GPIO.output(Motor_A+, True)
    GPIO.output(Motor_A-, False)
    GPIO.output(Motor_B+, True)
    GPIO.output(Motor_B-, False)
    time.sleep(tf)