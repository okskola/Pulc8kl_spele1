import pygame
import os
import random
import math


class Tower( pygame.sprite.Sprite ):

    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(os.path.join(self.game.get_folder_img(),"tower.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.range = 50#velāk jānomaina skaitlis
        self.reloadTime = 100# vēlāk jānomaina skaitlis

    def findDistance(mob):
            (x,y) = mob.rect.center
            xd = self.rectx - x
            yd = self.recty - y
            distance = math.sqrt(xd*xd + yd*yd)
            return distance

    def reload():
        if self.reloadTime == 0:
            return True
        else:
            self.reloadTime -= 1
            
    def shoot():
        if reload() == True:
            for mob in mobs:
                if findDistance(mob) <= self.range:
                    self.reloadTime = 100
                    b = Bullet()# jaieliek parametri lodem
                    all_sprites.add(b)
                    bullets.add(b)
                    break
