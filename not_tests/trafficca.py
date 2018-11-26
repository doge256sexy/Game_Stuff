from Game_Stuff.utilities import colors

__author__ = 'Gregorio Manabat III'

import sys
import random

import pygame

import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.grid as the_grid

pygame.init()

grid = the_grid.Grid(width=50, height=40, scale=10)

pygame.display.set_caption('Traffic Simulator')

cargen = set()
traffic = []
density = 0.3

for i in range(int(grid.width*grid.height*density)):
    cargen.add((random.randrange(grid.width), random.randrange(grid.height)))
for blank_car in cargen:
    traffic.append([blank_car[0], blank_car[1], round(random.random())])

def update():
    for car in traffic:
        if car[2] == 0:
            spam = int((car[0]+1) % grid.width)
            if [spam, car[1], 1] in traffic or [spam, car[1], 0] in traffic:
                pass
            else:
                car[0] = spam
        elif car[2] == 1:
            eggs = int((car[1]+1) % grid.height)
            if [car[0], eggs, 1] in traffic or [car[0], eggs, 0] in traffic:
                pass
            else:
                car[1] = eggs

def render():
    # draw on the surface object
    grid.DISPLAY_SURFACE.fill(colors.WHITE)
    for car in traffic:
        if car[2] == 0:
            pygame.draw.rect(grid.DISPLAY_SURFACE, colors.BLUE, (car[0] * grid.scale, car[1] * grid.scale, grid.scale, grid.scale))
        else:
            pygame.draw.rect(grid.DISPLAY_SURFACE, colors.RED, (car[0] * grid.scale, car[1] * grid.scale, grid.scale, grid.scale))


clock = pygame.time.Clock()
# run the game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    render()
    pygame.display.update()
    clock.tick(60)

    update()