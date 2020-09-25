# entities/Player.py
# Import pygame
import pygame

# Import sys
import sys
sys.path.append('../')

# Import local classes
from entities.EntityBase import EntityBase
from classes.Input import Input
from traits.go import goTrait

# Player class, inherits from EntityBase superclass
class Player(EntityBase):
    # Initializer
    def __init__(self, speed, screen, x, y):
        # Super initializer
        super(Player, self).__init__(x, y)

        # Properties
        # Input class instance
        self.input = Input(self)
        
        self.screen = screen
        self.speed = speed

        # Traits
        self.traits = {
            "goTrait": goTrait(self.screen, self, self.speed)
        }

    # Update method
    def update(self):
        # Call update on goTrait
        self.traits["goTrait"].update()

        # Check for input on input
        self.input.checkForInput()

        # Draw sprite
        self.draw()

    # Draw method
    def draw(self):
        # Draw blue circle
        pygame.draw.circle(self.screen, pygame.color.Color("#8080FF"), [int(self.rect[0]), int(self.rect[1])], 12)
