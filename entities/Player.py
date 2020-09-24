import pygame
import sys
sys.path.append('../')
from entities.EntityBase import EntityBase
from classes.Input import Input

class Player(EntityBase):
    def __init__(self, speed, screen):
        super(Player, self).__init__()
        
