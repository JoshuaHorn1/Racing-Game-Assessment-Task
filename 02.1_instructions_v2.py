"""Instructions Component - Version 2
A component to display the game instructions. Accessed through the
welcome_screen() function.
- Returns to the welcome screen after pressing back in the instructions. This
was done by moving the back button down.
"""

# IMPORTS...
import pygame

# INITIALISATIONS...
pygame.init()


# CLASSES...
class Button:
    # Initialises the button class
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_surface = (pygame.font.SysFont(
            "agencyfb", 45).render(
            text, True, (0, 0, 0)))

    # Draws the buttons on the screen
    def draw_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface,
                    (self.rect.x + (self.rect.width // 2 -
                                    self.text_surface.get_width() // 2),
                     self.rect.y + (self.rect.height // 2 -
                                    self.text_surface.get_height() // 2)))

    # If a button is clicked, it will return the position
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# FUNCTIONS...
# A function to scale assets to the correct size
def scale(image, factor):
    size = round(image.get_width() * factor), round(image.get_height() *
                                                    factor)
    return pygame.transform.scale(image, size)


# A function to centre buttons on the screen
def center_x(button_width, screen_width):
    return (screen_width // 2) - (button_width // 2)


# A function to draw all game assets
def draw_assets(draw_list):
    for asset, pos in draw_list:
        SCREEN.blit(asset, pos)


# A function to display the welcome screen
def welcome_screen():
    started = False

    BUTTON_WIDTH = 250
    button_x = center_x(BUTTON_WIDTH, WIDTH)

    # A list containing all of the buttons to display
    buttons = [
        Button(button_x, 225, BUTTON_WIDTH, 65,
               LIGHT_GREY, "Start Game"),
        Button(button_x, 325, BUTTON_WIDTH, 65,
               LIGHT_GREY, "Instructions"),
        Button(button_x, 425, BUTTON_WIDTH, 65,
               LIGHT_GREY, "Customise"),
        Button(button_x, 525, BUTTON_WIDTH, 65,
               LIGHT_GREY, "Quit"),
    ]

    while not started:
        # Checks if the user ever closes the window
        for event in pygame.event.get():
            # Exit PyGame if the user closes the window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Fill the screen with grey
        SCREEN.fill(DARK_GREY)

        # Display a title
        TITLE_TEXT1 = TITLE_FONT.render("Highway", True,
                                        VIBRANT_PURPLE)
        TITLE_TEXT2 = TITLE_FONT.render("Haulers", True,
                                        VIBRANT_PURPLE)
        TITLE_RECT1 = TITLE_TEXT1.get_rect(center=(WIDTH // 2, HEIGHT // 7))
        TITLE_RECT2 = TITLE_TEXT2.get_rect(center=(WIDTH // 2,
                                                   HEIGHT // 7 + 38))
        SCREEN.blit(TITLE_TEXT1, TITLE_RECT1)
        SCREEN.blit(TITLE_TEXT2, TITLE_RECT2)

        # Draw and handle clicks for buttons
        for button in buttons:
            button.draw_button(SCREEN)
            if pygame.mouse.get_pressed()[0] and button.is_clicked(
                    pygame.mouse.get_pos()):
                button_clicked = button.text

                # Checks which button the user clicked
                if button_clicked == "Start Game":
                    return
                if button_clicked == "Instructions":
                    instructions()
                if button_clicked == "Customise":
                    pass
                if button_clicked == "Quit":
                    print("test")
                    pygame.quit()
                    quit()

        # Updates the display
        pygame.display.flip()

    return


def instructions():
    back = False
    while not back:  # returns once user has pressed the back button
        for event in pygame.event.get():
            # Exit PyGame if the user closes the window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Fills the screen with a dark grey
        SCREEN.fill(DARK_GREY)

        # Displays the instructions text on the screen
        CONTROLS_TEXT1 = DEFAULT_FONT.render("Press 'A' or >LEFT ARROW< to", True, WHITE)
        CONTROLS_TEXT2 = DEFAULT_FONT.render("change lanes to the left.", True, WHITE)
        CONTROLS_RECT1 = CONTROLS_TEXT1.get_rect(center=(WIDTH // 2, 20))
        CONTROLS_RECT2 = CONTROLS_TEXT2.get_rect(center=(WIDTH // 2, 40))
        SCREEN.blit(CONTROLS_TEXT1, CONTROLS_RECT1)
        SCREEN.blit(CONTROLS_TEXT2, CONTROLS_RECT2)
        CONTROLS_TEXT3 = DEFAULT_FONT.render("Press 'W' or >RIGHT ARROW< to",True, WHITE)
        CONTROLS_TEXT4 = DEFAULT_FONT.render("change lanes to the right.", True, WHITE)
        CONTROLS_RECT3 = CONTROLS_TEXT3.get_rect(center=(WIDTH // 2, 80))
        CONTROLS_RECT4 = CONTROLS_TEXT4.get_rect(center=(WIDTH // 2, 100))
        SCREEN.blit(CONTROLS_TEXT3, CONTROLS_RECT3)
        SCREEN.blit(CONTROLS_TEXT4, CONTROLS_RECT4)
        # SCORE_TEXT1 = DEFAULT_FONT.render("Points are based off of how many", True, WHITE)
        # SCORE_TEXT2 = DEFAULT_FONT.render("cars you pass before you crash.", True, WHITE)
        # SCORE_RECT1 = CONTROLS_TEXT1.get_rect(center=(WIDTH // 2 - 40, 140))
        # SCORE_RECT2 = CONTROLS_TEXT2.get_rect(center=(WIDTH // 2 - 30, 160))
        # SCREEN.blit(SCORE_TEXT1, SCORE_RECT1)
        # SCREEN.blit(SCORE_TEXT2, SCORE_RECT2)

        BACK_BUTTON = Button(*BACK_BUTTON_INFO)
        BACK_BUTTON.draw_button(SCREEN)
        if pygame.mouse.get_pressed()[0] and BACK_BUTTON.is_clicked(
                pygame.mouse.get_pos()):
            return

        pygame.display.flip()


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
LIGHT_GREY = (150, 150, 150)
VIBRANT_PURPLE = (188, 0, 255)
WHITE = (255, 255, 255)

# Set Fonts:
DEFAULT_FONT = pygame.font.SysFont("couriernew", 20)
TITLE_FONT = pygame.font.SysFont("goudystout", 40)

# Calculate and store the height and width needed for the screen
WIDTH = HIGHWAY.get_width()
HEIGHT = HIGHWAY.get_height()

# Initialise PyGame screen and change name/icon
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Highway Haulers")
pygame.display.set_icon(ICON)

# Universal back button information
BACK_BUTTON_INFO = [center_x(250, WIDTH), HEIGHT - 75, 250, 65,
                    (150, 150, 150), "Back"]

# Game frame-rate via pygame clock
FPS = 60
clock = pygame.time.Clock()

# Displays welcome screen
welcome_screen()

# List containing all assets to draw and their positions
assets = [
    (HIGHWAY, (0, 0)),
]

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
    draw_assets(assets)

    # Updates the screen
    pygame.display.flip()

    # Ticks the clock at the value of the FPS
    clock.tick(FPS)

pygame.quit()
quit()
