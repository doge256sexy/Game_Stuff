__author__ = 'Gregorio Manabat III'

import pygame
import sys
pygame.init()

# set up the window

screendimensions = (1000, 500)
half = (500, 250)
DISPLAYSURF = pygame.display.set_mode(screendimensions, 0)
pygame.display.set_caption('Mandelbrot')
pixObj = pygame.PixelArray(DISPLAYSURF)
center = -1 + 0j
zoom = 150
iterationcap = 30

def render():
    for x in range(screendimensions[0]):
        for y in range(screendimensions[1]):
            orbiter = complex((((x - half[0]) / zoom) + center.real), (((y - half[1]) / zoom) + center.imag))
            original = orbiter
            iterations = 0
            while abs(orbiter) < 2 and iterations < iterationcap:
                orbiter = orbiter * orbiter + original
                iterations += 1
            pixObj[x][y] = ((iterations * 20) % 255, (iterations * 55) % 255, (iterations * 55) % 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    render()
