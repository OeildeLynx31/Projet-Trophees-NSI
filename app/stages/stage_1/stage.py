import pygame;
import os;
from ...components.player import Player
from ...utils.CollisionRect import get_sprite_collision_rects

class Stage():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.group = pygame.sprite.Group()

        self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', 'background1.png')), (1280, 720)).convert_alpha()
        self.backgroundColor = "WHITE"
        self.backdropRects = get_sprite_collision_rects(self.backdrop)

        self.player = Player(self.game)
        self.player.add(self.group)

        self.debugShowHitboxes = True


    def tick(self, game):
        #L'arrière-plan futur
        self.screen.blit(self.backdrop, (0, 0))
        self.group.draw(self.screen)
        

        for sprite in self.group.sprites():
            sprite.tick(game) #run the tick method for each sprite in the stage

        self.debug()
        pygame.display.flip()

        self.screen.fill(self.backgroundColor)

    def debug(self):
        for sprite in self.group.sprites():
            if (self.debugShowHitboxes):
                pygame.draw.rect(self.screen, "RED", sprite.rect, 2)
        if (self.debugShowHitboxes):
            for rect in self.backdropRects:
                pygame.draw.rect(self.screen, "RED", rect, 2)
