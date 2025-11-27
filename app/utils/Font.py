import pygame
import os

def initFonts(game):
    pygame.font.init()
    game.fonts = {
        "default": pygame.font.Font(None, 32),
    }

def getFont(game, font="default"):
    if hasattr(game.fonts, font):
        return game.fonts[font]
    else:
        return game.fonts["default"]

class Font:
    def __init__(self, text, pos, font, color, options={}):
        self.font = font
        self.text = text
        self.color = color

        self.options = options
        self.font.set_underline(self.options["underline"] if hasattr(self.options, "underline") else False)
        self.font.set_strikethrough(self.options["strikethrough"] if hasattr(self.options, "strikethrough") else False)
        self.font.set_bold(self.options["bold"] if hasattr(self.options, "bold") else False)
        self.font.set_italic(self.options["italic"] if hasattr(self.options, "italic") else False)

        self.size = self.font.size(self.text)
        self.rect = pygame.Rect(pos[0], pos[1], self.size[0], self.size[1])


    def draw(self, surface):
        self.image = self.font.render(self.text, self.options["antialias"] if hasattr(self.options, "italic") else True, self.color)
        surface.blit(self.image, self.rect)

        self.font.set_underline(self.options["underline"] if hasattr(self.options, "underline") else False)
        self.font.set_strikethrough(self.options["strikethrough"] if hasattr(self.options, "strikethrough") else False)
        self.font.set_bold(self.options["bold"] if hasattr(self.options, "bold") else False)
        self.font.set_italic(self.options["italic"] if hasattr(self.options, "italic") else False)

    def isHovered(self):
        mousePos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mousePos[0], mousePos[1])

    def isClicked(self):
        if (pygame.mouse.get_pressed()[0] and self.isHovered()):
            return True
        else:
            return False
