import pygame

class Input(object):
    def __init__(self, ent):
        self.ent = ent

    def checkForInput(self):
        events = pygame.event.get()
        self.checkForKeyboardInput()
