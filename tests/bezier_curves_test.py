__author__ = 'Gregorio Manabat III'

import sys

import random

import pygame

import Game_Stuff.utilities.draggable as draggable
import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.bezier_curves as bezier_curves

pygame.init()
clock = pygame.time.Clock()

width = 720
height = 480

# set up the window
DISPLAY_SURFACE = pygame.display.set_mode((width, height), 0)
pygame.display.set_caption('Bezier Curves')  # set up the colors

balls = []
ball_coords = []
ball_cap = 10

def draw_curve(function, start, end, steps):
    for t in range(steps):
        pygame.draw.line(DISPLAY_SURFACE, (0, 0, 0), function(start + t / steps), function(start + (t + 1) / steps), 1)

# run the game loop


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)

    # draw on the surface object
    DISPLAY_SURFACE.fill(colors.LIGHTBLUE)
    for ball in balls:
        pygame.draw.circle(DISPLAY_SURFACE, colors.DARKBLUE, (ball.x, ball.y), ball.radius, 0)

    draggable.ball_grabber(balls)

    while len(balls) < ball_cap:
        b = draggable.Ball(random.randrange(width), random.randrange(height), 10)
        balls.append(b)

    ball_coords.clear()
    for ball in balls:
        ball_coords.append((ball.x, ball.y))

    draw_curve((lambda x: bezier_curves.de_casteljaus(ball_coords, x)), 0, 1, 100)