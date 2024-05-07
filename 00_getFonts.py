"""Simple program to load all available fonts in PyGame."""

import pygame

# Initialize Pygame
pygame.init()

# Get the list of default installed fonts
pygame_fonts = pygame.font.get_fonts()

# Print the list of default installed fonts
for font in pygame_fonts:
    print(font)

# Quit Pygame
pygame.quit()