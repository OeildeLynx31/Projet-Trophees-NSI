import pygame
import os

from ...utils.Button import Button
from ...utils.Slider import Slider

class Stage():
  def __init__(self, game):
    self.game = game
    self.settings = self.game.settings
    self.screen = game.screen
    self.group = pygame.sprite.Group()
    self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', "bg_interface__main.png")), (1280, 720)).convert()

    self.back_button = Button(512, 576, 256, 128, "main_back.png")
    self.volume_slider = Slider(256, 128, 256, 48, 0, 100, self.settings["volume"], 2)

    self.volume_icons = {}
    self.volume_icons["pos"] = (192, 128)
    self.volume_icons["mute"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/icons/sound/', "sound_mute.png")), (48, 48)).convert_alpha()
    self.volume_icons["low"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/icons/sound/', "sound_low.png")), (48, 48)).convert_alpha()
    self.volume_icons["middle"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/icons/sound/', "sound_middle.png")), (48, 48)).convert_alpha()
    self.volume_icons["loud"] = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/icons/sound/', "sound_loud.png")), (48, 48)).convert_alpha()

  def tick(self, game):
    self.game = game
    self.screen.blit(self.backdrop, (0, 0))

    self.back_button.draw(self.screen)
    self.volume_slider.draw(self.screen)
    self.drawSoundIcon()

    self.group.draw(self.screen)

    if (self.back_button.isClicked()):
        self.game.changeStage("main")
    pygame.display.flip()

    self.updateSettings()

  def updateSettings(self):
    self.settings["volume"] = self.volume_slider.value

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
