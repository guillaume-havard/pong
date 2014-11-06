#! /usr/bin/python3
__author__ = 'Guillaume Havard'

import pygame

def print_text(surface, text, text_pos, text_color=pygame.Color(255, 255, 255)):
    """
    Print a text on a surface

    :param surface: Surface to blit the text on
    :param text: texte to print
    :param text_pos: tuple of the top left position
    :param text_color: color of the text
    """
    font_obj = pygame.font.Font("freesansbold.ttf", 32)
    msg_surface_obj = font_obj.render(text, False, text_color)
    msg_rect_obj = msg_surface_obj.get_rect()
    msg_rect_obj.topleft = text_pos
    surface.blit(msg_surface_obj, msg_rect_obj)