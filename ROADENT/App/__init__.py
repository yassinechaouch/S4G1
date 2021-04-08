import RPi.GPIO as GPIO
import time

Motor_A+ = 3
Motor_A- = 5
Motor_B+ = 7
Motor_B- = 11
Power   = 2  'variable that allows power to go to the motors as it is connected to the VCC pin.'

'tf is the time frame the motor runs for.'
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Motor_A+, GPIO.OUT)
    GPIO.setup(Motor_A-, GPIO.OUT)
    GPIO.setup(Motor_B+, GPIO.OUT)
    GPIO.setup(Motor_B-, GPIO.OUT)
    GPIO.setup(Power, GPIO.OUT)

'Pulse Width modulation (PWM) controls the amount of power supplied to the motors'