import pygame
from Check_Box import CheckBox
from Button import Button
from Input_Box import InputBox


class Menu:

    def __init__(self, window):

        self.window = window
        self.element = "fire"
        self.nick_name = "Pleas put your nickname here"
        self.nick_is_putted = False
        self.menu_content()

    def menu_content(self):
        self.check_box_fire = CheckBox(100, 100, self.window, "fire")
        self.check_box_fire.is_checked = True
        self.check_box_water = CheckBox(200, 100, self.window, "water")
        self.check_box_earth = CheckBox(300, 100, self.window, "earth")
        self.check_box_wind = CheckBox(400, 100, self.window, "wind")
        self.buttons = [self.check_box_fire, self.check_box_water, self.check_box_earth, self.check_box_wind]
        self.currnet_button = self.check_box_fire
        self.start_button = Button(300, 300, self.window)
        self.input_box1 = InputBox(250, 200, 140, 32)

    def buttons_checking(self, x, y):
        for i, button in enumerate(self.buttons):
            if (button.is_hover(x, y)):
                self.buttons[i].toggle()
                self.currnet_button.toggle()
                self.currnet_button = self.buttons[i]

        if (self.start_button.is_hover(x, y)):
            return True
        return False

    def buttons_display(self):
        for i, button in enumerate(self.buttons):
            self.buttons[i].display()
        self.start_button.display()

    def display(self):
        clock = pygame.time.Clock()
        flag = False
        while True:

            clock.tick(30)

            # get all events
            ev = pygame.event.get()

            # proceed events
            for event in ev:

                # handle MOUSEBUTTONUP
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    flag = self.buttons_checking(x, y)
                self.input_box1.handle_event(event)

            self.window.fill((255, 255, 255))
            self.buttons_display()
            self.input_box1.update()
            self.input_box1.draw(self.window)
            self.nick_name = self.input_box1.text
            pygame.display.flip()
            if flag:
                if  self.nick_name != "Pleas put your nickname here" and self.nick_name != "":
                    break

        return self.nick_name, self.currnet_button.represent_value
