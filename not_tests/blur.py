from Game_Stuff.utilities import colors

__author__ = 'Gregorio Manabat III'

import sys
import copy

import pygame

import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.grid as the_grid

pygame.init()

# set up the window
grid = the_grid.Grid(width=100, height=80, scale=7, fill_function=(lambda x, y: colors.random_color()))
pygame.display.set_caption('Blur')

bitmap_newframe = [[[] for x in range(grid.height)] for x in range(grid.width)]

def update():
    blur()

def blur():
    for x in range(grid.width):
        for y in range(grid.height):
            color = [0, 0, 0]
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    square = grid.grid[(x+a) % grid.width][(y+b) % grid.height]
                    for c in [0,1,2]:
                        color[c] += square[c]
            bitmap_newframe[x][y] = [color[0]/9, color[1]/9, color[2]/9]

clock = pygame.time.Clock()

# run the game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    update()
    grid.redraw()
    pygame.display.update()
    grid.grid = copy.copy(bitmap_newframe)