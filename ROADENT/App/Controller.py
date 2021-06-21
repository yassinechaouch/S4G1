import pygame

from ROADENT.App import Motor_1, Motor_2

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
                Motor_1.clockwise(5)
                Motor_2.c_clockwise(5)
            if(controller.get_button(12)): ## When DPAD-DOWN clicked
                print("DPADDOWN pressed -- Car goes backwards") ## motors start moving the car backwards
            if (controller.get_button(13)):  ## When DPAD-LEFT clicked
                print("DPADLEFT pressed -- Car goes left")
            if (controller.get_button(14)):  ## When DPAD-LEFT clicked
                print("DPADRIGHT pressed -- Car goes Right")
        elif(event.type == pygame.JOYBUTTONUP): ## when a button is released
            print("Car stops moving!") ## car stops moving
            Motor_1.stop()
            Motor_2.stop()