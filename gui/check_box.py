import pygame as pg


class CheckBox:
    IMAGE_HEIGHT = 50
    IMAGE_WIDTH = 50

    @staticmethod
    def get_check_image():
        return 'img/checked_radio.png'

    @staticmethod
    def get_unchecked_image():
        return 'img/unchecked_radio.png'

    def __init__(self, x, y, window, represent_value):
        self.is_checked = False
        self.x = x
        self.y = y
        self.window = window
        try:
            self.checked_img = pg.image.load(CheckBox.get_check_image())
            self.unchecked_image = pg.image.load(CheckBox.get_unchecked_image())
        except Exception as e:
            print(e)
        self.represent_value = represent_value

    def toggle(self):
        self.is_checked = not self.is_checked

    def display(self):

        if self.is_checked:
            self.window.blit(self.checked_img, (self.x - self.IMAGE_WIDTH/2, self.y - self.IMAGE_HEIGHT/2))
        else:
            self.window.blit(self.unchecked_image, (self.x - self.IMAGE_WIDTH/2, self.y - self.IMAGE_HEIGHT/2))

    def is_hover(self, x2, y2):
        return self.x - self.IMAGE_WIDTH / 2 <= x2 <= self.x + self.IMAGE_WIDTH / 2 and self.y - self.IMAGE_HEIGHT / 2 <= y2 <= self.y + self.IMAGE_HEIGHT / 2
