import pygame
from classes.Sound import Sound
from entities.Player import Player
from entities.Object import Object
from entities.Background import Background

def main():
    windowSize = [600, 600]
    keep_going = True
    timer = pygame.time.Clock()
    screen = pygame.display.set_mode(windowSize)
    sound = Sound()
    sound.playMusic(sound.soundtrack)
    object = Object(screen, windowSize[0] // 2, windowSize[1] // 2, "#e00000")
    player = Player(2, screen, windowSize[0] // 2, windowSize[1] // 2)
    background = Background(screen, windowSize[0] // -5, windowSize[1] // -5)
    while keep_going:
        screen.fill("#4287f5")
        background.update()
        player.update()
        object.update()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
    timer.tick(720)

if __name__ == "__main__":
    main()
