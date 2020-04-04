import Point
class Ball:

    def __init__(self,middle,radius):
        self.radius = radius
        self.middle = middle

#   Balls are equals when have common space
    def __eq__(self,ball):
        return not (self.middle.distance(ball.middle) > self.radius + ball.radius)

    def __ne__(self,ball):
        return not self == ball

    def __str__(self):
        print("(" + str(self.middle.x )+ " ,"  + str(self.middle.x)+" ," + str(self.radius) + ")")
