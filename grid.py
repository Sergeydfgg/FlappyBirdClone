import pygame
from display import dis


class Grid:
    def __init__(self, col=0, rol=0, x=0, y=0, width=0, height=0, source="pass", fon_color="balck",
                 border_color="white", font_size=20):
        self.col = col
        self.rol = rol
        self.width = width
        self.height = height
        self.col_names = []
        self.source = source
        self.done_source = {}

        self.fon_color = fon_color
        self.border_color = border_color

        self.cell_list = [[] for _ in range(self.col)]

        for col in range(self.col):
            for rol in range(self.rol):
                self.cell_list[col].append((pygame.Surface((self.width - 10, self.height - 5)),
                                            pygame.Rect(x + self.width*col, y + self.height*rol,
                                                        self.width, self.height + 5)))
        self.font = pygame.font.SysFont('Arial', font_size, bold=True)
        self.gridSurf = self.font.render("test", True, "white")

    def draw_grid(self):
        source_keys = list(self.done_source.keys())
        for col in range(self.col):
            self.gridSurf = self.font.render(str(source_keys[col]), True, "red")
            cur_rect = self.cell_list[col][0][1]
            cur_surface = self.cell_list[col][0][0]
            cur_surface.fill(self.fon_color)
            pygame.draw.rect(dis, self.border_color, cur_rect)
            cur_surface.blit(self.gridSurf,
                             [cur_surface.get_rect().width / 2 - self.gridSurf.get_rect().width / 2,
                              self.gridSurf.get_rect().height - 10])
            dis.blit(cur_surface, (cur_rect.x + 5, cur_rect.y + 5))
            for rol in range(0, self.rol - 1):
                try:
                    self.gridSurf = self.font.render(str(self.done_source[source_keys[col]][rol]), True, "white")
                    cur_rect = self.cell_list[col][rol+1][1]
                    cur_surface = self.cell_list[col][rol+1][0]
                    cur_surface.fill(self.fon_color)
                    pygame.draw.rect(dis, self.border_color, cur_rect)
                    cur_surface.blit(self.gridSurf,
                                     [cur_surface.get_rect().width / 2 - self.gridSurf.get_rect().width / 2,
                                      self.gridSurf.get_rect().height - 10])
                    dis.blit(cur_surface, (cur_rect.x + 5, cur_rect.y + 5))
                except IndexError:
                    pass

    def prepare_source(self):
        with open(self.source, "r") as file:
            for cur_line in file:
                cur_line_list = cur_line.split("=")
                cur_key = cur_line_list[0]
                self.col_names.append(cur_key)
                self.done_source.update({cur_key: []})
                for cur_res in cur_line_list[1].strip().split(" "):
                    self.done_source[cur_key].append(cur_res.strip())

        return self.done_source

    def update_source(self, new_source):
        with open(self.source, "w") as file:
            for key in new_source.keys():
                file.write(str(key)+"=")
                for val in new_source[key]:
                    file.write(str(val) + " ")
                file.write("\n")
