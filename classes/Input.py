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
            self.ent.traits["goTrait"].dir = -1
        elif keys[K_RIGHT] or keys[K_d]:
            self.ent.traits["goTriat"].dir = 1
        else:
            self.ent.traits["goTriat"].dir = 0
