from Game_Stuff.utilities import colors

__author__ = 'Gregorio Manabat III'

import sys
import random

import pygame

import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.grid as grid_python
import Game_Stuff.utilities.maze_ca as Nav
import Game_Stuff.utilities.doodles as doodles

pygame.init()

def fill(x, y):
    if (x * y % 2 == 0 or x + y & 4 == 2) and round(random.random()) == 0:
        return random.choice(['Wall'])
    else:
        return "Empty"

# set up the window
info_Object = pygame.display.Info()
the_grid = grid_python.Grid(width=int(info_Object.current_w / 8), height=int(info_Object.current_h / 8), scale=5, fill_function=fill)
pygame.display.set_caption('Maze Solver')

show_directions = True
ship_list = []

for i in range(100):
    the_grid.grid[random.randrange(the_grid.width)][random.randrange(the_grid.height)] = 'End'

the_grid.grid[int(the_grid.width / 2)][int(the_grid.height / 2)] = 'End'

# run the game loop
clock = pygame.time.Clock()


def random_blank_grid_tuple():
    coordinate = (random.randrange(the_grid.width), random.randrange(the_grid.height))
    while not the_grid.grid[coordinate[0]][coordinate[1]] == 'Empty':
        coordinate = (random.randrange(the_grid.width), random.randrange(the_grid.height))
    return coordinate


def update_draw(x, y, navigator, style):
    pen = colors.BLACK

    if show_directions:
        type_vs_color = {'Flow_Left': colors.BLUE, 'Flow_Right': colors.ROYALBLUE, 'Flow_Up': colors.DARKBLUE,
                         'Flow_Down': colors.LIGHTBLUE, "Wall": colors.GRAY, 'Flow_Start': style[1]}
        key = navigator.grid[x][y]
        if key in type_vs_color:
            pen = type_vs_color[key]

    if 'Path' in navigator.grid[x][y]:
        pen = style[0]

    the_grid.draw(x, y, pen)


def draw_walls():
    for x in range(the_grid.width):
        for y in range(the_grid.height):
            pen = colors.BLACK
            if the_grid.grid[x][y] == 'End':
                pen = colors.RED
            if the_grid.grid[x][y] == 'Wall':
                pen = colors.GRAY
            the_grid.draw(x, y, pen)


draw_walls()


def wall_draw(x, y):
    the_grid.draw(x, y, colors.BLACK if the_grid.grid[x][y] == 'Empty' else colors.GRAY)


def get_drawings():
    pygame.event.get()
    if pygame.mouse.get_pressed()[0]:
        spot = the_grid.get_click_pos()

        pen = None
        if the_grid.grid[spot[0]][spot[1]] == "Wall":
            pen = "Empty"
        else:
            pen = "Wall"

        while 1:
            pygame.event.get()
            if not pygame.mouse.get_pressed()[0]:
                break
            oldspot = spot
            spot = the_grid.get_click_pos()

            doodles.line(spot[0], spot[1], oldspot[0], oldspot[1], the_grid.grid, pen, wall_draw)
            pygame.display.update()


ship_cap = 1
while True:
    pygame.display.update()
    # clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:

        while len(ship_list) < ship_cap:
            ship_list.append(Nav.Navigator((the_grid.width, the_grid.height), the_grid.grid, start=(50, 50),
                                           style=[colors.random_color(), colors.random_color()], ship_list=ship_list))
            draw_walls()
        for ship in ship_list:
            ship.update()
            for coordinate in ship.active_coordinates:
                update_draw(coordinate[0], coordinate[1], ship, ship.style)

    get_drawings()
