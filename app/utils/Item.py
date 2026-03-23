import pygame
import os


class Item:
    def __init__(self, id):
        self.id = id
        self.category = self.getItemProp("category")
        self.description = self.getItemProp("description")
        self.slotType = self.getItemProp("slot_type")
        self.name = self.getItemProp("name")
        self.image = pygame.image.load(os.path.join('./assets/interface/items', self.id+".png")).convert_alpha()

    def getItemProp(self, prop):
        return self.item_register[self.id][prop]

    def getProps(self):
        return self.item_register[self.id]

    def isEmpty(self):
        if self.id != "empty":
            return False
        return True

    item_register = {
        "empty": {
            "name": "empty", # what is displayed
            "category": "", # item category
            "slot_type": "all",   # which slot in the inventory
            "description": "", # Item description in the inventory
        },
        "sword": {
            "name": "basic sword",
            "category": "weapons",
            "slot_type": "main",
            "description": "A simple sword to attack",
        },
        "spear": {
            "name": "basic spear",
            "category": "weapons",
            "slot_type": "main",
            "description": "A simple spear to attack",
        },
        "axe": {
            "name": "basic axe",
            "category": "weapons",
            "slot_type": "main",
            "description": "A simple axe to attack",
        },
        "mass": {
            "name": "basic mass",
            "category": "weapons",
            "slot_type": "main",
            "description": "A simple mass to attack",
        },
        "chepa": {
            "name": "basic chepa kwa",
            "category": "weapons",
            "slot_type": "main",
            "description": "A simple chepa kwa to attack",
        }
    }