import pygame as pg

class Element:

    @staticmethod
    def get_fire_image(flag):
        if flag:
            return 'img/h_fire.png'
        return 'img/fire.png'

    @staticmethod
    def get_wind_image(flag):
        if flag:
            return 'img/h_wind.png'
        return 'img/wind.png'
    
    @staticmethod
    def get_earth_image(flag):
        if flag:
            return 'img/h_earth.png'
        return 'img/earth.png'
    
    @staticmethod
    def get_water_image(flag):
        if flag:
            return 'img/h_water.png'
        return 'img/water.png'

    @staticmethod
    def get_element_image(element, r, flag):
        if element == "fire":
            image = pg.image.load(Element.get_fire_image(flag))

        if element == "wind":
            image = pg.image.load(Element.get_wind_image(flag))

        if element == "earth":
            image = pg.image.load(Element.get_earth_image(flag))
        
        if element == "water":
            image = pg.image.load(Element.get_water_image(flag))

        image = pg.transform.scale(image,(int(r*2),int(r*2)))
        return image



    def __init__(self, window, x, y, r, element):
        self.window = window
        self.flag = False
        self.x = x
        self.y = y
        self.r=r
        self.element = element
        self.image = Element.get_element_image(self.element, self.r, self.flag )
    
    def display(self):
        self.image = Element.get_element_image(self.element, self.r, self.flag )
        self.window.blit(self.image, (self.x - self.r, self.y - self.r))
