import pygame
import os

class Button:
    def __init__(self, x, y, width, height, img):
        self.image = pygame.image.load(os.path.join('./assets/interface/', img))
        self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def isHovered(self, mouseX, mouseY):
        return self.rect.collidepoint(mouseX, mouseY)