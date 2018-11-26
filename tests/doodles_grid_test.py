from Game_Stuff.utilities import colors

__author__ = 'Gregorio Manabat III'

import sys

import pygame

import Game_Stuff.utilities.grid as grid_class
import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.doodles as doodles

pygame.init()

# set up the window

bitmap = grid_class.Grid(width=100, height=100, scale=4, fill_function=(lambda x, y: colors.WHITE))
pygame.display.set_caption('drawing grid')

clock = pygame.time.Clock()

# run the game loop

bitmap.redraw()

while True:
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.event.get()
    if pygame.mouse.get_pressed()[0]:
        spot = bitmap.get_click_pos()

        pen = None
        if bitmap.grid[spot[0]][spot[1]] == colors.WHITE:
            pen = colors.BLACK
        else:
            pen = colors.WHITE
        while True:
            pygame.event.get()
            if not pygame.mouse.get_pressed()[0]:
                break
            old_spot = spot
            spot = bitmap.get_click_pos()
            doodles.line(old_spot[0], old_spot[1], spot[0], spot[1], grid=bitmap.grid, colored=pen, update_func=bitmap.update_coordinate)
            pygame.display.update()
