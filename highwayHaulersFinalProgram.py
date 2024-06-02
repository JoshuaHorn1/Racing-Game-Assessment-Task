"""Highway Haulers Racing Game - Final Program
"""

# IMPORTS...
import pygame
import random

# INITIALISATIONS...
pygame.init()
pygame.display.init()


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


def move(velocity, y_pos):
    y_pos = y_pos + velocity
    return y_pos


def draw(lane, y_pos, car_type):
    SCREEN.blit(car_type, (lane, y_pos))


class Car:
    def __init__(self, velocity, lane, y_pos, car_type):
        self.velocity = velocity
        self.lane = lane
        self.y_pos = y_pos
        self.car_type = car_type
        # New attribute to track if the car has been scored
        self.scored = False


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


# A function to randomly generate an AI car
def generate_car(spawn):
    # Random chance for car to be generated
    # Increment counter and attempt to spawn if a car
    global car_spawned_recently
    car_spawned_recently += 1

    # Incrementally changes the spawn delay timer
    if score > 100:
        spawn_delay = 20
    elif score > 50:
        spawn_delay = 35
    else:
        spawn_delay = 50

    if car_spawned_recently >= spawn_delay:
        create_car = random.randint(0, spawn)
        if create_car <= 5:  # assign created car random values
            direction_chance = random.randint(0, 10)
            if direction_chance <= 3:
                velocity_choice = (random.randint(1, 2))
                if velocity_choice == 1:
                    velocity = -3.5
                else:
                    velocity = -4.5
                y_pos = HEIGHT + 100
                car_type = CARS[car_list[random.randint(0, 5)]]
            else:
                velocity = scroll_value
                y_pos = -100
                car_type = pygame.transform.rotate(CARS[car_list[
                    random.randint(0, 5)]], 180)

            lane = random.choice(LANES)

            # Create car object and append to list
            new_car = Car(velocity, lane, y_pos, car_type)
            cars.append(new_car)

            car_spawned_recently = 0  # reset counter


