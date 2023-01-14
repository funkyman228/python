import pygame
pygame.init()
flags = pygame.OPENGL | pygame.FULLSCREEN
screen = pygame.display.set_mode((2560, 1440), flags, vsync=1)
print('driver =', pygame.display.get_driver())
