import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

MotorA+ = 3
MotorA- = 5
MotorB+ = 7
MotorB- = 9
enable = 8

GPIO.setup(MotorA+, GPIO.OUT)
GPIO.setup(MotorB+, GPIO.OUT)
GPIO.setup(MotorA-, GPIO.OUT)
GPIO.setup(MotorB-, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)

pwm=GPIO.PWM(enable, 100)
pwm.start(0)

#To set the direction forward
GPIO.output(MotorA+, True)
GPIO.output(MotorB+, True)
GPIO.output(MotorA-, True)
GPIO.output(MotorB-, True)

#runs forward at 50% power for 2 seconds
GPIO.output(enable, True)
sleep(2)