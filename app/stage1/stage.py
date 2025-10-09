import pygame;
from ..player import Player

class Stage():
    def __init__(self, game):
        self.group = pygame.sprite.Group()
        self.player = Player()
        self.player.add(self.group)
        self.game = game

    def tick(self):
        #L'arrière-plan futur
        #world.blit(backdrop, backdropbox)
        self.group.draw(self.game)
        pygame.display.flip()
