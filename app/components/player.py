import pygame;
import os;

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # costumes/skins
        self.images = {}
        self.images["normal_right"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/players/', 'player1.png')), (100, 100)).convert_alpha()
        self.images["normal_left"] = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('./assets/players/', 'player1.png')), (100, 100)), True, False).convert_alpha()
        self.images["walk_right"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/players/', 'player_walking.png')), (100, 100)).convert_alpha()
        self.images["walk_left"] = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('./assets/players/', 'player_walking.png')), (100, 100)), True, False).convert_alpha()
        
        self.image = self.images["normal_right"]
        self.costumeTicked = False

        # position and hitbox
        self.rect = self.image.get_rect()
        self.rect.x = 0 # go to x
        self.rect.y = 0 # go to y

        # movement
        self.speed = 5
        self.velocity = [0, 0]
        self.lastDir = 1 # 1 for right and -1 for left

        self.keys = []


    def tick(self):
        self.costumeTicked = False
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP]:
            self.move(0, -1)
        if self.keys[pygame.K_DOWN]:
            self.move(0, 1)
        if self.keys[pygame.K_LEFT]:
            self.move(-1, 0)
        if self.keys[pygame.K_RIGHT]:
            self.move(1, 0)
        self.checkCostume('endTick')

    
    def checkCostume(self, type=""):
        if (not self.costumeTicked): # To update costume only once by tick
            self.costumeTicked = True
            if (self.velocity[0] > 0):
                self.image = self.images["walk_right"]
            elif (self.velocity[0] < 0):
                self.image = self.images["walk_left"]
            else:
                if (self.lastDir < 0):
                    self.image = self.images["normal_left"]
                else:
                    self.image = self.images["normal_right"]


    def move(self, x, y):
        self.velocity = [x, y]
        if (x != 0): # if player is jumping or falling, do not change the player direction
            self.lastDir = self.velocity[0]
        self.rect.x += self.velocity[0]*self.speed
        self.rect.y += self.velocity[1]*self.speed
        self.checkCostume()
        self.velocity = [0, 0] 