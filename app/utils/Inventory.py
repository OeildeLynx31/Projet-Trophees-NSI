import pygame
import os

from .Font import *
from .CollisionRect import getSpriteCollisionRects
from .Item import Item

class InventoryInterface:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.invLayer = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/inventory/', "inventory_back.png")), (800, 384)).convert()
        self.backOverlay = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/', "pixel_overlay.png")), (1280, 720)).convert_alpha()
        self.backOverlay.set_alpha(160)
        self.openCloseCooldown = 250
        self.lastOpenClose = pygame.time.get_ticks()
        self.opened = False
        self.slots = []
        for id in range(0, 20):
            self.slots.append(InventorySlot(self.game, id))

        self.loadInv(self.testInv)

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
            if slot.isClicked():
                print(self.saveInv())

    def moveItem(self, origin, arrival):
        originSlot = self.slots[origin]
        arrivalSlot = self.slots[arrival]
        arrivalItem = arrivalSlot.getItem()
        arrivalSlot.setItem(originSlot.getItem())
        originSlot.setItem(arrivalItem)

    def loadInv(self, content):
        for index in range(len(self.slots)):
            if index in content:
                item = Item(content[index]["id"])
                self.slots[index].setItem(item)
            else:
                self.slots[index].setItem(Item("empty"))

    def saveInv(self):
        return {index:{"id": self.slots[index].item.id} for index in range(len(self.slots))}

    testInv = {
        0: {"id":"sword"},
        1: {"id":"spear"},
        2: {"id":"axe"},
        3: {"id":"chepa"},
        4: {"id":"mass"}

    }


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

        self.item = Item("empty")


    def tick(self, game):
        self.image.set_alpha(48 if self.isHovered() else 32)
        self.screen.blit(self.image, self.pos)
        self.screen.blit(self.getItemIcon(), self.getItemIconPos())

    def isHovered(self):
        mousePos = pygame.mouse.get_pos()
        return self.clickRect.collidepoint(mousePos[0], mousePos[1])

    def isClicked(self):
        if (pygame.mouse.get_pressed()[0] and self.isHovered()):
            return True
        else:
            return False

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

    def setItem(self, item):
        if self.type != "normal" and self.type != item.slotType and item.slotType != "all":
            print(f"This item {item.id} should NOT be there! slot.type:{self.type}, item.type:{item.slotType}")
        self.item = item

    def getItem(self):
        return self.item

    def emptySlot(self):
        self.setItem(Item("empty"))

    def getItemIcon(self):
        img = self.item.image
        if self.type == "main":
            img = pygame.transform.scale(img, (72, 72))
        elif self.type == "second":
            img = pygame.transform.scale(img, (48, 48))
        else:
            img = pygame.transform.scale(img, (40, 40))
        return img

    def getItemIconPos(self):
        center = self.clickRect.center
        x = center[0]
        y = center[1]
        scale = (72 / 2) if self.type == "main" else (48 / 2) if self.type == "second" else (40 / 2)
        adjust = 0 if self.type == "normal" else -1
        return (x - scale + adjust, y - scale + adjust)

