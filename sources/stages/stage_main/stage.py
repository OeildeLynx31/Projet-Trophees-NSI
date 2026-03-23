import pygame
import os

from ...engine.Button import Button
from ...engine.Storage import *

from ...engine.Font import *

class Stage():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.id = "main" # Added stage ID
        self.group = pygame.sprite.Group()
        self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', "bg_interface__main.png")), (1280, 720)).convert()

        self.play_button = Button(self.game, 512, 288, 256, 128, "PLAY")
        self.quit_button = Button(self.game, 512, 576, 256, 128, "QUIT")
        self.settings_button = Button(self.game, 512, 384, 256, 128, "SETTINGS")
        self.presentation_button = Button(self.game, 512, 480, 256, 128, "ABOUT")
        self.title = pygame.transform.scale_by(pygame.image.load(os.path.join('./assets/interface/', "title.png")), 4).convert_alpha()
        self.fontLabels = []

        self.game.musicManager.play_music('powerful_adventure', game.settings, interrupt=False)

    def tick(self, game):
        self.game = game
        self.screen.blit(self.backdrop, (0, 0))
        self.screen.blit(self.title, (238, 48)) # Apply X_OFFSET to title
        self.play_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        self.settings_button.draw(self.screen)
        self.presentation_button.draw(self.screen)
        self.group.draw(self.screen)
        self.renderGUI()
        if (self.play_button.isClicked()):
            self.game.changeStage("1")
        if (self.presentation_button.isClicked()):
            self.game.changeStage("presentation")
        if (self.settings_button.isClicked()):
            self.game.changeStage("settings")
        if (self.quit_button.isClicked()):
            self.game.quit()
        pygame.display.flip()

    def renderGUI(self):
        self.play_button.draw(self.screen)
        # self.quit_button.draw(self.screen)
        self.settings_button.draw(self.screen)
        for label in self.fontLabels:
            label.draw(self.screen)
