# classes/Input.py
# Import pygame
import pygame

# Input class
class Input(object):
    # Initializer
    def __init__(self, ent):
        # Properties
        self.ent = ent

    # Method checkForInput
    def checkForInput(self):
        # Call checkForKeyboardInput
        self.checkForKeyboardInput()

    # Method checkForKeyboardInput
    def checkForKeyboardInput(self):
        # List keys
        keys = pygame.key.get_pressed()

        # Check get_pressed
        # If left or a pressed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # Set direction of self.ent to 0
            self.ent.traits["goTrait"].dir = 0
        # If right or d pressed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # Set direction of self.ent to 1
            self.ent.traits["goTrait"].dir = 1
        # If up or w pressed
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            # Set direction of self.ent to 2
            self.ent.traits["goTrait"].dir = 2
        # If down or s pressed
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # Set direction of self.ent to 3
            self.ent.traits["goTrait"].dir = 3
        # If nothing pressed
        else:
            # Set direction of self.ent to 4
            self.ent.traits["goTrait"].dir = 4
