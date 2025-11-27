import pygame
from ..utils.StageHandler import getStageByID
from ..utils.Font import initFonts
from ..utils.Storage import readFile

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Trophées NSI 2025-2026")

        initFonts(self)

        self.screen = pygame.display.set_mode((1280, 720))
        self.running = False
        self.currentStage = getStageByID("main")(self)
        self.clock = pygame.time.Clock()
        self.settings = {}
        self.settings["volume"] = 100
        self.loadSettings()
        
    def loadSettings(self):
        try:
            settingsData = readFile('settings')
            if settingsData and len(settingsData) > 0:
                for row in settingsData:
                    key = row.get('name', '').strip()
                    value = row.get('value', '').strip()
                    if key:
                        try:
                            self.settings[key] = int(value)
                        except ValueError:
                            try:
                                self.settings[key] = float(value)
                            except ValueError:
                                self.settings[key] = value
                print(f"Loaded {len(settingsData)} setting(s) from storage")
        except Exception as e:
            print(f"Could not load settings from storage: {e}, using defaults")

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