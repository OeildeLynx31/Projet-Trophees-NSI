import pygame
from ..utils.StageHandler import getStageByID
from ..utils.Font import initFonts
from ..utils.Settings import loadSettings
from ..utils.Musics import MusicManager
from ..utils.Storage import initFile, upsertData, getData
from ..utils.Pause import PauseInterface

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Trophées NSI 2025-2026")

        initFonts(self)

        self.debug = {
            "show_hitboxes": False,
            "fullscreen": True
        }

        self.flags = (pygame.FULLSCREEN | pygame.SCALED) if self.debug["fullscreen"] else 0
        self.screen = pygame.display.set_mode((1280, 720), flags=self.flags, vsync=1)
        self.running = False
        self.musicManager = MusicManager()
        self.clock = pygame.time.Clock()
        self.settings = loadSettings()
        self.previousStageID = "main" # Added for pause menu
        self.pauseInterface = PauseInterface(self)
        self.score = 0

        initFile("save", ["name", "stage", "player_x", "player_y", "player_health", "player_boosts"])

        # Load the main stage
        self.currentStage = getStageByID("main")(self)


    def run(self):
        self.running = True
        while self.running :
            self.tick()
            self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

    def quit(self):
        print("Quitting game...")
        self.running = False
        pygame.quit()
        exit()
    
    def changeStage(self, stageID, load_data=None):
        self.currentStage = getStageByID(stageID)(self)
        if load_data:
            self.currentStage.player.goto(load_data['player_x'], load_data['player_y'], rel=False)
            self.currentStage.player.health = int(load_data['player_health'])
            self.currentStage.player.boosts = load_data['player_boosts'].split(',') if load_data['player_boosts'] else []
        if stageID != "pause":
            self.isPaused = False

    def saveGame(self):
        if hasattr(self.currentStage, 'player'):
            player_data = {
                "name": "player_data",
                "stage": self.currentStage.id if hasattr(self.currentStage, 'id') else "main",
                "player_x": str(self.currentStage.player.rect.x),
                "player_y": str(self.currentStage.player.rect.y),
                "player_health": str(self.currentStage.player.health),
                "player_boosts": ",".join(self.currentStage.player.boosts)
            }
            upsertData("save", ["name", "player_data"], player_data)
            print("Game Saved!")
        else:
            print("Cannot save game: player object not found in current stage.")

    def loadGame(self):
        saved_data = getData("save", ["name", "player_data"])
        if saved_data:
            print("Game Loaded!")
            self.changeStage(saved_data['stage'], load_data=saved_data)
            return True
        else:
            print("No saved game found.")
            return False

    def tick(self):
        self.currentStage.tick(self)