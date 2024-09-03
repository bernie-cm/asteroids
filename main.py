from constants import *
import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # his will check if the user has closed the window
        # and exit the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("BLACK")    # Set the rectangle to be solid black
        pygame.display.flip()



if __name__ == "__main__":
    main()