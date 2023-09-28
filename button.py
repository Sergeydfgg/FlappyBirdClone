import pygame
from display import dis


class Button:
    def __init__(self, x, y, width, height, button_text='Button', onclick_function=None,
                 already_clicked=False, font_size=40, is_italic=True, normal_color='#A0522D'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclick_function
        self.already_clicked = already_clicked

        self.fillColors = {
            'normal': normal_color,
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        font = pygame.font.SysFont('Arial', font_size, bold=True, italic=is_italic)
        self.buttonSurf = font.render(button_text, True, "white")

    def process(self):
        mouse_pos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mouse_pos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0] and self.already_clicked is False:
                self.buttonSurface.fill(self.fillColors['pressed'])
                self.onclickFunction()
                self.already_clicked = True

        if not pygame.mouse.get_pressed(num_buttons=3)[0] and self.already_clicked:
            self.already_clicked = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])

        dis.blit(self.buttonSurface, self.buttonRect)
