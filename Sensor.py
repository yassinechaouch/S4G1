import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

Led = 10
Sensor = 8

GPIO.setup(Led, GPIO.OUT)
GPIO.setup(Sensor, GPIO.IN)

if GPIO.input(Sensor):
    GPIO.output(Led,GPIO.HIGH)
else:
    GPIO.output(Led, GPIO.LOW)
