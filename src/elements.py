#! /usr/bin/python3


class Player:
    """
    Class representing a player
        score
        color
        position and size
    """
    
    def __init__(self, color, rect):
        """
        color [in] : color of the player
        rect pygame.Rect [in] : pos and size of the paddle
        """
        self.color = color
        self.rect = rect
        self.score = 0
        
    
