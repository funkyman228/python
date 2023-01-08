import pygame

pygame.init()

# Set up the joystick
pygame.joystick.init()

# Get the number of joysticks
joystick_count = pygame.joystick.get_count()
print(joystick_count)

# For each joystick:
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()



joystick = 0
# Main game loop
while True:
    for joystick in range(joystick_count):
        joystickob = pygame.joystick.Joystick(joystick)
        buttons = joystickob.get_numbuttons()
        for i in range(buttons):
            button = joystickob.get_button(i)
            print(button)
            if button == 1:
                print(f"Button {buttons} on joystick {joystick.get_id()} is {button}")




    # Check for events
#    for event in pygame.event.get():
        # Check if the event is a button press
#        if event.type == pygame.JOYBUTTONDOWN:
#            # Get the button index
#            button = event.button
#            # Get the joystick object
#            joystick = pygame.joystick.Joystick(event.joy)
#            # Get the button state (True = pressed, False = not pressed)
#            state = joystick.get_button(button)
#            # Print the button press event
#            print(f"Button {button} on joystick {joystick.get_id()} is {state}")

