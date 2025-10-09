import pygame;
from ..player import Player

class Stage():
    def __init__(self, game):
        self.game = game
        self.group = pygame.sprite.Group()

        self.player = Player()
        self.player.add(self.group)

    def tick(self):
        #L'arrière-plan futur
        #world.blit(backdrop, backdropbox)
        self.group.draw(self.game)
        pygame.display.flip()

        for sprite in self.group.sprites():
            sprite.tick() #run the tick method for each sprite in the stage
