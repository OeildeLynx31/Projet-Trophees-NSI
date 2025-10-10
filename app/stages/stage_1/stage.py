import pygame;
import os;
from ...components.player import Player

class Stage():
    def __init__(self, game):
        self.game = game
        self.group = pygame.sprite.Group()

        self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', 'background1.png')), (1280, 720))
        self.backgroundColor = "WHITE"


        self.player = Player()
        self.player.add(self.group)



    def tick(self):
        #L'arrière-plan futur
        self.game.blit(self.backdrop, (0, 0))
        self.group.draw(self.game)
        pygame.display.flip()

        for sprite in self.group.sprites():
            sprite.tick() #run the tick method for each sprite in the stage

        self.game.fill(self.backgroundColor)
