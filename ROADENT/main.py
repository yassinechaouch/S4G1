



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

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()