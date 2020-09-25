import pygame
pygame.mixer.init()

class Sound:
    def __init__(self):
        self.musicChannel = pygame.mixer.Channel(0)
        self.musicChannel.set_volume(0.5)
        self.soundtrack = pygame.mixer.Sound("./sfx/main.mp3")

    def playMusic(self, music):
        self.musicChannel.play(music)
