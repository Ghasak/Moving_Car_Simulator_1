'''
    We will try to understand the motion of objects

'''
import pygame
from pygame.locals import *
from sys import exit
import os
# --------------------------------------------------------
CURRENT_DIR = os.getcwd()
BACKGROUND_IMAGE_FILENAME =  os.path.join(CURRENT_DIR,"resources/background.png")
CAR_FILENAME = os.path.join(CURRENT_DIR,"resources/car2.png")

# print(os.listdir())
# --------------------------------------------------------
import pygame
from pygame.locals import *
from sys import exit

# --------------------------------------------------------
# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('SF Mono', 30)

# --------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((1800,800), 0, 32)
background = pygame.image.load(BACKGROUND_IMAGE_FILENAME).convert()
car = pygame.image.load(CAR_FILENAME)
# Our clock object
clock = pygame.time.Clock()
x1 = 0.
x2 = 0.
# Speed in pixels per second
speed = 36.  # pixel/second (1 second)
frame_no = 0
# --------------------------------------------------------
time_passed_seconds_cumulative = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))
    screen.blit(car, (x1, 500))
    textsurface = myfont.render(f"Time {int(time_passed_seconds_cumulative)}", True, green, blue)
    screen.blit(textsurface,(x1+50,500))

    #screen.blit(car, (x2, 560))
    time_passed = clock.tick(120)  # This is a timer
    time_passed_seconds = time_passed / 1000.0
    distance_moved = time_passed_seconds * speed
    x1 += distance_moved
    if (frame_no % 5) == 0:
        distance_moved = time_passed_seconds * speed
        x2 += distance_moved * 5.
    # If the image goes off the end of the screen, move it back
    if x1 > 1800:
        x1 -= 1800
        time_passed_seconds_cumulative = 0
    if x2 > 640:
        x2 -= 1800
    pygame.display.update()
    frame_no += 1
    time_passed_seconds_cumulative = time_passed_seconds_cumulative+ time_passed_seconds
    print(f"Time spent since lanching =  {int(time_passed_seconds_cumulative)}")
    print(f"while the delta time in millisecond = {time_passed *1000}")
    os.system('cls' if os.name == 'nt' else 'clear')





