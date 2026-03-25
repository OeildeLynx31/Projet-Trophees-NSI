import pygame
import time
from .StageMovement import getRelativePos
from .StageMovement import getStaticPos
 
class Damage:
    def __init__(self, stage, pos, size, damage, duration, origin, relative=False):
        self.stage = stage
        self.time = time.time()
        self.duration = duration
        self.damage = damage
        self.origin = origin
        self.relative = relative
        self.position = pos
        self.damagedEntities = []
        if not self.relative:
            self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        else:
            xMiddle = self.origin.hitbox.x + (self.origin.hitbox.width / 2)
            yMiddle = self.origin.hitbox.y + (self.origin.hitbox.height / 2)
            self.rect = pygame.Rect((xMiddle + pos[0]) if (self.origin.lastDir > 0) else (xMiddle - pos[0] - size[0]), yMiddle + pos[1], size[0], size[1])
        # add the damage
        self.stage.damages.append(self)
    
    def tick(self):
        xMiddle = self.origin.hitbox.x + (self.origin.hitbox.width / 2)
        yMiddle = self.origin.hitbox.y + (self.origin.hitbox.height / 2)
        self.rect = pygame.Rect((xMiddle + self.position[0]) if (self.origin.lastDir > 0) else (xMiddle - self.position[0] - self.rect.width), yMiddle + self.position[1], self.rect.width, self.rect.height)
