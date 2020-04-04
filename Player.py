from Ball import Ball
from Point import Point
import random
class Player:

    @staticmethod
    def rand_color():
        red = random.randint(0,256)
        green = random.randint(0,256)
        blue = random.randint(0,256)

        return (red,green,blue)

    def __init__(self,ball,id,name,elem):

        self.ball = ball
        self.id = id
        self.name = name
        self.elem = elem
        self.color = Player.rand_color()

    def get_x(self):
        return self.ball.middle.x

    def get_y(self):
        return self.ball.middle.get_y


