import pygame
from .StageMovement import isInScreen
from .StageMovement import getStaticPos

### Stage methods ###

def stageTick(stage, game):

    stage.screen.blit(stage.backdrop, (stage.scroll[0], stage.scroll[1]))
    
    # blit and tick the entities that are rendered behind the player (-1)
    for sprite in stage.group.sprites():
        if ((isInScreen(sprite) or sprite.isLivingEntity) and not sprite.dead and not sprite.Player and sprite.renderLayer == -1):
            sprite.tick(game)
            stage.screen.blit(sprite.image, sprite.rect)

        if sprite.dead:
            stage.group.remove(sprite)
            if (sprite.hitbox in stage.physicalEntitiesHitboxes):
                stage.physicalEntitiesHitboxes.remove(sprite.hitbox)
    
    for particle in stage.particles:
        if particle.renderLayer == -1:
            particle.tick()

    # blit and tick the player
    stage.player.tick(game)
    stage.screen.blit(stage.player.image, stage.player.rect)

    for sprite in stage.group.sprites():
        if ((isInScreen(sprite) or sprite.isLivingEntity) and not sprite.dead and not sprite.Player and sprite.renderLayer == 1):
            sprite.tick(game)
            stage.screen.blit(sprite.image, sprite.rect)

    for particle in stage.particles:
        if particle.renderLayer == 1:
            particle.tick()


    stage.debug()
    drawInterface(stage)
    pygame.display.flip()

    stage.screen.fill(stage.backgroundColor)

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
    stage.moveEntities(x2, y2)
    return [x2, y2]

def stageGoto(stage, x, y):
    for rect in stage.backdropRects:
        rect.x = rect.x - stage.scroll[0] + x
        rect.y = rect.y - stage.scroll[1] + y
    stage.scroll[0] = x
    stage.scroll[1] = y

    stage.moveEntities(0, 0) # To also move all entities

def stageDebug(stage):
    for sprite in stage.group.sprites():
        if (stage.debugShowHitboxes and isInScreen(sprite)):
            if (hasattr(sprite, 'hitbox')):
                pygame.draw.rect(stage.screen, "RED" if sprite.physical else "BLUE", sprite.hitbox, 2)
            else:
                pygame.draw.rect(stage.screen, "RED" if sprite.physical else "BLUE", sprite.rect, 2)
    if (stage.debugShowHitboxes):
        for rect in stage.backdropRects:
            pygame.draw.rect(stage.screen, "RED", rect, 2)

def moveEntities(stage, sprites, x, y):
    for sprite in sprites:
        pos = getStaticPos(stage, sprite.rect.x, sprite.rect.y)
        sprite.rect.x +=  x
        sprite.rect.y += y

def drawInterface(stage):
    drawLifeBar(stage, stage.player)

def drawLifeBar(stage, player):
    player.lifeWaveAnimationStep += 4
    if (player.lifeWaveAnimationStep > 200):
        player.lifeWaveAnimationStep = 0
        if ("regeneration" in player.boosts):
            player.heal(1)
    
    health = player.health
    i = 0
    heartList = []
    for i in range(0, 20, 2):
        if (i+1 < health):
            heartList.append(2)
        elif (i < health):
            heartList.append(1)
        else:
            heartList.append(0)
        heartAnimPos = 650
        if (player.lifeWaveAnimationStep//10 == i and "regeneration" in player.boosts):
            heartAnimPos = 645
        elif (health < 5):
            if (player.lifeWaveAnimationStep % (1/(player.lifeWaveAnimationStep//(21-i)+1)) != 0):
                heartAnimPos = 645
        stage.screen.blit(player.heart[heartList[-1]], (840 + i * 20, heartAnimPos))
    

    