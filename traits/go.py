import pygame

class goTrait(object):
    def __init__(self, screen, ent):
        self.dir = 0
        self.speed = ent.speed
        self.screen = screen
        self.ent = ent

    def update(self):
        self.move()

    def move(self):
        if self.dir == 0:
            self.ent.rect[0] += -self.speed
        elif self.dir == 1:
            self.ent.rect[0] += self.speed
        elif self.dir == 2:
            self.ent.rect[1] += -self.speed
        elif self.dir == 3:
            self.ent.rect[1] += self.speed
