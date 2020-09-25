import pygame
import sys
sys.path.append('../')
from entities.EntityBase import EntityBase
from classes.Input import Input
from traits.go import goTrait

class Background(EntityBase):
    def __init__(self, screen, x, y):
        super(Background, self).__init__(x, y)
        self.input = Input(self)
        self.img = pygame.transform.rotozoom(pygame.image.load("imgs\grass2.png"), 0, 10)
        self.screen = screen
        self.speed = 0
        self.traits = {
            "goTrait": goTrait(self.screen, self, self.speed)
        }

    def update(self):
        self.traits["goTrait"].update()
        self.input.checkForInput()
        self.draw()

    def draw(self):
        self.screen.blit(self.img, (self.rect[0], self.rect[1]))