# A function to display the welcome screen
def welcome_screen(high):
    started = False

    button_width = 250
    button_x = center_x(button_width, WIDTH)

    # Buttons to display
    buttons = [
        Button(button_x, 175, button_width, 65,
               LIGHT_GREY, "Start Game"),
        Button(button_x, 275, button_width, 65,
               LIGHT_GREY, "Instructions"),
        Button(button_x, 375, button_width, 65,
               LIGHT_GREY, "Customise"),
        Button(button_x, 475, button_width, 65,
               LIGHT_GREY, "Quit"),
    ]

    while not started:
        # Checks if the user ever closes the window
        quit_check()

        # Fill the screen with grey
        SCREEN.fill(DARK_GREY)

        # Display a title
        title_text1 = TITLE_FONT.render("Highway", True,
                                        VIBRANT_PURPLE)
        title_text2 = TITLE_FONT.render("Haulers", True,
                                        VIBRANT_PURPLE)
        title_rect1 = title_text1.get_rect(center=(WIDTH // 2, HEIGHT // 9))
        title_rect2 = title_text2.get_rect(center=(WIDTH // 2,
                                                   HEIGHT // 9 + 38))
        SCREEN.blit(title_text1, title_rect1)
        SCREEN.blit(title_text2, title_rect2)

        # Display the highscore
        highscore_text = HIGHSCORE_FONT.render(f"Highscore: {high}",
                                               True, WHITE)
        highscore_rect = highscore_text.get_rect(center=(WIDTH // 2, 600))
        SCREEN.blit(highscore_text, highscore_rect)

        # Draw and handle clicks for buttons
        for button in buttons:
            button.draw_button(SCREEN)
            if pygame.mouse.get_pressed()[0] and button.is_clicked(
                    pygame.mouse.get_pos()):
                button_clicked = button.text

                # Checks which button the user clicked
                if button_clicked == "Start Game":
                    started = True
                if button_clicked == "Instructions":
                    instructions()
                if button_clicked == "Customise":
                    customise()
                if button_clicked == "Quit":
                    pygame.quit()
                    quit()

        # Updates the display
        pygame.display.update()

    return


# A function to display instructions
def instructions():
    back = False

    # Define and load the back button
    back_button_info = [center_x(250, WIDTH), HEIGHT - 75,
                        250, 65, (150, 150, 150), "Back"]
    back_button = Button(*back_button_info)

    while not back:  # returns once user has pressed the back button
        quit_check()  # check if the user closes the window

        # Fills the screen with a dark grey
        SCREEN.fill(DARK_GREY)

        # Display instructions text on the screen
        controls_text1 = DEFAULT_FONT.render("Press 'A' or >LEFT ARROW< "
                                             "to", True, WHITE)
        controls_text2 = DEFAULT_FONT.render("change lanes to the left.",
                                             True, WHITE)
        controls_rect1 = controls_text1.get_rect(center=(WIDTH // 2, 20))
        controls_rect2 = controls_text2.get_rect(center=(WIDTH // 2, 40))
        SCREEN.blit(controls_text1, controls_rect1)
        SCREEN.blit(controls_text2, controls_rect2)
        controls_text3 = DEFAULT_FONT.render("Press 'D' or >RIGHT ARROW"
                                             "< to", True, WHITE)
        controls_text4 = DEFAULT_FONT.render("change lanes to the "
                                             "right.", True, WHITE)
        controls_rect3 = controls_text3.get_rect(center=(WIDTH // 2, 80))
        controls_rect4 = controls_text4.get_rect(center=(WIDTH // 2, 100))
        SCREEN.blit(controls_text3, controls_rect3)
        SCREEN.blit(controls_text4, controls_rect4)
        score_text1 = DEFAULT_FONT.render("Points are based off of how "
                                          "many", True, WHITE)
        score_text2 = DEFAULT_FONT.render("cars you pass before you "
                                          "crash.", True, WHITE)
        score_rect1 = score_text1.get_rect(center=(WIDTH // 2, 140))
        score_rect2 = score_text2.get_rect(center=(WIDTH // 2, 160))
        SCREEN.blit(score_text1, score_rect1)
        SCREEN.blit(score_text2, score_rect2)
        score_text3 = DEFAULT_FONT.render("The game ends when you crash "
                                          "into", True, WHITE)
        score_text4 = DEFAULT_FONT.render("another vehicle on the "
                                          "highway.", True, WHITE)
        score_rect3 = score_text3.get_rect(center=(WIDTH // 2, 200))
        score_rect4 = score_text4.get_rect(center=(WIDTH // 2, 220))
        SCREEN.blit(score_text3, score_rect3)
        SCREEN.blit(score_text4, score_rect4)
        score_text5 = DEFAULT_FONT.render("Other vehicles will travel "
                                          "towards", True, WHITE)
        score_text6 = DEFAULT_FONT.render("you and away from you (up "
                                          "and down).", True, WHITE)
        score_rect5 = score_text5.get_rect(center=(WIDTH // 2, 260))
        score_rect6 = score_text6.get_rect(center=(WIDTH // 2, 280))
        SCREEN.blit(score_text5, score_rect5)
        SCREEN.blit(score_text6, score_rect6)
        score_text7 = DEFAULT_FONT.render("The game will slowly speed "
                                          "up",True, WHITE)
        score_text8 = DEFAULT_FONT.render("as you gain a higher score.",
                                          True, WHITE)
        score_rect7 = score_text7.get_rect(center=(WIDTH // 2, 320))
        score_rect8 = score_text8.get_rect(center=(WIDTH // 2, 340))
        SCREEN.blit(score_text7, score_rect7)
        SCREEN.blit(score_text8, score_rect8)
        misc_text1 = DEFAULT_FONT.render("Use the customise button on "
                                         "the main", True, WHITE)
        misc_text2 = DEFAULT_FONT.render("menu to change your car "
                                         "colour.", True, WHITE)
        misc_rect1 = misc_text1.get_rect(center=(WIDTH // 2, 380))
        misc_rect2 = misc_text2.get_rect(center=(WIDTH // 2, 400))
        SCREEN.blit(misc_text1, misc_rect1)
        SCREEN.blit(misc_text2, misc_rect2)
        misc_text3 = DEFAULT_FONT.render("Whenever any cars collide or "
                                         "crash", True, WHITE)
        misc_text4 = DEFAULT_FONT.render("on the highway, they will "
                                         "explode!", True, WHITE)
        misc_rect3 = misc_text3.get_rect(center=(WIDTH // 2, 440))
        misc_rect4 = misc_text4.get_rect(center=(WIDTH // 2, 460))
        SCREEN.blit(misc_text3, misc_rect3)
        SCREEN.blit(misc_text4, misc_rect4)
        misc_text5 = DEFAULT_FONT.render("Good luck,",
                                         True, WHITE)
        misc_text6 = DEFAULT_FONT.render("drive safe,",
                                         True, WHITE)
        misc_text7 = DEFAULT_FONT.render("have fun!",
                                         True, WHITE)
        misc_rect5 = misc_text5.get_rect(center=(WIDTH // 2, 500))
        misc_rect6 = misc_text6.get_rect(center=(WIDTH // 2, 520))
        misc_rect7 = misc_text7.get_rect(center=(WIDTH // 2, 540))
        SCREEN.blit(misc_text5, misc_rect5)
        SCREEN.blit(misc_text6, misc_rect6)
        SCREEN.blit(misc_text7, misc_rect7)

        # Returns to the main menu if the back button is pressed
        back_button.draw_button(SCREEN)
        if pygame.mouse.get_pressed()[0] and back_button.is_clicked(
                pygame.mouse.get_pos()):
            return

        # Update display
        pygame.display.flip()


# A function to allow the user to select their car type
def customise():
    global user_car
    back = False

    select_arrow = pygame.image.load("selectarrow.png")
    select_arrow = pygame.transform.rotate(select_arrow, 270)
    select_arrow = scale(select_arrow, 0.13)

    # Get the index of current user_car
    car_num = car_list.index([key for key, value in CARS.items() if
                              value == user_car][0])

    # Buttons needed for this function
    buttons = [
        Button(center_x(250, WIDTH), HEIGHT - 75, 250,
               65, (150, 150, 150), "Select"),
        Button(center_x(100, WIDTH + 325), 200, 100,
               65, (46, 137, 255), ">>>>>"),
        Button(center_x(100, WIDTH - 325), 200, 100,
               65, (255, 137, 46), "<<<<<")
    ]

    spread_value = WIDTH // 9
    y_value = 460

    display_coordinates = {
        "blue": (spread_value * 2),
        "green": (spread_value * 3),
        "orange": (spread_value * 4),
        "purple": (spread_value * 5),
        "red": (spread_value * 6),
        "teal": (spread_value * 7),
    }

    # Track if a button has been clicked this loop
    button_clicked = False

    while not back:  # returns once back button is pressed
        quit_check()

        # Fill the screen with dark grey

        SCREEN.fill(DARK_GREY)

        for display_car in car_list:
            car_colour = CARS[display_car]
            coordinate = display_coordinates[display_car]
            car_rect = car_colour.get_rect(center=(coordinate, y_value))
            SCREEN.blit(car_colour, car_rect)

        # Draw the buttons and check for user interaction
        for button in buttons:
            button.draw_button(SCREEN)
            if (pygame.mouse.get_pressed()[0] and button.is_clicked(
                    pygame.mouse.get_pos()) and not button_clicked):
                button_clicked = True
                button_text = button.text

                # Checks which button the user clicked
                if button_text == "Select":
                    return
                if button_text == ">>>>>":
                    if car_num < 5:
                        car_num += 1
                if button_text == "<<<<<":
                    if car_num > 0:
                        car_num -= 1

        if not pygame.mouse.get_pressed()[0]:
            button_clicked = False

        # Display arrow sprite below the selected car
        arrow_rect = select_arrow.get_rect(center=(
            display_coordinates[car_list[car_num]], y_value + 75))
        SCREEN.blit(select_arrow, arrow_rect)

        # Assign the user car
        user_car = CARS[car_list[car_num]]

        # Format user_car for display on screen
        scaled_user_car = scale(user_car, 4.5)
        user_car_rect = scaled_user_car.get_rect(center=(WIDTH // 2 - 5,
                                                         HEIGHT // 3.2))
        SCREEN.blit(scaled_user_car, user_car_rect)

        # Update display
        pygame.display.flip()


# A function to check for collisions between the user car and AI cars
def user_ai_collision(user, user_lane, ai_cars):
    user_mask = pygame.mask.from_surface(user)  # Create user car mask

    # Checks if the user mask collides with any AI cars
    for ai in ai_cars:
        # Create AI car mask
        car_mask = pygame.mask.from_surface(ai.car_type)
        offset = (ai.lane - user_lane, ai.y_pos - USER_Y)

        # Check for overlapping masks; return True if collision detected
        if user_mask.overlap(car_mask, offset):
            explosion_rect = EXPLOSION.get_rect(center=(user_lane + 20,
                                                        USER_Y + 40))
            SCREEN.blit(EXPLOSION, explosion_rect)

            return True

    # If no collisions detected, return false
    return False


# A function to check for collisions between multiple AI cars
def ai_ai_collision(ai_cars, background_velocity):
    for i, car1 in enumerate(ai_cars):
        car1_mask = pygame.mask.from_surface(car1.car_type)
        for j, car2 in enumerate(ai_cars):
            if i != j:
                car2_mask = pygame.mask.from_surface(car2.car_type)
                offset = (car2.lane - car1.lane, car2.y_pos - car1.y_pos)

                # Check for overlapping masks
                if car1_mask.overlap(car2_mask, offset):
                    # Set velocities of both cars to scroll_value
                    car1.velocity = background_velocity
                    car2.velocity = background_velocity

                    average_y = ((car1.y_pos + car2.y_pos) // 2) + 30
                    explosion_rect = EXPLOSION.get_rect(center=(
                        car1.lane + 20, average_y))
                    SCREEN.blit(EXPLOSION, explosion_rect)


# A function to check if the user passes an AI car
def passed_car(ai_cars, user_y):
    global score
    for ai in ai_cars:
        if not ai.scored:  # Score only if the car hasn't been scored yet
            if (ai.velocity > 0 and ai.y_pos > user_y >=
                    ai.y_pos - ai.velocity):
                score += 1
                ai.scored = True  # Mark the car as scored
            elif (ai.velocity < 0 and ai.y_pos < user_y <=
                  ai.y_pos - ai.velocity):
                score += 1
                ai.scored = True  # Mark the car as scored


# A function to display the user's score
def display_score():
    score_text = SCORE_FONT.render(f" Score: {score} ",
                                   True, BLACK, LIGHT_GREY)
    SCREEN.blit(score_text, (5, 5))


# A function to display the user's speed in km/h
def display_speed(background):
    speed = (background * 5)
    if speed < 100:
        formatted_speed = "{:.1f}".format(speed)
    else:
        formatted_speed = "{:.0f}".format(speed)
    speed_text1 = SCORE_FONT.render(f"{formatted_speed:}     ",
                                    True, BLACK, LIGHT_GREY)
    speed_text2 = SCORE_FONT.render("km/h",
                                    True, BLACK, LIGHT_GREY)
    SCREEN.blit(speed_text1, (376, 5))
    SCREEN.blit(speed_text2, (413, 5))


# A function to save the user's highscore
def save_highscore(user, high):
    # Update high score if the current score is higher
    if user > high:
        high = user
        # Save high score to file
        with open("highscore.txt", "w") as file_type:
            file_type.write(str(high))


# A function to display a game over screen
def game_over_screen(user_score):
    button_width = 250

    while True:
        # Still draw AI cars
        for ai_car in cars:
            draw(ai_car.lane, ai_car.y_pos, ai_car.car_type)

        # Display game over message
        game_over_text1 = GAME_OVER_FONT.render("Game", True,
                                                VIBRANT_RED)
        game_over_text2 = GAME_OVER_FONT.render("Over", True,
                                                VIBRANT_RED)
        game_over_rect1 = game_over_text1.get_rect(center=(WIDTH // 2,
                                                           HEIGHT // 6))
        game_over_rect2 = game_over_text2.get_rect(center=(WIDTH // 2,
                                                           HEIGHT // 6 + 76))
        SCREEN.blit(game_over_text1, game_over_rect1)
        SCREEN.blit(game_over_text2, game_over_rect2)

        # Display final score
        final_score_text = GAME_OVER_SCORE_FONT.render(f"Your Score: "
                                                       f"{user_score}",
                                                       True, BLACK)
        final_score_rect = final_score_text.get_rect(center=(WIDTH // 2,
                                                             HEIGHT // 2
                                                             - 20))
        SCREEN.blit(final_score_text, final_score_rect)

        if user_score > high_score:
            new_highscore = GAME_OVER_SCORE_FONT.render(f"NEW "
                                                        f"HIGHSCORE!",
                                                        True, BLACK)
            new_highscore_rect = new_highscore.get_rect(center=(WIDTH // 2,
                                                                HEIGHT // 2
                                                                + 40))
            SCREEN.blit(new_highscore, new_highscore_rect)

        # Display play again and quit buttons
        main_menu_button = Button(center_x(button_width, WIDTH),
                                  450, button_width, 65,
                                  LIGHT_GREY, "Main Menu")
        quit_button = Button(center_x(button_width, WIDTH),
                             550, button_width, 65,
                             LIGHT_GREY, "Quit")

        main_menu_button.draw_button(SCREEN)
        quit_button.draw_button(SCREEN)

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.is_clicked(pygame.mouse.get_pos()):
                    mouse_up = False
                    while not mouse_up:
                        for secondary_event in pygame.event.get():
                            if secondary_event.type == pygame.MOUSEBUTTONUP:
                                return True
                elif quit_button.is_clicked(pygame.mouse.get_pos()):
                    pygame.quit()
                    quit()

        pygame.display.flip()  # Update the display


# MAIN PROGRAM...
# Load Game Assets:
HIGHWAY = scale(pygame.image.load("highway.jpg"), 0.9)
HIGHWAY2 = HIGHWAY.copy()  # copies highway image for background motion
ICON = pygame.image.load("icon.png")
EXPLOSION = scale(pygame.image.load("explosion.png"), 0.15)
CARS = {  # a dictionary storing all the cars
    "blue": scale(pygame.image.load("blue-car.png"), 0.13),
    "green": scale(pygame.image.load("green-car.png"), 0.13),
    "orange": scale(pygame.image.load("orange-car.png"), 0.13),
    "purple": scale(pygame.image.load("purple-car.png"), 0.13),
    "red": scale(pygame.image.load("red-car.png"), 0.13),
    "teal": scale(pygame.image.load("teal-car.png"), 0.13),
}

# Load highscore from text file
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    # Create the file if it doesn't exist
    with open("highscore.txt", "w") as file:
        file.write("0")

# Create a variable to store the user score
score = 0

# Load the keys able to be pressed
keys = pygame.key.get_pressed()

# Set Colour Tuples:
DARK_GREY = (60, 60, 60)
LIGHT_GREY = (150, 150, 150)
VIBRANT_PURPLE = (188, 0, 255)
VIBRANT_RED = (173, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set Fonts:
DEFAULT_FONT = pygame.font.SysFont("couriernew", 20)
TITLE_FONT = pygame.font.SysFont("goudystout", 40)
SCORE_FONT = pygame.font.SysFont("bahnschrift", 20)
HIGHSCORE_FONT = pygame.font.SysFont("castellar", 40)
GAME_OVER_SCORE_FONT = pygame.font.SysFont("britannic", 55)
GAME_OVER_FONT = pygame.font.SysFont("goudystout", 80)

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
LANES = [  # list containing the lane x-values for the User and AI cars
    (WIDTH // 2 + (-85 - (user_car.get_width() // 2))),
    (WIDTH // 2 + (-30 - (user_car.get_width() // 2))),
    (WIDTH // 2 + (30 - (user_car.get_width() // 2))),
    (WIDTH // 2 + (85 - (user_car.get_width() // 2)))
]
USER_Y = (HEIGHT // 2) + 50

# Game frame-rate via pygame clock
FPS = 60
clock = pygame.time.Clock()

# Displays welcome screen
welcome_screen(high_score)

# Game loop variables
current_lane = random.randint(0, 3)
scroll_position = 0  # Keep track of the background scroll position
scroll_time = 0
scroll_value = 5

# List containing all assets to draw and their positions
assets = [
    (HIGHWAY, (0, 0)),
    (HIGHWAY2, (0, (-1 * HEIGHT))),
    (user_car, (LANES[current_lane], USER_Y))
]

# A list containing all the cars
cars = []

# A variable containing whether a car spawned recently.
car_spawned_recently = 0

# A variable containing the chance for an AI car to spawn
AI_spawn_value = 300

# Game Loop:
running = True
prev_keys = pygame.key.get_pressed()  # Store previous key states
while running:
    # Handle events
    quit_check()
    keys = pygame.key.get_pressed()  # Get current key states

    # Check for lane change only if key is pressed down this frame
    if (keys[pygame.K_a] and not prev_keys[pygame.K_a] and current_lane > 0
            or keys[pygame.K_LEFT] and not prev_keys[pygame.K_LEFT] and
            current_lane > 0):
        current_lane -= 1
    if (keys[pygame.K_d] and not prev_keys[pygame.K_d] and current_lane < 3
            or keys[pygame.K_RIGHT] and not prev_keys[pygame.K_RIGHT] and
            current_lane < 3):
        current_lane += 1

    # Slowly speed up the background's motion as time goes on
    scroll_time += 1
    if scroll_time >= 250:
        scroll_value += 0.20
        # Increase random AI car spawn chance as background scrolls faster
        if AI_spawn_value > 100:
            AI_spawn_value -= 10
        scroll_time = 0

    # Move the background images
    scroll_position -= scroll_value
    # Check if the background needs to reset with negative scroll position
    if scroll_position < -HIGHWAY.get_height():
        scroll_position = 0

    # Update the background positions in the assets list
    assets[0] = (HIGHWAY, (0, -scroll_position))
    assets[1] = (HIGHWAY2, (0, -scroll_position - HIGHWAY.get_height()))
    assets[2] = (user_car, (LANES[current_lane], USER_Y))

    # Calls the draw_assets() function to draw all assets on the screen
    draw_assets(assets)

    # Chance to generate AI car
    generate_car(AI_spawn_value)

    # Draws all AI cars
    for car in cars:
        new_y = move(car.velocity, car.y_pos)
        car.y_pos = new_y

        if car.y_pos > HEIGHT + 150 or car.y_pos < -150:
            cars.remove(car)
        else:
            draw(car.lane, car.y_pos, car.car_type)

        # Check for collision between two AI cars
        ai_ai_collision(cars, scroll_value)

        # Check for collision between user and AI
        if user_ai_collision(user_car, LANES[current_lane], cars):
            # Handle collision if detected
            running = False

            # Saves highscore as a precaution
            save_highscore(score, high_score)

            # Display game over screen
            if game_over_screen(score):

                # Update highscore for new game
                if score > high_score:
                    high_score = score

                # Call welcome screen function
                welcome_screen(high_score)

                running = True  # Restart the game loop
                # Reset game values
                cars.clear()
                car_spawned_recently = 0
                current_lane = random.randint(0, 3)
                scroll_position = 0
                scroll_time = 0
                scroll_value = 5
                score = 0

    # Checks if the user has passed any cars
    passed_car(cars, USER_Y)

    # Displays the user's score
    display_score()

    # Displays the user's speed
    display_speed(scroll_value)

    # Saves highscore if it is greater than the user score
    save_highscore(score, high_score)

    # Update previous key states for next loop
    prev_keys = keys

    # Updates the screen
    pygame.display.flip()

    # Ticks the clock at the value of the FPS
    clock.tick(FPS)

pygame.quit()
quit()
