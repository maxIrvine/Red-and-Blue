# points awarded based upon time
import pygame, sys
import pygame.gfxdraw
from pygame.locals import *

def moveBlue(pos):
    count = 0
    clock = pygame.time.Clock()
    for x in range (0, 100):
        clock.tick(360)
        count += 1
        pos -= count
    return pos


def play(window_size, surface, black, blue, red, white):
    radius = 40
    ball_height = window_size - (radius + 1) 
    middle = window_size / 2
    blue_x = 357
    red_x = 443

    # main loop of game
    while True:
        surface.fill(white)
        pygame.draw.line(surface, black, (middle, 0), (middle, window_size), 5)
        pygame.gfxdraw.filled_circle(surface, blue_x, ball_height, radius, blue)
        pygame.gfxdraw.filled_circle(surface, red_x, ball_height, radius, red)
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == KEYDOWN:
                if (event.key == K_LEFT):
                    moveBlue(blue_x)
                elif (event.key == K_RIGHT):
                    red_x += 10
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
    

    play(window_size, surface, black, blue, red, white)


main()