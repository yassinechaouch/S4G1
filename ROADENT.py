import RPi.GPIO as GPIO
import time

Motor_1 = 3
Motor_2 = 5
Motor_3 = 7
Motor_4 = 9
Power   = 8  'variable that allows power to go to the motors as it is connected to the VCC pin.'

'tf is the time frame the motor runs for.'
def init(tf):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Motor_1, GPIO.OUT)
    GPIO.setup(Motor_2, GPIO.OUT)
    GPIO.setup(Motor_3, GPIO.OUT)
    GPIO.setup(Motor_4, GPIO.OUT)
    GPIO.setup(Power, GPIO.OUT)
    time.sleep(tf)

'Pulse Width modulation (PWM) controls the amount of power supplied to the motors'

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

forward(1)
forward_slow(1)
GPIO.cleanup()

'Code is not finalized, we need to know which motor is which. As from research it appears two of the motors'
'Go reverse on their own, therefore we need to test which motors do that. it simplifies the code greatly.'





'''GPIO.setmode(GPIO.BOARD)

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

#To set the rA-direction forward
GPIO.output(MotorA+, True)
GPIO.output(MotorB+, True)
GPIO.output(Moto, True)
GPIO.output(MotorB-, True)

#runs forward at 50% power for 2 seconds
GPIO.output(enable, True)
sleep(2)'''