import pygame

class Input(object):
    def __init__(self, ent):
        self.ent = ent

    def checkForInput(self):
        self.checkForKeyboardInput()

    def checkForKeyboardInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.ent.traits["goTrait"].dir = 0
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.ent.traits["goTrait"].dir = 1
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.ent.traits["goTrait"].dir = 2
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.ent.traits["goTrait"].dir = 3
        else:
            self.ent.traits["goTrait"].dir = 4
