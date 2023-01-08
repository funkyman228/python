import pygame

pygame.init()

# Set up the joystick
pygame.joystick.init()

# Get the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(joystick)

# Main game loop
while True:
    # Check for events
    for event in pygame.event.get():
        # Check if the event is a button press
        if event.type == pygame.JOYBUTTONDOWN:
            # Get the button index
            button = event.button
            # Get the button state (True = pressed, False = not pressed)
            state = joystick.get_button(button)
            # Print the button press event
            print(f"Button {button} is {state}")

