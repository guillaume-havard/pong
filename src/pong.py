#! /usr/bin/python3



"""
1 game
    level
    ball (multi ?)
    2 players (or more ? 4)
    
    For the moment, basic version
"""

import pygame, sys
from pygame.locals import *
from elements import *

pygame.init()
fps_clock = pygame.time.Clock()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
windos_surface_obj = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("pong")

red_color = pygame.Color(255, 0, 0)
green_color = pygame.Color(0, 255, 0)
blue_color = pygame.Color(0, 0, 255)
white_color = pygame.Color(255, 255, 255)
black_color = pygame.Color(0, 0, 0)

player1 = Player(red_color, pygame.Rect((0, 0), (20, 100)))
player1.rect.center = (30, WINDOW_HEIGHT/2)
player2 = Player(blue_color, pygame.Rect((0, 0), (20, 100)))
player2.rect.center = (WINDOW_WIDTH-30, WINDOW_HEIGHT/2)

while True:
    
    windos_surface_obj.fill(black_color)
    
    # pygame.event.get() returns a list off all Event objects that happened
    # since the last time get() was called.
    # The Event object has type, pos, key and other attributes depending on
    # type of event it is.
    for event in pygame.event.get():
        if event.type == QUIT:
            # quit() is the opposite of init()
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            pass
        elif event.type == MOUSEBUTTONUP:
            pass
                            
        elif event.type == KEYDOWN:
            if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                msg = ("Arrow key pressed")
            if event.key == K_a:
                msg = "'a' key pressed"
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    
    pygame.draw.rect(windos_surface_obj, red_color, player1.rect)
    pygame.draw.rect(windos_surface_obj, red_color, player2.rect)
    
    
    pygame.display.update()   
    fps_clock.tick(30)
