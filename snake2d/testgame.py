import pygame
import sys
import time
import cProfile

pygame.init()

screenver = 720
screenhor = 1280
speed = 1
framerate = 10
framerate = 1000000/framerate

screen = pygame.display.set_mode((screenhor, screenver))
pygame.display.set_caption('Runner')
#clock = pygame.time.Clock()
#pygame.display.toggle_fullscreen()

apple = pygame.image.load('test image.png')
# width, height = apple.get_size()
apple = pygame.transform.scale(apple, (256, 256))

print(apple)

direc = 0
direu = 0
posx = 0
posy = 0
i = 0
f = 0
a = 0

frame = time.time_ns()

for event in pygame.event.get():
    pass

def mloop():
    frame = time.time_ns()
    direc = 0
    direu = 0
    posx = 0
    posy = 0
    frame_buffer = 0
    i = 0
    f = 0
    a = 0
    while True:
        tick = time.time_ns()
        if i == 1000:
            tim = (tick - frame)/1000000
            print(f' fps = {round(tim)} {framerate}', end='\r')
            frame = tick
            i = 0


        if direc == 0:
            posx += speed
            if posx > screenhor-256:
                direc = 1
        else:
            posx -= speed
            if posx == 0:
                direc = 0

        if direu == 0:
            posy += speed
            if posy > screenver-256:
                direu = 1
        else:
            posy -= speed
            if posy == 0:
                direu = 0

        i += 1
        f += 1
        a += 1

        if f == 1000:
            screen.fill((0, 0, 0))
            screen.blit(apple, (posx, posy))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            f = 0

        frame_buffer = tick+10000
        while time.time_ns() < frame_buffer:
            pass
    #    clock.tick(1000)

mloop()

#cProfile.run('mloop()', 'testgame2.profile')