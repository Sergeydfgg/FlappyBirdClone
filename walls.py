from random import randrange
from pygame import Rect, image, transform


class Walls:
    def __init__(self, x: int):
        self.x_pos = x
        self.y_pos = 0
        self.up_height = randrange(50, 300)

    def __getitem__(self, item):
        if item == 0:
            return Rect(self.x_pos, self.y_pos, 50, self.up_height)
        elif item == 1:
            return Rect(self.x_pos, self.up_height + 170, 50, 500 - (self.up_height + 170))

    def wall_move(self):
        self.x_pos -= 2
