import pygame
from display import dis


class TextFiled:
    def __init__(self, x, y, width, height, font_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.now_edit = False
        self.text = ""

        self.fieldSurface = pygame.Surface((self.width, self.height))
        self.fieldRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.font = pygame.font.SysFont('Arial', font_size, bold=True, italic=True)
        self.filedSurf = self.font.render(self.text, True, "black")

    def text_editing(self):
        mouse_pos = pygame.mouse.get_pos()
        self.fieldSurface.fill('#a0522d')
        self.filedSurf = self.font.render(self.text, True, "white")
        if self.fieldRect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed(num_buttons=3)[0] and self.now_edit is False:
                self.now_edit = True
        if self.now_edit:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.filedSurf = self.font.render(self.text, True, "white")
                        self.now_edit = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                        self.filedSurf = self.font.render(self.text, True, "white")
                    else:
                        self.text += event.unicode
                        self.filedSurf = self.font.render(self.text, True, "white")

        self.fieldSurface.blit(self.filedSurf, [
            self.fieldRect.width / 2 - self.filedSurf.get_rect().width / 2,
            self.fieldRect.height / 2 - self.filedSurf.get_rect().height / 2
        ])

        dis.blit(self.fieldSurface, self.fieldRect)
