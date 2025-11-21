import pygame
import os

def get_sprite_collision_rects(image_surface):
    # Return a list of rects for each area of non-transparent pixels.
    mask = pygame.mask.from_surface(image_surface)
    rects = mask.get_bounding_rects()
    return rects

def get_collision_rects_for_background(path, file):
    background = pygame.image.load(os.path.join(path, file.replace(".png", ".hitbox.png")))
    backgroundHitBox = pygame.transform.scale(background, (720 * background.get_width() / background.get_height(), 720)).convert_alpha()
    return get_sprite_collision_rects(backgroundHitBox)

def get_enlarged_hitbox(rect, marginX, marginY):
    enlargedBox = rect.copy()
    enlargedBox.x = enlargedBox.x + marginX
    enlargedBox.y = enlargedBox.y + marginY
    return enlargedBox

def nearVoid(sprite, dir):
    rect = pygame.Rect(0, 0, 0, 0)
    if (dir > 0):
        rect = pygame.Rect(sprite.rect.x+sprite.rect.width, sprite.rect.y+sprite.rect.height, 1, 720-sprite.rect.y-sprite.rect.height)
    else:
        rect = pygame.Rect(sprite.rect.x, sprite.rect.y+sprite.rect.height, 1, 720-sprite.rect.y-sprite.rect.height)
    if (sprite.stage.debugShowHitboxes):
        pygame.draw.rect(sprite.stage.screen, "RED", rect, 2)
    return (True if rect.collideobjects(sprite.stage.backdropRects) == None else False)