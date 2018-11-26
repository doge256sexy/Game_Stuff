from Game_Stuff.utilities import colors

__author__ = 'Gregorio Manabat III'

import sys
import random

import pygame

import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.grid as grid_class

pygame.init()

# set up the window
grid = grid_class.Grid(width=100, height=100, scale=1, fill_function=(lambda x, y: [colors.random_color(), 0, 0]))
pygame.display.set_caption('Sifting Colors')
pixels = pygame.PixelArray(grid.DISPLAY_SURFACE)

width = grid.width
height = grid.height
array = grid.grid

def generate_values(up, right):
    for x in range(width):
        for y in range(height):
            pixel = array[x][y]
            pixel[1] = sum(pixel[0][c] * up[c] for c in range(3))
            pixel[2] = sum(pixel[0][c] * right[c] for c in range(3))

def sort_color():
    for x in range(width):
        array[x] = sorted((element for element in array[x]), key=lambda elem: elem[1])

    for y in range(height):
        new_list = sorted((array[index][y] for index in range(width)), key=lambda elem: elem[2])
        for x in range(width):
            array[x][y] = new_list[x]
            pixels[x][y] = array[x][y][0]

clock = pygame.time.Clock()

def random_from(start, stop):
    return random.random() * (stop - start) + start

def init():
    weight_one = [random_from(-1, 1),random_from(-1, 1),random_from(-1, 1)]
    weight_two = [random_from(-1, 1),random_from(-1, 1),random_from(-1, 1)]
    generate_values(weight_one, weight_two)
    pygame.display.set_caption('Sifting Colors')
    print(str(weight_one) + str(weight_two))

init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        init()


    sort_color()
    # weights determine how the colors should be compared to one another and whether or not they should switch

