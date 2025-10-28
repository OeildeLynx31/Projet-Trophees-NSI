import pygame
import os

from ...utils.Button import Button
from ...utils.Slider import Slider

class Stage():
  def __init__(self, game):
    self.game = game
    self.screen = game.screen
    self.group = pygame.sprite.Group()
    self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', "bg_interface__main.png")), (1280, 720)).convert()

    self.back_button = Button(512, 576, 256, 128, "main_back.png")
    self.volume_slider = Slider(512, 256, 256, 48, 0, 100, 50, 2)

  def tick(self, game):
    self.game = game
    self.screen.blit(self.backdrop, (0, 0))

    self.back_button.draw(self.screen)
    self.volume_slider.draw(self.screen)

    self.group.draw(self.screen)

    if (self.back_button.isClicked()):
        self.game.changeStage("main")
    pygame.display.flip()
