########## Credits
# Sprites idea by KidsCanCode on Youtube
# https://www.youtube.com/watch?v=VO8rTszcW4s&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw

# Music Guinea Pig Hero by Trevor Lentz
# https://opengameart.org/content/guinea-pig-hero
# Art by Kenney, www.kenney.nl
# https://opengameart.org/content/platformer-art-xeno-diversity
# Explosion https://opengameart.org/content/bubble-explosion

# Programmed by Ojars

import pygame


from game import *

_WDT = 700
_HGT = 400
_FPS = 30

pygame.init()
pygame.mixer.init() #required to play sounds
screen = pygame.display.set_mode((_WDT,_HGT))
clock = pygame.time.Clock()

game = Game(screen, _WDT, _HGT)

# Game loop
running = True
while running:
    # keep right speed
    clock.tick(_FPS)
    # process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and (event.mod & pygame.KMOD_ALT):
                running = False
            else:# event.key == pygame.K_SPACE:
                game.keydown(event.key)

    #update
    game.update()

    # draw/render
    screen.fill(GRAY)
    game.draw()

    # after drawing everything, flip display
    pygame.display.flip()

pygame.quit()


##    # mob hits player
##    hits = pygame.sprite.spritecollide(player, mobs, False)
##    if hits:
##        running = False
##
##    #bullet hits mob
##    hits = pygame.sprite.groupcollide( mobs, bullets, True, True )
##    for hit in hits:
##        score += hit.speedx
##        random.choice(expl_sounds).play()
##        expl = Explosion( hit.rect.center, hit.speedx )
##        all_sprites.add(expl)
##        m = Mob()
##        all_sprites.add(m)
##        mobs.add(m)
##
