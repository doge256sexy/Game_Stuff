__author__ = 'Gregorio Manabat III'

import math
import sys

import Game_Stuff.utilities.vector as vector



# This script finds the convex hull of a given set of 2D points

def wrap(points):

    point = points[0]

    farthest = 0
    starter_coords = points[0]
    new = 0
    for point_two in points:
        new = distance(point, point_two)
        if farthest < new:
            starter_coords = point_two
            farthest = new

    start = vector.Vector(point, starter_coords)
    outside_points = [starter_coords]

    flag = True
    iterations = 0

    while flag:
        iterations += 1
        point_with_lowest_angle = None
        lowest_angle = math.pi
        smallest_vector = None
        shortest_dist = sys.maxsize

        for next_point in points:
            if not (next_point == start.p2 or next_point == start.p1):
                next_vector = vector.Vector(start.p2, next_point)
                angle = vector.Vector.angle_between_two_vectors(start, next_vector)

                dist = distance(start.p2, next_point)
                if angle < lowest_angle or (angle == lowest_angle and dist < shortest_dist):
                    lowest_angle = angle
                    shortest_dist = dist
                    smallest_vector = next_vector
                    point_with_lowest_angle = next_point


        if not smallest_vector == None:
            start = smallest_vector
        if point_with_lowest_angle in outside_points:
            flag = False
        outside_points.append(point_with_lowest_angle)

    return outside_points

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])