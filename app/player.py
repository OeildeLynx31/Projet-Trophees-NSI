import pygame;
import os;

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load(os.path.join('./assets/player/', 'player1.png')).convert())
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 0   # go to x
        self.rect.y = 0   # go to y

    def tick(self):
        print('tick du joueur!')