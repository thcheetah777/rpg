# main.py
# Import pygame
import pygame

# Import local classes
from classes.Sound import Sound
from entities.Player import Player
from entities.Object import Object
from entities.Background import Background

# Function main
def main():
    # Set window size
    windowSize = [600, 600]

    # Create variable keep_going
    keep_going = True

    # Create pygame Clock class instance
    timer = pygame.time.Clock()

    # Create display
    screen = pygame.display.set_mode(windowSize)

    # Create instances of local classes
    sound = Sound()
    sound.playMusic(sound.soundtrack)
    object = Object(screen, windowSize[0] // 2, windowSize[1] // 2, "#e00000")
    player = Player(2, screen, windowSize[0] // 2, windowSize[1] // 2)
    background = Background(screen, -windowSize[0], -windowSize[1])

    # Play soundtrack in sound class
    sound.playMusic(sound.soundtrack)

    # Game loop
    while keep_going:
        # Fill screen with blue
        screen.fill("#4287f5")

        # Update entities
        background.update()
        player.update()
        object.update()

        # Flip display
        pygame.display.flip()

        # Check if quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Set keep_going to false
                keep_going = False

    # Call tick method in timer instance
    timer.tick(720)

# Call main function
if __name__ == "__main__":
    main()
