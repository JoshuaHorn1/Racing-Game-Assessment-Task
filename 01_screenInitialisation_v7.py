""" Screen Initialisation Component - Version 7
A component to create the game window and load all of the game assets.
- Created a separate function for drawing all assets.
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
    SCREEN.blit(GRASS, (0, 0))
    SCREEN.blit(TRACK, (0, 0))
    SCREEN.blit(FINISH, (0, 0))


# MAIN PROGRAM...
# Load Game Assets
FINISH = pygame.image.load("finish.png")
GRASS = scale(pygame.image.load("grass.jpg"), 2.5)
TRACK = scale(pygame.image.load("track.png"), 0.9)
TRACK_BORDER = scale(pygame.image.load("track-border.png"), 0.9)
BLUE_CAR = scale(pygame.image.load("blue-car.png"), 0.07)
GREEN_CAR = scale(pygame.image.load("green-car.png"), 0.07)
ORANGE_CAR = scale(pygame.image.load("orange-car.png"), 0.07)
PURPLE_CAR = scale(pygame.image.load("purple-car.png"), 0.07)
RED_CAR = scale(pygame.image.load("red-car.png"), 0.07)
TEAL_CAR = scale(pygame.image.load("teal-car.png"), 0.07)
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
