import pygame
import os

from ..utils.Font import *
from .Slot import Slot # Import the new Slot class

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

        # Inventory slots
        self.slots = []
        slot_size = 64
        slot_padding = 10
        start_x = 240 + 50 # X position of invLayer + some internal padding
        start_y = 168 + 100 # Y position of invLayer + some internal padding
        for row in range(4): # Example 4x4 grid
            for col in range(4):
                x = start_x + col * (slot_size + slot_padding)
                y = start_y + row * (slot_size + slot_padding)
                self.slots.append(Slot(x, y, slot_size, slot_size))

    def changeState(self):
        newDate = pygame.time.get_ticks()
        if newDate - self.lastOpenClose > self.openCloseCooldown:
            self.opened = not self.opened
            self.lastOpenClose = pygame.time.get_ticks()

    def tick(self, game):
        self.screen.blit(self.backOverlay, (0, 0))
        self.screen.blit(self.invLayer, (240, 168))
        self.title.draw(self.screen)

        for slot in self.slots:
            slot.draw(self.screen)

        