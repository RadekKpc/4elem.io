import pygame as pg
from game_view.element import Element


class Background:

    @staticmethod
    def get_background_image():
        return 'img/background.png'

    def __init__(self, window, width, height):
        self.window = window
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        try:
            self.image = pg.image.load(Background.get_background_image())
        except Exception as e:
            print(e)
        self.image = pg.transform.scale(self.image, (width, height))
        self.fire = Element(window, 100, 300, 100, "fire")
        self.water = Element(window, 180, 240, 100, "water")
        self.earth = Element(window, 700, 300, 100, "earth")
        self.wind = Element(window, 620, 240, 100, "wind")

    def is_hover_flag(self, element, flag):
        if element == "fire":
            self.fire.flag = flag
        if element == "water":
            self.water.flag = flag
        if element == "earth":
            self.earth.flag = flag
        if element == "wind":
            self.wind.flag = flag

    def display(self):
        self.window.blit(self.image, (self.x, self.y))
        self.fire.display()
        self.earth.display()
        self.water.display()
        self.wind.display()
