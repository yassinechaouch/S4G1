import pygame
from pygame.locals import *


pygame.init()
pygame.joystick.init()

controllers = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(controllers)

controller = pygame.joystick.Joystick(0)
controller.init()

if(pygame.joystick.get_init()):
    print("Joystick module initialized!")
else:
    print("Joystick module not initialized!")

while True:
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.JOYBUTTONDOWN): ## when a button is clicked
            if(controller.get_button(11)): ## When DPAD-UP clicked
                print("DPADUP pressed -- Car goes forwards") ## motors start moving the car forwards
            if(controller.get_button(12)): ## When DPAD-DOWN clicked
                print("DPADDOWN pressed -- Car goes backwards") ## motors start moving the car backwards
        elif(event.type == pygame.JOYBUTTONUP): ## when a button is released
            print("Car stops moving!") ## car stops moving