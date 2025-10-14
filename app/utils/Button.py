import pygame
import os
from .CollisionRect import get_sprite_collision_rects

class Button:
    def __init__(self, x, y, width, height, img):
        self.image = pygame.image.load(os.path.join('./assets/interface/', img))
        self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clickRect = get_sprite_collision_rects(self.image)[0] # supposing that a button is composed by only one surface
        self.clickRect.x += x
        self.clickRect.y += y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def isHovered(self):
        mousePos = pygame.mouse.get_pos()
        print(self.clickRect.collidepoint(mousePos[0], mousePos[1]))
        return self.clickRect.collidepoint(mousePos[0], mousePos[1])

    def isClicked(self):
        if (pygame.mouse.get_pressed()[0] and self.isHovered()):
            return True
        else:
            return False
