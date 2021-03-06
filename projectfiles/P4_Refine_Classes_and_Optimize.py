'''
    Added the Class object - Movement is in one direction only.
'''
import pygame
from pygame.locals import *
from sys import exit
import os
# --------------------------------------------------------
CURRENT_DIR = os.getcwd()
BACKGROUND_IMAGE_FILENAME =  os.path.join(CURRENT_DIR,"resources/background.png")
CAR_FILENAME = os.path.join(CURRENT_DIR,"resources/car3.png")
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
blue  = (0, 0, 128)
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('SF Mono', 30)
# --------------------------------------------------------
class car(object):
    def __init__(self,x,time_passed,speed,time_passed_seconds_cumulative,offset):
        self.x = x
        self.time_passed = time_passed
        self.speed = speed
        self.time_passed_seconds_cumulative = time_passed_seconds_cumulative
        self.offset = offset

    def draw(self):
        car = pygame.image.load(CAR_FILENAME)
        screen.blit(car, (self.x+self.offset, 568))
        self.textsurface = myfont.render(f"Time {int(self.time_passed_seconds_cumulative)} sec.", True, green, blue)
        self.distance_traveled_label = myfont.render(f"Distance {int(self.x)} m.", True, green, blue)
        screen.blit(self.textsurface,(self.x+self.offset,500))
        screen.blit(self.distance_traveled_label,(self.x+self.offset,530))

    def move(self):
        self.time_passed_seconds = self.time_passed / 1000.0
        self.distance_moved = self.time_passed_seconds * self.speed
        self.x += self.distance_moved
        self.time_passed_seconds_cumulative += self.time_passed_seconds
        # If the image goes off the end of the screen, move it back
        if self.x > (1800-self.offset):
            self.x -= (1800-self.offset)
            self.time_passed_seconds_cumulative = 0.00
        return self.x,self.time_passed_seconds_cumulative


#pygame.init()
screen = pygame.display.set_mode((1800,800), 0, 32)
background = pygame.image.load(BACKGROUND_IMAGE_FILENAME).convert()

def Engine():
    # --------------------------------------------------------
    # Our clock object
    clock = pygame.time.Clock()
    x1 = 0.
    x2 = 0.
    x3 = 0.
    # Speed in pixels per second
    speed = 100.  # pixel/second (1 second)
    # --------------------------------------------------------
    time_passed_seconds_cumulative = t1 = t2 = t3 = 0.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.blit(background, (0,0))
        time_passed = clock.tick(60)  # This is a timer ,In a 1000 millesecond / 60 (max frame) = no. of frames in millsecond.
        car1 = car(x1,time_passed,40,t1,0)
        car2 = car(x2, time_passed,35,t2,-300)
        car3 = car(x3,time_passed,33,t3,-500)
        car1.draw()
        car2.draw()
        car3.draw()
        x1,t1 = car1.move()
        x2,t2 = car2.move()
        x3,t3 = car3.move()
        pygame.display.update()

        os.system('cls' if os.name =='nt' else 'clear')
        print(f"Distance traveled by car1 {car1.x:.4}")
        print(f"time travel by car1 {car1.time_passed_seconds_cumulative:.4}")

# --------------------------------------------------------
if __name__ == "__main__":
    Engine()

