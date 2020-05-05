# przeciązanie operatorów
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)

    def distance(self, point):
        p = self - point
        return math.sqrt(p.x ** 2 + p.y ** 2)

    def __eq__(self, point):
        return self.x == self.y and point.x == point.y

    def __ne__(self, point):
        return not self == point

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
