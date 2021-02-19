from gpiozero import LED
from time import sleep

red_led =LED(14) '''GPIO14'''
blue_led = LED(15) '''GPIO15'''

while True:
    red_led.on()
    sleep(1)
    red_led.off()
    blue_led.on()
    sleep(1)
    blue_led.off()