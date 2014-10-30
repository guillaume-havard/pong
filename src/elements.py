#! /usr/bin/python3

import random
import pygame


class Player:
    """
    Class representing a player
        score
        color
        position and size
    """

    def __init__(self, level, color, rect):
        """
        level pygame.Rect [in] : reference to the level Rect
        color pygame.Color [in] : color of the player
        rect pygame.Rect [in] : pos and size of the paddle
        """
        self.level = level
        self.color = color
        self.rect = rect
        self.score = 0

        self.speed = 10
        self.moving = 0

    def move_up(self):
        """
        Set an upward mouvement
        """
        self.moving = -1

    def move_down(self):
        """
        Set an upward mouvement
        """
        self.moving = 1

    def move_stop(self):
        """
        Stop movements
        """
        self.moving = 0

    def step(self):
        """
        Step in the player state
        """
        self.rect.bottom += self.moving * self.speed

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > self.level.bottom:
            self.rect.bottom = self.level.bottom

    def render(self, screen):
        """
        Blit the player on the screen

        :param screen: pygame.Surface you want the player on
        :param self
        :return:
        """
        pygame.draw.rect(screen, self.color, self.rect)


class Ball:
    """
    pos
    size
    speed
    direction
    """
    # TODO: deduce the position from the screen by default.
    def __init__(self, level, color, pos):
        """
        level pygame.Rect [in] : reference to the level Rect
        color pygame.Color [in] : color of the player
        pos set of 2 int [in] : position of the ball
        radius [in] :
        speed [in] :
        direction rad/deg ? [in] :
        """
        self.level = level
        self.color = color
        self.pos = [int(x) for x in pos]
        self.radius = 5
        self.speed_x = 5 + random.randint(0, 5)
        self.speed_x *= random.choice((-1, 1))
        self.speed_y = 0 + random.randint(0, 5)
        self.speed_y *= random.choice((-1, 1))

        print("Nouvelle Balle")
        print(self.pos)
        print(self.speed_x, self.speed_y)

    def step(self, player_left, player_right):
        """
        one ball step
        test if collision with players
        Act accordingly
        return a non empty string if the ball fall on one side

        /!\ Make the ball bounce when its circumference touch the paddle or border
        """
        new_x = self.pos[0] + self.speed_x
        new_y = self.pos[1] + self.speed_y

        # Collisions with the walls
        if new_x - self.radius < 0:
            return "left"
        elif new_x + self.radius > self.level.width:
            return "right"

        if not 0 <= new_y <= self.level.height:
            self.speed_y = -self.speed_y

        # Collisions with the players
        rect_coll = pygame.Rect((0, 0), (self.radius * 2, self.radius * 2))
        rect_coll.center = (new_x, new_y)

        if rect_coll.colliderect(player_left) and self.speed_x != abs(self.speed_x):
            self.speed_x = abs(self.speed_x)
            return ""
        if rect_coll.colliderect(player_right) and self.speed_x == abs(self.speed_x):
            self.speed_x = -abs(self.speed_x)
            return ""

        self.pos[0] = new_x
        self.pos[1] = new_y

        return ""

    def render(self, screen):
        """
        Blit the ball on the screen

        :param screen: pygame.Surface you want the ball on
        :param self
        :return:
        """
        pygame.draw.circle(screen, self.color, self.pos, self.radius)