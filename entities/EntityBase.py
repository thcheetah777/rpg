# entities/EntityBase
# Import pygame
import pygame

# EntityBase class
class EntityBase(object):
    # Initializer
    def __init__(self, x, y):
        # Properties
        self.type = ""
        self.rect = [x, y]
        self.alive = True
