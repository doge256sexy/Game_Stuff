__author__ = 'Gregorio Manabat III'

import sys

import random

import pygame

import Game_Stuff.utilities.colors as colors
import Game_Stuff.utilities.gift_wrapping as gift_wrapping
import Game_Stuff.utilities.k_means_clustering as k_means
import Game_Stuff.utilities.draggable as draggable
import Game_Stuff.utilities.voronoi as voronoi

pygame.init()

width = 720
height = 480
# set up the window
DISPLAY_SURFACE = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption('K-Means Clustering')  # set up the colors

balls = []
cluster_cap = 10

voronoi_on = True
wrapping_on = False

def init_clusters():
    return colors.random_color(), random.randrange(width), random.randrange(height)

controller = k_means.KMeansController(balls, cluster_cap, init_clusters, 1)

def create_a_ball(x, y, radius):
    new_ball = draggable.Ball(x, y, radius)
    new_ball.category = colors.BLACK
    balls.append(new_ball)

def create_balls():
    for x in range(int(width / 20)):
        for y in range(int(height / 50)):
            #create_a_ball(x * 50, y * 50, 5)
            create_a_ball(random.randrange(width), random.randrange(height), random.randrange(5, 10))

create_balls()
controller.create()
clock = pygame.time.Clock()
def exit():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def tuple_to_int(pt):
    return int(pt[0]), int(pt[1])

class voronoi_ball:
    def __init__(self, x, y):
        self.participation = set()
        self.x = x
        self.y = y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        exit()

    pygame.display.update()
    clock.tick(60)
    draggable.ball_grabber(balls)

    controller.update_points()

    # draw on the surface object
    DISPLAY_SURFACE.fill(colors.WHITE)

    for ball in balls:
        pygame.draw.circle(DISPLAY_SURFACE, ball.category, (ball.x, ball.y), ball.radius, 0)

    for cluster in controller.k_means_clusters:
        pygame.draw.circle(DISPLAY_SURFACE, cluster.category, (int(cluster.average[0]), int(cluster.average[1])), 6, 2)
        if wrapping_on:
            new_wrap = []
            if len(cluster.weights) > 0:
                for ball in cluster.weights:
                    new_wrap.append((ball.x, ball.y))
                pts = gift_wrapping.wrap(new_wrap)
                if len(pts) > 2:
                    pygame.draw.polygon(DISPLAY_SURFACE, cluster.category, pts)

    if voronoi_on:
        voronoi_pts = [voronoi_ball(*cluster.average) for cluster in controller.k_means_clusters]
        voronoi_info = voronoi.voronoi_diagram(voronoi_pts)

        for lines in voronoi_info[0]:
            pygame.draw.line(DISPLAY_SURFACE, colors.GREEN, lines[0], lines[1], 1)
        for lines_to_infinity in voronoi_info[1]:
            pygame.draw.line(DISPLAY_SURFACE, colors.GREEN, lines_to_infinity[0], lines_to_infinity[1], 1)


    controller.update_clusters()