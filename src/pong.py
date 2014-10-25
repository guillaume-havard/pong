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

player1 = Player(windos_surface_obj.get_rect(), red_color,
                 pygame.Rect((0, 0), (20, 100)))
player1.rect.center = (30, WINDOW_HEIGHT / 2)
player2 = Player(windos_surface_obj.get_rect(), blue_color,
                 pygame.Rect((0, 0), (20, 100)))
player2.rect.center = (WINDOW_WIDTH - 30, WINDOW_HEIGHT / 2)

ball = Ball(windos_surface_obj.get_rect(), white_color,
            (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

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
            if event.key == K_UP:
                player2.move_up()
            elif event.key == K_DOWN:
                player2.move_down()
            elif event.key == K_a:
                player1.move_up()
            elif event.key == K_q:
                player1.move_down()
            elif event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
        elif event.type == KEYUP:
            if event.key in (K_UP, K_DOWN):
                player2.move_stop()
            if event.key in (K_a, K_q):
                player1.move_stop()

    player1.step()
    player2.step()
    ret_ball = ball.step()

    # ball collision test
    ball.test_collisions((player1, player2))

    if ret_ball == "left":
        print("Le joueur 1 a gagne")
        player1.score += 1
        ball = Ball(windos_surface_obj.get_rect(), white_color,
                    (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    elif ret_ball == "right":
        print("Le joueur 2 a gagne")
        player2.score += 1
        ball = Ball(windos_surface_obj.get_rect(), white_color,
                    (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))



    pygame.draw.rect(windos_surface_obj, player1.color, player1.rect)
    pygame.draw.rect(windos_surface_obj, player2.color, player2.rect)
    #print(ball.pos)
    pygame.draw.circle(windos_surface_obj, ball.color, ball.pos, ball.size)

    pygame.display.update()
    fps_clock.tick(30)
