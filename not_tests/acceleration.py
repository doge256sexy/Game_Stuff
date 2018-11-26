__author__ = 'Gregorio Manabat III'

import sys

import pygame

import Game_Stuff.utilities.colors as colors

pygame.init()

# set up the window

screendimensions = (500, 400)
DISPLAYSURF = pygame.display.set_mode(screendimensions)
pixObj = pygame.PixelArray(DISPLAYSURF)
pygame.display.set_caption('Gravity Ball')

# this script uses complex numbers in order to model 2 - space

class Ball:
    def __init__(self):
        self.position = 0 + 0J
        self.velocity = 0 + 0J
        self.acceleration = 0 + 0J

    # Changing values

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity

    def drawready(self, ):
        self.xy = (int(self.position.real) % screendimensions[0],
                   (screendimensions[1] - int(self.position.imag)) % screendimensions[1])

    # Setting values

    def setpos(self, xy):
        self.position = xy

    def setvel(self, xy):
        self.velocity = xy

    def setaccel(self, xy):
        self.acceleration = xy


ball = Ball()
friction = 0.9

def ballhandler():
    ball.update()
    ball.setvel( ball.velocity*friction)
    ball.drawready()

def render():
    # draw on the surface object
    DISPLAYSURF.fill(colors.WHITE)
    mp = pygame.mouse.get_pos()
    pygame.draw.circle(DISPLAYSURF, colors.BLACK, mp, 20, 4)
    pixObj[ball.xy[0]][ball.xy[1]] = colors.WHITE
    for i in range(-1,2):
        for j in range(-1,2):
            pygame.draw.circle(DISPLAYSURF, colors.BLACK, (ball.xy[0] + (i * screendimensions[0]), ball.xy[1] + (j * screendimensions[1])), 10, 0)

def keyhandler():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        ball.setvel(ball.velocity + 1j)
    if pressed[pygame.K_s]:
        ball.setvel(ball.velocity + -1j)
    if pressed[pygame.K_a]:
        ball.setvel(ball.velocity + -1)
    if pressed[pygame.K_d]:
        ball.setvel(ball.velocity + 1)

clock = pygame.time.Clock()
# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if pygame.mouse.get_focused():

        pygame.display.update()
        clock.tick(60)
        keyhandler()
        ballhandler()
        render()

