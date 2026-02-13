import pygame
import os

from .Font import *
from .CollisionRect import getSpriteCollisionRects

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
        self.slots = []
        for id in range(0, 20):
            self.slots.append(InventorySlot(self.game, id))

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
        for slot in self.slots:
            slot.tick(self.game)


class InventorySlot:
    def __init__(self, game, id:int):
        self.game = game
        self.screen = game.screen

        self.id = id
        self.pos = self.getSlotPosFromID(id)
        self.type = self.getSlotTypeFromID(id)

        self.image = pygame.transform.scale_by(pygame.image.load(os.path.join('./assets/interface/inventory/', self.type+"_slot.png")), 8).convert_alpha()
        self.image.set_alpha(32)

        self.clickRect = getSpriteCollisionRects(self.image)[0] # supposing that a button is composed by only one surface
        self.clickRect.x += self.pos[0]
        self.clickRect.y += self.pos[1]


    def tick(self, game):
        self.image.set_alpha(48 if self.isHovered() else 32)
        self.screen.blit(self.image, self.pos)

    def isHovered(self):
        mousePos = pygame.mouse.get_pos()
        return self.clickRect.collidepoint(mousePos[0], mousePos[1])

    def getSlotPosFromID(self, id:int):
        x = 0
        y = 0
        if id < 5:
            if id == 0:
                x, y = 66, 15
            elif id == 1:
                x, y = 53, 6
            elif id == 2:
                x, y = 85, 6
            elif id == 3:
                x, y = 53, 31
            else:
                x, y = 85, 31
        else:
            id = id - 5
            x = 4 + 9 * (id%5)
            y = 21 + 9 * (id//5)
        return (240 + 8 * x, 168 + 8 * y)

    def getSlotTypeFromID(self, id:int):
        if id == 0:
            return "main"
        elif id < 5:
            return "second"
        else:
            return "normal"
