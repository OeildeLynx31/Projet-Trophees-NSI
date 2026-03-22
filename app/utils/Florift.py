import pygame
import os
import math
import time
from .StageMovement import getRelativePos

class Florift(pygame.sprite.Sprite):
    def __init__(self, stage, game, posX, posY):
        pygame.sprite.Sprite.__init__(self)

        self.stage = stage
        self.game = game
        self.Player = False
        self.isLivingEntity = False
        self.dead = False
        self.physical = False
        self.renderLayer = -1
        self.entityType = "florift"

        raw = pygame.image.load(os.path.join('./assets/entities/', 'fleurtp.png')).convert_alpha()
        self.baseImage = pygame.transform.scale(raw, (64, 64))

        self.image = self.baseImage.copy()
        self.rect = self.image.get_rect()

        pos = getRelativePos(self.stage, posX, posY)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.hitbox = pygame.Rect(
            self.rect.x, self.rect.y,
            64, 64
        )

        self.partner = None

        self.animTick = 0

        self.tpCooldown = 0
        self.TP_COOLDOWN_DURATION = 1500

        self.shiftWasReleased = True

    def tick(self, game):
        self.game = game

        if game.currentStage is not self.stage:
            return

        self.animTick += 1
        self.calcHitbox()
        self.updateAnim()
        self.checkTeleport()

    def calcHitbox(self):
        self.hitbox.x = self.rect.x
        self.hitbox.y = self.rect.y
        self.hitbox.width = self.rect.width
        self.hitbox.height = self.rect.height

    def updateAnim(self):
        pulse = 1.0 + 0.06 * math.sin(self.animTick * 0.08)
        size = int(64 * pulse)
        self.image = pygame.transform.scale(self.baseImage, (size, size))
        cx = self.rect.centerx
        cy = self.rect.centery
        self.rect = self.image.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy

    def checkTeleport(self):
        if self.partner is None:
            return

        keys = pygame.key.get_pressed()
        shiftPressed = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

        if not shiftPressed:
            self.shiftWasReleased = True

        player = self.stage.player
        now = pygame.time.get_ticks()

        if (self.hitbox.colliderect(player.hitbox) and shiftPressed and self.shiftWasReleased  and now > self.tpCooldown and now > self.partner.tpCooldown):
            self.shiftWasReleased = False

            stage = self.stage

            partnerWorldX = self.partner.rect.x - stage.scroll[0]

            targetScroll = -(partnerWorldX - 640)
            targetScroll = max(stage.scrollMin, min(stage.scrollMax, targetScroll))
            deltaX = targetScroll - stage.scroll[0]
            stage.move(deltaX, 0)

            player.rect.x = self.partner.rect.x
            player.rect.y = self.partner.rect.y - player.rect.height + self.partner.rect.height
            player.calcHitbox()
            player.velocity[1] = 0

            player.giveEffect("floriftBoost", 0.7)

            self.tpCooldown = now + self.TP_COOLDOWN_DURATION
            self.partner.tpCooldown = now + self.TP_COOLDOWN_DURATION
            self.partner.shiftWasReleased = False