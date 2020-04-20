import pygame
import os
import sys
import random

from scene import Scene
from bullet import Bullet

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
GREEN = (0, 0, 255)


class Game:
    def __init__(self, screen, wdt, hgt):
        """ Main game class.
            Parameters: screen
        """
        self.screen = screen
        self.wdt = wdt
        self.hgt = hgt
        # set up assets folders
        self.folder_game = os.path.dirname(__file__)
        self.folder_img = os.path.join(self.folder_game, "img")
        self.folder_sound = os.path.join(self.folder_game, "sound")
        #pygame.mixer.music.load(os.path.join(folder_sound, "Guinea Pig Hero.ogg"))
        #pygame.mixer.music.play(loops=-1)

        self.score = 0

#player = Player()
#all_sprites.add(player)
#mobs = pygame.sprite.Group()
#for i in range(8):
#    m = Mob()
#    all_sprites.add(m)
#    mobs.add(m)
#bullets = pygame.sprite.Group()

        #Sprites
        self.all_sprites = pygame.sprite.Group()

        # make first scene
        self.scene = Scene(self, 0, 0)
        self.all_sprites.add( self.scene )

    def get_folder_game(self):
        return self.folder_game

    def get_folder_img(self):
        return self.folder_img

    def get_folder_sound(self):
        return self.folder_sound

    def get_wdt(self):
        return self.wdt

    def get_hgt(self):
        return self.hgt

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.all_sprites.draw(self.screen)
        self.drawtext( self.screen, "Score="+str(self.score), 18, self.get_wdt()//2, 10 )

    def add_sprite(self, sprite):
        self.all_sprites.add(sprite)

    def keydown( self, key ):
        if key == pygame.K_SPACE:
            bullet = Bullet( self, 0, random.randint(10,self.get_hgt()-10) )
            self.all_sprites.add( bullet )

    def drawtext(self, surf, text, size, x, y):
        fontname = pygame.font.match_font('arial') # varētu pārcelt uz klases mainīgo, lai nav katru reizi jātaisa no jauna
        font= pygame.font.Font(fontname, size)
        textsurface = font.render(text, True, WHITE)
        textrect = textsurface.get_rect()
        textrect.midtop = (x,y)
        surf.blit(textsurface, textrect)

    def stop():
        pass
