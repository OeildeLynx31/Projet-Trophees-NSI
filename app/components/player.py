import pygame;
import os;

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = {}
        self.images["normal_right"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/players/', 'player1.png')).convert(), (100, 100))
        self.images["normal_left"] = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('./assets/players/', 'player1.png')).convert(), (100, 100)), True, False)
        self.images["walk_right"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/players/', 'player_walking.png')).convert(), (100, 100))
        self.images["walk_left"] = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('./assets/players/', 'player_walking.png')).convert(), (100, 100)), True, False)
        self.image = self.images["normal_right"]

        self.rect = self.image.get_rect()
        self.rect.x = 0   # go to x
        self.rect.y = 0   # go to y

        self.speed = 5
        self.velocity = [0, 0]
        self.lastDir = [0, 0]

        self.keys = []


    def tick(self):
        self.moving = False
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP]:
            self.move(0, -1)
        if self.keys[pygame.K_DOWN]:
            self.move(0, 1)
        if self.keys[pygame.K_LEFT]:
            self.move(-1, 0)
        if self.keys[pygame.K_RIGHT]:
            self.move(1, 0)
        self.checkCostume()

    
    def checkCostume(self):
        if (self.velocity[0] > 0):
            self.image = self.images["walk_right"]
        elif (self.velocity[0] < 0):
            self.image = self.images["walk_left"]
        else:
            self.image = self.images["normal_right"]

        self.velocity = [0, 0] 
        
    def move(self, x, y):
        self.velocity = [x, y]
        self.lastDir = [x, y]
        self.rect.x += self.velocity[0]*self.speed
        self.rect.y += self.velocity[1]*self.speed
        print(self.velocity)