import pygame
from gui.check_box import CheckBox
from gui.button import Button
from gui.input_box import InputBox
from gui.background import Background


class Menu:

    def __init__(self, window, width, height):

        self.window = window
        self.element = "fire"
        self.nick_name = "Please put your nickname here"
        self.nick_is_putted = False
        self.window_width = width
        self.window_heigth = height
        self.menu_content()
        self.ip = "127.0.0.1"
        self.port = 22000

    def menu_content(self):
        self.check_box_fire = CheckBox(self.window_width / 2 - 150, 100, self.window, "fire")
        self.check_box_fire.is_checked = True
        self.check_box_water = CheckBox(self.window_width / 2 - 50, 100, self.window, "water")
        self.check_box_earth = CheckBox(self.window_width / 2 + 50, 100, self.window, "earth")
        self.check_box_wind = CheckBox(self.window_width / 2 + 150, 100, self.window, "wind")
        self.buttons = [self.check_box_fire, self.check_box_water, self.check_box_earth, self.check_box_wind]
        self.currnet_button = self.check_box_fire
        self.start_button = Button(self.window_width / 2, 350, self.window)
        self.input_box1 = InputBox(self.window_width / 2, 200, 140, 32)
        self.background = Background(self.window, self.window_width, self.window_heigth)
        self.input_port = InputBox(self.window_width / 2, 300, 140, 32)
        self.input_ip = InputBox(self.window_width / 2, 250, 140, 32)

    def buttons_checking(self, x, y):
        for i, button in enumerate(self.buttons):
            if (button.is_hover(x, y)):
                self.buttons[i].toggle()
                self.currnet_button.toggle()
                self.currnet_button = self.buttons[i]

        if self.start_button.is_hover(x, y):
            return True
        return False

    def buttons_display(self):
        for i, button in enumerate(self.buttons):
            self.buttons[i].display()
        self.start_button.display()

    def is_button_hovered(self):
        x, y = pygame.mouse.get_pos()
        if self.start_button.is_hover(x, y):
            try:
                self.start_button.image = pygame.image.load(Button.get_hover_image())
            except Exception as e:
                print(e)
        else:
            try:
                self.start_button.image = pygame.image.load(Button.get_image())
            except Exception as e:
                print(e)
        for i, button in enumerate(self.buttons):
            flag = button.is_hover(x, y)
            # print(flag,button.represent_value)
            if button.is_checked:
                self.background.is_hover_flag(button.represent_value, True)
            else:
                self.background.is_hover_flag(button.represent_value, flag)

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
                self.input_port.handle_event(event)
                self.input_ip.handle_event(event)


            self.window.fill((255, 255, 255))
            self.background.display()
            self.is_button_hovered()
            self.background.display()
            self.buttons_display()
            self.input_box1.update()
            self.input_box1.draw(self.window)
            self.nick_name = self.input_box1.text

            self.input_ip.update()
            self.input_ip.draw(self.window)
            self.ip = self.input_ip.text

            self.input_port.update()
            self.input_port.draw(self.window)
            self.port = self.input_port.text
            pygame.display.flip()
            if flag:
                if self.nick_name != "Please put your nickname here" and self.nick_name != "":
                    break

        return self.nick_name, self.currnet_button.represent_value, self.ip, self.port
