import pygame


class Rank:

    def __init__(self, window, x, y):

        self.window = window
        self.x = x
        self.y = y
        self.width = 150
        self.height = 200
        self.font_size = 18
        self.image = pygame.image.load('img/rank.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def display(self, players_list):

        self.window.blit(self.image,(self.x,self.y))

        for i, p in enumerate(players_list):
            font = pygame.font.SysFont("Consolas", self.font_size)
            text = font.render(str(p.score) + " " + p.name, True, pygame.Color(0, 0, 0))
            self.window.blit(text, (self.x + 4, self.y + i * (self.font_size + 2)))
            if i >= 9:
                break
