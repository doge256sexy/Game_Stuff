__author__ = 'Gregorio Manabat III'

import pygame
import math

grabbed_balls = set()
ball_cap = 40

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

grabbed = False

def ball_grabber(balls):
    delta = pygame.mouse.get_rel()
    if pygame.mouse.get_pressed()[0]:
        mp = pygame.mouse.get_pos()
        for ball in balls:
            distance_to_mouse = dist(mp, (ball.x, ball.y))
            if distance_to_mouse < ball.radius:
                if len(grabbed_balls) < 1:
                    grabbed_balls.add(ball)
        for ball in grabbed_balls:
            ball.x = ball.x + delta[0]
            ball.y = ball.y + delta[1]
    else:
        grabbed_balls.clear()
