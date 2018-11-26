__author__ = 'Gregorio Manabat III'
import math

class Vector:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.x = p2[0] - p1[0]
        self.y = p2[1] - p1[1]
        self.length = math.hypot(self.x, self.y)

    @staticmethod
    def dot_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y

    @staticmethod
    def angle_between_two_vectors(v1, v2):
        length_product = v1.length * v2.length
        if length_product == 0:
            return 0
        else:
            result = Vector.dot_product(v1, v2)/length_product
            more = None
            if -1 <= result <= 1:
                more = math.acos(result)
            else:
                if -1 > result:
                    more = math.acos(-1)
                if result > 1:
                    more = math.acos(1)
            return more
