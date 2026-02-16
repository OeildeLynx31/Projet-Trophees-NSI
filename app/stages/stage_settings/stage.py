import pygame
import os

from ...utils.Button import Button
from ...utils.Slider import Slider
from ...utils.Settings import saveSettings

class Stage():
    def __init__(self, game):
        self.game = game
        self.settings = self.game.settings
        self.screen = game.screen
        self.id = "settings"
        self.group = pygame.sprite.Group()
        self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', "bg_interface__main.png")), (1280, 720)).convert()

        self.back_button = Button(self.game, 512, 576, 256, 128, "BACK")
        self.volume_slider = Slider(256, 128, 256, 48, 0, 100, self.settings["volume"], 2)
        self.sensibility_slider = Slider(256, 256, 256, 48, 0, 64, self.settings["sensibility"], 2)

        self.volume_icons = {}
        self.volume_icons["pos"] = (160, 108)
        self.volume_icons["mute"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/icons/sound/', "sound_mute.png")), (96, 96)).convert_alpha()
        self.volume_icons["low"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/icons/sound/', "sound_low.png")), (96, 96)).convert_alpha()
        self.volume_icons["middle"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/icons/sound/', "sound_middle.png")), (96, 96)).convert_alpha()
        self.volume_icons["loud"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/icons/sound/', "sound_loud.png")), (96, 96)).convert_alpha()

    def tick(self, game):
        self.game = game
        self.screen.blit(self.backdrop, (0, 0))

        self.back_button.draw(self.screen)
        self.volume_slider.draw(self.screen)
        self.sensibility_slider.draw(self.screen)
        self.drawSoundIcon()

        self.group.draw(self.screen)

        if (self.back_button.isClicked()):
            saveSettings(self.settings)
            self.game.changeStage("main")
        pygame.display.flip()

        self.updateSettings()

    def updateSettings(self):
        self.settings["volume"] = self.volume_slider.value
        self.game.musicManager.updateVolume(self.settings)

        self.settings["sensibility"] = self.sensibility_slider.value

    def drawSoundIcon(self):
        value = self.volume_slider.value
        icon = self.volume_icons["mute"]
        if (value > 0 and value < 30 ):
            icon = self.volume_icons["low"]
        if (value >= 30 and value < 70 ):
            icon = self.volume_icons["middle"]
        if (value >= 70):
            icon = self.volume_icons["loud"]
        self.screen.blit(icon, self.volume_icons["pos"])
