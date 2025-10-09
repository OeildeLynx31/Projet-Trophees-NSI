import pygame;
from app.stage1.stage import Stage

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.running = False
        self.currentStage = Stage(self.screen)

    def run(self):
        self.running = True
        while self.running :
            self.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

    def quit(self):
        self.running = False
        pygame.quit()

    def tick(self):
        self.currentStage.tick()

game = Game()
game.run()
