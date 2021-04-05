import RPi.GPIO as GPIO
import time

Motor_1 = 3
Motor_2 = 5
Motor_3 = 7
Motor_4 = 9
Power   = 8  'variable that allows power to go to the motors as it is connected to the VCC pin.'

'tf is the time frame the motor runs for.'
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Motor_1, GPIO.OUT)
    GPIO.setup(Motor_2, GPIO.OUT)
    GPIO.setup(Motor_3, GPIO.OUT)
    GPIO.setup(Motor_4, GPIO.OUT)
    GPIO.setup(Power, GPIO.OUT)

'Pulse Width modulation (PWM) controls the amount of power supplied to the motors'