__author__ = 'Gregorio Manabat III'
import math

import Game_Stuff.utilities.lines as lines


def average(a, b):
    return (a+b)/2

def circumcenter(x1, y1, x2, y2, x3, y3):

    line1 = lines.Line(average(x1, x2), average(y1, y2), (x1 - x2), (y2 - y1))
    line2 = lines.Line(average(x1, x3), average(y1, y3), (x1 - x3), (y3 - y1))
    return lines.intersection_two_lines(line1, line2)

def circumcenter(p1, p2, p3):

    line1 = lines.Line(average(p1[0], p2[0]), average(p1[1], p2[1]), (p1[0] - p2[0]), (p2[1] - p1[1]))
    line2 = lines.Line(average(p1[0], p3[0]), average(p1[1], p3[1]), (p1[0] - p3[0]), (p3[1] - p1[1]))
    return lines.intersection_two_lines(line1, line2)
