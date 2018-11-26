from Game_Stuff.utilities import colors

__author__ = 'Gregorio Manabat III'

import sys
import random

import pygame

import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.grid as array_grid

pygame.init()

COLORS = [colors.random_color() for i in range(4)]
def function(x, y):
    return random.choice(COLORS)

the_grid = array_grid.Grid(width=100, height=100, scale=6, fill_function=function)
# set up the window

pygame.display.set_caption('Flood it')  # set up the colors

the_grid.redraw()

def colour_checker(x, y, colour):
    value_to_fill = the_grid.grid[x][y]
    if not value_to_fill == colour:
        need_check = set()
        need_check.add((x, y))
        while len(need_check) > 0:
            new_check = []
            for value in need_check:
                the_grid.grid[value[0]][value[1]] = colour
                the_grid.draw(value[0], value[1], colour)
                for a, b in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    x = value[0] + a
                    y = value[1] + b
                    if -1 < x < the_grid.width and -1 < y < the_grid.height:
                        if the_grid.grid[x][y] == value_to_fill:
                            new_check.append((x, y))
            need_check.clear()
            for pos in new_check:
                need_check.add(pos)
            pygame.display.update()

# run the game loop

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    mouse = the_grid.get_click_pos()
    colour_checker(mouse[0], mouse[1], random.choice(COLORS))

    #flood(random.randrange(width), random.randrange(height), random.choice(COLORS))