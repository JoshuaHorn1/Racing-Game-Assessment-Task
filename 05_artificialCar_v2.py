"""Artificial Car Component - Version 2
A component to generate and start AI controlled (simulated) cars down both
directions along the lanes for the user car to collide with.
- Created a list to store all of the AI cars.
- Created generate_car() function
"""

# IMPORTS...
import pygame
import random

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


class Car:
    def __init__(self, x, y, lane, color, velocity):
        self.x = x
        self.y = y
        self.lane = lane
        self.color = color
        self.velocity = velocity

    def move(self, background_scroll):
        # Update car's y position based on its velocity and background scroll
        self.y += self.velocity - background_scroll

    def draw(self, screen):
        # Draw the car on the screen at its current position
        screen.blit(self.color, (self.x + self.lane, self.y))


# FUNCTIONS...


# A function to check if the window is ever closed
def quit_check():
    for event in pygame.event.get():
        # Exit PyGame if the user closes the window
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


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


def generate_car(background_velocity):
    create_car = random.randint(1, 600)  # randomly create car
    if create_car <= 5:
        # Choose a random lane, color, and set a negative velocity (moving up)
        lane = random.choice(LANES)
        random_colour = CARS[car_list[random.randint(0, 5)]]
        velocity = - (background_velocity + random.randint(1, 5))
        # Create a new Car object and add it to the cars list
        new_car = Car(WIDTH, HEIGHT, lane, random_colour, velocity)
        cars.append(new_car)


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
        quit_check()

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
                    customise(car_selection)
                if button_clicked == "Quit":
                    pygame.quit()

        # Updates the display
        pygame.display.flip()

    return


