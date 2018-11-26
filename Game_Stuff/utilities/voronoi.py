__author__ = 'Gregorio Manabat III'

import sys
import itertools
import Game_Stuff.utilities.circumcenter as circum
import math

def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

class CircleWithBoundaryPoints:
    def __init__(self, center, radius, boundary_points):
        self.center = center
        self.radius = radius
        self.boundary_points = boundary_points

def slope(p1, p2):
    denominator = p1[0] - p2[0]
    if denominator == 0:
        return sys.maxsize
    else:
        return (p1[1] - p2[1]) / denominator

def clockwise_sort(p1, p2, p3):

    if slope((p1.x, p1.y), (p2.x, p2.y)) > slope((p1.x, p1.y), (p3.x, p3.y)):
        return p1, p2, p3
    else:
        return p1, p3, p2

def voronoi_diagram(points):
    lines = []
    lines_to_infinity = []
    circumcircles = []

    for ball in points:
        ball.participation.clear()

    for ball_combos in itertools.combinations(points, 3):

        coordinates = [(ball.x, ball.y) for ball in ball_combos]
        pt = circum.circumcenter(*coordinates)
        circumcenter_exists = not pt == 'Parallel lines!'

        dist = 0
        balls_inside = False
        if circumcenter_exists:
            dist = distance(ball_combos[0].x, ball_combos[0].y, pt[0], pt[1])
            for ball in points:
                if not ball in ball_combos:
                    if distance(ball.x, ball.y, pt[0], pt[1]) < dist:
                        balls_inside = True
            if not balls_inside:
                new_cc = CircleWithBoundaryPoints(pt, dist, coordinates)

                magic = 1000

                sort_1 = sorted(ball_combos, key=lambda p: p.x * magic + p.y)

                new_cc.boundary_points = clockwise_sort(*sort_1)

                circumcircles.append(new_cc)

                for ball in ball_combos:
                    ball.participation.add(new_cc)

    for circle in circumcircles:

        for i in range(3):

            point = circle.boundary_points[i]
            next_point = circle.boundary_points[(i + 1) % 3]

            circle_other = (point.participation & next_point.participation) - {circle}

            if len(circle_other) == 0:

                delta_y = point.y - next_point.y
                delta_x = point.x - next_point.x

                a = 5500

                x = circle.center[0] + a * delta_y
                y = circle.center[1] - a * delta_x

                lines_to_infinity.append((circle.center, (x, y)))
            if len(circle_other) == 1:
                lines.append((circle.center, circle_other.pop().center))

    return lines, lines_to_infinity, circumcircles