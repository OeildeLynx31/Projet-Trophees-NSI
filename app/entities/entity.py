import pygame;
import os;
import time
from ..utils.CollisionRect import getEnlargedHitbox
from ..utils.CollisionRect import nearVoid
from ..utils.CollisionRect import mustJump
from ..utils.CollisionRect import horizontalDistance
from ..utils.CollisionRect import getCollisionRectsWithoutSelf
from ..utils.StageMovement import getRelativePos
from ..utils.Entity import getProperties
from ..utils.ImgFilter import damageFilter
from ..utils.Damage import Damage

class Entity(pygame.sprite.Sprite):
    def __init__(self, stage, game, entityType, posX, posY):
        pygame.sprite.Sprite.__init__(self)

        self.properties = getProperties(entityType)

        self.game = game
        self.stage = stage
        self.isLivingEntity = self.properties["living"]
        self.isDestructible = self.properties['destructible'] if 'destructible' in self.properties else False
        self.Player = False
        self.entityType = entityType
        self.entityName = self.properties["name"]

        # costumes/skins
        self.images = {}
        for skin in self.properties["skins"]:
            self.images[skin[0]] = pygame.transform.flip(pygame.image.load(os.path.join('./assets/entities/', skin[1]+'.png')), skin[2], False)

        damageImages = {}
        for image in self.images:
            if (self.isLivingEntity):
                damageImages[image+"_damaged"] = pygame.transform.scale(damageFilter(self.images[image]), (self.properties["textW"] * self.properties["growFactor"], self.properties["textH"] * self.properties["growFactor"])).convert_alpha()
            self.images[image] = pygame.transform.scale(self.images[image], (self.properties["textW"] * self.properties["growFactor"], self.properties["textH"] * self.properties["growFactor"])).convert_alpha()
        
        self.images = self.images | damageImages

        self.image = self.images["normal_right"]
        self.costumeTicked = False

        # position and hitbox
        self.rect = self.image.get_rect()
        pos = getRelativePos(self.stage, posX, posY)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.hitbox = self.rect.copy()
        self.hitbox.width = self.properties["hitboxW"] * self.properties["growFactor"]
        self.hitbox.height = self.properties["hitboxH"] * self.properties["growFactor"]
        self.physical = self.properties["physical"]
        self.renderLayer = self.properties["renderLayer"] if "renderLayer" in self.properties else -1

        # movement
        self.velocity = [0, 0]
        self.gravity = 0.2
        self.lastDir = 1 # 1 for right and -1 for left
        self.health = 1
        self.growFactor = self.properties["growFactor"]
        self.dead = False
        if self.isLivingEntity:
            self.health = self.properties["health"]
            self.speed = self.properties["walkingSpeed"]
            self.jumpHeight = self.properties["jumpHeight"]
            self.jumping = False
            self.isFalling = False
            self.walkingTick = 0
            self.walkingSpeed = self.properties["walkingSpeed"]
            self.damaged = False
            if self.isDestructible:
                print('An alive entity shouldn\' be destructible!')

        if self.isDestructible:
            self.health = self.properties["health"]
            self.damaged = False

        self.keys = []

        # game changers
        self.damageCooldown = pygame.time.get_ticks()
        self.lastAttackTime = time.time()
        self.attackSpeed = 1.0 # 1 second cooldown
        self.lifeWaveAnimationStep = 0
        self.effects = []

    def tick(self, game):
        self.game = game
        self.stage = game.currentStage
        self.costumeTicked = False
        if (self.isLivingEntity):
            self.runAI()
            self.checkGravity()
        if (self.isLivingEntity or self.isDestructible):
            self.checkDamage()
        self.calcHitbox()
        self.checkCostume('endTick')
    
    def checkCostume(self, type=""):
        damaged = "_damaged" if self.isLivingEntity and self.damaged else ""
        if (not self.costumeTicked): # To update costume only once by tick
            self.costumeTicked = True
            if (self.velocity[0] > 0):
                self.walkingTick = self.walkingTick + 1
                if (self.walkingTick <= self.walkingSpeed * 4):
                    self.image = self.images["normal_right"+damaged]
                elif (self.walkingTick <= self.walkingSpeed * 8):
                    self.image = self.images["walk_right1"+damaged]
                elif (self.walkingTick <= self.walkingSpeed * 12):
                    self.image = self.images["walk_right2"+damaged]
                else:
                    if (self.walkingTick > self.walkingSpeed * 12):
                        self.walkingTick = 0

            elif (self.velocity[0] < 0):
                self.walkingTick = self.walkingTick + 1
                if (self.walkingTick <= self.walkingSpeed * 4):
                    self.image = self.images["walk_left1"+damaged]
                elif (self.walkingTick <= self.walkingSpeed * 8):
                    self.image = self.images["normal_left"+damaged]
                elif (self.walkingTick <= self.walkingSpeed * 12):
                    self.image = self.images["walk_left2"+damaged]
                else:
                    self.image = self.images["normal_left"+damaged]
                    if (self.walkingTick > self.walkingSpeed * 12):
                        self.walkingTick = 0
            else:
                self.walkingTick = 0
                if (self.lastDir < 0):
                    self.image = self.images["normal_left"+damaged]
                else:
                    self.image = self.images["normal_right"+damaged]


    def move(self, x, y):
        self.velocity[0] = x
        if x != 0:
            self.lastDir = x
            if getEnlargedHitbox(self.hitbox, x * self.speed, 0).collideobjects(getCollisionRectsWithoutSelf(self)) == None:
                    self.rect.x += x * self.speed
        if getEnlargedHitbox(self.hitbox, 0, y * self.speed).collideobjects(getCollisionRectsWithoutSelf(self)) == None:
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
        distFromPlayer = horizontalDistance(self, self.stage.player)
        dir = 1 if distFromPlayer < 0 else -1
        if abs(distFromPlayer) < self.properties["maxPlayerDistance"] and abs(distFromPlayer) > self.properties["attackRange"] and (not nearVoid(self, dir) or self.properties["fallInVoid"]): # absolute value
            self.move(dir, 0)
            if mustJump(self, dir) and self.properties["canJump"]:
                self.jump(self.properties["jumpHeight"])
        elif abs(distFromPlayer) <= self.properties["attackRange"] and self.properties.get("attackDamage", 0) > 0: # Check if attackDamage is defined and > 0
            self.attack()
        if self.properties.get("touchKill", False) and self.hitbox.collideobjects([self.stage.player.hitbox]):
            self.stage.player.kill()

    def checkDamage(self):
        for damage in self.stage.damages:
            if damage.rect.collideobjects([self.hitbox]) and not self in damage.damagedEntities and self != damage.origin:
                self.damage(damage.damage, damage.origin)
                damage.damagedEntities.append(self)
        if pygame.time.get_ticks() - self.damageCooldown > 120:
            self.damaged = False

    def jump(self, force=3):
        if (not self.jumping):
            self.velocity[1] = -force
            self.jumping = True

    def calcHitbox(self):
        self.hitbox.x = self.rect.x + (self.rect.width - self.hitbox.width)/2 # centrage horizontal à partir des deux largeurs
        self.hitbox.y = self.rect.y + (self.rect.height - self.hitbox.height) # basage de la hitbox à partir du bas

    def damage(self, damage, source = None):
        if (pygame.time.get_ticks() - self.damageCooldown > 50): # to prevent player from spam-damages killing it directly
            if not self.properties["immortal"]:
                self.health -= damage
                self.damaged = True
                self.damageCooldown = pygame.time.get_ticks()
                if self.health < 1:
                    self.kill(source)

    def attack(self):
        if (time.time() - self.lastAttackTime > self.attackSpeed):
            self.lastAttackTime = time.time()
            hw = self.properties["hitboxW"] * self.growFactor
            hh = self.properties["hitboxH"] * self.growFactor
            reach = self.properties["attackRange"]
            # Assuming properties["attackRange"] and properties["attackDamage"] exist
            # For now, using placeholder values and a simple attack in front of the entity
            Damage(self.stage, [0, -hh // 2], [hw // 2 + reach, hh], self.properties["attackDamage"], 0.2, self, True)

    def heal(self, damage, source = None):
        self.health += damage
        if (self.health > 20):
            self.health = 20

    def kill(self, source = None):
        self.dead = True
        if source and source.Player == True:
            points = self.properties["points"]
            source.game.score += points
        print(self.entityName, "was killed by", str(source))