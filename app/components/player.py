import pygame;
import os;
from ..utils.CollisionRect import get_enlarged_hitbox
from ..utils.StageMovement import getRelativePos

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.isLiving = True

        # costumes/skins
        self.images = {}
        self.images["normal_right"] = pygame.image.load(os.path.join('./assets/players/', 'player1.png'))
        self.images["normal_left"] = pygame.transform.flip(pygame.image.load(os.path.join('./assets/players/', 'player1.png')), True, False)
        self.images["walk_right1"] = pygame.image.load(os.path.join('./assets/players/', 'player1-f1.png'))
        self.images["walk_right2"] = pygame.image.load(os.path.join('./assets/players/', 'player1-f2.png'))
        self.images["walk_left1"] = pygame.transform.flip(pygame.image.load(os.path.join('./assets/players/', 'player1-f1.png')), True, False)
        self.images["walk_left2"] = pygame.transform.flip(pygame.image.load(os.path.join("./assets/players/", "player1-f2.png")), True, False)

        self.heart = []
        self.heart.append(pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/life_bar/', 'empty_heart.png')), (64, 64)).convert_alpha())
        self.heart.append(pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/life_bar/', 'half_heart.png')), (64, 64)).convert_alpha())
        self.heart.append(pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/life_bar/', 'heart.png')), (64, 64)).convert_alpha())
        
        for image in self.images:
            self.images[image] = pygame.transform.scale(self.images[image], (28 * 2, 52 * 2)).convert_alpha()

        self.image = self.images["normal_right"]
        self.costumeTicked = False
        self.walkingTick = 0
        self.walkingSpeed = 10

        # position and hitbox
        self.rect = self.image.get_rect()
        self.rect.x = 100 # go to x
        self.rect.y = 300 # go to y
        self.hitbox = self.rect.copy()
        self.hitbox.width = 50
        self.hitbox.height = 100

        # movement
        self.speed = 5
        self.jumpHeight = 4
        self.gravity = 0.2
        self.jumping = False
        self.velocity = [0, 0]
        self.lastDir = 1 # 1 for right and -1 for left

        self.keys = []

        # game changers
        self.boosts = [] #jumpStick pour rester collé au plafond
        self.health = 17


    def tick(self, game):
        self.game = game
        self.stage = game.currentStage
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
                self.walkingTick = self.walkingTick + 1
                if (self.walkingTick <= self.walkingSpeed):
                    self.image = self.images["walk_right1"]
                elif (self.walkingTick <= self.walkingSpeed * 2):
                    self.image = self.images["walk_right2"]
                else:
                    self.image = self.images["normal_right"]
                    if (self.walkingTick > self.walkingSpeed * 2):
                        self.walkingTick = 0

            elif (self.velocity[0] < 0):
                self.walkingTick = self.walkingTick + 1
                if (self.walkingTick <= self.walkingSpeed):
                    self.image = self.images["walk_left1"]
                elif (self.walkingTick <= self.walkingSpeed * 2):
                    self.image = self.images["normal_left"]
                else:
                    self.image = self.images["normal_left"]
                    if (self.walkingTick > self.walkingSpeed * 2):
                        self.walkingTick = 0
            else:
                self.walkingTick = 0
                if (self.lastDir < 0):
                    self.image = self.images["normal_left"]
                else:
                    self.image = self.images["normal_right"]


    def move(self, x, y):
        self.velocity[0] = x
        if x != 0:
            self.lastDir = x
            if get_enlarged_hitbox(self.hitbox, x * self.speed, 0).collideobjects(self.stage.backdropRects) == None:
                if ((self.rect.x > (self.game.screen.get_width()-self.stage.scrollSpace) and x > 0) or (self.rect.x < self.stage.scrollSpace and x < 0)):
                    stageMovement = self.stage.move(-x * self.speed, 0)
                    if (stageMovement[0] == 0):
                        self.rect.x += x * self.speed
                else:
                    self.rect.x += x * self.speed
        if get_enlarged_hitbox(self.hitbox, 0, y * self.speed).collideobjects(self.stage.backdropRects) == None:
            self.rect.y += y * self.speed
        else:
            if y > 0 and "jumpStick" not in self.boosts:
                self.jumping = False
            self.velocity[1] = 0
        
        self.calcHitbox()
        self.checkCostume()

    def goto(self, x, y, rel=True):
        pos = [x, y]
        if (rel):
            pos = getRelativePos(self.stage, x, y)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def checkGravity(self):
        self.velocity[1] += self.gravity
        self.move(0, self.velocity[1])
        if (self.rect.y > 1000): # if falling in the "void"
            self.respawn()

    def jump(self, force=3):
        if not self.jumping:
            self.velocity[1] = -force
            self.jumping = True

    def calcHitbox(self):
        self.hitbox.x = self.rect.x + (self.rect.width - self.hitbox.width)/2 # centrage horizontal à partir des deux largeurs
        self.hitbox.y = self.rect.y + (self.rect.height - self.hitbox.height) # basage de la hitbox à partir du bas

    def respawn(self):
        self.stage.goto(0, 0)
        self.goto(100, 300)
        self.health = 20