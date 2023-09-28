import pygame
import math
from display import dis


class Slider:
    def __init__(self, x, y, width, height, slider_value, font_size=20):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_end = self.x + self.width
        self.y_end = self.y + self.height
        self.slider_value = slider_value

        self.sliderSurface = pygame.Surface((self.width, self.height))
        self.sliderRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.startRect = pygame.Rect(self.x, self.y + 5, 15, self.height - 10)
        self.endRect = pygame.Rect(self.x + self.width - 15, self.y + 5, 15, self.height - 10)
        self.tubeRect = pygame.Rect(self.x + 15, self.y + (self.height / 2 - 4), self.width - 30, 8)
        self.miniSliderRect = pygame.Rect((self.x + 15) + self.slider_value*((self.width - 44) / 100),
                                          self.y + (self.height / 2 - 7), 14, 14)

        self.font = pygame.font.SysFont('Arial', font_size, bold=True)
        self.sliderSurf = self.font.render(str(100), True, "white")

    def process(self):
        self.sliderSurface.fill("brown")

        dis.blit(self.sliderSurface, self.sliderRect)
        pygame.draw.rect(dis, "yellow", self.startRect)
        pygame.draw.rect(dis, "yellow", self.endRect)
        pygame.draw.rect(dis, "red", self.tubeRect)
        pygame.draw.rect(dis, "green", self.miniSliderRect)

        self.miniSliderRect = pygame.Rect((self.x + 15) + int(self.slider_value)*((self.width - 44) / 100),
                                          self.y + (self.height / 2 - 7), 14, 14)

        mouse_pos = pygame.mouse.get_pos()
        if self.sliderRect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if self.x + 14 < mouse_pos[0] < self.x + self.width - 28:
                    self.slider_value = (abs(mouse_pos[0] - (self.x + 15)) / ((self.width - 44) / 100))
                    self.miniSliderRect = pygame.Rect(
                        (self.x + 15) + int(self.slider_value) * ((self.width - 44) / 100),
                        self.y + (self.height / 2 - 7), 14, 14)

        if self.startRect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.slider_value = 0
                self.miniSliderRect = pygame.Rect((self.x + 15) + int(self.slider_value) * ((self.width - 44) / 100),
                                                  self.y + (self.height / 2 - 7), 14, 14)

        if self.endRect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.slider_value = 100
                self.miniSliderRect = pygame.Rect((self.x + 15) + int(self.slider_value) * ((self.width - 44) / 100),
                                                  self.y + (self.height / 2 - 7), 14, 14)

        self.sliderSurf = self.font.render(str(int(self.slider_value)), True, "white")
        dis.blit(self.sliderSurf, [(self.x + self.width / 2) - 12, self.y + 30])
