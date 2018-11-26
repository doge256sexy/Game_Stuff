
__author__ = 'Gregorio Manabat III'

import sys
import random

import pygame

import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.grid as grid_class

pygame.init()

# set up the window
grid = grid_class.Grid(width=100, height=100, scale=1, fill_function=(lambda x, y: [colors.random_color(), 0, 0]), screen_mode=0)
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
            pixels[x][y] = (pixel[0][0], pixel[0][1], pixel[0][2])

def sort_color():
    for x in range(width):
        for y in range(height - 1):
            a = (y + 1) % height
            if array[x][y][2] >= array[x][a][1]:
                array[x][a], array[x][y] = array[x][y], array[x][a]
                pixels[x][a], pixels[x][y] = pixels[x][y], pixels[x][a]

    for x in range(width - 1):
        for y in range(height):
            b = (x + 1) % width
            if array[x][y][2] >= array[b][y][1]:
                array[b][y], array[x][y] = array[x][y], array[b][y]
                pixels[b][y], pixels[x][y] = pixels[x][y], pixels[b][y]

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