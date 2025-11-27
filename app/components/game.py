import pygame
from ..utils.StageHandler import getStageByID
from ..utils.Font import initFonts
from ..utils.Settings import loadSettings

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Trophées NSI 2025-2026")

        initFonts(self)

        self.flags = pygame.FULLSCREEN | pygame.SCALED
        self.screen = pygame.display.set_mode((1280, 720), flags=self.flags, vsync=1)
        self.running = False
        self.currentStage = getStageByID("main")(self)
        self.clock = pygame.time.Clock()
        self.settings = loadSettings()


    def run(self):
        self.running = True
        while self.running :
            self.tick()
            self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

    def quit(self):
        self.running = False
        pygame.quit()
    
    def changeStage(self, stageID):
        self.currentStage = getStageByID(stageID)(self)

    def tick(self):
        self.currentStage.tick(self)