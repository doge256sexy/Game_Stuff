__author__ = 'Gregorio Manabat III'
import sys

class Line:
    def __init__(self, x, y, slope_numerator, slope_denominator):
        self.x = x
        self.y = y
        self.slope_numerator = slope_numerator
        self.slope_denominator = slope_denominator
        if not self.slope_denominator == 0:
            self.slope = self.slope_numerator / self.slope_denominator
        else:
            self.slope = sys.maxsize
        if not self.slope_numerator == 0:
            self.inverse_slope = self.slope_denominator / self.slope_numerator
        else:
            self.inverse_slope = sys.maxsize

def intersection_two_lines(line1, line2):
    slope_difference = line1.slope - line2.slope
    inverse_slope_difference = line1.inverse_slope - line2.inverse_slope
    if not slope_difference == 0:
        x = ((line2.y - line1.y) + (line1.x * line1.slope) - (line2.x * line2.slope))/slope_difference
        y = ((line2.x - line1.x) + (line1.y * line1.inverse_slope) - (line2.y * line2.inverse_slope))/inverse_slope_difference
    else:
        return 'Parallel lines!'

    return x, y
