import pygame
import os

class Explosion( pygame.sprite.Sprite ):
    sounds = []
    images = []

    def __init__(self, game, center, speedx):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        if not Explosion.sounds:
             for snd in ["Hit_Hurt1.wav", "Hit_Hurt2.wav"]:
                 Explosion.sounds.append( pygame.mixer.Sound(os.path.join(self.game.get_folder_sound(), snd)) )

        if not Explosion.images:
            for i in range(10):
                Explosion.images.append( pygame.image.load(os.path.join(self.game.get_folder_img(),"explode{}.png".format(i))).convert_alpha() )
        self.lastupdate = pygame.time.get_ticks()
        self.frame = 0
        self.image = Explosion.images[self.frame]
        self.rect = self.image.get_rect()
        self.center = center
        self.rect.center = center
        self.speedx = speedx

    def update(self):
        self.rect.x -= self.speedx
        if pygame.time.get_ticks()-self.lastupdate > 50:
            self.lastupdate = pygame.time.get_ticks()
            self.frame += 1
            if self.frame == len( Explosion.images ):
                self.kill()
            else:
                self.image = Explosion.images[self.frame]
