from pygame import Rect


class Bird:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.pos_x = 40
        self.pos_y = 210

        self.speed = 1
        self.jump_dur = 0

        self.state = "fall"

    def make_bird(self) -> Rect:
        return Rect(self.pos_x, self.pos_y, self.width, self.height)

    def bird_jump(self):
        if self.jump_dur == 0:
            self.speed = 10

        if self.speed <= 0:
            self.state = "fall"
            self.speed = 0
            self.jump_dur = 0
            return

        self.pos_y -= self.speed
        self.jump_dur += 1
        self.speed -= 1

    def bird_fall(self):
        self.pos_y += self.speed
        self.speed += 1

    def is_collide(self, rect_1, rect_2):
        bird_rect = Rect(self.pos_x, self.pos_y, self.width, self.height)
        if bird_rect.colliderect(rect_1) or bird_rect.colliderect(rect_2):
            return True
        return False
