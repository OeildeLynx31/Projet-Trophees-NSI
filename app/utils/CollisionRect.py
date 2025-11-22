import pygame
import os

def getSpriteCollisionRects(image_surface):
    # Return a list of rects for each area of non-transparent pixels.
    mask = pygame.mask.from_surface(image_surface)
    rects = mask.get_bounding_rects()
    return rects

def getBackgroundCollisionRects(path, file):
    background = pygame.image.load(os.path.join(path, file.replace(".png", ".hitbox.png")))
    backgroundHitBox = pygame.transform.scale(background, (720 * background.get_width() / background.get_height(), 720)).convert_alpha()
    return getSpriteCollisionRects(backgroundHitBox)

def getEnlargedHitbox(rect, marginX, marginY):
    enlargedBox = rect.copy()
    enlargedBox.x = enlargedBox.x + marginX
    enlargedBox.y = enlargedBox.y + marginY
    return enlargedBox

def nearVoid(sprite, dir):
    rect = pygame.Rect(0, 0, 0, 0)
    if (dir > 0):
        rect = pygame.Rect(sprite.hitbox.x + sprite.hitbox.width + 10, sprite.hitbox.y + sprite.hitbox.height, sprite.hitbox.width / 2, 720 - sprite.hitbox.y - sprite.hitbox.height)
    else:
        rect = pygame.Rect(sprite.hitbox.x - 10 - sprite.hitbox.width / 2, sprite.hitbox.y + sprite.hitbox.height, sprite.hitbox.width / 2, 720 - sprite.hitbox.y - sprite.hitbox.height)
    if (sprite.stage.debugShowHitboxes):
        pygame.draw.rect(sprite.stage.screen, "BLUE", rect, 2)
    return (True if rect.collideobjects(sprite.stage.backdropRects) == None else False)

def mustJump(sprite, dir):
    rect1 = pygame.Rect(0, 0, 0, 0)
    rect2 = pygame.Rect(0, 0, 0, 0)
    if (dir > 0):
        rect1 = pygame.Rect(sprite.hitbox.x + sprite.hitbox.width + 10, sprite.hitbox.y + sprite.hitbox.height - 20, 2, 10)
        rect2 = pygame.Rect(sprite.hitbox.x + sprite.hitbox.width + 10, sprite.hitbox.y - sprite.properties["jumpHeight"] * 5, 2, 2)
    else:
        rect1 = pygame.Rect(sprite.hitbox.x - 10, sprite.hitbox.y + sprite.hitbox.height - 20, 2, 10)
        rect2 = pygame.Rect(sprite.hitbox.x - 10, sprite.hitbox.y - sprite.properties["jumpHeight"] * 5, 2, 2)

    if (sprite.stage.debugShowHitboxes):
        pygame.draw.rect(sprite.stage.screen, "BLUE", rect1, 4)
        pygame.draw.rect(sprite.stage.screen, "BLUE", rect2, 4)
    
    isBlocked = (False if rect1.collideobjects(sprite.stage.backdropRects) == None else True)
    canJump = (True if rect2.collideobjects(sprite.stage.backdropRects) == None else False)
    return isBlocked and canJump

def horizontalDistance(sprite, sprite2):
    return (sprite.hitbox.x + sprite.hitbox.width / 2) - (sprite2.hitbox.x + sprite2.hitbox.width / 2)

def verticalDistance(sprite, sprite2):
    return (sprite.hitbox.y + sprite.hitbox.height / 2) - (sprite2.hitbox.y + sprite2.hitbox.height / 2)

def getCollisionRectsWithoutSelf(sprite):
    fullList = sprite.stage.backdropRects + sprite.stage.physicalEntitiesHitboxes
    newList = []
    for i in range(len(fullList)):
        if (fullList[i] != sprite.hitbox):
            newList.append(fullList[i])
    return newList