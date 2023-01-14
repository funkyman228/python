import pygame
import sys
import time
import cProfile

pygame.init()

screenver = 720
screenhor = 1280
speed = 2
framerate = 144
framerate = 1/framerate

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
tick = 0

frame = time.time()

for event in pygame.event.get():
    pass

def wait(tickw):
    frame_buffer = tickw+framerate
    while time.time() < frame_buffer:
        pass

def mloop():
    frame = time.time()
    direc = 0
    direu = 0
    posx = 0
    posy = 0
    frame_buffer = 0
    i = 0
    f = 0
    a = 0
    while a < 2000:
        tick = time.time()
        if i == 10:
            tim = 10/(tick - frame)
            print(f' fps = {round(tim)}', end='\r')
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

        if f == 1:
            screen.fill((0, 0, 0))
            screen.blit(apple, (posx, posy))
            #wait(tick)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            f = 0

        wait(tick)

    #    clock.tick(1000)

mloop()

#cProfile.run('mloop()', 'testgame3.profile')
# snakeviz testgame3.profile