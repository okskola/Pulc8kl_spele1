import pygame
import os
import random


class Mob( pygame.sprite.Sprite ):

    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
