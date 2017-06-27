# points awarded based upon time
import pygame, sys, time
import pygame.gfxdraw
from pygame.locals import *

# main loop of game
def play(window_size, surface, black, blue, red):
    #contains main loop
    radius = 40
    ball_height = window_size - (radius + 1) 
    middle = window_size / 2

    print ball_height
    pygame.draw.line(surface, black, (middle, 0), (middle, window_size), 5)
    pygame.gfxdraw.filled_circle(surface, 357, ball_height, radius, blue)
    pygame.gfxdraw.filled_circle(surface, 443, ball_height, radius, red)

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
    # platform light_blue
    # deadly triangles black
    black = (12, 18, 12)
    light_blue  = (168, 218, 220)
    white = (241, 250, 238)
    red = (230, 57, 70)
    blue = (35, 87, 137)
    surface.fill(white)

    play(window_size, surface, black, blue, red)


main()