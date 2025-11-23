import pygame;
import os;
from ...components.player import Player
from ...entities.entity import Entity
from ...utils.CollisionRect import *
from ...utils.StageMovement import genStageMin
from ...utils.StageUtils import *
from ...utils.Entity import getEntitiesForStage

class Stage():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

        background = pygame.image.load(os.path.join('./assets/backgrounds/', 'background1.png'))
        self.backdrop = pygame.transform.scale(background, (720 * background.get_width() / background.get_height(), 720)).convert_alpha()
        self.backgroundColor = "WHITE"
        self.backdropRects = getBackgroundCollisionRects('./assets/backgrounds/', 'background1.png')

        self.player = Player(self.game)

        # Groups
        self.group = pygame.sprite.Group()               # Global sprite rendering group, including all entities
        self.visualEntityGroup = pygame.sprite.Group()   # Visual entities that doesn't have any hitbox
        self.physicalEntityGroup = pygame.sprite.Group() # Phisical entities that has an hitbox
        self.physicalEntitiesHitboxes = []
        self.particles = []

        self.group.add(self.visualEntityGroup.sprites())
        self.group.add(self.physicalEntityGroup.sprites())
        self.player.add(self.group)                      # Player is managed autonomously, so has no specific group

        self.debugShowHitboxes = True

        self.scroll = [0, 0]
        self.scrollMax = 0
        self.scrollMin = genStageMin(self, 0)
        self.scrollSpace = 400

        self.start()

    def tick(self, game):
        stageTick(self, game)

    def debug(self):
        stageDebug(self)

    def move(self, x, y):
        returned = stageMove(self, x, y)
        return returned

    def goto(self, x, y):
        stageGoto(self, x, y)

    def moveEntities(self, x, y):
        moveEntities(self, self.visualEntityGroup.sprites() + self.physicalEntityGroup.sprites(), x, y)

    def spawnEntities(self):
        entityList = getEntitiesForStage("stage1")
        for entity in entityList:
            self.physicalEntityGroup.add(Entity(self, self.game, entity["id"], entity["pos"][0], entity["pos"][1]))
        
        self.group.add(self.visualEntityGroup.sprites())
        self.group.add(self.physicalEntityGroup.sprites())
        self.physicalEntitiesHitboxes = []
        for entity in self.group:
            if not entity.Player and entity.physical:
                self.physicalEntitiesHitboxes.append(entity.hitbox)

    def start(self):
        for sprite in self.group:
            if (not sprite.Player):
                sprite.kill()
        self.goto(0, 0)
        self.spawnEntities()

