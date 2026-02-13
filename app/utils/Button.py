import pygame
import os
from .CollisionRect import getSpriteCollisionRects

from .Font import *

class Button:
    def __init__(self, game, x, y, width, height, txt):
        self.game = game
        self.image = pygame.image.load(os.path.join('./assets/interface/buttons/', 'button_base.png'))
        self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clickRect = getSpriteCollisionRects(self.image)[0] # supposing that a button is composed by only one surface
        self.clickRect.x += x
        self.clickRect.y += y
        self.label = Label(txt, (x, y), getFont(self.game, "yoster"), "#c4a497", 32, {"center": (x + width/2 - 2, y + height/2)})

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.label.draw(self.game.screen)

    def isHovered(self):
        mousePos = pygame.mouse.get_pos()
        return self.clickRect.collidepoint(mousePos[0], mousePos[1])

    def isClicked(self):
        if (pygame.mouse.get_pressed()[0] and self.isHovered()):
            return True
        else:
            return False
