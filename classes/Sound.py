# classes/Sound.py
# Import pygame
import pygame

# Initialize pygame.mixer
pygame.mixer.init()

# Sound class
class Sound:
    # Initializer
    def __init__(self):
        # Properties
        self.musicChannel = pygame.mixer.Channel(0)

        # Set volume
        self.musicChannel.set_volume(0.5)

        # File path
        self.soundtrack = pygame.mixer.Sound("./sfx/overworld.ogg")

    # PlayMusic method
    def playMusic(self, music):
        self.musicChannel.play(music)
