"""Welcome Screen Component - Version 2
A component to welcome the user to the program, and give them options, such as
to display instructions, to customise their car, to start the game, or to quit
the program.
- Renamed the game window to match the title: "Highway Haulers"
- Created a class to create buttons to detect user inputs
"""

# IMPORTS...
import pygame

# INITIALISATIONS...
pygame.init()


# CLASSES...
class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_surface = (pygame.font.Font(None, 32).render
                             (text, True, (0, 0, 0)))

    def draw_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface,
                    (self.rect.x + (self.rect.width // 2 -
                                    self.text_surface.get_width() // 2),
                     self.rect.y + (self.rect.height // 2 -
                                    self.text_surface.get_height() // 2)))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# FUNCTIONS...
def scale(image, factor):
    size = round(image.get_width() * factor), round(image.get_height() *
                                                    factor)
    return pygame.transform.scale(image, size)


def draw_assets():
    # Display the track and grassy background
    SCREEN.blit(HIGHWAY, (0, 0))


def welcome_screen():
    started = False
    while not started:
        # Fill the screen with grey
        SCREEN.fill(DARK_GREY)
        # Display a title
        TITLE_TEXT1 = TITLE_FONT.render("Highway", True,
                                        VIBRANT_PURPLE)
        TITLE_TEXT2 = TITLE_FONT.render("Haulers", True,
                                        VIBRANT_PURPLE)
        TITLE_RECT1 = TITLE_TEXT1.get_rect(center=(WIDTH // 2, HEIGHT // 6))
        TITLE_RECT2 = TITLE_TEXT2.get_rect(center=(WIDTH // 2,
                                                   HEIGHT // 6 + 38))
        SCREEN.blit(TITLE_TEXT1, TITLE_RECT1)
        SCREEN.blit(TITLE_TEXT2, TITLE_RECT2)
        pygame.display.flip()

    return


# MAIN PROGRAM...
# Load Game Assets:
HIGHWAY = scale(pygame.image.load("highway.jpg"), 0.9)
BLUE_CAR = scale(pygame.image.load("blue-car.png"), 0.1)
GREEN_CAR = scale(pygame.image.load("green-car.png"), 0.1)
ORANGE_CAR = scale(pygame.image.load("orange-car.png"), 0.1)
PURPLE_CAR = scale(pygame.image.load("purple-car.png"), 0.1)
RED_CAR = scale(pygame.image.load("red-car.png"), 0.1)
TEAL_CAR = scale(pygame.image.load("teal-car.png"), 0.1)
ICON = pygame.image.load("icon.png")

# Set Colour Tuples:
DARK_GREY = (60, 60, 60)
VIBRANT_PURPLE = (188, 0, 255)

# Set Fonts:
TITLE_FONT = pygame.font.SysFont("goudystout", 40)

# Calculate and store the height and width needed for the screen
WIDTH = HIGHWAY.get_width()
HEIGHT = HIGHWAY.get_height()

# Initialise PyGame screen and change name/icon
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Highway Haulers")
pygame.display.set_icon(ICON)

# Game frame-rate via pygame clock
FPS = 60
clock = pygame.time.Clock()

# Displays welcome screen
welcome_screen()

# Game Loop:
running = True
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
