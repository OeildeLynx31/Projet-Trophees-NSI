import pygame
import os

class Stage():
  def __init__(self, game):
    self.game = game
    self.screen = game.screen
    self.group = pygame.sprite.Group()

    self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', "bg_interface__main.png")), (1280, 720)).convert_alpha()

  def tick(self, game):
    self.screen.blit(self.backdrop, (0, 0))
    self.group.draw(self.screen)

    pygame.display.flip()