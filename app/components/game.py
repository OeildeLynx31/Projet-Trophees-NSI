import pygame
from ..utils.StageHandler import getStageByID

class Game():
    def __init__(self, currentStage=None):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1280, 720))
        self.running = False
        self.currentStage = getStageByID("1")(self.screen)
        self.clock = pygame.time.Clock()

    def run(self):
        self.running = True
        while self.running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            self.tick()
            self.clock.tick(60)

    def quit(self):
        self.running = False
        pygame.quit()

    def tick(self):
        self.currentStage.tick()