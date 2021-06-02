#Libraries
import RPi.GPIO as GPIO
import time
class sensors():
    def __init__(self, echo_pin, trigger_pin):
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BOARD)

        # set GPIO Pins
        self.echo_pin = echo_pin
        self.trigger_pin = trigger_pin

        # set GPIO direction (IN / OUT)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)


    def distance():
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance


