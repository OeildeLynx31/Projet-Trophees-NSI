import pygame
import os

from ...utils.Button import Button
from ...utils.Storage import *

from ...utils.Font import *

class Stage():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.id = "main" # Added stage ID
        self.group = pygame.sprite.Group()
        self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('./assets/backgrounds/', "bg_interface__main.png")), (1280, 720)).convert()

        self.X_OFFSET = 50 # Manual offset to adjust for perceived off-centering

        self.play_button = Button(512 + self.X_OFFSET, 150, 256, 128, "main_play.png")
        
        # Calculate centered position for "Load Game" label
        font_for_size = getFont(self.game, "alagard")
        label_width, label_height = font_for_size.size("Load Game")
        load_game_label_x = (1280 / 2) - (label_width / 2) + self.X_OFFSET
        load_game_label_y = (310 + 128/2) - (label_height / 2)
        self.load_game_label = Label("Load Game", [load_game_label_x, load_game_label_y], font_for_size, "WHITE", 40)
        
        self.settings_button = Button(512 + self.X_OFFSET, 470, 256, 128, "main_settings.png")
        self.quit_button = Button(512 + self.X_OFFSET, 630, 256, 128, "main_quit.png")
        self.title = pygame.transform.scale(pygame.image.load(os.path.join('./assets/interface/', "title.png")), (876, 248)).convert_alpha()
        self.fontLabels = []
        self.fontLabels.append(Label("ABCDEEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789", [0, 0], getFont(self.game, "yoster"), "WHITE", 32))
        self.fontLabels.append(Label("ABCDEEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789", [5, 30], getFont(self.game, "alagard"), "WHITE", 32))

        self.game.musicManager.play_music('base_loop', game.settings)

    def tick(self, game):
        self.game = game
        self.screen.blit(self.backdrop, (0, 0))
        self.screen.blit(self.title, (202 + self.X_OFFSET, 48)) # Apply X_OFFSET to title
        self.play_button.draw(self.screen)
        self.load_game_label.draw(self.screen) # Draw the label
        self.quit_button.draw(self.screen)
        self.settings_button.draw(self.screen)
        self.group.draw(self.screen)
        self.renderGUI()
        if (self.play_button.isClicked()):
            self.game.changeStage("1")
        
        if self.load_game_label.isClicked(): # Using Label's isClicked method
            self.game.loadGame()

        if (self.settings_button.isClicked()):
            self.game.changeStage("settings")
        if (self.quit_button.isClicked()):
            print("Quitting game...")
            pygame.quit()
            exit()
        pygame.display.flip()

    def renderGUI(self):
        self.play_button.draw(self.screen)
        self.load_game_label.draw(self.screen) # Draw the label in renderGUI too
        self.quit_button.draw(self.screen)
        self.settings_button.draw(self.screen)
        for label in self.fontLabels:
            label.draw(self.screen)
