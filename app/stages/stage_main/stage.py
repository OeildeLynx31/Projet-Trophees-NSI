import pygame
import os

from ...utils.Button import Button
from ...utils.Storage import *
from ...utils.Font import Font
from ...utils.Font import getFont

class Stage():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.group = pygame.sprite.Group()
        self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', "bg_interface__main.png")), (1280, 720)).convert()

        self.play_button = Button(512, 288, 256, 128, "main_play.png")
        self.quit_button = Button(512, 480, 256, 128, "main_quit.png")
        self.settings_button = Button(512, 384, 256, 128, "main_settings.png")
        self.title = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/', "title.png")), (876, 248)).convert_alpha()

        self.fontLabels = []
        self.fontLabels.append(Font("Hello world", [0, 0], getFont(self.game, "default"), "WHITE", {}))

    def tick(self, game):
        self.game = game
        self.screen.blit(self.backdrop, (0, 0))
        self.screen.blit(self.title, (202, 48))
        self.group.draw(self.screen)
        self.renderGUI()
        if (self.play_button.isClicked()):
            self.game.changeStage("1")
        if (self.settings_button.isClicked()):
            self.game.changeStage("settings")
        if (self.quit_button.isClicked()):
            pygame.quit()
            exit()
        pygame.display.flip()

    def renderGUI(self):
        self.play_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        self.settings_button.draw(self.screen)
        for label in self.fontLabels:
            label.draw(self.screen)
