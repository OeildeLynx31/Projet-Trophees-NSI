import pygame;
import os;
from ...components.player import Player
from ...utils.CollisionRect import *

class Stage():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.group = pygame.sprite.Group()

        self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', 'background1.png')), (1280, 720)).convert_alpha()
        self.backgroundColor = "WHITE"
        self.backdropRects = get_collision_rects_for_background('./assets/backgrounds/', 'background1.png')

        self.player = Player(self.game)
        self.player.add(self.group)

        self.debugShowHitboxes = True

        self.scroll = [0, 0]


    def tick(self, game):
        #L'arrière-plan futur
        self.screen.blit(self.backdrop, (self.scroll[0], self.scroll[1]))
        self.group.draw(self.screen)
        

        for sprite in self.group.sprites():
            sprite.tick(game) #run the tick method for each sprite in the stage

        self.debug()
        pygame.display.flip()

        self.screen.fill(self.backgroundColor)

    def debug(self):
        for sprite in self.group.sprites():
            if (self.debugShowHitboxes):
                if (hasattr(sprite, 'hitbox')):
                    pygame.draw.rect(self.screen, "RED", sprite.hitbox, 2)
                else:
                    pygame.draw.rect(self.screen, "RED", sprite.rect, 2)
        if (self.debugShowHitboxes):
            for rect in self.backdropRects:
                pygame.draw.rect(self.screen, "RED", rect, 2)

    def move(self, x, y):
        self.scroll[0] += x
        self.scroll[1] += y
        for rect in self.backdropRects:
            rect.x += x
            rect.y += y