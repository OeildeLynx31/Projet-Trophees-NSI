import pygame;
import os;
from ..utils.CollisionRect import get_enlarged_hitbox

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        # costumes/skins
        self.images = {}
        self.images["normal_right"] = pygame.image.load(os.path.join('./assets/players/', 'player1.png')).convert_alpha()
        self.images["normal_left"] = pygame.transform.flip(pygame.image.load(os.path.join('./assets/players/', 'player1.png')), True, False).convert_alpha()
        self.images["walk_right1"] = pygame.image.load(os.path.join('./assets/players/', 'player1-mv1.png')).convert_alpha()
        self.images["walk_right2"] = pygame.image.load(os.path.join('./assets/players/', 'player1-mv2.png')).convert_alpha()
        self.images["walk_left1"] = pygame.transform.flip(pygame.image.load(os.path.join('./assets/players/', 'player1-mv1.png')), True, False).convert_alpha()
        self.images["walk_left2"] = pygame.transform.flip(pygame.image.load(os.path.join("./assets/players/", "player1-mv2.png")), True, False).convert_alpha()
        
        self.image = self.images["normal_right"]
        self.costumeTicked = False

        # position and hitbox
        self.rect = self.image.get_rect()
        self.rect.x = 100 # go to x
        self.rect.y = 300 # go to y
        self.hitbox = self.rect.copy()
        self.hitbox.width = 56
        self.hitbox.height = 100

        # movement
        self.speed = 5
        self.jumpHeight = 4
        self.gravity = 0.2
        self.jumping = False
        self.velocity = [0, 0]
        self.lastDir = 1 # 1 for right and -1 for left

        self.keys = []


    def tick(self, game):
        self.game = game
        self.costumeTicked = False
        self.keys = pygame.key.get_pressed()
        if not self.jumping and self.keys[pygame.K_SPACE] or self.keys[pygame.K_UP]:
            self.jump(self.jumpHeight)
        if self.keys[pygame.K_LEFT]:
            self.move(-1, 0)
        if self.keys[pygame.K_RIGHT]:
            self.move(1, 0)
        self.checkGravity()
        self.checkCostume('endTick')

    
    def checkCostume(self, type=""):
        if (not self.costumeTicked): # To update costume only once by tick
            self.costumeTicked = True
            if (self.velocity[0] > 0):
                self.image = self.images["walk_right1"]
                self.image = self.images["walk_right2"]
            elif (self.velocity[0] < 0):
                self.image = self.images["walk_left1"]
                self.image = self.images["walk_left2"]
            else:
                if (self.lastDir < 0):
                    self.image = self.images["normal_left"]
                else:
                    self.image = self.images["normal_right"]


    def move(self, x, y):
        self.velocity[0] = x
        if x != 0:
            self.lastDir = x
            if get_enlarged_hitbox(self.hitbox, x * self.speed, 0).collideobjects(self.game.currentStage.backdropRects) == None:
                self.rect.x += x * self.speed
        
        if get_enlarged_hitbox(self.hitbox, 0, y * self.speed).collideobjects(self.game.currentStage.backdropRects) == None:
            self.rect.y += y * self.speed
        else:
            self.velocity[1] = 0
            self.jumping = False
        
        self.calcHitbox()
        self.checkCostume()

    def checkGravity(self):
        self.velocity[1] += self.gravity
        self.move(0, self.velocity[1])

    def jump(self, force=3):
        if not self.jumping:
            self.velocity[1] = -force
            self.jumping = True

    def calcHitbox(self):
        self.hitbox.x = self.rect.x + (self.rect.width - self.hitbox.width)/2 # centrage horizontal à partir des deux largeurs
        self.hitbox.y = self.rect.y + (self.rect.height - self.hitbox.height) # basage de la hitbox à partir du bas
