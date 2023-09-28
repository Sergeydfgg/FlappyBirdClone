import pygame
from random import randrange, choice

dis_width = 600
dis_height = 500
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Flappy Bird')

color_dict = {"windows": [(240, 230, 140), (255, 255, 0), (255, 215, 0)],
              "door": [(210, 105, 30), (139, 69, 19), (160, 82, 45)],
              "wall": [(188, 143, 143), (230, 230, 250), (176, 196, 222)],
              "tree": [(210, 105, 30), (139, 69, 19), (244, 164, 96)],
              "leaves": [(107, 142, 45), (85, 107, 47), (34, 139, 34)],
              "fon": [(0, 255, 255), (70, 130, 180), (0, 191, 255)]}


class Fon:
    def __init__(self):
        self.col = int(dis_width/12)
        self.rol = int(dis_height/10)
        self.cur_iter = 0
        self.fon_matrix = []
        for col in range(self.col):
            self.fon_matrix.append([])

        for col in range(len(self.fon_matrix)):
            for rol in range(self.rol):
                self.fon_matrix[col].append(pygame.Rect(50*col, 50*rol, 50, 50))

        self.fon_color = ()
        self.wall_color = ()
        self.window_color = ()
        self.leaves_color = ()
        self.tree_color = ()

    def draw_fon(self):

        if self.cur_iter == 0:
            self.fon_color = choice(color_dict["fon"])
            self.wall_color = choice(color_dict["wall"])
            self.window_color = choice(color_dict["windows"])
            self.leaves_color = choice(color_dict["leaves"])
            self.tree_color = choice(color_dict["tree"])

            for col in range(0, 3):
                for rol in range(0, 10):
                    pygame.draw.rect(dis, self.fon_color,
                                     self.fon_matrix[col][rol])

            for col in range(3, 13):
                for rol in range(self.rol):
                    pygame.draw.rect(dis, self.wall_color,
                                     self.fon_matrix[col][rol])

            for col in range(4, 13, 3):
                for rol in range(1, 10, 3):
                    pygame.draw.rect(dis, self.window_color,
                                     self.fon_matrix[col][rol])
                    pygame.draw.rect(dis, self.window_color,
                                     self.fon_matrix[col+1][rol])
                    pygame.draw.rect(dis, self.window_color,
                                     self.fon_matrix[col][rol+1])
                    pygame.draw.rect(dis, self.window_color,
                                     self.fon_matrix[col+1][rol+1])

            for col in range(1, 6):
                for rol in range(3, 8):
                    pygame.draw.rect(dis, self.leaves_color,
                                     self.fon_matrix[col][rol])

            pygame.draw.rect(dis, self.tree_color, self.fon_matrix[3][8])
            pygame.draw.rect(dis, self.tree_color, self.fon_matrix[3][9])

        else:
            for col in range(0, 3):
                for rol in range(0, 10):
                    pygame.draw.rect(dis, self.fon_color,
                                     self.fon_matrix[col][rol])

            for col in range(3, 13):
                for rol in range(self.rol):
                    pygame.draw.rect(dis, self.wall_color,
                                     self.fon_matrix[col][rol])

            for col in range(4, 13, 3):

                for rol in range(1, 10, 3):
                    pygame.draw.rect(dis, self.window_color,
                                     self.fon_matrix[col][rol])
                    pygame.draw.rect(dis, self.window_color,
                                     self.fon_matrix[col + 1][rol])
                    pygame.draw.rect(dis, self.window_color,
                                     self.fon_matrix[col][rol + 1])
                    pygame.draw.rect(dis, self.window_color,
                                     self.fon_matrix[col + 1][rol + 1])

            for col in range(1, 6):
                for rol in range(3, 8):
                    pygame.draw.rect(dis, self.leaves_color,
                                     self.fon_matrix[col][rol])

            pygame.draw.rect(dis, self.tree_color, self.fon_matrix[3][8])
            pygame.draw.rect(dis, self.tree_color, self.fon_matrix[3][9])

            if self.cur_iter == 350:
                self.cur_iter = -1

        self.cur_iter += 1
