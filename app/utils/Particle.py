import pygame
import random
import os
from .StageMovement import getRelativePos
from .StageMovement import getStaticPos
 
class Particle:
    def __init__(self, stage, x:int, y:int, size:int=1, parType:str="circle", speed:float=2, gravity:float=0, lifeTime:int=100):
        self.stage = stage
        pos = getStaticPos(self.stage, x, y)
        self.x = pos[0]
        self.y = pos[1]
        self.vx = random.uniform(-speed, speed)
        self.vy = random.uniform(-speed, speed)
        self.gravity = gravity
        self.size = size
        self.lifetime = lifeTime  # Durée de vie de la particule
        self.type = parType
        self.stage.particles.append(self)
        self.img = pygame.transform.scale(pygame.image.load(os.path.join('./assets/particles/', self.type+'.png')), (8 * self.size, 8 * self.size))
        self.renderLayer = -1
 
    def tick(self):
        self.x += self.vx
        self.y += self.vy
        if self.gravity:
            self.y += 0.5
        self.lifetime -= 1
        if self.lifetime == 0:
            self.stage.particles.remove(self)
        else:
            self.draw(self.stage.screen)

        if len(self.stage.particles) > 1000:
            print("Warning: Too much particles")
 
    def draw(self, screen):
        pos = getRelativePos(self.stage, self.x, self.y)
        if self.type == "circle":
            pygame.draw.circle(screen, (255, 255, 0), (pos[0], pos[1]), 3 * self.size)
        else:
            screen.blit(self.img, pygame.Rect(pos[0], pos[1], 8, 8))