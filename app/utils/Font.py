import pygame
import os

def initFonts(game):
    pygame.font.init()
    game.fonts = {
        "default": pygame.font.Font(None, 512),
        "yoster": pygame.font.Font(os.path.join('./assets/fonts', "yoster.ttf"), 512),
    }

def getFont(game, font="default"):
    if font in game.fonts:
        return game.fonts[font]
    else:
        return game.fonts["default"]

class Label:
    def __init__(self, text, pos, font, color, scale, options={"underline":True}):
        self.font = font
        self.text = text
        self.color = color

        self.options = options
        self.font.set_underline(self.options["underline"] if "underline" in self.options else False)
        self.font.set_strikethrough(self.options["strikethrough"] if "strikethrough" in self.options else False)
        self.font.set_bold(self.options["bold"] if "bold" in self.options else False)
        self.font.set_italic(self.options["italic"] if "italic" in self.options else False)

        self.size = self.font.size(self.text)
        self.scale = scale
        self.rect = pygame.Rect(pos[0], pos[1], self.size[0], self.size[1])


    def draw(self, surface):
        self.font.set_underline(self.options["underline"] if "underline" in self.options else False)
        self.font.set_strikethrough(self.options["strikethrough"] if "strikethrough" in self.options else False)
        self.font.set_bold(self.options["bold"] if "bold" in self.options else False)
        self.font.set_italic(self.options["italic"] if "italic" in self.options else False)

        self.image = pygame.transform.scale_by(self.font.render(self.text, self.options["antialias"] if "antialias" in self.options else True, self.color), self.scale/512).convert_alpha()
        surface.blit(self.image, self.rect)

    def isHovered(self):
        mousePos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mousePos[0], mousePos[1])

    def isClicked(self):
        if (pygame.mouse.get_pressed()[0] and self.isHovered()):
            return True
        else:
            return False
