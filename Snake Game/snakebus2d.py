import pygame
import time
import os

fps = 5

pygame.init()

# Set up the joystick
pygame.joystick.init()

button = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Get the number of joysticks
joystick_count = pygame.joystick.get_count()
print(joystick_count)

# initiliz joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# game setup
player = []
matrix = []
width = []
matrix = [[0 for col in range(10)] for row in range(10)]

# place player
matrix[5][5] = 1


 # Main game loop
while True:
#    start = time.time()
    # clear events
    for event in pygame.event.get():
        pass

    # scan controller
    for but in range(len(button)):
        button[but] = joystick.get_button(but)

    # game
    
    # clear screen
    os.system('cls')

    # look for player
    colc = 0
    rowc = 0
    for col in matrix:
        for row in col:
            if row == 1:
                player = [colc, rowc]
            rowc += 1
        rowc = 0
        colc += 1

    # move player
    if button[0] == 1 and player[0] < 9:
        matrix[player[0]][player[1]] = 0
        matrix[player[0]+1][player[1]] = 1

    elif button[1] == 1 and player[1] < 9:
        matrix[player[0]][player[1]] = 0
        matrix[player[0]][player[1]+1] = 1

    elif button[2] == 1 and player[1] > 0:
        matrix[player[0]][player[1]] = 0
        matrix[player[0]][player[1]-1] = 1

    elif button[3] == 1 and player[0] > 0:
        matrix[player[0]][player[1]] = 0
        matrix[player[0]-1][player[1]] = 1

    # draw screen
    for col in matrix:
        for row in col:
            print(row, end=' ')
        print()

    # measure fps
#    end = round(1/(time.time()-start))
#    print(end)

    # wait
    time.sleep(1/fps)
