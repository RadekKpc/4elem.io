import pygame as pg

class Element:

    @staticmethod
    def get_fire_image():
        return 'img/fire.png'

    @staticmethod
    def get_wind_image():
        return 'img/wind.png'
    
    @staticmethod
    def get_earth_image():
        return 'img/earth.png'
    
    @staticmethod
    def get_water_image():
        return 'img/water.png'

    @staticmethod
    def get_element_image(element, r):
        if element == "fire":
            image = pg.image.load(Element.get_fire_image())

        if element == "wind":
            image = pg.image.load(Element.get_wind_image())

        if element == "earth":
            image = pg.image.load(Element.get_earth_image())
        
        if element == "water":
            image = pg.image.load(Element.get_water_image())

        image = pg.transform.scale(image,(int(r*2),int(r*2)))
        return image



    def __init__(self, window, x, y, r, element):
        self.window = window
        self.x = x
        self.y = y
        self.r=r*0.5
        self.element = element
        self.image = Element.get_element_image(self.element, self.r)
    
    def display(self):
        self.window.blit(self.image, (self.x - self.r, self.y - self.r))
