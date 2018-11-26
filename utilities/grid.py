__author__ = 'Greg'
import pygame
import math

class Grid:


    def __init__(self, width, height, scale, fill_function=(lambda x, y: None), screen_mode=0):
        self.grid = [[fill_function(x, y) for x in range(height)] for y in range(width)]
        self.height = height
        self.width = width
        self.scale = scale
        self.DISPLAY_SURFACE = pygame.display.set_mode((width * scale, height * scale), screen_mode, 32)

    def update_coordinate(self, x, y):
        pygame.draw.rect(self.DISPLAY_SURFACE, self.grid[x][y], (x * self.scale, y * self.scale, self.scale, self.scale))

    def update_coordinate_function(self, x, y, function):
        pygame.draw.rect(self.DISPLAY_SURFACE, function(x, y), (x * self.scale, y * self.scale, self.scale, self.scale))

    def redraw(self):
        for x in range(self.width):
            for y in range(self.height):
                self.draw(x, y, self.grid[x][y])

    def redraw_function(self, function):
        for x in range(self.width):
            for y in range(self.height):
                self.draw(x, y, function(x, y))

    def draw(self, x, y, value):
            pygame.draw.rect(self.DISPLAY_SURFACE, value, (x * self.scale, y * self.scale, self.scale, self.scale))

    def get_click_pos(self):
        mouse_pos = pygame.mouse.get_pos()
        return int(math.floor(mouse_pos[0] / self.scale)), int(math.floor(mouse_pos[1] / self.scale))
