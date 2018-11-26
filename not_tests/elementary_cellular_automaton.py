__author__ = 'Gregorio Manabat III'

import sys
import random

import pygame

import Game_Stuff.utilities.grid as grid_class

pygame.init()

# initialize fonts
myfont = pygame.font.SysFont("consolas", 24)
grid = grid_class.Grid(width=512, height=256, scale=3, fill_function=(lambda x, y: 0))
random_init = True
def init():
    if random_init:
        for u in range(grid.width): grid.grid[u][0] = round(random.random())
    else:
        for u in range(grid.width): grid.grid[u][0] = 0
        grid.grid[int(grid.width/2)][0] = 1

pygame.display.set_caption('Elementary Cellular Automaton')

init()
rule = 122

def CA(y, rules):
        for x in range(grid.width):
            state = 2 ** (grid.grid[x - 1][y] * 4 + grid.grid[x][y] * 2 + grid.grid[(x + 1) % grid.width][y] * 1)
            grid.grid[x][(y + 1) % grid.height] = 1 if state & rules == state else 0


def render(y):
    for x in range(grid.width):
       pygame.draw.rect(grid.DISPLAY_SURFACE, (0,0,0) if grid.grid[x][y] == 1 else (255,255,255), (x * grid.scale, y * grid.scale, grid.scale, grid.scale))

    pygame.draw.rect(grid.DISPLAY_SURFACE, (128, 128, 128), (10, 10, 40, 24))
    rule_text = myfont.render(str(rule), 1, (255, 0, 255))
    grid.DISPLAY_SURFACE.blit(rule_text, (10,10))

clock = pygame.time.Clock()

# run the game loop

while True:
    for y in range(grid.height):
        CA(y,rule)
        render(y)
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_r]:
            rule = random.randrange(0, 256)
        if pressed[pygame.K_f]:
            init()
            break
