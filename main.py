from constants import *
import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a pygame Clock object to track of time
    clock = pygame.time.Clock()
    delta = 0

    while True:
        # This will check if the user has closed the window
        # and exit the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("BLACK")    # Set the rectangle to be solid black
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        delta = clock.tick(60) / 1000  # Convert from msec to sec


if __name__ == "__main__":
    main()