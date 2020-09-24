import pygame

class goTrait(object):
    def __init__(self, screen, ent):
        self.dir = 0
        self.speed = ent.speed
        self.screen = screen
        self.ent = ent

    def update(self):
        move(self.speed)

    def move(self, speed):
        self.ent.rect.x += speed
