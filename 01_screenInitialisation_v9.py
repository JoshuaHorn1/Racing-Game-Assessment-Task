""" Screen Initialisation Component - Version 9
A component to create the game window and load all of the game assets.
- Decided to continue to develop 01_screenInitialisation_v8.
- Removed old/unneeded game asset code.
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


def draw_assets():
    # Display the track and grassy background
    SCREEN.blit(HIGHWAY, (0, 0))


# MAIN PROGRAM...
# Load Game Assets
HIGHWAY = scale(pygame.image.load("highway.jpg"), 0.9)
BLUE_CAR = scale(pygame.image.load("blue-car.png"), 0.1)
GREEN_CAR = scale(pygame.image.load("green-car.png"), 0.1)
ORANGE_CAR = scale(pygame.image.load("orange-car.png"), 0.1)
PURPLE_CAR = scale(pygame.image.load("purple-car.png"), 0.1)
RED_CAR = scale(pygame.image.load("red-car.png"), 0.1)
TEAL_CAR = scale(pygame.image.load("teal-car.png"), 0.1)
ICON = pygame.image.load("icon.png")

# Calculate and store the height and width needed for the screen
WIDTH = HIGHWAY.get_width()
HEIGHT = HIGHWAY.get_height()

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
        # Exit PyGame if the user closes the window
        if event.type == pygame.QUIT:
            running = False
            break

    # Calls the draw_assets() function to draw all assets on the screen
    draw_assets()

    # Updates the screen
    pygame.display.flip()

    # Ticks the clock at the value of the FPS
    clock.tick(FPS)

pygame.quit()
quit()
