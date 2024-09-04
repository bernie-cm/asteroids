from constants import *
from player import Player
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create a pygame Clock object to track of time
    clock = pygame.time.Clock()
    # Instantiate a Player class object
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        # This will check if the user has closed the window
        # and exit the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")    # Set the rectangle to be solid black
        # Render the player shape
        player.draw(screen)
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000  # Convert from msec to sec




if __name__ == "__main__":
    main()