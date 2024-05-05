""" Screen Initialisation Component - Version 1
A component to create the game window and load all of the game assets.
- Found and loaded images to use as game assets.
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
