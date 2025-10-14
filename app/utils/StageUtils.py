import pygame

### Stage methods ###

def stageTick(self, game):

    self.screen.blit(self.backdrop, (self.scroll[0], self.scroll[1]))
    self.group.draw(self.screen)
    
    for sprite in self.group.sprites():
        sprite.tick(game) #run the tick method for each sprite in the stage

    self.debug()
    pygame.display.flip()

    self.screen.fill(self.backgroundColor)

def stageMove(stage, x, y):
    x2 = x
    y2 = y
    if ((stage.scroll[0] + x) > stage.scrollMax):
        x2 = stage.scrollMax - stage.scroll[0]
    elif ((stage.scroll[0] + x) < stage.scrollMin):
        x2 = stage.scrollMin - stage.scroll[0]
    stage.scroll[0] += x2
    stage.scroll[1] += y2
    for rect in stage.backdropRects:
        rect.x += x2
        rect.y += y2
    return [x2, y2]

def stageGoto(stage, x, y):
    for rect in stage.backdropRects:
        rect.x = rect.x - stage.scroll[0] + x
        rect.y = rect.y - stage.scroll[1] + y
    stage.scroll[0] = x
    stage.scroll[1] = y

    stage.moveAllEntities() # To also move all entities

def stageDebug(stage):
    for sprite in stage.group.sprites():
        if (stage.debugShowHitboxes):
            if (hasattr(sprite, 'hitbox')):
                pygame.draw.rect(stage.screen, "RED", sprite.hitbox, 2)
            else:
                pygame.draw.rect(stage.screen, "RED", sprite.rect, 2)
    if (stage.debugShowHitboxes):
        for rect in stage.backdropRects:
            pygame.draw.rect(stage.screen, "RED", rect, 2)

def moveEntities(self, sprites):
    for sprite in sprites:
        pos = getRelativePos(self, sprite.rect.x, sprite.rect.y)
        sprite.rect.x = pos[0]
        sprite.rect.y = pos[1]