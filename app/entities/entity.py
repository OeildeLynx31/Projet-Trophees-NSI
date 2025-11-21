import pygame;
import os;
import time
from ..utils.CollisionRect import get_enlarged_hitbox
from ..utils.CollisionRect import nearVoid
from ..utils.CollisionRect import mustJump
from ..utils.StageMovement import getRelativePos
from ..utils.Entity import getProperties

class Entity(pygame.sprite.Sprite):
    def __init__(self, stage, game, entityType, posX, posY):
        pygame.sprite.Sprite.__init__(self)

        self.properties = getProperties(entityType)

        self.game = game
        self.stage = stage
        self.isLivingEntity = self.properties["living"]
        self.dead = False
        self.Player = False
        self.entityType = entityType
        self.entityName = self.properties["name"]


        # costumes/skins
        self.images = {}
        self.images["normal_right"] = pygame.image.load(os.path.join('./assets/entities/', self.entityType+'.png'))
        self.images["normal_left"] = pygame.transform.flip(pygame.image.load(os.path.join('./assets/entities/', self.entityType+'.png')), True, False)
        self.images["walk_right1"] = pygame.image.load(os.path.join('./assets/entities/', self.entityType+'-walk.png'))
        self.images["walk_right2"] = pygame.image.load(os.path.join('./assets/entities/', self.entityType+'-walk2.png'))
        self.images["walk_left1"] = pygame.transform.flip(pygame.image.load(os.path.join('./assets/entities/', self.entityType+'-walk.png')), True, False)
        self.images["walk_left2"] = pygame.transform.flip(pygame.image.load(os.path.join("./assets/entities/", self.entityType+'-walk2.png')), True, False)
        
        for image in self.images:
            self.images[image] = pygame.transform.scale(self.images[image], (self.properties["textW"] * self.properties["growFactor"], self.properties["textH"] * self.properties["growFactor"])).convert_alpha()

        self.image = self.images["normal_right"]
        self.costumeTicked = False
        self.walkingTick = 0
        self.walkingSpeed = self.properties["walkingSpeed"]

        # position and hitbox
        self.rect = self.image.get_rect()
        pos = getRelativePos(self.stage, posX, posY)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.hitbox = self.rect.copy()
        self.hitbox.width = self.properties["hitboxW"] * self.properties["growFactor"]
        self.hitbox.height = self.properties["hitboxH"] * self.properties["growFactor"]

        # movement
        self.speed = self.properties["walkingSpeed"]
        self.jumpHeight = self.properties["jumpHeight"]
        self.gravity = 0.2
        self.velocity = [0, 0]
        self.lastDir = 1 # 1 for right and -1 for left
        self.jumping = False
        self.isFalling = False

        self.keys = []

        # game changers
        self.health = self.properties["health"]
        self.damageCooldown = pygame.time.get_ticks()
        self.lifeWaveAnimationStep = 0
        self.effects = []

    def tick(self, game):
        self.game = game
        self.stage = game.currentStage
        self.costumeTicked = False
        if (self.isLivingEntity):
            self.runAI()
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
                    self.rect.x += x * self.speed
        if get_enlarged_hitbox(self.hitbox, 0, y * self.speed).collideobjects(self.stage.backdropRects) == None:
            self.rect.y += y * self.speed
            self.isFalling = True
        else:
            if y > 0:
                self.jumping = False
                self.isFalling = False
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
        if (self.rect.y > 1000): # if falling into the "void"
            self.damage(3)

    def runAI(self):
        distFromPlayer = self.rect.x-self.stage.player.rect.x
        dir = 1 if distFromPlayer < 0 else -1
        if abs(distFromPlayer) < self.properties["detectionDistance"] and abs(distFromPlayer) > 20 and (not nearVoid(self, dir) or self.properties["fallInVoid"]): # absolute value
            self.move(dir, 0)
            if mustJump(self, dir) and self.properties["canJump"]:
                print(self.jumping, self.isFalling)
                self.jump(self.properties["jumpHeight"])

    def jump(self, force=3):
        if (not self.jumping):
            self.velocity[1] = -force
            self.jumping = True

    def calcHitbox(self):
        self.hitbox.x = self.rect.x + (self.rect.width - self.hitbox.width)/2 # centrage horizontal à partir des deux largeurs
        self.hitbox.y = self.rect.y + (self.rect.height - self.hitbox.height) # basage de la hitbox à partir du bas

    def damage(self, damage, source = None):
        if (pygame.time.get_ticks() - self.damageCooldown > 120): # to prevent player from spam-damages killing it directly
            self.health -= damage
            self.damaged = True
            self.damageCooldown = pygame.time.get_ticks()
            if self.health < 1:
                self.kill(source)

    def heal(self, damage, source = None):
        self.health += damage
        if (self.health > 20):
            self.health = 20

    def kill(self, source = None):
        self.dead = True
        print(self.entityName, "was killed by", str(source))