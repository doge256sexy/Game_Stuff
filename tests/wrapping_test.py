__author__ = 'Greg'

import sys

import random

import pygame

import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.draggable as draggable
import Game_Stuff.utilities.gift_wrapping as gift



# set up the window
pygame.init()

height = 480
width = 720
DISPLAY_SURFACE = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Wrapping')  # set up the colors

Balls = []
def random_ball():
    return draggable.Ball(random.randrange(100, width - 100), random.randrange(100, height - 100), 10)

def gen_balls(num_balls):
    for i in range(num_balls):
        Balls.append(random_ball())

def render():
    # draw on the surface object
    DISPLAY_SURFACE.fill(colors.GRAY)
    pts = gift.wrap([(ball.x, ball.y) for ball in Balls])
    if len(pts) > 2:
        pygame.draw.polygon(DISPLAY_SURFACE, colors.BLACK, (pts))

    for ball in Balls:
        pygame.draw.circle(DISPLAY_SURFACE, colors.ROYALBLUE, (ball.x, ball.y), ball.radius, 0)
        ball.x += random.randrange(-1,2)
        ball.y += random.randrange(-1,2)


clock = pygame.time.Clock()
# run the game loop

gen_balls(50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    draggable.ball_grabber(Balls)
    #clock.tick(30)
    render()

pygame.quit()
sys.exit()
