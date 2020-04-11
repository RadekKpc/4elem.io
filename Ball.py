from Point import Point
import math

class Ball:

    def __init__(self,middle,radius):
        self.radius = radius
        self.middle = middle

#   Balls are equal when have common space
    def __eq__(self,ball):
        return not (self.middle.distance(ball.middle) > self.radius + ball.radius)

    def __ne__(self,ball):
        return not self == ball

    def __str__(self):
        print("(" + str(self.middle.x )+ " ,"  + str(self.middle.x)+" ," + str(self.radius) + ")")

    def calculate_field(self):
        return math.pi*(self.radius**2)
    
    def calculate_radius_after_eating(self,ball): #ball is eaten element       
        self.radius = math.sqrt((self.calculate_field()+ball.calculate_field())/math.pi)


    def can_eat(self,other_player): #check if other player middle is inside self
        return self.middle.distance(other_player.middle)<self.radius

