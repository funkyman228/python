import pygame
import sys

pygame.init()

screenver = 1440
screenhor = 2560
speed = 1

screen = pygame.display.set_mode((screenhor, screenver))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
pygame.display.toggle_fullscreen()

apple = pygame.image.load('snake2d/test image.png')
width, height = apple.get_size()
apple = pygame.transform.scale(apple, (256, 265))


direc = 0
direu = 0
posx = 0
posy = 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

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

    screen.blit(apple, (posx, posy))

    pygame.display.update()
    clock.tick(144)