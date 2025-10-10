import pygame;
import os;

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        self.images.append(pygame.image.load(os.path.join('./assets/players/', 'player1.png')).convert())
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.x = 0   # go to x
        self.rect.y = 0   # go to y

        self.speed = 5

        self.keys = []

    def tick(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP]:
            self.move(0, -1)
        if self.keys[pygame.K_DOWN]:
            self.move(0, 1)
        if self.keys[pygame.K_LEFT]:
            self.move(-1, 0)
        if self.keys[pygame.K_RIGHT]:
            self.move(1, 0)

    def move(self, x, y):
        self.rect.x += x*self.speed
        self.rect.y += y*self.speed