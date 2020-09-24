import pygame
import sys
sys.path.append('../')
from entities.EntityBase import EntityBase
from classes.Input import Input

class Player(EntityBase):
    def __init__(self, speed, screen):
        super(Player, self).__init__()
        self.input = Input(self)
        self.screen = screen
        self.speed = speed
        self.traits = {
            "goTrait": goTrait(self.screen, self)
        }

    def update(self):
        self.input.checkForInput()
        self.draw()

    def draw(self):
        pygame.draw.circle(self.screen, pygame.color.Color("#8080FF"), [int(self.rect[0]), int(self.rect[1])], 6)
