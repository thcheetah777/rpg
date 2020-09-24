import pygame

class EntityBase(object):
    def __init__(self, x, y):
        self.type = ""
        self.rect = [x, y]
        self.alive = True
