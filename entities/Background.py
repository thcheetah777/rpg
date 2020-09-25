# entities/Background.py
# Import pygame
import pygame

# Import sys
import sys
sys.path.append('../')

# Import local classes
from entities.EntityBase import EntityBase
from classes.Input import Input
from traits.go import goTrait

# Background class
class Background(EntityBase):
    # Initializer
    def __init__(self, screen, x, y):
        # Super initializer
        super(Background, self).__init__(x, y)

        # Input class instance
        self.input = Input(self)

        # Properties
        self.img = pygame.transform.rotozoom(pygame.image.load("imgs\grass2.png"), 0, 10)
        self.screen = screen
        self.speed = 0

        # Traits
        self.traits = {
            "goTrait": goTrait(self.screen, self, self.speed)
        }

    # Update method
    def update(self):
        # Call update on goTrait class instance
        self.traits["goTrait"].update()

        # Check for input on input instance
        self.input.checkForInput()

        # Draw sprite
        self.draw()

    # Draw method
    def draw(self):
        # Blit self.img
        self.screen.blit(self.img, (self.rect[0], self.rect[1]))
