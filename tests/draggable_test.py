__author__ = 'Gregorio Manabat III'

import sys

import random

import math

import pygame

import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.draggable as draggable

pygame.init()

width = 360
height = 240

# set up the window
DISPLAY_SURFACE = pygame.display.set_mode((width, height), 0)
pygame.display.set_caption('Draggable')  # set up the colors

balls = []
ball_cap = 40

def render():
    # draw on the surface object
    DISPLAY_SURFACE.fill(colors.BLACK)
    for ball in balls:
        pygame.draw.circle(DISPLAY_SURFACE, ball.color, (ball.x, ball.y), ball.radius, 0)

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

grabbed = False

# run the game loop

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
    render()
    draggable.ball_grabber(balls)

    while len(balls) < ball_cap:
        new_ball = draggable.Ball(random.randrange(width), random.randrange(height), random.randrange(10, 20))
        new_ball.color = colors.WHITE
        balls.append(new_ball)