# A function to display instructions
def instructions():
    back = False

    # Defines and loads the back button
    BACK_BUTTON_INFO = [center_x(250, WIDTH), HEIGHT - 75,
                        250, 65, (150, 150, 150), "Back"]
    BACK_BUTTON = Button(*BACK_BUTTON_INFO)

    while not back:  # returns once user has pressed the back button
        quit_check()  # check if the user closes the window

        # Fills the screen with a dark grey
        SCREEN.fill(DARK_GREY)

        # Displays the instructions text on the screen
        CONTROLS_TEXT1 = DEFAULT_FONT.render("Press 'A' or >LEFT ARROW< to", True, WHITE)
        CONTROLS_TEXT2 = DEFAULT_FONT.render("change lanes to the left.", True, WHITE)
        CONTROLS_RECT1 = CONTROLS_TEXT1.get_rect(center=(WIDTH // 2, 20))
        CONTROLS_RECT2 = CONTROLS_TEXT2.get_rect(center=(WIDTH // 2, 40))
        SCREEN.blit(CONTROLS_TEXT1, CONTROLS_RECT1)
        SCREEN.blit(CONTROLS_TEXT2, CONTROLS_RECT2)
        CONTROLS_TEXT3 = DEFAULT_FONT.render("Press 'D' or >RIGHT ARROW< to",True, WHITE)
        CONTROLS_TEXT4 = DEFAULT_FONT.render("change lanes to the right.", True, WHITE)
        CONTROLS_RECT3 = CONTROLS_TEXT3.get_rect(center=(WIDTH // 2, 80))
        CONTROLS_RECT4 = CONTROLS_TEXT4.get_rect(center=(WIDTH // 2, 100))
        SCREEN.blit(CONTROLS_TEXT3, CONTROLS_RECT3)
        SCREEN.blit(CONTROLS_TEXT4, CONTROLS_RECT4)
        SCORE_TEXT1 = DEFAULT_FONT.render("Points are based off of how many", True, WHITE)
        SCORE_TEXT2 = DEFAULT_FONT.render("cars you pass before you crash.", True, WHITE)
        SCORE_RECT1 = SCORE_TEXT1.get_rect(center=(WIDTH // 2, 140))
        SCORE_RECT2 = SCORE_TEXT2.get_rect(center=(WIDTH // 2, 160))
        SCREEN.blit(SCORE_TEXT1, SCORE_RECT1)
        SCREEN.blit(SCORE_TEXT2, SCORE_RECT2)
        SCORE_TEXT3 = DEFAULT_FONT.render("The game ends when you crash into", True, WHITE)
        SCORE_TEXT4 = DEFAULT_FONT.render("another vehicle on the highway.", True, WHITE)
        SCORE_RECT3 = SCORE_TEXT3.get_rect(center=(WIDTH // 2, 200))
        SCORE_RECT4 = SCORE_TEXT4.get_rect(center=(WIDTH // 2, 220))
        SCREEN.blit(SCORE_TEXT3, SCORE_RECT3)
        SCREEN.blit(SCORE_TEXT4, SCORE_RECT4)
        SCORE_TEXT5 = DEFAULT_FONT.render("Other vehicles will travel towards", True, WHITE)
        SCORE_TEXT6 = DEFAULT_FONT.render("you and away from you.", True, WHITE)
        SCORE_RECT5 = SCORE_TEXT5.get_rect(center=(WIDTH // 2, 260))
        SCORE_RECT6 = SCORE_TEXT6.get_rect(center=(WIDTH // 2, 280))
        SCREEN.blit(SCORE_TEXT5, SCORE_RECT5)
        SCREEN.blit(SCORE_TEXT6, SCORE_RECT6)
        SCORE_TEXT7 = DEFAULT_FONT.render("The game will slowly speed up", True, WHITE)
        SCORE_TEXT8 = DEFAULT_FONT.render("as you gain a higher score.", True, WHITE)
        SCORE_RECT7 = SCORE_TEXT7.get_rect(center=(WIDTH // 2, 320))
        SCORE_RECT8 = SCORE_TEXT8.get_rect(center=(WIDTH // 2, 340))
        SCREEN.blit(SCORE_TEXT7, SCORE_RECT7)
        SCREEN.blit(SCORE_TEXT8, SCORE_RECT8)

        # Returns to the main menu if the back button is pressed
        BACK_BUTTON.draw_button(SCREEN)
        if pygame.mouse.get_pressed()[0] and BACK_BUTTON.is_clicked(
                pygame.mouse.get_pos()):
            return

        # Update display
        pygame.display.flip()


def customise(car_num):
    global user_car
    back = False

    # A list containing all the buttons needed for this function
    buttons = [
        Button(center_x(250, WIDTH), HEIGHT - 75, 250,
               65, (150, 150, 150), "Select"),
        Button(center_x(100, WIDTH + 150), 500, 100,
               65, (67, 190, 67), "--->"),
        Button(center_x(100, WIDTH - 150), 500, 100,
               65, (190, 67, 67), "<---")
    ]

    # Keep track of if a button has already been clicked this loop
    button_clicked = False
    click_counter = 0

    while not back:  # returns once user has pressed the back button
        quit_check()

        # Fills the screen with a dark grey
        SCREEN.fill(DARK_GREY)

        # Creates a delay between user inputs to prevent errors
        click_counter += 1
        if click_counter >= 300:
            button_clicked = False
            click_counter = 0

        # Draw the buttons and check for user interaction
        for button in buttons:
            button.draw_button(SCREEN)
            if (pygame.mouse.get_pressed()[0] and button.is_clicked
                (pygame.mouse.get_pos()) and not button_clicked):
                button_clicked = True
                button_text = button.text

                # Checks which button the user clicked
                if button_text == "Select":
                    return
                if button_text == "--->":
                    if car_num < 5:
                        car_num += 1
                if button_text == "<---":
                    if car_num > 0:
                        car_num -= 1

        # Assign the user car
        user_car = CARS[car_list[car_num]]

        # Format user_car to display on screen
        scaled_user_car = scale(user_car, 4.5)
        user_car_rect = scaled_user_car.get_rect(center=(WIDTH // 2,
                                                         HEIGHT // 2 - 85))
        SCREEN.blit(scaled_user_car, user_car_rect)

        # Update display
        pygame.display.flip()


# MAIN PROGRAM...
# Load Game Assets:
HIGHWAY = scale(pygame.image.load("highway.jpg"), 0.9)
HIGHWAY2 = HIGHWAY.copy()  # copies highway image for background motion
ICON = pygame.image.load("icon.png")
CARS = {  # a dictionary storing all the cars
    "blue": scale(pygame.image.load("blue-car.png"), 0.13),
    "green": scale(pygame.image.load("green-car.png"), 0.13),
    "orange": scale(pygame.image.load("orange-car.png"), 0.13),
    "purple": scale(pygame.image.load("purple-car.png"), 0.13),
    "red": scale(pygame.image.load("red-car.png"), 0.13),
    "teal": scale(pygame.image.load("teal-car.png"), 0.13),
}

# Load the keys able to be pressed
keys = pygame.key.get_pressed()

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

# Randomly set user car colour
car_list = list(CARS.keys())  # Get a list of all car colours
car_selection = random.randint(0, 5)  # Pick a random car
user_car = CARS[car_list[car_selection]]

# X/Y Values for the lanes and user car placement
LANES = [  # list containing the lane x-values
    (-85 - (user_car.get_width() // 2)),
    (-30 - (user_car.get_width() // 2)),
    (30 - (user_car.get_width() // 2)),
    (85 - (user_car.get_width() // 2))
]
USER_Y = (HEIGHT // 2) + 80

# Game frame-rate via pygame clock
FPS = 60
clock = pygame.time.Clock()

# Displays welcome screen
welcome_screen()

# Game loop variables
current_lane = random.randint(0, 3)
scroll_position = 0  # Keep track of the background scroll position
scroll_time = 0
scroll_value = 5

# List containing all assets to draw and their positions
assets = [
    (HIGHWAY, (0, 0)),
    (HIGHWAY2, (0, (-1 * HEIGHT))),
    (user_car, (WIDTH // 2 + LANES[current_lane], USER_Y))
]

# Initialise a list to store all the AI cars
cars = []

# Game Loop:
running = True
prev_keys = pygame.key.get_pressed()  # Store previous key states
while running:
    # Handle events
    quit_check()
    keys = pygame.key.get_pressed()  # Get current key states

    # Randomly generates a car
    generate_car(scroll_value)

    for car in cars:
        car.move(scroll_value)
        # Check if the car has gone off the screen (top) and remove it if so
        if car.y < -car.color.get_height():
            cars.remove(car)
        else:
            car.draw(SCREEN)

    # Check for lane change only if key is pressed down this frame
    if (keys[pygame.K_a] and not prev_keys[pygame.K_a] and current_lane > 0 or
            keys[pygame.K_LEFT] and not prev_keys[pygame.K_LEFT] and
            current_lane > 0):
        current_lane -= 1
    if (keys[pygame.K_d] and not prev_keys[pygame.K_d] and current_lane < 3 or
            keys[pygame.K_RIGHT] and not prev_keys[pygame.K_RIGHT] and
            current_lane < 3):
        current_lane += 1

    # Slowly speed up the background's motion as time goes on
    scroll_time += 1
    if scroll_time >= 500:
        scroll_value += 0.25
        scroll_time = 0
    print(scroll_time)

    # Move the background images
    scroll_position -= scroll_value
    # Check if the background needs to reset with negative scroll position
    if scroll_position < -HIGHWAY.get_height():
        scroll_position = 0

    # Update the background positions in the assets list
    assets[0] = (HIGHWAY, (0, -scroll_position))
    assets[1] = (HIGHWAY2, (0, -scroll_position - HIGHWAY.get_height()))
    assets[2] = (user_car, (WIDTH // 2 + LANES[current_lane], USER_Y))

    # Calls the draw_assets() function to draw all assets on the screen
    draw_assets(assets)
    draw_assets(cars)

    # Update previous key states for next loop
    prev_keys = keys

    # Updates the screen
    pygame.display.flip()

    # Ticks the clock at the value of the FPS
    clock.tick(FPS)

pygame.quit()
quit()
