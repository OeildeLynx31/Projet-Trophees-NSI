import pygame
import os

from ...utils.Button import Button

class Stage():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.id = "pause" # Added stage ID
        self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', "bg_interface__main.png")), (1280, 720)).convert()

        self.resume_button = Button(512, 200, 256, 128, "main_play.png")
        self.save_button = Button(512, 330, 256, 128, "main_settings.png")
        self.quit_button = Button(512, 460, 256, 128, "main_quit.png")

    def tick(self, game):
        self.game = game
        self.screen.blit(self.backdrop, (0, 0))

        self.resume_button.draw(self.screen)
        self.save_button.draw(self.screen)
        self.quit_button.draw(self.screen)

        if (self.resume_button.isClicked()):
            self.game.changeStage(self.game.previousStageID)
        
        if (self.save_button.isClicked()):
            self.game.saveGame()

        if (self.quit_button.isClicked()):
            self.game.quit()

        pygame.display.flip()
