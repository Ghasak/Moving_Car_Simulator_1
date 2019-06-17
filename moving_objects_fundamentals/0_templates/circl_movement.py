# website: codeblockgetter.wordpress.com

from pygame.locals import *
import pygame, sys

pygame.init() # Initializing the pygame module

FPS = 60
clock = pygame.time.Clock()

# RGB
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)

rect1_x = 290
rect1_y = 190
rect1_size_x = 20
rect1_size_y = 20

rect1_x_change = 0
rect1_y_change = 0

rect2_x = 500
rect2_y = 150
rect2_size_x = 100
rect2_size_y = 100

window = pygame.display.set_mode((600, 400))
window.fill(WHITE)

color = WHITE

rect1 = pygame.draw.rect(window, BLUE, [rect1_x, rect1_y, rect1_size_x, rect1_size_y])
rect2 = pygame.draw.rect(window, color, [rect2_x, rect2_y, rect2_size_x, rect2_size_y])

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT: # QUIT
            pygame.quit
            sys.exit()

    window.fill(WHITE)

    if rect1_x+20 == rect2_x:
        color = GREEN
        rect1_x_change = 0
    else:
        rect1_x_change = 5

    rect1_x += rect1_x_change

    rect1 = pygame.draw.rect(window, BLUE, [rect1_x, rect1_y, rect1_size_x, rect1_size_y])
    rect2 = pygame.draw.rect(window, color, [rect2_x, rect2_y, rect2_size_x, rect2_size_y])

    clock.tick(FPS) # changes the frames per 60 sec
    pygame.display.flip() # updates the display
