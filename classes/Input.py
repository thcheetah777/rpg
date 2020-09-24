import pygame

class Input(object):
    def __init__(self, ent):
        self.ent = ent

    def checkForInput(self):
        events = pygame.event.get()
        self.checkForKeyboardInput()

    def checkForKeyboardInput(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT] or keys[K_a]:
            self.ent.traits["goTrait"].dir = -ent.speed
        elif keys[K_RIGHT] or keys[K_d]:
            self.ent.traits["goTrait"].dir = ent.speed
        else:
            self.ent.traits["goTrait"].dir = 0
