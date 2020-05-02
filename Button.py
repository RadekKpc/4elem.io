import pygame as pg


class Button:
    IMAGE_WIDTH = 100
    IMAGE_HEIGHT = 50
    @staticmethod
    def get_image():
        return 'img/button.png'

    def __init__(self, x, y, window):
        self.is_checked = False
        self.x = x
        self.y = y
        self.window = window
        self.image = pg.image.load(Button.get_image())

    def display(self):
        self.window.blit(self.image, (self.x, self.y))

    def is_hover(self, x2, y2):
        return x2 >= self.x and x2 <= self.x + self.IMAGE_WIDTH and y2 >= self.y and y2 <= self.y + self.IMAGE_HEIGHT

