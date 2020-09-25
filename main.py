import pygame
from entities.Player import Player
from entities.Object import Object

windowSize = [600, 600]
screen = pygame.display.set_mode(windowSize)
player = Player(0.3, screen, windowSize[0] // 2, windowSize[1] // 2)
object = Object(screen, windowSize[0] // 2, windowSize[1] // 2)
def main():
    keep_going = True
    while keep_going:
        screen.fill(pygame.color.Color("#ffffff"))
        player.update()
        object.update()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False

if __name__ == "__main__":
    main()
