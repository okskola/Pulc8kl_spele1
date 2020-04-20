import pygame
import os
import random
from explosion import Explosion


class Bullet( pygame.sprite.Sprite ):

    shoot_sound = None

    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(os.path.join(self.game.get_folder_img(),"bullet.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speedx = random.randint(5,15)
        if Bullet.shoot_sound is None:
            Bullet.shoot_sound = pygame.mixer.Sound(os.path.join(self.game.get_folder_sound(), "Laser_Shoot.wav"))
        Bullet.shoot_sound.play()

    def update(self):
        self.rect.x += self.speedx
        # destroy bullet if out of screen
        if self.rect.x > self.game.get_wdt()-10:
            expl = Explosion( self.game, self.rect.center, self.speedx )
            self.game.add_sprite(expl)

            self.kill()
