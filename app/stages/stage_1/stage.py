import pygame;
import os;
from ...components.player import Player
from ...utils.CollisionRect import *
from ...utils.StageMovement import *

class Stage():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

        background = pygame.image.load(os.path.join('./assets/backgrounds/', 'background1.png'))
        self.backdrop = pygame.transform.scale(background, (720 * background.get_width() / background.get_height(), 720)).convert_alpha()
        self.backgroundColor = "WHITE"
        self.backdropRects = get_collision_rects_for_background('./assets/backgrounds/', 'background1.png')

        self.player = Player(self.game)

        # Groups
        self.group = pygame.sprite.Group()               # Global sprite rendering group, including all entities
        self.visualEntityGroup = pygame.sprite.Group()   # Visual entities that doesn't have any hitbox
        self.physicalEntityGroup = pygame.sprite.Group() # Phisical entities that has an hitbox

        self.group.add(self.visualEntityGroup.sprites())
        self.group.add(self.physicalEntityGroup.sprites())
        self.player.add(self.group)                      # Player is managed autonomously, so has no specific group

        self.debugShowHitboxes = True

        self.scroll = [0, 0]
        self.scrollMax = 0
        self.scrollMin = genStageMin(self, 0)
        self.scrollSpace = 400


    def tick(self, game):
        #L'arrière-plan futur
        self.screen.blit(self.backdrop, (self.scroll[0], self.scroll[1]))
        self.group.draw(self.screen)
        
        for sprite in self.group.sprites():
            sprite.tick(game) #run the tick method for each sprite in the stage

        self.debug()
        pygame.display.flip()

        self.screen.fill(self.backgroundColor)

    def debug(self):
        for sprite in self.group.sprites():
            if (self.debugShowHitboxes):
                if (hasattr(sprite, 'hitbox')):
                    pygame.draw.rect(self.screen, "RED", sprite.hitbox, 2)
                else:
                    pygame.draw.rect(self.screen, "RED", sprite.rect, 2)
        if (self.debugShowHitboxes):
            for rect in self.backdropRects:
                pygame.draw.rect(self.screen, "RED", rect, 2)

    def move(self, x, y):
        x2 = x
        y2 = y
        if ((self.scroll[0] + x) > self.scrollMax):
            x2 = self.scrollMax - self.scroll[0]
        elif ((self.scroll[0] + x) < self.scrollMin):
            x2 = self.scrollMin - self.scroll[0]
        self.scroll[0] += x2
        self.scroll[1] += y2
        for rect in self.backdropRects:
            rect.x += x2
            rect.y += y2

        self.moveAllEntities() # To also move all entities
        
        return [x2, y2]

    def goto(self, x, y):
        for rect in self.backdropRects:
            rect.x = rect.x - self.scroll[0] + x
            rect.y = rect.y - self.scroll[1] + y
        self.scroll[0] = x
        self.scroll[1] = y

        self.moveAllEntities() # To also move all entities

    def moveAllEntities(self):
        allEntities = self.visualEntityGroup.sprites() + self.physicalEntityGroup.sprites()
        for sprite in allEntities:
            pos = getRelativePos(self, sprite.rect.x, sprite.rect.y)
            sprite.rect.x = pos[0]
            sprite.rect.y = pos[1]
