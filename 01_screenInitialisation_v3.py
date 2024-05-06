""" Screen Initialisation Component - Version 3
A component to create the game window and load all of the game assets.
- Placed the screen in a while loop to keep it on until the user closes the
window.
"""

# IMPORTS...
import pygame

# INITIALISATIONS...
pygame.init()

# MAIN PROGRAM...
# Load Game Assets
FINISH = pygame.image.load("finish.png")
GRASS = pygame.image.load("grass.jpg")
TRACK = pygame.image.load("track.png")
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

# Game Loop:
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Initialise PyGame screen and change name/icon
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Racing Game")
    pygame.display.set_icon(ICON)