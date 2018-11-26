__author__ = 'Gregorio Manabat III'

import sys
import random
import pygame
import math

import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.draggable as draggable
import Game_Stuff.utilities.voronoi as voronoi

# set up the window
pygame.init()

height = 480
width = 720
DISPLAY_SURFACE = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Circumcenter')  # set up the colors
myfont = pygame.font.SysFont("consolas", 24)

show_help = False
Balls = []
def random_ball():
    return draggable.Ball(random.randrange(100, width - 100), random.randrange(100, height - 100), 10)

def tuple_to_int(pt):
    return int(pt[0]), int(pt[1])

def ball_tuple(ball):
    return ball.x, ball.y

def gen_balls(num_balls):
    for i in range(num_balls):
        ball = random_ball()
        Balls.append(ball)
        ball.participation = set()

def render():
    # draw on the screen
    DISPLAY_SURFACE.fill(colors.GRAY)

    voronoi_info = voronoi.voronoi_diagram(Balls)

    for lines in voronoi_info[0]:
        pygame.draw.line(DISPLAY_SURFACE, colors.GREEN, lines[0], lines[1], 1)
    for lines_to_infinity in voronoi_info[1]:
        pygame.draw.line(DISPLAY_SURFACE, colors.GREEN, lines_to_infinity[0], lines_to_infinity[1], 1)
    for circumcircle in voronoi_info[2]:
        pygame.draw.circle(DISPLAY_SURFACE, colors.RED, tuple_to_int(circumcircle.center), int(circumcircle.radius), 1)

    for i, ball in enumerate(Balls):
        pygame.draw.circle(DISPLAY_SURFACE, colors.ROYALBLUE, (ball.x, ball.y), ball.radius, 0)
        rule_text = myfont.render(str(i), 1, (255, 255, 255))
        DISPLAY_SURFACE.blit(rule_text, (ball.x, ball.y))

clock = pygame.time.Clock()
# run the game loop

gen_balls(10)

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