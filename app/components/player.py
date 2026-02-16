import pygame;
import os;
import time
from ..utils.CollisionRect import getEnlargedHitbox
from ..utils.CollisionRect import walkOnEntityID
from ..utils.StageMovement import getRelativePos
from ..utils.Particle import Particle
from ..utils.Damage import Damage
from ..utils.ImgFilter import damageFilter

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.isLivingEntity = True
        self.dead = False
        self.Player = True

        # costumes/skins
        self.images = {}
        self.images["normal_right"] = pygame.image.load(os.path.join('./assets/players/', 'player1.png'))
        self.images["walk_right1"] = pygame.image.load(os.path.join('./assets/players/', 'player1-f1.png'))
        self.images["walk_right2"] = pygame.image.load(os.path.join('./assets/players/', 'player1-f2.png'))
        self.images["fall_right"] = pygame.image.load(os.path.join("./assets/players/", "player-fall.png"))


        self.heart = []
        self.heart.append(pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/life_bar/', 'empty_heart.png')), (64, 64)).convert_alpha())
        self.heart.append(pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/life_bar/', 'half_heart.png')), (64, 64)).convert_alpha())
        self.heart.append(pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/life_bar/', 'heart.png')), (64, 64)).convert_alpha())
        
        for image in self.images | {}:
            if image.find("right") > -1:
                newImgName = image.replace("right", "left")
                self.images[newImgName] = pygame.transform.flip(self.images[image], True, False)

        damageImages = {}
        for image in self.images:
            damageImages[image+"_damaged"] = pygame.transform.scale_by(damageFilter(self.images[image]), 2).convert_alpha()
            self.images[image] = pygame.transform.scale_by(self.images[image], 2).convert_alpha()
        
        self.images = self.images | damageImages

        self.image = self.images["normal_right"]
        self.costumeTicked = False
        self.walkingTick = 0
        self.walkingSpeed = 10

        # position and hitbox
        self.rect = self.image.get_rect()
        self.rect.x = 100 # go to x
        self.rect.y = 300 # go to y
        self.hitbox = self.rect.copy()
        self.hitbox.width = 38
        self.hitbox.height = 100
        self.physical = False

        # movement
        self.speed = 5
        self.jumpHeight = 3
        self.gravity = 0.2
        self.velocity = [0, 0]
        self.lastDir = 1 # 1 for right and -1 for left
        self.jumping = False
        self.isSneaking = False
        self.isFalling = False

        # attack
        self.isAttacking = False
        self.lastAttackTime = time.time()
        self.attackSpeed = 0.5

        self.keys = []

        # game changers
        self.boosts = []
                        #jumpStick pour rester collé au plafond, 
                        #jumpFall pour sauter depuis le vide (1 fois)
                        #immortal pour être immortel
                        #fly pour voler comme avec un jetpack
                        #regeneration pour regénérer de la vie naturellement
        self.health = 17
        self.damageCooldown = pygame.time.get_ticks()
        self.damaged = False
        self.lifeWaveAnimationStep = 0
        self.effects = []

    def tick(self, game):
        self.game = game
        self.stage = game.currentStage
        self.costumeTicked = False
        self.keys = pygame.key.get_pressed()
        if not self.stage.inventory.opened:
            if (self.keys[pygame.K_SPACE] or self.keys[pygame.K_UP]):
                self.jump(self.jumpHeight)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.attack()
            self.sneak(self.keys[pygame.K_DOWN])
        if self.keys[pygame.K_e]:
            self.stage.inventory.changeState()


        self.updateEffects()
        self.checkGravity()
        self.checkDamage()
        self.checkCostume('endTick')
    
    def checkCostume(self, type=""):
        damaged = "_damaged" if self.damaged else ""
        playerDir = "right" if self.lastDir > 0 else "left"
        if (not self.costumeTicked): # To update costume only once by tick
            if (self.isFalling):
                    self.image = self.images["fall_"+playerDir+damaged]
            elif (self.velocity[0] != 0):
                self.costumeTicked = True
                self.walkingTick = self.walkingTick + 1
                if (self.walkingTick <= self.walkingSpeed):
                    self.image = self.images["walk_"+playerDir+"1"+damaged]
                elif (self.walkingTick <= self.walkingSpeed * 2):
                    self.image = self.images["walk_"+playerDir+"2"+damaged]
                else:
                    self.image = self.images["normal_"+playerDir+damaged]
                    if (self.walkingTick > self.walkingSpeed * 2):
                        self.walkingTick = 0
            else:                  
                self.walkingTick = 0
                self.image = self.images["normal_"+playerDir+damaged]

    def move(self, x, y):
        self.velocity[0] = x
        if x != 0 and self.rect.y < 1000: # if not falling into the "void"
            self.lastDir = x
            if getEnlargedHitbox(self.hitbox, (x + 0.1) * self.speed, 0).collideobjects(self.stage.backdropRects + self.stage.physicalEntitiesHitboxes) == None:
                if ((self.rect.x > (self.game.screen.get_width()-self.stage.scrollSpace) and x > 0) or (self.rect.x < self.stage.scrollSpace and x < 0)):
                    stageMovement = self.stage.move(-x * self.speed, 0)
                    if (stageMovement[0] == 0):
                        self.rect.x += x * self.speed
                else:
                    self.rect.x += x * self.speed
        if getEnlargedHitbox(self.hitbox, 0, (y + 0.1) * self.speed).collideobjects(self.stage.backdropRects + self.stage.physicalEntitiesHitboxes) == None and self.velocity[1] != 0:
            self.rect.y += y * self.speed
            self.isFalling = True
        else:
            if y > 0 and "jumpStick" not in self.boosts:
                distToFloor = y if y >= 0 else 0
                while distToFloor > 0 and getEnlargedHitbox(self.hitbox, 0, distToFloor * self.speed).collideobjects(self.stage.backdropRects + self.stage.physicalEntitiesHitboxes) != None:
                    distToFloor = distToFloor - 0.1
                if distToFloor >= 0:
                    self.rect.y += (distToFloor - 0.1) * self.speed
                else:
                    self.rect.y += self.gravity * self.speed
                if y == self.gravity:
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
        xMovement = 0
        # Old movement system
        """if not self.stage.inventory.opened:
            if self.keys[pygame.K_LEFT] and not self.keys[pygame.K_RIGHT]:
                xMovement = -1
            if self.keys[pygame.K_RIGHT] and not self.keys[pygame.K_LEFT]:
                xMovement = 1
        """
        mouseRel = pygame.mouse.get_rel()
        if abs(mouseRel[0]) > 50 - self.game.settings["sensibility"]:
            self.lastDir = 1 if mouseRel[0] > 0 else -1
        print(mouseRel)
        if not self.stage.inventory.opened and self.keys[pygame.K_z]:
            xMovement = self.lastDir
        self.move(xMovement, self.velocity[1])

        if (self.rect.y > 1000): # if falling into the "void"
            self.damage(3)
        if (walkOnEntityID(self, "champoline", 20)):
            self.jump(5)
        if (walkOnEntityID(self, "vines")):
            self.velocity[1] = self.gravity

    def checkDamage(self):
        for damage in self.stage.damages:
            if damage.rect.collideobjects([self.hitbox]) and not self in damage.damagedEntities and self != damage.origin:
                self.damage(damage.damage, damage.origin)
                damage.damagedEntities.append(self)
        if pygame.time.get_ticks() - self.damageCooldown > 120:
            self.damaged = False

    def jump(self, force=3):
        if (walkOnEntityID(self, "vines")):
            self.velocity[1] = -0.7
        if (not self.jumping and (not self.isFalling or "jumpFall" in self.boosts) and not self.isSneaking):
            self.velocity[1] = -force
            self.jumping = True
        if ("fly" in self.boosts):
            self.jumping = False
            self.velocity[1] = -force/2

    def sneak(self, state):
        self.isSneaking = state
        if not self.isFalling and state and not self.jumping:
            Particle(self.stage, self.rect.x, self.rect.y + 50, 3, "part1", 0.5, 5)
            self.hitbox.height = 50
        else:
            self.hitbox.height = 100
        self.calcHitbox()
    
    def attack(self):
        if (time.time() - self.lastAttackTime > self.attackSpeed):
            self.lastAttackTime = time.time()
            self.isAttacking = 1
            Damage(self.stage, [50, 0], [50, 20], 5, 0.2, self, True)

    def calcHitbox(self):
        self.hitbox.x = self.rect.x + (self.rect.width - self.hitbox.width)/2 # centrage horizontal à partir des deux largeurs
        self.hitbox.y = self.rect.y + (self.rect.height - self.hitbox.height) # basage de la hitbox à partir du bas

    def respawn(self):
        self.stage.start()
        self.giveEffect("regeneration", 2)
        self.goto(100, 300)
        self.health = 20

    def damage(self, damage, source = None):
        if (pygame.time.get_ticks() - self.damageCooldown > 120 and "immortal" not in self.boosts): # to prevent player from spam-damages killing it directly
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
        print("Player was killed by", str(source))
        self.respawn()
    
    def updateEffects(self):
        for effect in self.effects:
            effect.tick()
            if (effect.initTime + effect.duration < time.time() and effect.active):
                effect.active = False
                effect.onEnd()


    def giveEffect(self, effectType, duration):
        class Effect:
            def __init__(self, player, effectType, duration):
                self.player = player
                self.type = effectType
                self.duration = duration
                self.initTime = time.time()
                self.active = True
                self.init()

            def init(self):
                if (self.type == "regeneration"):
                    self.player.boosts.append("regeneration")
                    self.player.lifeWaveAnimationStep = 0

            def tick(self):
                pass

            def onEnd(self):
                if (self.type == "regeneration"):
                    self.player.boosts.remove("regeneration")
                self.player.effects.remove(self)


        self.effects.append(Effect(self, effectType, duration))