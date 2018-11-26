
import pygame
import sys
from pygame.locals import *
pygame.init()

# set up the window

DISPLAY_SURFACE = pygame.display.set_mode((256, 256), 0, 32)
pygame.display.set_caption('Basic Blank screen loop')

clock = pygame.time.Clock()
# run the game loop

def exit():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

alive = True
while alive:
    for event in pygame.event.get():
        if event.type == QUIT:
            alive = False

        print(event)

    pygame.display.update()
    clock.tick(60)  # keep 60 fps
exit()


