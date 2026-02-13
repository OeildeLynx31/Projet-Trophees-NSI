import pygame
import os

from ..utils.Font import *

class InventoryInterface:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.invLayer = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/inventory/', "inventory_back.png")), (800, 384)).convert()
        self.backOverlay = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/', "pixel_overlay.png")), (1280, 720)).convert_alpha()
        self.backOverlay.set_alpha(200)
        self.openCloseCooldown = 250
        self.lastOpenClose = pygame.time.get_ticks()
        self.opened = False

        self.title = Label("INVENTORY", [270, 188], getFont(self.game, "yoster"), "#2b1501", 48)

    def changeState(self):
        newDate = pygame.time.get_ticks()
        if newDate - self.lastOpenClose > self.openCloseCooldown:
            self.opened = not self.opened
            self.lastOpenClose = pygame.time.get_ticks()

    def tick(self, game):
        self.screen.blit(self.backOverlay, (0, 0))
        self.screen.blit(self.invLayer, (240, 168))
        self.title.draw(self.screen)


class InventorySlot:
    def __init__(self, position:tuple, slotType="normal"):
        self.pos = position
        self.type = slotType
        