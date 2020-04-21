import pygame
import os
import random


class Tower( pygame.sprite.Sprite ):

    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(os.path.join(self.game.get_folder_img(),"tower.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
