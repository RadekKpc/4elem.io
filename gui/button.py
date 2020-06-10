import pygame as pg


class Button:
    IMAGE_WIDTH = 100
    IMAGE_HEIGHT = 50

    @staticmethod
    def get_image():
        return 'img/button.png'

    @staticmethod
    def get_hover_image():
        return 'img/button_hover.png'

    def __init__(self, x, y, window):
        self.is_checked = False
        self.x = x
        self.y = y
        self.window = window
        try:
            self.image = pg.image.load(Button.get_image())
        except Exception as e:
            print(e)

    def display(self):
        self.window.blit(self.image, (self.x - self.IMAGE_WIDTH / 2, self.y - self.IMAGE_HEIGHT / 2))

    def is_hover(self, x2, y2):
        return self.x - self.IMAGE_WIDTH / 2 <= x2 <= self.x + self.IMAGE_WIDTH / 2 and self.y - self.IMAGE_HEIGHT / 2 <= y2 <= self.y + self.IMAGE_HEIGHT / 2
