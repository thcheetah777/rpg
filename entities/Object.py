# entities/Objects.py
# Import pygame
import pygame

# Import sys
import sys
sys.path.append('../')

# Import local classes
from entities.EntityBase import EntityBase
from classes.Input import Input
from traits.go import goTrait

# Object class
class Object(EntityBase):
    # Initializer
    def __init__(self, screen, x, y, color):
        # Super initializer
        super(Object, self).__init__(x, y)

        # Input class instance
        self.input = Input(self)

        self.screen = screen
        self.color = color
        self.speed = 0

        # Traits
        self.traits = {
            "goTrait": goTrait(self.screen, self, self.speed)
        }

    # Update method
    def update(self):
        # Calls update on goTrait instance
        self.traits["goTrait"].update()
        self.input.checkForInput()
        self.draw()

    # Draw method
    def draw(self):
        # Draw red circle
        pygame.draw.circle(self.screen, pygame.color.Color(self.color), [int(self.rect[0]), int(self.rect[1])], 12)
