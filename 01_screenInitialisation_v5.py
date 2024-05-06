""" Screen Initialisation Component - Version 5
A component to create the game window and load all of the game assets.
- Created a function to scale the images to the needed size for the screen.
- Scaled the grass background and the track to size.
"""

# IMPORTS...
import pygame

# INITIALISATIONS...
pygame.init()

# FUNCTIONS...
def scale(image, factor):
    size = round(image.get_width() * factor), round(image.get_height() *
                                                    factor)
    return pygame.transform.scale(image, size)


# MAIN PROGRAM...
# Load Game Assets
FINISH = pygame.image.load("finish.png")
GRASS = scale(pygame.image.load("grass.jpg"), 2.5)
TRACK = scale(pygame.image.load("track.png"), 0.9)
TRACK_BORDER = pygame.image.load("track-border.png")
BLUE_CAR = pygame.image.load("blue-car.png")
GREEN_CAR = pygame.image.load("green-car.png")
ORANGE_CAR = pygame.image.load("orange-car.png")
PURPLE_CAR = pygame.image.load("purple-car.png")
RED_CAR = pygame.image.load("red-car.png")
TEAL_CAR = pygame.image.load("teal-car.png")
ICON = pygame.image.load("icon.png")

# Calculate and store the height and width needed for the screen
WIDTH = TRACK.get_width()
HEIGHT = TRACK.get_height()

# Initialise PyGame screen and change name/icon
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")
pygame.display.set_icon(ICON)

# Game frame-rate via pygame clock
FPS = 60
clock = pygame.time.Clock()

running = True

# Game Loop:
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Display the track and grassy background
    SCREEN.blit(GRASS, (0, 0))
    SCREEN.blit(TRACK, (0, 0))
    SCREEN.blit((FINISH), (0, 0))

    pygame.display.flip()

    # Ticks the clock at the value of the FPS
    clock.tick(FPS)

pygame.quit()
quit()
