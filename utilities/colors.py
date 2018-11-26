__author__ = 'Greg'
import random

def random_color():
    return (int((random.random() * 255) % 255), int((random.random() * 255) % 255), int((random.random() * 255) % 255))

def random_color_just_blue():
    return (0, 0, (random.random() * 255) % 255)

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (125, 158, 192)
ROYALBLUE = (65, 105, 225)
DARKBLUE = (0, 0, 139)
ORANGE = (255, 128, 0)
GRAY = (100, 100, 100)
