# points awarded based upon time
import pygame, sys, time
from pygame.locals import *

def keyboard_input(self):
    key = pygame.key.get_pressed()
    dist = 1
    if key[pygame.K_LEFT]:
        self.rect.move(-1, 0)
    if key[pygame.K_RIGHT]:
        self.rect.move(1, 0)
    if key[pygame.K_UP]:
        self.rect.move(0, -1)
    if key[pygame.K_DOWN]:
        self.rect.move(0, 1)

# main loop of game
def play(window_size, surface, black, blue, red):
    #contains main loop
    radius = 40
    ball_height = window_size - (radius + 1) 
    middle = window_size / 2

    print ball_height
    pygame.draw.line(surface, black, (middle, 0), (middle, window_size), 5)
    pygame.draw.circle(surface, blue, (358, ball_height), radius, 0)
    pygame.draw.circle(surface, red, (443, ball_height), radius, 0)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
    
def main():
    # set up pygame
    pygame.init()

    # set up window
    window_size = 800
    surface = pygame.display.set_mode((window_size, window_size))
    pygame.display.set_caption('Red and Blue') 

    # set up the colors
    # balls red and blue
    # platform gray
    # deadly triangles black
    black = (0, 0, 0)
    gray  = (77, 77, 77)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    surface.fill(white)

    play(window_size, surface, black, blue, red)


main()