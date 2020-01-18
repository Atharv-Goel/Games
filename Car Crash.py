import pygame
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)

colors = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE]

class Car(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the car,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the car, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Instance variables that control the edges of where the car bounces
        self.left_boundary = 0

        # Instance variables for the current speed and direction
        self.change_x = 0
        self.change_y = 0

    def update(self):

        global score
        
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.left <= self.left_boundary:
            self.rect.x = 740
            self.rect.y = random.randrange(screen_height)
            self.change_x = random.randrange(-8, -3)
            score += 2


class Player(Car):
    """ The player class derives from car, but overrides the 'update'
    functionality with new a movement function that will move the car
    with the mouse. """
    def update(self):
        # Get the current mouse position
        pos = pygame.mouse.get_pos()

        # Fetch the x and y out of the list
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Car Crash | Made by Atharv")
 
# Sprite list for non-player cars
car_list = pygame.sprite.Group()

# Sprite List for all sprites
all_sprites_list = pygame.sprite.Group()

for i in range(75):
    # This represents a car
    car = Car(random.choice(colors), 40, 15)

    # Set a random location for the car
    car.rect.x = 740
    car.rect.y = random.randrange(screen_height)

    car.change_x = random.randrange(-8, -3)
    car.change_y = 0
    car.left_boundary = 0

    # Add the car to the list of objects
    car_list.add(car)
    all_sprites_list.add(car)

# Create a black player car
player = Player(BLACK, 20, 15)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False
# Keep time going until game over
cont = True

# Text setup for game over
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Game Over!!!", True, BLACK)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

health = 100
score = 0

# -------- Main Program Loop -----------
a = time.time()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill(WHITE)

    # Calls update() method on every sprite in the list
    
    all_sprites_list.update()

    # See if the player car has collided with anything
    cars_hit_list = pygame.sprite.spritecollide(player, car_list, True)

    # Check the list of collisions
    for car in cars_hit_list:
        if cont:
            health -= 5

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Find scor and health 
    if cont:
        scoreText = font.render("Score: " + str(score), True, BLACK)
        healthText = font.render("Health: " + str(health), True, BLACK)

    # Draw the score and health onto the screen
    screen.blit(scoreText, (680 - scoreText.get_width(), 20))
    screen.blit(healthText, (680 - healthText.get_width(), 60))

    # Check to see if health is below zero
    if health <= 0:
        screen.blit(text, (350 - text.get_width() // 2, 200 - text.get_height() // 2))
        cont = False
        healthText = font.render("Health: 0", True, BLACK)

    # Limit to 60 frames per second
    clock.tick(60)

    # Update Screen
    pygame.display.flip()


pygame.quit()
