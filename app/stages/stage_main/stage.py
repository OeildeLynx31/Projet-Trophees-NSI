import pygame
import os

from ...utils.Button import Button

class Stage():
  def __init__(self, game):
    self.game = game
    self.screen = game.screen
    self.group = pygame.sprite.Group()
    self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', "bg_interface__main.png")), (1280, 720)).convert_alpha()

    self.play_button = Button(540, 250, 200, 200, "main_play.png")
    self.quit_button = Button(540, 470, 200, 200, "main_quit.png")

  def tick(self, game):
    self.game = game
    self.screen.blit(self.backdrop, (0, 0))
    self.play_button.draw(self.screen)
    self.group.draw(self.screen)
    if (self.play_button.isClicked()):
        self.game.changeStage("1")
    if (self.quit_button.isClicked()):
        pygame.quit()
        exit()
    pygame.display.flip()
