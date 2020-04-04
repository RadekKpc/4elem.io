from Point import Point
class Map:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.lower_left = Point(0,0)
        self.upper_right = Point(width,height)
