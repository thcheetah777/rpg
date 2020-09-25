# traits/go.py
# Import pygame
import pygame

# GoTrait class
class goTrait(object):
    # Initializer
    def __init__(self, screen, ent, speed):
        self.dir = 0
        self.speed = speed
        self.screen = screen
        self.ent = ent

    # Update method
    def update(self):
        # Call self.move
        self.move()

    # Move method
    def move(self):
        # Checks what dir ent is in
        if self.dir == 0:
            self.ent.rect[0] += -self.speed - -2
        elif self.dir == 1:
            self.ent.rect[0] += self.speed - 2
        elif self.dir == 2:
            self.ent.rect[1] += -self.speed - -2
        elif self.dir == 3:
            self.ent.rect[1] += self.speed - 2
