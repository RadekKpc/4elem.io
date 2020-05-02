import pygame as pg

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
        self.image = pg.image.load(Background.get_background_image())
        self.image = pg.transform.scale(self.image, (width, height))
    
    def display(self):
        self.window.blit(self.image, (self.x, self.y))
