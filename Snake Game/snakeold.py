import pygame
import time

pygame.init()

# Set up the joystick
pygame.joystick.init()

buttons = []
button = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
joysticks = {}

# Get the number of joysticks
joystick_count = pygame.joystick.get_count()
print(joystick_count)


joystick = pygame.joystick.Joystick(0)
joystick.init()


## For each joystick:
#for i in range(joystick_count):
#    joystick = pygame.joystick.Joystick(i)
#    joystick.init()
#    for but in range(joystick.get_numbuttons()):
#        button.append(0)
#    print(joystick.get_button(0))




 # Main game loop
while True:
    for i in range(joystick_count):
#        joystick = pygame.joystick.Joystick(i)
        for but in button:
            button[but] = joystick.get_button(i)
#    print(button)
    print(joystick.get_button(0))
    time.sleep(0.1)
