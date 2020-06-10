import pygame
from gui.button import Button
from map_components.player import Player
from gui.background import Background
from game_view.element import Element

FONT = pygame.font.Font('font/Purisa, Regular.ttf', 50)
FONT_2 = pygame.font.Font('font/Purisa, Regular.ttf', 32)


class EndGame:
    def __init__(self, window, width, height):
        self.window = window
        self.window_width = width
        self.window_heigth = height
        self.start_button = Button(self.window_width / 2, 350, self.window)
        try:
            self.background_image = pygame.image.load('img/background_plain.png')
            self.background_image = pygame.transform.scale(self.background_image,
                                                           (self.window_width, self.window_heigth))
            self.crown_image = pygame.image.load('img/crown.png')
        except Exception as e:
            print(e)
        self.crown_image = pygame.transform.scale(self.crown_image, (100, 50))
        self.crown_image = pygame.transform.rotate(self.crown_image, 360 - 35)
        # FONT.render(self.player_winner.name)

    def is_button_hovered(self):
        x, y = pygame.mouse.get_pos()
        try:
            if self.start_button.is_hover(x, y):
                self.start_button.image = pygame.image.load(Button.get_hover_image())
            else:
                self.start_button.image = pygame.image.load(Button.get_image())
        except Exception as e:
            print(e)

    def display(self, winner):
        text = "Player " + winner.name + " wins"
        txt_surface = FONT.render(text, True, (0, 0, 0))
        text_2 = "Click button to play again"
        txt_surface2 = FONT_2.render(text_2, True, (0, 0, 0))
        player_element = Element(self.window, 100, 300, 100, winner.get_element())

        clock = pygame.time.Clock()
        flag_play_agian = False
        end_game_flag = True
        while end_game_flag:
            clock.tick(30)

            # get all events
            ev = pygame.event.get()

            # proceed events
            for event in ev:

                # handle MOUSEBUTTONUP
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    flag_play_agian = self.start_button.is_hover(x, y)
                if event.type == pygame.QUIT:
                    end_game_flag = False

            self.window.fill((255, 255, 255))
            self.window.blit(self.background_image, (0, 0))
            self.is_button_hovered()
            self.start_button.display()
            self.window.blit(txt_surface, (self.window_width / 2 - txt_surface.get_width() / 2, 100))
            self.window.blit(txt_surface2, (self.window_width / 2 - txt_surface2.get_width() / 2, 200))
            player_element.display()
            self.window.blit(self.crown_image, (self.window_width / 2 + txt_surface.get_width() / 2 - 50, 50))
            pygame.display.flip()

            if flag_play_agian:
                break
        return flag_play_agian
