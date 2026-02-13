import pygame
import os

from .Font import *
from .CollisionRect import getSpriteCollisionRects
from .Button import Button


class PauseInterface:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.pauseLayer = pygame.transform.scale_by(pygame.image.load(os.path.join('./assets/interface/pause/', "pause_interface.png")), 8).convert()
        self.backOverlay = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/', "pixel_overlay.png")), (1280, 720)).convert_alpha()
        self.backOverlay.set_alpha(200)
        self.openCloseCooldown = 250
        self.lastOpenClose = pygame.time.get_ticks()
        self.paused = False
        self.buttons = {}
        self.buttons["resume"] = Button(self.game, 512, 224, 256, 128, "RESUME")
        self.buttons["restart"] = Button(self.game, 512, 320, 256, 128, "RESTART")
        self.buttons["menu"] = Button(self.game, 512, 416, 256, 128, "MAIN MENU")
        self.buttons["quit"] = Button(self.game, 512, 512, 256, 128, "QUIT")


        self.title = Label("GAME PAUSED", [472, 148], getFont(self.game, "yoster"), "#2b1501", 48)

        self.previousScreen = pygame.Surface((0, 0))

    def tick(self, game):
        self.screen.blit(self.previousScreen, (0, 0))
        self.screen.blit(self.backOverlay, (0, 0))
        self.screen.blit(self.pauseLayer, (448, 128))
        for bntName in self.buttons:
            self.buttons[bntName].draw(self.screen)
            if self.buttons[bntName].isClicked():
                self.switchPause(False)
        self.title.draw(self.screen)


    def switchPause(self, state):
        if not self.paused and state:
            self.previousScreen = self.game.screen.copy()
        self.paused = state
